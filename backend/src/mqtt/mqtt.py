import paho.mqtt.client as mqtt
import json
from django.apps import apps

# # Récupérer le modèle correspondant à votre table dans la base de données
# MyModel = apps.get_model(app_label='votre_app', model_name='VotreModele')

# # Créer une instance du modèle avec les données reçues
# instance = MyModel(**data)

# # Enregistrer l'instance dans la base de données
# instance.save()


# Créer un dictionnaire pour stocker les données des capteurs
donnees_capteurs = {}

# Fonction de rappel appelée lorsqu'une connexion MQTT est établie
def on_connect(client, userdata, flags, rc):
    print("Connecté avec le code de retour : " + str(rc))
    # Abonnez-vous à plusieurs topics MQTT
    client.subscribe([
        ("groupe6/packet/a2e7d3e5-eb32-40f3-9ac9-f8863e35ffc9/b4cabb04-2c31-4a69-8840-ac79ac769904/112", 0),
        ("groupe6/packet/1df2b39a-8a3c-488c-8c93-361d85367473/96dc697c-e18c-4b63-9c62-667a98fbf517/114", 0),
        ("groupe6/packet/1df2b39a-8a3c-488c-8c93-361d85367473/478d1826-fad5-490e-a531-ccb7510aefc1/115", 0),
        ("groupe6/packet/1df2b39a-8a3c-488c-8c93-361d85367473/0ad0bf15-aac9-4595-a3cc-15eafc005f53/118", 0),
        ("groupe6/packet/1df2b39a-8a3c-488c-8c93-361d85367473/ca9fdeab-fdcc-4c45-b867-e49eb1fb04a6/119", 0)
    ])


# Fonction de rappel appelée lorsqu'un message MQTT est reçu
def on_message(client, userdata, msg):
    # print("Message reçu : " + msg.topic + " " + str(msg.payload))

    # Convertir le payload en chaîne de caractères (string) depuis le format bytes
    payload_str = msg.payload.decode("utf-8")

    # Ajoutez ici votre logique de traitement des messages en fonction du topic
    if msg.topic == "groupe6/packet/a2e7d3e5-eb32-40f3-9ac9-f8863e35ffc9/b4cabb04-2c31-4a69-8840-ac79ac769904/112":
        # Traitement des messages pour le topic 112
        data = json.loads(payload_str)
        temperature = data["data"]["temperature"]
        # Faites quelque chose avec la température pour le topic 112
        del data["source_address"]  # Supprimer le champ "source_address" des données
        print("Données : " + str(data))
        # Stocker les données dans le dictionnaire
        donnees_capteurs["capteur1"] = data

    elif msg.topic == "groupe6/packet/1df2b39a-8a3c-488c-8c93-361d85367473/96dc697c-e18c-4b63-9c62-667a98fbf517/114":
        # Traitement des messages pour le topic 114
        data = json.loads(payload_str)
        # Effectuez d'autres opérations avec les données du topic 114
        del data["source_address"]  # Supprimer le champ "source_address" des données
        print("Données : " + str(data))
        # Stocker les données dans le dictionnaire
        donnees_capteurs["capteur2"] = data

    elif msg.topic == "groupe6/packet/1df2b39a-8a3c-488c-8c93-361d85367473/478d1826-fad5-490e-a531-ccb7510aefc1/115":
        # Traitement des messages pour le topic 115
        data = json.loads(payload_str)
        # Effectuez d'autres opérations avec les données du topic 115
        del data["source_address"]  # Supprimer le champ "source_address" des données
        print("Données : " + str(data))
        # Stocker les données dans le dictionnaire
        donnees_capteurs["capteur3"] = data

    elif msg.topic == "groupe6/packet/1df2b39a-8a3c-488c-8c93-361d85367473/0ad0bf15-aac9-4595-a3cc-15eafc005f53/118":
        # Traitement des messages pour le topic 118
        data = json.loads(payload_str)
        # Effectuez d'autres opérations avec les données du topic 118
        del data["source_address"]  # Supprimer le champ "source_address" des données
        print("Données : " + str(data))
        # Stocker les données dans le dictionnaire
        donnees_capteurs["capteur4"] = data

    elif msg.topic == "groupe6/packet/1df2b39a-8a3c-488c-8c93-361d85367473/ca9fdeab-fdcc-4c45-b867-e49eb1fb04a6/119":
        # Traitement des messages pour le topic 119
        data = json.loads(payload_str)
        # Effectuez d'autres opérations avec les données du topic 119
        del data["source_address"]  # Supprimer le champ "source_address" des données
        print("Données : " + str(data))
        # Stocker les données dans le dictionnaire
        donnees_capteurs["capteur5"] = data

# Créez un client MQTT
client = mqtt.Client()

# Les identifiants de connexion
client.username_pw_set("groupe6", "q8T61yj4Lwq7")

# Définir les fonctions de rappel
client.on_connect = on_connect
client.on_message = on_message

# Connexion au broker MQTT
client.connect("mqtt.arcplex.fr", 2295, 10)

# Boucle de gestion des messages MQTT
client.loop_forever()
