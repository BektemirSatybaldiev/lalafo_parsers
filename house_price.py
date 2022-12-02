import requests, bs4

"""This parser gets average price of house in elite regions of Bishkek"""

house_dict = {
    'elite_house': 'https://lalafo.kg/bishkek/doma-i-dachi/prodazha-domov/house/ortosajskij-rynok/rajon-bgu/filarmoniya/politekh/kirgiziya/zhilgorodok/p-23249-asanbaj/yug-2/med-akademiya/ak-keme-staryj-ajeroport/ata-tjurk-park/beta-stores-2/bishkek-park-trc/dvorec-sporta/knu/ala-archa-tc?parameters[71][from]=4&parameters[71][to]=12&currency=USD&price[from]=15000&page={}'
}
result = []
amount_of_house = 0
for i in range(1, 10):
    site = requests.get(house_dict['elite_house'].format(i))
    soup = bs4.BeautifulSoup(site.text, 'lxml')
    elems = soup.select('div > p > span')
    for j in elems:
        if str(j).endswith('KGS</span>'):
            result.append(int(str(j)[6:-10].replace(' ', '')) / 84.45)
            amount_of_house += 1
        elif str(j).endswith('USD</span>'):
            result.append(int(str(j)[6:-10].replace(' ', '')))
            amount_of_house += 1
average_house_price = int(sum(result)/len(result))

print('Amount of houses =', amount_of_house)
print('Average house price =', average_house_price)


