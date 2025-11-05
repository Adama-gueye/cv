from pathlib import Path
import streamlit as st
from PIL import Image

# ----- PATH SETTINGS -----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"

# ----- GENERAL SETTINGS -----
PAGE_TITLE = "👋 Digital CV | Adama Gueye"
NAME = "Adama Gueye"
DESCRIPTION = """
Étudiante en Master Data Science & Intelligence Artificielle, passionnée par l’analyse, la visualisation et la valorisation des données.
Rigoureuse, curieuse et motivée à apprendre au sein d’équipes innovantes.
"""
EMAIL = "adamarahma99@gmail.com"

SOCIAL_MEDIA = {
    'LinkedIn': 'https://www.linkedin.com/in/adama-gueye-763a8423b/',
    'GitHub': 'https://github.com/Adama-gueye/'  # si tu as un GitHub
}

PROJECTS = {
    "📊 Tableau de bord Power BI - Suivi des ventes et performances clients": "https://app.powerbi.com/groups/me/reports/23b657bf-c95f-476e-a7e2-639c3dd3da1f/90dbb611c566aef889c0?experience=power-bi",
    "💻 Application de gestion de stock - Laravel & MySQL": "https://www.stock.bijouterieislam.com/",
    # "🧠 Modèles de classification - Python (scikit-learn)": ""
}

st.set_page_config(page_title=PAGE_TITLE)

# ----- LOAD CSS, PDF & PROFILE PIC -----
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# ----- HERO SECTION -----
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Télécharger le CV",
        data=PDFbyte,
        file_name=resume_file.name
    )
    st.write("📫", EMAIL)

# ----- SOCIAL LINKS -----
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# ----- EXPERIENCE & QUALIFICATIONS -----
st.write('\n')
st.subheader("Expérience & Qualifications")
st.write("""
- ✔️ Expérience en analyse et visualisation de données (Power BI, pandas)
- ✔️ Solides compétences en Python, SQL et développement backend (Laravel)
- ✔️ Bonne compréhension des modèles statistiques et de Machine Learning
- ✔️ Capacité d’adaptation, apprentissage rapide et rigueur professionnelle
""")

# ----- SKILLS -----
st.write('\n')
st.subheader("Compétences Techniques")
st.write("""
- 💻 Langages : Python, SQL, PHP, JavaScript, R
- 📊 Data Viz : Power BI, Streamlit, Excel
- 🧠 Machine Learning : Scikit-learn, Pandas, K-Means, Régression
- 🗄️ Bases de données : MySQL, PostgreSQL
- 🌐 Frameworks : Laravel, Flask, Django, React
""")

# ----- PROJECTS -----
st.write('\n')
st.subheader("Projets")
st.write('---')
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
