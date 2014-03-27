from bs4 import BeautifulSoup
import requests
import math

def get_prize():
    r = requests.get('http://www.powerball.com/')
    soup = BeautifulSoup(r.content)
    amount_table_content = soup('table')[1].findAll('font', attrs={'size':'6'})
    if len(amount_table_content) < 1:
    	return 0
    full_amount = amount_table_content[0].string
    amount = [int(s.replace('$','')) for s in full_amount.split() if s.replace('$','').isdigit()]
    return amount[0]

def threshold():
    total_choices = math.factorial(59) / (math.factorial(5) * math.factorial(54)) * 35
    return total_choices


