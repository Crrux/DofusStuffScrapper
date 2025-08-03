# DofusStuffScrapper

Ce projet permet de récupérer automatiquement des données depuis les sites **dofusdb** et **dofusbook** afin de compiler les composants de craft des items dans un fichier Excel.

## Fonctionnalités
- Scraping des informations d'items et de recettes depuis dofusdb et dofusbook
- Génération d'un fichier Excel listant les composants nécessaires pour crafter chaque item

## Prérequis
- Python 3.10 ou supérieur
- Les dépendances listées dans `requirements.txt`

## Installation
1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/Crrux/DofusStuffScrapper.git
   ```
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation
Lancez le script principal pour générer le fichier Excel :
```bash
python DofusStuffScrapper.py
```

Un fichier Excel sera généré avec la liste des items et leurs composants de craft.

## Remarques
- Le projet utilise des modules comme `bs4` (BeautifulSoup) pour le scraping web.

## Auteurs
- Projet réalisé par Crrux

