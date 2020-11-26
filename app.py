import requests
import time
import datetime
from bs4 import BeautifulSoup

now = datetime.date.today()
r = requests.get('https://www.trinidadjob.com/latest-job/').text
soup = BeautifulSoup(r, 'lxml')

job_card = soup.find_all('div', class_='grid-content')

def get_all_job_info():

    for index, jobs in enumerate(job_card):
        job_info = jobs.find('div', class_='job-info')
        further_job_info = job_info.find('h3', class_='job-title').a['href']
        job_title = job_info.find('h3', class_='job-title').text
        company = job_info.find('div', class_='company').a.text
        company_info = job_info.find('div', class_='company').a['href']
        company_address_group = job_info.find('div', class_='address').span
        company_locality = company_address_group.find('span', itemprop='addressLocality').text
        company_upload = job_info.find('div', class_='time-ago').text

        with open(f'jobs/{now}-{index}.txt', 'w') as f:
            f.write(f'More information on this job - {further_job_info} \n')
            f.write(f'Job Title - {job_title} \n')
            f.write(f'Company - {company} \n')
            f.write(f'More company info - {company_info} \n')
            f.write(f'Company location - {company_locality} \n')
            f.write(f'Uploaded time - {company_upload} \n')

if __name__ == '__main__':
    while True:
        get_all_job_info()
        pause = 15
        time.sleep(pause * 60)
        print(f'Waiting {pause} minutes before getting more info...')
