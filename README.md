# Web Scraping des Offres d'Emploi

Ce projet est un simple outil de scraping web pour récupérer des offres d'emploi à partir d'une page web, filtrer les emplois par mot-clé, et afficher les détails de chaque emploi.

## Prérequis

Avant de commencer, assurez-vous d'avoir les bibliothèques suivantes installées :

- `requests`
- `beautifulsoup4`

Vous pouvez installer ces bibliothèques en utilisant pip :

```bash
pip install requests beautifulsoup4
```

## Utilisation

Le script `scraping.py` contient les fonctions nécessaires pour récupérer et afficher les offres d'emploi.

### Fonctions Principales

#### `get_jobs(url, name)`

Récupère les offres d'emploi depuis l'URL spécifiée.

- `url`: L'URL de la page de liste des emplois à scraper.
- `name`: Le terme de recherche pour filtrer les emplois (optionnel).

Retourne une liste de dictionnaires, chaque dictionnaire contenant des détails sur un emploi : titre, entreprise, localisation, et URL de candidature.

#### `print_job_details(job)`

Affiche les détails d'un seul emploi.

- `job`: Un dictionnaire contenant les détails de l'emploi comme le titre, l'entreprise, la localisation, et l'URL de candidature.

#### `print_jobs(jobs)`

Affiche les détails d'une liste d'emplois.

- `jobs`: Une liste de dictionnaires d'emplois, où chaque dictionnaire contient les détails de l'emploi comme le titre, l'entreprise, la localisation, et l'URL de candidature.

### Exemple d'Exécution

Le script principal effectue les actions suivantes :

1. Récupère et affiche toutes les offres d'emploi.
2. Récupère et affiche les offres d'emploi contenant "python" dans leur titre.

Voici comment vous pouvez exécuter le script :

```python
import requests as req
from bs4 import BeautifulSoup as bs

# URL de la page d'offres d'emploi
url_jobs = 'https://realpython.github.io/fake-jobs/'

# Récupération de toutes les offres d'emploi
all_jobs = get_jobs(url_jobs, '')
print('--------- ALL JOBS ---------')
print_jobs(all_jobs)

# Récupération des offres d'emploi pour "python"
python_jobs = get_jobs(url_jobs, 'python')
print('--------- PYTHON JOBS ---------')
print_jobs(python_jobs)
```

### Exemple de Sortie

```plaintext
--------- ALL JOBS ---------
Title: Lead Python Developer
Company: Pay-tech
Location: Springfield
Apply here: https://fake-apply-link.com

Title: Senior Backend Developer
Company: Worksys
Location: New York
Apply here: https://fake-apply-link.com

... [Autres emplois]

--------- PYTHON JOBS ---------
Title: Lead Python Developer
Company: Pay-tech
Location: Springfield
Apply here: https://fake-apply-link.com

... [Autres emplois filtés par "python"]
```

## Auteurs

Ce projet a été développé par [Votre Nom] (Mettre votre nom ou le nom de l'équipe.).

## License

Ce projet est sous licence MIT - voir le fichier `LICENSE` pour plus de détails.