import streamlit as st
import psycopg2

# Fonction de connexion à la base de données PostgreSQL
def init_connection():
    return psycopg2.connect(
        host=st.secrets["host"],
        port=st.secrets["port"],
        database=st.secrets["database"],
        user=st.secrets["user"],
        password=st.secrets["password"]
    )

# Fonction pour insérer les données dans la base
def insert_data(idcommune, codepostal, commune):
    conn = init_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """INSERT INTO "Test"."Streamlitdatabase" (idcommune, codepostal, commune) VALUES (%s, %s, %s)""",
            (idcommune, codepostal, commune)
        )
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de l'insertion : {e}")
    finally:
        cursor.close()
        conn.close()

# Interface utilisateur Streamlit
st.title("Formulaire de Saisie d'Utilisateurs")

idcommune = st.text_input("id")
codepostal = st.number_input("codepostal")
commune = st.text_input("commune")

if st.button("Envoyer"):
    if idcommune and codepostal and commune:  # Vérifier que les champs ne sont pas vides
        insert_data(idcommune, codepostal, commune)
        st.success("Données envoyées avec succès !")
    else:
        st.warning("Veuillez remplir tous les champs.")