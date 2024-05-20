import os
import smtplib
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

IT_URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3921610216&keywords=aws%20internship&originalSubdomain=in'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(IT_URL)
  return driver

def get_intern(driver):
  driver.get(IT_URL)
  parent_element = driver.find_element(By.CLASS_NAME, 'jobs-search__results-list')
  job_div='base-search-card__info'
  jobs = parent_element.find_elements(By.CLASS_NAME, job_div)
  return jobs

def parse(intern):
  title_element_tag = intern.find_element(By.CSS_SELECTOR, 'h3.base-search-card__title')
  title_element=title_element_tag.text

  parent_anchor = intern.find_element(By.XPATH, '..').find_element(By.TAG_NAME, 'a')
  url=parent_anchor.get_attribute('href')

  photo_tag= intern.find_element(By.XPATH, '..').find_element(By.TAG_NAME,'img')
  photo_url=photo_tag.get_attribute('src')

  company_element = intern.find_element(By.CSS_SELECTOR, 'h4.base-search-card__subtitle').text

  location_element = intern.find_element(By.CSS_SELECTOR, 'span.job-search-card__location').text

  date_details = intern.find_element(By.CSS_SELECTOR, 'time.job-search-card__listdate').text

  
  return{
    'job title':title_element,
    'company':company_element,
    'company url':url,
    'photo url':photo_url,
    'location':location_element,
    'date':date_details
  }

def send_email(body):
  try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo() 
  
    SENDER_EMAIL = 'top.intern.info@gmail.com'
    RECEIVER_EMAIL = 'top.intern.info@gmail.com'
    #SENDER_PASSWORD = os.environ['GMAIL_PASSWORD']
    subject = 'Internships at AWS'
    
    SENDER_PASSWORD = os.environ['GMAIL_PASSWORD']

    email_text = f"""
    From: {SENDER_EMAIL}
    To: {RECEIVER_EMAIL}
    Subject: {subject}

    {body}
    """

    server_ssl.login(SENDER_EMAIL, SENDER_PASSWORD)
    server_ssl.sendmail(SENDER_EMAIL,RECEIVER_EMAIL,email_text)
    print('mail sent to',RECEIVER_EMAIL)
    
  except:
    print('Something went wrong...')
  

if __name__=="__main__":
    print('Creating Driver')
    driver = get_driver()
    

    print('Fetching the Internships')
    internship=get_intern(driver)
    
    print(f'Found {len(internship)} internships')

    print('Printing the top 10 internship')
  #job title,company name,place,hiring status,date,photo
    int_data=[parse(intern) for intern in internship[:10]]
   # intern=internship[0]
    #print(int_data)
    print('save to csv')
    intern_df=pd.DataFrame(int_data)
    print(intern_df)
    intern_df.to_csv('internship.csv')
    print("Send the results over email")
    body = json.dumps(int_data, indent=2)
    send_email(body)

    print('Finished..')
    print('Mail Finished..')
    
  
    

  
    