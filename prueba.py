import streamlit as st
import pandas as pd

# Título de la app
st.title("Simulador de Clasificación - Mundial de Clubes FIFA 2025")

# Paso 1: Elegir grupo
st.markdown("### Paso 1: Selecciona el grupo que quieres")

# Diccionario con escudos de los equipos (reemplaza con los URLs de los escudos que necesites)
escudos = {
    "River Plate": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Escudo_del_C_A_River_Plate.svg/800px-Escudo_del_C_A_River_Plate.svg.png",
    "Rayados": "https://i.pinimg.com/originals/c3/1b/1e/c31b1ef8686dec98ab36d5d90751e36e.png",
    "Al-Ain": "https://upload.wikimedia.org/wikipedia/en/6/62/Al_Ain_FC_logo_2024.png",
    "Chelsea": "https://1000marcas.net/wp-content/uploads/2020/03/Logo-Chelsea.png",
    "Al-Hilal": "https://logodownload.org/wp-content/uploads/2019/12/al-hilal-logo-0.png",
    "Manchester City": "https://1000marcas.net/wp-content/uploads/2020/02/Manchester-City-logo.jpg",
    "Real Madrid": "https://c0.klipartz.com/pngpicture/912/91/gratis-png-real-madrid-c-f-logo-real-madrid-c-f-logo-dream-league-soccer-uefa-champions-league-la-liga-thumbnail.png",
    "Bayern Munich": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/FC_Bayern_München_logo_%282017%29.svg/250px-FC_Bayern_München_logo_%282017%29.svg.png",
    "Boca Juniors": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Escudo_del_Club_Atlético_Boca_Juniors.svg/1200px-Escudo_del_Club_Atlético_Boca_Juniors.svg.png",
    "Auckland City": "https://upload.wikimedia.org/wikipedia/en/5/53/New_Auckland_City_FC_logo_%28updated_2022%29.png",
    "Benfica": "https://as01.epimg.net/img/comunes/fotos/fichas/equipos/large/44.png",
    "Flamengo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Flamengo_braz_logo.svg/1200px-Flamengo_braz_logo.svg.png",
    "Espérance": "https://upload.wikimedia.org/wikipedia/en/f/fb/Espérance_Sportive_de_Tunis_logo.png",
    "LAFC": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Los_Angeles_Football_Club.svg/800px-Los_Angeles_Football_Club.svg.png",
    "Urawa Reds": "https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Urawa_Red_Diamonds_logo.svg/640px-Urawa_Red_Diamonds_logo.svg.png",
    "Inter Milan": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/FC_Internazionale_Milano_2021.svg/800px-FC_Internazionale_Milano_2021.svg.png",
    "Fluminense": "https://upload.wikimedia.org/wikipedia/commons/a/ad/Fluminense_FC_escudo.png",
    "Borussia Dortmund": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Borussia_Dortmund_logo.svg/640px-Borussia_Dortmund_logo.svg.png",
    "Ulsan Hyundai": "https://upload.wikimedia.org/wikipedia/en/thumb/b/b5/Ulsan_Hyundai_FC.svg/1200px-Ulsan_Hyundai_FC.svg.png",
    "Mamelodi Sundowns": "https://upload.wikimedia.org/wikipedia/pt/9/93/Mamelodi_Sundowns_FC.png?20250621123428g",
    "WAC": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Wydad_Athletic_Club_logo.svg/1200px-Wydad_Athletic_Club_logo.svg.png",
    "Pachuca": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6tr7QbNHYUJ2N1FeSgv-Q1hbDNFjRwUib_Fp_GumFcxt8ybLVmWo39zXXBGJ-IJZu96C1ZPeqB7R31lKuhdrGElfJ-kaePLXBgTN-d8dA-31HGYZ5N_qlF3k_4qAXnQUZ6tcAavW__rQ/s1600/LoGO+Pachuca.png",
    "Salzburg": "https://a.espncdn.com/combiner/i?img=/i/teamlogos/soccer/500/2790.png",
    "Juventus": "https://1000marcas.net/wp-content/uploads/2020/01/Juventus-logo.png",
}

# Selector de grupo
grupo = st.selectbox("Selecciona el grupo:", ["Grupo C", "Grupo D", "Grupo E", "Grupo F", "Grupo G", "Grupo H"])

# Asignación de equipos
if grupo == "Grupo C":
    team_names = ["Bayern Munich", "Benfica", "Boca Juniors", "Auckland City"]
elif grupo == "Grupo D":
    team_names = ["Flamengo", "Chelsea", "Espérance", "LAFC"]
elif grupo == "Grupo E":
    team_names = ["River Plate", "Inter Milan", "Rayados", "Urawa Reds"]
elif grupo == "Grupo F":
    team_names = ["Fluminense", "Borussia Dortmund", "Ulsan Hyundai", "Mamelodi Sundowns"]
elif grupo == "Grupo G":
    team_names = ["Manchester City", "Juventus", "WAC", "Al-Ain"]
elif grupo == "Grupo H":
    team_names = ["Real Madrid", "Salzburg", "Al-Hilal", "Pachuca"]
else:
    team_names = ["Equipo 1", "Equipo 2", "Equipo 3", "Equipo 4"]

# Mostrar equipos con sus escudos
for i, team in enumerate(team_names):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(escudos.get(team, ""), width=40)
    with col2:
        team_names[i] = st.text_input(f"Equipo {i+1}:", value=team)


