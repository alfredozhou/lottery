from bs4 import BeautifulSoup
import requests
import math


def get_prize(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content)

    amount = soup.findAll('div', attrs={'class':'home-next-drawing-estimated-jackpot-dollar-amount'})[0].string
    unit = soup.findAll('div', attrs={'class':'home-next-drawing-estimated-jackpot-million'})[0].string
    draw_date = soup.findAll('div', attrs={'class':'home-next-drawing-estimated-jackpot-date'})[0].div.contents[4]
    return amount, unit, draw_date

def worth_it():
    mega_prize, prize_unit, date = get_prize('http://www.megamillions.com/')
    total_choices = math.factorial(75) / (math.factorial(5) * math.factorial(70)) * 15
    amount = int(mega_prize) * 1000000
    return amount > total_choices

