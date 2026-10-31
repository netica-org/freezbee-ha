# Pilotage FreezBee pour Home Assistant

[![Licence Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2026.10%2B-41BDF5.svg)](https://www.home-assistant.io/)

Pilotez votre chauffage pièce par pièce avec votre thermostat FreezBee et des vannes thermostatiques.

Ce dépôt contient le Blueprint officiel permettant d'associer
vos têtes thermostatiques connectées (Zigbee, Z-Wave, Matter, Wi-Fi...)
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

## Remerciements

Merci à Aymeric Chessoux ([@achessoux](https://github.com/achessoux)) pour ses retours et la première preuve de concept ayant largement inspiré ce Blueprint.