import pandas as pd

url = "https://kf.kobotoolbox.org/api/v2/assets/aRXemgoLnWQA5GuszorbPa/export-settings/esrugoQhPp5qaxzHntQBSik/data.csv"

df_enquete = pd.read_csv(url,sep=";")




rename_columns = {
    "_id": "id_soummission",
    "Agent d'appel": "agent_appel",
    "1. Numéro de téléphone": "numero_telephone",
    "nom_client": "nom_client",
    "Acceptez-vous de répondre à quelques questions sur votre utilisation de nos services ?": "consentement_enquete",
    "2. Combien de service utiliser vous le plus souvent ?": "nombre_services_utilises",
    "3. Quel service utilisez-vous le plus ?": "service_principal",
    "4. À quelle fréquence utilisez-vous le serice <span style=\"color:blue; font-weight: bold; font-size:100%; font-family: Modern No. 20\">${service_1}</span> ?": "frequence_service_principal",
    "5. Quel est le second service le plus utilisé ?": "service_secondaire",
    "6. À quelle fréquence utilisez-vous le serice <span style=\"color:blue; font-weight: bold; font-size:100%; font-family: Modern No. 20\">${service_2}</span>  ?": "frequence_service_secondaire",
    "10. Le service est-il facilement accessible ?": "accessibilite_service",
    "11. Le service est-il rapide ?": "rapidite_service",
    "7. Globalement, êtes-vous satisfait du service ?": "satisfaction_globale",
    "8. Comment évaluez-vous la qualité du service ?": "qualite_service",
    "9. Avez-vous confiance en ce service ?": "confiance_service",
    "12. Êtes-vous satisfait du support client ?": "satisfaction_support_client",
    "13. Avez-vous rencontré des problèmes ? Si oui, lesquels ?": "problemes_rencontres",
    "14. Quelles améliorations proposez-vous ?": "propositions_amelioration",
    "15. Donnez une note globale de 1 à 10": "note_globale",
    "16. Selectionnez le mois de l'enquête": "mois_enquete",
    "17. mettez l'année de l'enquête": "annee_enquete",
    "_submission_time": "date_soumission"
}

# Renommage
df_enquete.rename(columns=rename_columns, inplace=True)

# Traitements
df_enquete["id_soummission"] = df_enquete["id_soummission"].astype(str)
df_enquete["numero_telephone"] = df_enquete["numero_telephone"].astype(str)
df_enquete["note_globale"] = pd.to_numeric(df_enquete["note_globale"], errors="coerce")
df_enquete["annee_enquete"] = pd.to_numeric(df_enquete["annee_enquete"], errors="coerce")

# Date
#df_enquete["date_soumission"] = pd.to_datetime(
#    df_enquete["date_soumission"],
#    format="%d/%m/%Y %H:%M",
#    errors="coerce"
#)

# Normalisation texte
cols_text = [
    "agent_appel",
    "nom_client",
    "service_principal",
    "service_secondaire",
    "satisfaction_globale",
    "qualite_service",
    "confiance_service",
    "satisfaction_support_client"
]

for col in cols_text:
    df_enquete[col] = df_enquete[col].astype(str).str.strip().str.lower()

# Valeurs manquantes
df_enquete["service_secondaire"] = df_enquete["service_secondaire"].fillna("aucun")
df_enquete["frequence_service_secondaire"] = df_enquete["frequence_service_secondaire"].fillna("non applicable")
df_enquete["problemes_rencontres"] = df_enquete["problemes_rencontres"].fillna("aucun")
df_enquete["propositions_amelioration"] = df_enquete["propositions_amelioration"].fillna("aucune")

# Variable score satisfaction
mapping_satisfaction = {
    "insatisfait": 1,
    "peu satisfait": 2,
    "moyen": 3,
    "satisfait": 4,
    "très satisfait": 5
}

df_enquete["score_satisfaction"] = df_enquete["satisfaction_globale"].map(mapping_satisfaction)

# Sélection
df_enquete = df_enquete[[
 "id_soummission",
 "agent_appel",
 "numero_telephone",
 "nom_client",
 "consentement_enquete",
 "nombre_services_utilises",
 "service_principal",
 "frequence_service_principal",
 "service_secondaire",
 "frequence_service_secondaire",
 "accessibilite_service",
 "rapidite_service",
 "satisfaction_globale",
 "qualite_service",
 "confiance_service",
 "satisfaction_support_client",
 "problemes_rencontres",
 "propositions_amelioration",
 "note_globale",
 "mois_enquete",
 "annee_enquete",
 "date_soumission"
]]


clients = pd.read_excel(
    "data/raw/clients.xlsx"
)



def clean_phone(x):

    if pd.isna(x):
        return None

    x = str(x)

    x = x.replace(" ", "")
    x = x.replace("+221", "")
    x = x.replace("-", "")

    return x

clients["numero"] = (
    clients["numero"]
    .apply(clean_phone)
)

df_enquete["numero_telephone"] = (
    df_enquete["numero_telephone"]
    .apply(clean_phone)
)

df = df_enquete.merge(
    clients,
    left_on="numero_telephone",
    right_on="numero",
    how="inner"
)

df.to_excel(
    "data/processed/base_finale.xlsx",
    index=False
)

print("Jointure terminée")

