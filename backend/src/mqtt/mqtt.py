from django.shortcuts import render
from mqtt_client import client, donnees_capteurs


def mqtt_data_view(request):
    # Connexion au broker MQTT
    client.connect("mqtt.arcplex.fr", 2295, 10)

    # Boucle de gestion des messages MQTT
    client.loop_start()

    # Récupérer les données des capteurs
    capteur1_data = donnees_capteurs.get("temperature", {})
    capteur3_data = donnees_capteurs.get("lux", {})
    capteur4_data = donnees_capteurs.get("level", {})
    capteur5_data = donnees_capteurs.get("motion", {})

    if donnees_capteurs ==
