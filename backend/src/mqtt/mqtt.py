from django.shortcuts import render
from mqtt_client import client, donnees_capteurs


def mqtt_data_view(request):
    # Connexion au broker MQTT
    client.connect("mqtt.arcplex.fr", 2295, 10)

    # Boucle de gestion des messages MQTT
    client.loop_start()
