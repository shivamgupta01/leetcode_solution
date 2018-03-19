import requests
from bs4 import BeautifulSoup
import hashlib

def calculateSHA256(url,email):


    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    body = soup.find('body').get_text()
    print body
    hash_object = hashlib.sha256((body + email).encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


if __name__ == '__main__':
    print "the Hash Value of (Body || Email): " + str(calculateSHA256("https://truveris.github.io/jobs/","shivamgupta01@gmail.com"))
