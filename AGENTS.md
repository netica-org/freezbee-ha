# Instructions pour les agents IA

## Longueur des lignes

- Utiliser une longueur maximale de 100 caractères par ligne plutôt que 80.

## README

- Ne modifier le README que sur demande explicite, ou si les changements le rendent manifestement
  incohérent ou incomplet au point d'empêcher le bon usage du logiciel.

## Python : guillemets

- Utiliser de préférence les guillemets simples pour les chaînes techniques :
  clés, identifiants, chemins, noms de domaines et valeurs de configuration.
- Réserver les guillemets doubles au texte destiné aux humains, typiquement
  rédigé en langue naturelle : messages d'erreur, explications et libellés.

```python
domain = 'automation'
assert blueprints, "Aucun blueprint YAML trouvé"
```

## Commentaires et docstrings

- Privilégier le présent descriptif, qui explique ce que fait le code :
  « prépare une température », « exécute les actions », « vérifie le résultat ».
- Éviter les formulations impératives ou à l'infinitif comme « préparer » ou « faire ».
- Préserver les commentaires existants lorsqu'ils sont clairs et pertinents.
