# Pilotage FreezBee pour Home Assistant

[![Licence Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2026.10%2B-41BDF5.svg)](https://www.home-assistant.io/)

Pilotez votre chauffage pièce par pièce avec votre thermostat FreezBee et des vannes thermostatiques.

Ce dépôt contient le Blueprint officiel permettant d'associer
vos vannes thermostatiques connectées (Zigbee, Z-Wave, Matter, Wi-Fi...)
à votre thermostat FreezBee dans Home Assistant,
afin d'envoyer automatiquement les consignes optimales à votre chaudière.

## Installation rapide

Cliquez sur le bouton ci-dessous pour importer directement ce Blueprint dans votre instance Home Assistant :

[![Ouvrir dans Home Assistant et importer le Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fnetica-org%2Ffreezbee-ha%2Fblob%2Fmain%2Fblueprints%2Fpilotage-freezbee.yaml)

### Importation manuelle

Vous pouvez aussi importer le Blueprint manuellement :

1. Dans Home Assistant, rendez-vous dans **Paramètres** › **Automatisations et scènes** › **Blueprints**.
2. Cliquez sur **Importer un blueprint** (en bas à droite).
3. Collez l'URL suivante :
   ```text
   https://github.com/netica-org/freezbee-ha/blob/main/blueprints/pilotage-freezbee.yaml
   ```

## Utilisation

Pour utiliser ce blueprint, sélectionnez votre thermostat FreezBee, puis associez-lui les vannes thermostatiques qui contrôlent la température de chaque pièce de votre maison.

<img width="805" height="792" alt="image" src="https://github.com/user-attachments/assets/f9a6ee27-ca51-4bd1-b780-e3a523305dab" />

L’automatisation récupère automatiquement les informations de chaque vanne thermostatique pour n’allumer la chaudière que lorsqu‘il y a au moins une pièce à chauffer, avec la consigne et la température ambiante adaptées.

### Algorithme “_delta max_”

L’automatisation détermine la pièce avec le plus grand écart entre la consigne et la température ambiante. Elle utilise les données de cette pièce (consigne et température ambiante) comme valeurs de référence à envoyer à votre chaudière.

### Algorithme “_delta moyen_”

L’automatisation ne considère que les pièces qui doivent être chauffées (température ambiante inférieure à la consigne et vanne thermostatique allumée en mode chauffage ou auto). Elle calcule les valeurs moyennes de la température ambiante ainsi que de la consigne de ces pièces, puis utilise ces valeurs comme référence à envoyer à votre chaudière.

S’il y a moins de 2 pièces à chauffer, l’algorithme “delta moyen” est équivalent à “delta max”.

### Optimisations

Ce blueprint comporte plusieurs garde-fous pour assurer un bon fonctionnement en cas d’erreur ou d’indisponibilité d’un appareil. Le thermostat FreezBee est synchronisé dès qu’une modification de consigne est enregistrée sur au moins une des vannes thermostatiques associées. Un rafraîchissement toutes les 10 minutes est également en place pour surveiller l’évolution de la température ambiante.

## Remerciements

Merci à Aymeric Chessoux ([@achessoux](https://github.com/achessoux)) pour ses retours et la première preuve de concept ayant largement inspiré ce Blueprint.
