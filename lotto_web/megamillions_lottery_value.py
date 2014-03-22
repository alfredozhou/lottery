from bs4 import BeautifulSoup
import requests
import math


def get_prize():
    url = 'http://www.megamillions.com'
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    moneyDiv = soup.findAll('div', attrs={'class':'home-next-drawing-estimated-jackpot-dollar-amount'})
    if (moneyDiv is None):
    	return "Unknown"
    amount = moneyDiv[0].string
    return amount

def threshold():
    total_choices = math.factorial(75) / (math.factorial(5) * math.factorial(70)) * 15
    return total_choices

