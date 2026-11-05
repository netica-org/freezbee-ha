# Piloter FreezBee avec Home Assistant

[![Tests](https://github.com/netica-org/freezbee-ha/actions/workflows/tests.yaml/badge.svg?branch=main)](https://github.com/netica-org/freezbee-ha/actions/workflows/tests.yaml)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2026.10%2B-41BDF5.svg)](https://www.home-assistant.io/)
[![Licence Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE)
![Conçu en France](https://img.shields.io/badge/Made_in-%F0%9F%87%AB%F0%9F%87%B7-white)

Pilotez votre chauffage pièce par pièce avec votre thermostat FreezBee et des vannes thermostatiques.

Ce dépôt contient les blueprints officiels FreezBee pour Home Assistant :

- Le blueprint [Pilotage FreezBee](#pilotage-freezbee) :
  <br/>
  Permet d'associer vos vannes thermostatiques connectées (Zigbee, Z-Wave, Matter, Wi-Fi...)
  à votre thermostat FreezBee dans Home Assistant,
  afin d'envoyer automatiquement les consignes optimales à votre chaudière.
- Le blueprint [Température ambiante déportée](#température-ambiante-déportée) :
  <br/>
  Remplace la température ambiante d’une vanne thermostatique connectée par celle d’un capteur déporté, pour éviter de mesurer la température trop près du radiateur.

## Prérequis

- Home Assistant **2026.10 ou plus récent** ;
- Un thermostat [FreezBee](https://freezbee.fr/products/thermostat-connecte-freezbee) (ou générique[^1]) ;
- Des vannes thermostatiques connectées qui se comportent comme des thermostats
  (entité `climate` dans Home Assistant) ;
- En option, un ou plusieurs capteurs de température ambiante par pièce.

[^1]: Si vous n’avez pas de thermostat FreezBee (conçu pour les chaudières Frisquet Visio),
vous devez utiliser une version pour [thermostat générique](#bonus-pilotage-dun-thermostat-générique).

## Pilotage FreezBee

### Installation

Cliquez sur le bouton ci-dessous pour importer directement ce blueprint dans votre instance Home Assistant :

[![Ouvrir dans Home Assistant et importer le blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fnetica-org%2Ffreezbee-ha%2Fblob%2Fmain%2Fblueprints%2Fvalves2freezbee.yaml)

Vous pouvez aussi importer le blueprint manuellement :

1. Dans Home Assistant, rendez-vous dans **Paramètres** › **Automatisations et scènes** › **Blueprints**.
2. Cliquez sur **Importer un blueprint** (en bas à droite).
3. Collez l'URL suivante :
   ```text
   https://github.com/netica-org/freezbee-ha/blob/main/blueprints/valves2freezbee.yaml
   ```

### Utilisation

Pour utiliser ce blueprint, sélectionnez votre thermostat FreezBee, puis associez-lui les vannes thermostatiques qui contrôlent vos radiateurs.

<img width="805" height="792" alt="image" src="https://github.com/user-attachments/assets/f9a6ee27-ca51-4bd1-b780-e3a523305dab" />

L’automatisation récupère automatiquement les informations de chaque vanne thermostatique pour n’allumer la chaudière que lorsqu‘il y a au moins une pièce à chauffer, avec la consigne et la température ambiante adaptées.

### Algorithme “_delta max_”

L’automatisation détermine la pièce avec le plus grand écart entre la consigne et la température ambiante. Elle utilise les données de cette pièce (consigne et température ambiante) comme valeurs de référence à envoyer à votre chaudière.

### Algorithme “_delta moyen_”

L’automatisation ne considère que les pièces qui doivent être chauffées (température ambiante inférieure à la consigne). Elle calcule la valeur moyenne de la température ambiante ainsi que de la consigne de ces pièces, puis utilise ces valeurs comme référence à envoyer à votre chaudière.

S’il y a moins de 2 pièces à chauffer, l’algorithme “*delta moyen*” est équivalent à “*delta max*”.

## Température ambiante déportée

Une vanne mesure la température à proximité du radiateur, qui peut être différente
de celle ressentie dans la pièce.

Le blueprint [Température ambiante déportée](./blueprints/remote-ambient.yaml)
permet d’utiliser la mesure d’un capteur de température ambiante mieux placé.

### Installation

Cliquez sur le bouton ci-dessous pour importer directement ce blueprint dans votre instance Home Assistant :

[![Ouvrir dans Home Assistant et importer le Blueprint de synchronisation](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fnetica-org%2Ffreezbee-ha%2Fblob%2Fmain%2Fblueprints%2Fremote-ambient.yaml)

Si vous préférez, vous pouvez également importer ce blueprint manuellement avec l’adresse suivante :

```text
https://github.com/netica-org/freezbee-ha/blob/main/blueprints/remote-ambient.yaml
```

### Utilisation

Vous devez créer autant d’automatisations que de pièces à contrôler.

Exemple :

1. Créez une automatisation et nommez-la, par exemple **Température ambiante — Salon**.
2. Dans **Capteurs de température**, sélectionnez tous les capteurs
   d'ambiance de cette pièce. Attention, ne sélectionnez pas la température interne des
   vannes destinataires, pour éviter une boucle de mesure.
3. Dans **Vannes thermostatiques**, sélectionnez directement les vannes de votre pièce.
4. Vérifiez les conditions d’utilisation avant d’activer l’automatisation et l’enregistrer.
5. Cliquez sur **Exécuter les actions** puis consultez la page **Historique des exécutions**
   pour tester immédiatement la première synchronisation.
6. Répétez ces étapes pour chaque pièce. N'associez pas une même vanne
   à plusieurs automatisations de synchronisation.

## Optimisations

Ces blueprints comportent plusieurs garde-fous pour assurer un bon fonctionnement en cas d’erreur ou d’indisponibilité d’un appareil. Le thermostat FreezBee est synchronisé dès qu’une modification de consigne est enregistrée sur au moins une des vannes thermostatiques associées. Un rafraîchissement toutes les 10 minutes est également en place pour surveiller l’évolution de la température ambiante.

## Bonus : pilotage d’un thermostat générique

Si vous n’avez pas de thermostat FreezBee, une version générique est disponible.
Celle-ci fonctionne avec n’importe quelle entité de type thermostat.
Importez [ce blueprint](./blueprints/valves2thermostat.yaml), puis sélectionnez
le thermostat central et ses vannes. Le thermostat doit exposer les attributs
`current_temperature` et `temperature`, accepter le mode `heat`, ainsi que les
méthodes `climate.set_temperature` et `climate.turn_off`.

Les algorithmes **delta max** et **delta moyen** restent identiques, mais seule
la consigne du thermostat est modifiée :
**consigne = température ambiante du thermostat central + delta calculé**,
arrondie à un chiffre après la virgule. Par exemple, avec une température centrale
de 20 °C et un delta de +2 °C, la consigne envoyée est de 22 °C.

## Licence

Ces blueprints sont distribués sous [licence Apache 2.0](./LICENSE).
Les mentions d'attribution sont disponibles dans [NOTICE](./NOTICE).

## Remerciements

Merci à Aymeric Chessoux ([@achessoux](https://github.com/achessoux)) pour ses retours et la première preuve de concept ayant largement inspiré ce blueprint.

## Contribuer

Le projet utilise [Python 3.14](https://www.python.org/) ainsi que les outils [uv](https://docs.astral.sh/uv/getting-started/installation/) et `make`.

### Lancer les tests

```bash
make test
```

`uv` crée si nécessaire un environnement virtuel `.venv` et installe les versions
de dépendances requises.
