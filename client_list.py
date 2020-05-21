"""Este primeiro programa apenas procura os vendedores"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time, random, os, csv, datetime


class Sellers:

    # cleaning a file from before
    open ("clients.txt", "w").close ()

    def __init__(self, lista_url):

        for url in lista_url:
            print (url)
            self.url = url

            self.uClient = uReq (self.url)
            self.page_html = self.uClient.read ()
            #self.uClient.close ()  # fecha o pedido anterior qndo eu terminar

            # html parsing
            self.page_soup = soup (self.page_html, "html.parser")

            # grabs each vacancy
            self.containers = self.page_soup.findAll ("span", {"class": "item__brand-title-tos"})

            self.lojas = []
            #self.vendedores = []

            for container in self.containers:
                # Vendedor
                vendedor = container.text[4:].strip ()
                self.lojas.append(vendedor)

                self.lojas = list (dict.fromkeys (self.lojas))  # remover duplicatas

            print (self.lojas)

            with open ("clients.txt", "a") as file:
                for x in self.lojas:
                    file.write ('%s\n' %x)

        self.rearrange()

    def rearrange(self):

        self.vendedores =[]
        # open file and read the content in a list
        with open ('clients.txt', 'r') as filehandle:
            for line in filehandle:
                # remove linebreak which is the last character of the string
                currentPlace = line[:-1]

                # add item to the list
                self.vendedores.append (currentPlace)

            print(len(self.vendedores))
            self.vendedores = list (dict.fromkeys (self.vendedores))  # remover duplicatas
            print (len (self.vendedores))

            print(self.vendedores)

        with open ("clients.txt", "w") as file:
            for i in self.vendedores:
                file.write ('%s\n' % i)


lista_url =[]
with open ('url.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        pular = line[:-1]

        # add item to the list
        lista_url.append (pular)

print(lista_url)

clientes = Sellers(lista_url)
