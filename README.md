# 🌐 Image Host with Logging 📸

Ce projet est un mini-serveur web en Python qui permet d'héberger une image et de la rendre accessible publiquement à toute personne possédant le lien. Chaque visite est enregistrée avec son adresse IP et l'heure d'accès dans un fichier de logs `log.txt` ! 

## 🚀 Fonctionnalités

- Affiche une image PNG en ligne sans téléchargement direct.
- Enregistre chaque visite avec l'adresse IP et l'heure dans un fichier de logs.
- Accessible publiquement si configuré avec l'IP publique.

## 📋 Prérequis

- **Python 3** doit être installé.
- **Flask** doit être installé :
  ```bash
  pip install flask
