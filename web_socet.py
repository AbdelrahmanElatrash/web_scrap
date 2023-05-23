from bs4 import BeautifulSoup
import requests 


html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
print(html_text)

soup=BeautifulSoup(html_text,'lxml')

#  inspect the page then find tags you want to extract

job=soup.find('li', class_='clearfix job-bx wht-shd-bx')

comp_name=job.find('h3' , class_='joblist-comp-name').text.replace(' ','')
skills=job.find('span', class_='srp-skills')
print(comp_name)
