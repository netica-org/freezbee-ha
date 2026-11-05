# Instructions pour les agents IA

## Python : guillemets

- Utiliser de préférence les guillemets simples pour les chaînes techniques :
  clés, identifiants, chemins, noms de domaines et valeurs de configuration.
- Réserver les guillemets doubles au texte destiné aux humains, typiquement
  rédigé en langue naturelle : messages d'erreur, explications et libellés.

```python
domain = 'automation'
assert blueprints, "Aucun blueprint YAML trouvé"
```
