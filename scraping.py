import requests as req
from bs4 import BeautifulSoup as bs

# Récupération des élèments HTML contenant les jobs
def get_jobs(url, name):
    status_ok = 200
    response_jobs = req.get(url_jobs)
    if response_jobs.status_code == status_ok:
        # Get HTML from response
        html_jobs = response_jobs.text
        # Parsing HTML with BeautifulSoup
        soup_jobs = bs(html_jobs, 'html.parser')
        # Finding the div containing the jobs
        job_results = soup_jobs.find(id='ResultsContainer')
        # Filter the jobs
        if not name:
            # Finding all the jobs
            job_elements = job_results.find_all('div', class_='card-content')
        else:
            searched_jobs = job_results.find_all(
                "h2", string=lambda text: "python" in text.lower()
            )

            job_elements = [
                h2_element.parent.parent.parent for h2_element in searched_jobs
            ]

        return job_elements


def print_jobs(jobs):
    for job in jobs:
        title = job.find('h2', class_='title').get_text().strip()
        company = job.find('h3', class_='company').get_text().strip()
        location = job.find('p', class_='location').get_text().strip()
        link = job.find('a', string=lambda text: 'apply' in text.lower())
        apply_url = link['href']
        print(f'Title: {title}')
        print(f'Company: {company}')
        print(f'Location: {location}')
        print(f'Apply here: {apply_url}')
        print()

url_jobs = 'https://realpython.github.io/fake-jobs/'

# Printing all the jobs
all_jobs = get_jobs(url_jobs,'')
print('--------- ALL JOBS ---------')
print_jobs(all_jobs)
# Printing Python jobs
python_jobs = get_jobs(url_jobs, 'python')
print('--------- PYTHON JOBS ---------')
print_jobs(python_jobs)








