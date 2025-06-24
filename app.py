import streamlit as st
import pandas as pd

st.title("Simulador de Clasificación - Mundial de Clubes FIFA 2025")

# Paso 1: Nombres de equipos
st.markdown("### Paso 1: Nombres de los equipos")
team_names = []
for i in range(4):
    team = st.text_input(f"Equipo {i+1}", key=f"team_{i}")
    team_names.append(team)

if all(team_names):
    st.markdown("### Paso 2: Ingresar resultados de los partidos")

    match_results = []
    matchups = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

    for i, (a, b) in enumerate(matchups):
        col1, col2, col3 = st.columns(3)
        with col1:
            g1 = st.number_input(f"{team_names[a]} goles", min_value=0, key=f"g1_{i}")
        with col2:
            st.markdown(f"**vs**")
        with col3:
            g2 = st.number_input(f"{team_names[b]} goles", min_value=0, key=f"g2_{i}")

        match_results.append((team_names[a], g1, g2, team_names[b]))

    # Inicializar estadísticas
    stats = {team: {"Puntos": 0, "GF": 0, "GC": 0} for team in team_names}

    for team1, g1, g2, team2 in match_results:
        stats[team1]["GF"] += g1
        stats[team1]["GC"] += g2
        stats[team2]["GF"] += g2
        stats[team2]["GC"] += g1

        if g1 > g2:
            stats[team1]["Puntos"] += 3
        elif g2 > g1:
            stats[team2]["Puntos"] += 3
        else:
            stats[team1]["Puntos"] += 1
            stats[team2]["Puntos"] += 1

    # Crear DataFrame
    df = pd.DataFrame([
        {
            "Equipo": team,
            "Puntos": data["Puntos"],
            "GF": data["GF"],
            "GC": data["GC"],
            "DG": data["GF"] - data["GC"]
        }
        for team, data in stats.items()
    ])

    # Paso 4: Desempates entre equipos empatados según FIFA
    st.markdown("### Paso 4: Desempates entre equipos empatados")

    grupos = df.groupby("Puntos", sort=False)
    orden_final = []

    for puntos, grupo in grupos:
        if len(grupo) == 1:
            orden_final.append(grupo.iloc[0])
        else:
            equipos_empatados = list(grupo["Equipo"])
            sub_stats = {team: {"Puntos": 0, "GF": 0, "GC": 0} for team in equipos_empatados}

            for team1, g1, g2, team2 in match_results:
                if team1 in equipos_empatados and team2 in equipos_empatados:
                    sub_stats[team1]["GF"] += g1
                    sub_stats[team1]["GC"] += g2
                    sub_stats[team2]["GF"] += g2
                    sub_stats[team2]["GC"] += g1

                    if g1 > g2:
                        sub_stats[team1]["Puntos"] += 3
                    elif g2 > g1:
                        sub_stats[team2]["Puntos"] += 3
                    else:
                        sub_stats[team1]["Puntos"] += 1
                        sub_stats[team2]["Puntos"] += 1

            sub_df = pd.DataFrame([
                {
                    "Equipo": team,
                    "Puntos entre ellos": data["Puntos"],
                    "DG entre ellos": data["GF"] - data["GC"],
                    "GF entre ellos": data["GF"]
                }
                for team, data in sub_stats.items()
            ])

            sub_df = sub_df.sort_values(
                by=["Puntos entre ellos", "DG entre ellos", "GF entre ellos"],
                ascending=False
            )

            empate_final = sub_df.duplicated(
                subset=["Puntos entre ellos", "DG entre ellos", "GF entre ellos"],
                keep=False
            )

            if empate_final.any():
                equipos_a_desempatar = sub_df[empate_final]["Equipo"].tolist()
                global_df = df[df["Equipo"].isin(equipos_a_desempatar)].copy()

                global_df = global_df.sort_values(
                    by=["DG", "GF"],
                    ascending=False
                )

                for _, fila in global_df.iterrows():
                    orden_final.append(fila)

                for _, fila in sub_df.iterrows():
                    if fila["Equipo"] not in equipos_a_desempatar:
                        fila_completa = df[df["Equipo"] == fila["Equipo"]].iloc[0]
                        orden_final.append(fila_completa)
            else:
                for _, fila in sub_df.iterrows():
                    fila_completa = df[df["Equipo"] == fila["Equipo"]].iloc[0]
                    orden_final.append(fila_completa)

    # Paso 5: Mostrar tabla final ordenada y coloreada
    st.markdown("### Clasificación Final (con criterios FIFA aplicados)")

    orden_final_df = pd.DataFrame(orden_final)

    orden_final_df.reset_index(drop=True, inplace=True)
    orden_final_df.insert(0, "Posición", orden_final_df.index + 1)

    def estilo_posicion(val):
        if val in [1, 2]:
            return "background-color: green; color: white"
        else:
            return "background-color: red; color: white"

    def fondo_negro_blanco(val):
        return "background-color: black; color: white"

    styled_df = (
        orden_final_df.style
        .applymap(estilo_posicion, subset=["Posición"])
        .applymap(fondo_negro_blanco, subset=[col for col in orden_final_df.columns if col != "Posición"])
    )

    st.dataframe(styled_df)

else:
    st.warning("Por favor, ingresa los nombres de los 4 equipos.")
