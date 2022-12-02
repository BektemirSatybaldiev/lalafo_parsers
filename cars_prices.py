import requests, os
import bs4

"""This parser gets information about average price of a few famous car models in Bishkek.
This data may be interesting for car sellers"""

cars_dict = {
    'toyota_ist': 'https://lalafo.kg/kyrgyzstan/avtomobili-s-probegom/prodazha-avtomobiley/toyota/ist?currency=USD&price[from]=4000&price[to]=9000&page={}',
    'toyota_raum': 'https://lalafo.kg/kyrgyzstan/avtomobili-s-probegom/prodazha-avtomobiley/toyota/raum?currency=USD&price[from]=4000&price[to]=9000&page={}',
    'honda_fit': 'https://lalafo.kg/kyrgyzstan/avtomobili-s-probegom/prodazha-avtomobiley/honda-avtomobili-s-probegom/fit?price[from]=4000&currency=USD&price[to]=9000&page={}',
    'toyota_prius': 'https://lalafo.kg/kyrgyzstan/avtomobili-s-probegom/prodazha-avtomobiley/toyota/prius?price[from]=4000&currency=USD&parameters[62][from]=2004&parameters[62][to]=2006&page={}'
}

os.chdir('E:\\Bot\\templates')
result = []
amount_of_cars = 0
for i in range(1, 10):
    site = requests.get(cars_dict['toyota_raum'].format(i))
    pars = bs4.BeautifulSoup(site.text, 'html.parser')
    elems = pars.select('div > p > span')
    for j in elems:
        if str(j).endswith('KGS</span>'):
            result.append(int(str(j)[6:-10].replace(" ", "")))
            amount_of_cars += 1
        elif str(j).endswith('USD</span>'):
            konvertaciya = int(int(str(j)[6:-10].replace(" ", "")) * 84.45)
            result.append(konvertaciya)
            amount_of_cars += 1
average_lalafo_price = int(sum(result) / len(result))
print('Total parsed cars amount =', amount_of_cars)
print('Average price of this model =', average_lalafo_price)