resultados_fijos = {
    "Grupo C": {
        (0, 3): (10, 0),
        (1, 2): (2, 2),
        (0, 2): (2, 1),
        (1, 3): (6, 0)
    },
    "Grupo D": {
        (0, 2): (2, 0),
        (1, 3): (2, 0),
        (0, 1): (3, 1),
        (2, 3): (1, 0)
    },
    "Grupo E": {
        (0, 3): (3, 1),
        (1, 2): (1, 1),
        (0, 2): (0, 0),
        (1, 3): (2, 1)
    },
    "Grupo F": {
        (0, 1): (0, 0),
        (2, 3): (0, 1),
        (0, 2): (4, 2),
        (1, 3): (4, 3)
    },
    "Grupo G": {
        (1, 2): (4, 1),
        (0, 3): (6, 0),
        (0, 2): (2, 0),
        (1, 3): (5, 0)
    },
    "Grupo H": {
        (0, 3): (3, 1),
        (1, 2): (0, 0),
        (0, 2): (1, 1),
        (1, 3): (2, 1)
    }
}
#Método clave usando todo lo que la FIFA se inventó
def desempatar_fifa(equipos, match_results, global_stats, historial=None):
    if len(equipos) == 1:
        return equipos

    if historial is None:
        historial = set()
    key = tuple(sorted(equipos))
    if key in historial:
        return equipos  # Evita bucles infinitos
    historial.add(key)

    # Crear estadísticas entre los equipos empatados
    sub_stats = {team: {"Puntos": 0, "GF": 0, "GC": 0} for team in equipos}
    for team1, g1, g2, team2 in match_results:
        if team1 in equipos and team2 in equipos:
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
        {"Equipo": team, "Puntos": data["Puntos"], "DG": data["GF"] - data["GC"], "GF": data["GF"]}
        for team, data in sub_stats.items()
    ])
    sub_df = sub_df.sort_values(by=["Puntos", "DG", "GF"], ascending=False).reset_index(drop=True)

    # Verificamos si TODOS siguen empatados en Puntos, DG y GF
    empate_total = (
        sub_df[["Puntos", "DG", "GF"]].nunique().max() == 1
    )

    if empate_total:
        # Aplicar criterios d) y e)
        return criterios_d_e(global_stats, equipos)

    else:
        # Desempatar recursivamente si hay empates internos
        duplicated = sub_df.duplicated(subset=["Puntos", "DG", "GF"], keep=False)
        if not duplicated.any():
            return sub_df["Equipo"].tolist()
        else:
            empatados = sub_df[duplicated]
            no_empatados = sub_df[~duplicated]
            suborden = desempatar_fifa(empatados["Equipo"].tolist(), match_results, global_stats, historial)
            return no_empatados["Equipo"].tolist() + suborden

def criterios_d_e(df, equipos_empatados):
    sub_df = df[df["Equipo"].isin(equipos_empatados)].copy()
    sub_df = sub_df.sort_values(by=["DG", "GF"], ascending=False)
    return sub_df["Equipo"].tolist()

# Paso 2: Ingresar resultados de los partidos
if all(team_names):
    match_results = []
    matchups = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

    for i, (a, b) in enumerate(matchups):
        col1, col2, col3 = st.columns(3)

        if grupo in resultados_fijos and (a, b) in resultados_fijos[grupo]:
            g1, g2 = resultados_fijos[grupo][(a, b)]
            match_results.append((team_names[a], g1, g2, team_names[b]))
            with col1:
                st.image(escudos.get(team_names[a], ""), width=40)
                st.markdown(f"**{team_names[a]} {g1}**")
            with col2:
                st.markdown("**vs**")
            with col3:
                st.image(escudos.get(team_names[b], ""), width=40)
                st.markdown(f"**{g2} {team_names[b]}**")
        else:
            with col1:
                g1 = st.number_input(f"{team_names[a]} goles", min_value=0, key=f"g1_{i}")
            with col2:
                st.markdown("**vs**")
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
    #st.markdown("### Paso 4: Desempates entre equipos empatados")

    orden_final = []
    df_sorted = df.sort_values(by=["Puntos"], ascending=False)

    # Agrupar equipos por puntos
    for puntos, grupo_puntos in df_sorted.groupby("Puntos", sort=False):
        if len(grupo_puntos) == 1:
            orden_final.append(grupo_puntos.iloc[0])
        else:
            equipos_empatados = list(grupo_puntos["Equipo"])

            equipos_ordenados = desempatar_fifa(equipos_empatados, match_results, df)

            # Si aún hay empate total, usar criterios d) y e)
            if len(set(equipos_ordenados)) < len(equipos_empatados):
                equipos_ordenados = criterios_d_e(df, equipos_empatados)

            for equipo in equipos_ordenados:
                fila = df[df["Equipo"] == equipo].iloc[0]
                orden_final.append(fila)

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


    orden_final_df["Equipo"] = orden_final_df["Equipo"].apply(lambda team: f'<img src="{escudos.get(team, "")}" style="height:20px; vertical-align: middle; margin-right: 6px;"> {team}')
    styled_df = (
        orden_final_df.style
        .applymap(estilo_posicion, subset=["Posición"])
        .applymap(fondo_negro_blanco, subset=[col for col in orden_final_df.columns if col != "Posición"])
    )

    st.markdown(styled_df.to_html(escape=False, index=False), unsafe_allow_html=True)

else:
    st.warning("Por favor, ingresa los nombres de los 4 equipos.")

st.markdown("---")
st.markdown("Creado por Diego Lozano León @lozdie_ff © 2025", unsafe_allow_html=True)
