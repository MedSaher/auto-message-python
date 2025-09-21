import pywhatkit as kit
import pandas as pd
import time

default_country_code = "+212"

# Read CSV and strip spaces
df = pd.read_csv("data.csv", dtype={"phone_number": str})

for index, row in df.iterrows():
    phone = row["phone_number"].strip().replace(" ", "")
    name = row["full_name"].strip()

    # Add +212 if missing
    if not phone.startswith("+"):
        phone = default_country_code + phone.lstrip("0")

    message = (
        f"Bonjour {name}, merci pour ton inscription au formulaire de l’Association des étudiants-Ziri de l’ENCG Oujda 🤍. "
        "Nous avons le plaisir de t’informer que ton entretien aura lieu ce mardi à 12h00 à la salle des activités parascolaires. "
        "Nous comptons sur ta présence !"
    )

    kit.sendwhatmsg_instantly(phone, message, wait_time=15, tab_close=False)
    print(f"Message envoyé à {phone}")
    time.sleep(5)
