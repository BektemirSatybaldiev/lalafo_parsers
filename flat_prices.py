import bs4, requests, os, re

"""This parser gets average price, amount and 1 meter price of flat in micro-regions
and center of Bishkek"""

os.chdir('E:\\Bot\\templates')

flat_dict = {
    '1_mkr': 'https://lalafo.kg/bishkek/kvartiry/1-bedroom/10-mkr/11-mkr/12-mkr/3-mkr/4-mkr/5-mkr/6-mkr/7-mkr/8-mkr/9-mkr?currency=USD&price[from]=10000&page={}',
    'centr': 'https://lalafo.kg/bishkek/kvartiry/1-bedroom/filarmoniya/mossovet/azija-moll/ak-keme-staryj-ajeroport/beta-stores-2/bishkek-park-trc/dvorec-sporta/karavan-trc/knu?currency=USD&price[from]=10000&page={}',
}
result = []
amount_of_flats = 0
temp = re.compile(r'\d\d\s+м²')
kv = []
for i in range(1, 10):
    flat_site = requests.get(flat_dict['1_mkr'].format(i))
    pars = bs4.BeautifulSoup(flat_site.text, 'lxml')
    elems = pars.select('div > p > span')
    square = pars.select('div > a.adTile-title')
    for j in elems:
        if str(j).endswith('USD</span>'):
            result.append(int(str(j)[6:-10].replace(" ", "")))
            amount_of_flats += 1
        elif str(j).endswith('KGS</span>'):
            konvertaciya = int(int(str(j)[6:-10].replace(" ", "")) / 84.45)
            result.append(konvertaciya)
            amount_of_flats += 1
    for k in square:
        res = temp.findall(str(k))
        try:
            kv.append(int(str(res)[2:4]))
        except:
            ValueError

average_lalafo_square = int(sum(kv) / len(kv))
average_lalafo_price = int(sum(result) / len(result))
square_meter_price = int(average_lalafo_price/average_lalafo_square)
print('Total parsed flat amount =', amount_of_flats)
print('Average price of flat =', average_lalafo_price)
print('Average square =', average_lalafo_square)
print('1 square meter price =', square_meter_price)
