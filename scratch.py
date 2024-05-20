import requests
from bs4 import BeautifulSoup


IT_URL='https://www.linkedin.com/jobs/search/?currentJobId=3921610216&keywords=aws%20internship&originalSubdomain=in'
#doesnot execute java Script
res=requests.get(IT_URL)

print('Status_code:',res.status_code)

with open('Intern.html','w') as f:
  f.write(res.text)

doc =BeautifulSoup(res.text,'html.parser')
print('Page title:',doc.title.text)

#find all the job divs

job_div=doc.find_all('div',class_='base-card__content')

print(f'Found {len(job_div)} jobs')
