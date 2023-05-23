from bs4 import BeautifulSoup

with open('./home.html', 'r') as html_file :

    content = html_file.read()
    # print(content)

    soup= BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    tag=soup.find('h5')  # find h5 tag first one
    tags= soup.find_all('h5') # find all h5 tags
    # print(tag) 

    for tag in tags:
        print(tag.text) 

    cards=soup.find_all('div', class_='cards') # add _ to class world becouse it's reversed to python

    for card in cards:
        name=card.h5.text
        price=card.a.text.split()[-1]

        print(f'{card} cost {price}')

        
        




