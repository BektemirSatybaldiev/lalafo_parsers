import bs4, requests, os, re

"""This parser gets average rent price of 1room apartment in Bishkek"""

os.chdir('E:\\Bot\\templates')

flat_dict = {
    '1_kom': 'https://lalafo.kg/bishkek/kvartiry/arenda-kvartir/1-bedroom?currency=KGS&price[from]=12000'
}
result = []
amount_of_flats = 0
temp = re.compile(r'\d\d\s+м²')
for i in range(1, 10):
    flat_site = requests.get(flat_dict['1_kom'].format(i))
    pars = bs4.BeautifulSoup(flat_site.text, 'html.parser')
    elems = pars.select('div > p > span')
    for j in elems:
        if str(j).endswith('KGS</span>'):
            result.append(int(str(j)[6:-10].replace(" ", "")))
            amount_of_flats += 1
        elif str(j).endswith('USD</span>'):
            konvertaciya = int(int(str(j)[6:-10].replace(" ", "")) * 84.45)
            result.append(konvertaciya)
            amount_of_flats += 1
    

average_rent_price = int(sum(result) / len(result))
print('Amount of flats =', amount_of_flats)
print('Average rent price =', average_rent_price)

