import requests, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


###CoinGecko HAS THEIR OWN API THAT WOULD MAKE THIS EASIER###
#from pycoingecko import CoinGeckoAPI

TITLE = 'Crypto currency application'
WIDTH = 800
HEIGHT = 400
DEFAULT_CURRENCY = 'sek'
CURRENCY = DEFAULT_CURRENCY

class Market():  
    def __init__(self, given_currency):
        self.currency = given_currency
        params_value = {'vs_currency':self.currency} 
        url_value = "https://api.coingecko.com/api/v3/coins/markets"

        r = requests.get(url = url_value, params = params_value)
        data = r.json()

        self.collection_of_coins = self.fill_colltection2(data)
        self.items_per_key = self.calc_items_per_key()
        self.sort_coins_price_des()

    def calc_items_per_key(self):
        numbr_items = sum(map(len, self.collection_of_coins.values()))/len(self.collection_of_coins)
        return numbr_items

    def fill_collection(self, data):
        temp_list = {}
        for i in data:
            temp_list[i['name']] = i['current_price', 'symbol']
        return temp_list

    def fill_colltection2(self, data):
        temp_list = {}
        for i in data:
            key = i['id']
            temp_list.setdefault(key, [])
            temp_list[key].append(i['name'])
            temp_list[key].append(i['current_price'])
            #{'id': 'usd-coin', 'symbol': 'usdc', 'name': 'USD Coin', 'image': 'https://assets.coingecko.com/coins/images/6319/large/USD_Coin_icon.png?1547042389',
            #'current_price': 8.36, 'market_cap': 70838861305, 'market_cap_rank': 11, 'fully_diluted_valuation': None, 'total_volume': 21508620882, 'high_24h': 8.42,
            #'low_24h': 8.18, 'price_change_24h': 0.06363, 'price_change_percentage_24h': 0.7668, 'market_cap_change_24h': 1111601501,
            #'market_cap_change_percentage_24h': 1.59421, 'circulating_supply': 8534820867.93955, 'total_supply': 8534820867.93955,
            #'max_supply': None, 'ath': 11.28, 'ath_change_percentage': -26.39754, 'ath_date': '2020-03-13T02:35:16.858Z', 'atl': 7.88,
            #'atl_change_percentage': 5.32724, 'atl_date': '2021-01-05T02:00:53.927Z', 'roi': None, 'last_updated': '2021-02-26T07:48:05.819Z'}
            temp_list[key].append(i['market_cap'])
            temp_list[key].append(i['market_cap_rank'])
            temp_list[key].append(i['high_24h'])
            temp_list[key].append(i['low_24h'])
            temp_list[key].append(i['price_change_24h'])
        return temp_list


    def print_collection(self):
        for i in self.collection_of_coins:
            print(i, self.collection_of_coins[i])

    def sort_coins_price_des(self):
        #LINE FOR SORTING WHEN IT WAS ONLY ONE VALUE AND NOT A LIST
        #self.collection_of_coins = dict(sorted(self.collection_of_coins.items(), key=lambda item: item[1], reverse=True))
        self.collection_of_coins = dict(sorted(self.collection_of_coins.items(), key=lambda e: e[1][1], reverse=True))
        
    def sort_coins_price_asc(self):
        #IF THE SORT IS BASED ON OTHER VALUE IN LIST, CHANGE SECOND VALUE IN e[1][HERE]
        self.collection_of_coins = dict(sorted(self.collection_of_coins.items(), key=lambda e: e[1][1]))
        


class Table(QTableWidget):
    def __init__(self, *args):
        super().__init__()
        self.title = 'PyQt5 - QTableWidget'
        self.left = 0
        self.top = 0
        self.width = WIDTH
        self.height = HEIGHT

        self.setWindowTitle(self.title) 
        self.setGeometry(self.left, self.top, self.width, self.height) 
     
        self.m = Market(DEFAULT_CURRENCY)        

        self.create_table() 
   
        self.layout = QVBoxLayout() 
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 

        #Show window 
        self.show()

    def create_table(self):
        self.tableWidget = QTableWidget() 

        self.tableWidget.setRowCount(len(self.m.collection_of_coins)) 

        #Column count 
        self.tableWidget.setColumnCount(self.m.items_per_key)

        self.tableWidget.horizontalHeader().setStretchLastSection(True) 
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setmydata()

        
    def setmydata(self):
        temp_list = [] 
        self.tableWidget.setItem(0,0, QTableWidgetItem("Name")) 
        self.tableWidget.setItem(0,1, QTableWidgetItem("Current price (" + CURRENCY + ")"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Market Cap")) 
        self.tableWidget.setItem(0,3, QTableWidgetItem("Market Cap rank")) 
        self.tableWidget.setItem(0,4, QTableWidgetItem("High 24h"))
        self.tableWidget.setItem(0,5, QTableWidgetItem("Low 24h")) 
        self.tableWidget.setItem(0,6, QTableWidgetItem("Price change 24h"))

        for row, key in enumerate(self.m.collection_of_coins.items()):
            temp_val, temp_list = key
            column = 0
            for value in temp_list:
                
                if isinstance(value, int) or isinstance(value, float):
                    value = str(value)
                newitem = QTableWidgetItem(value)
                self.tableWidget.setItem((row+1), column, newitem)
                column += 1
            
    def setmydata2(self):
        
        for key, value in self.m.collection_of_coins.items():
            print(key, value)

    def setmydata3(self):
        my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
        #for row in zip(*([key] + (value) for key, value in sorted(self.m.collection_of_coins.items()))):
        #    print(*row)
        #self.setmydata()
        for key, value in sorted(self.m.collection_of_coins.items(), key=lambda e: e[1][2]):
            print(key, value)




def main(args):
    app = QApplication(args)
    a = Table(150, 150)
    a.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main(sys.argv)



