from utilites import format_datetime, get_country_name_by_code
import requests, config


class orders_manager:
    url = config.endpoints['orders_endpoint']  
    headers = {"Authorization": config.WB_TOKEN}   

    def __init__(self):
        self.update_orders_data()

    def is_there_any_order(self):
        self.update_orders_data()
        return len(self.orders) != 0 

    def is_there_new_order(self):
        new_orders = self.get_orders_data()
        new_orders_quantity = len(new_orders)
        old_orders_quantity = len(self.orders)
        if new_orders_quantity > old_orders_quantity:
            self.orders = new_orders
            return True
        elif new_orders_quantity == 0 and old_orders_quantity != 0:
            self.orders = new_orders
        return False

    def update_orders_data(self):
        self.orders = self.get_orders_data()

    def get_orders_data(self):
        response = requests.get(self.url, headers=self.headers)
        data = response.json()
        orders = data['orders']
        orders.reverse()
        return orders

    def get_orders_text(self):
        self.update_orders_text()
        return self.order_text

    def update_orders_text(self):
        indexes=[]
        cities=[]
        prices=[]
        datesandtimes=[] 
        amount = len(self.orders)
        is_single_order = len(self.orders)==1

        self.order_text = f'🟩 You have {"a" if is_single_order else amount} new ' \
        f'{"order" if is_single_order else "orders"} 📤🛒🛍️'

        for i in range(len(self.orders)):
            country_name = get_country_name_by_code(self.orders[i]['currencyCode']) 
            indexes.append(i)
            cities.append(country_name)
            prices.append(self.orders[i]['convertedFinalPrice'] // 100)
            datesandtimes.append(format_datetime(self.orders[i]['createdAt']))

        for i in range(len(self.orders)):
            self.order_text += f'\n\n{indexes[i]+1}.\n'
            self.order_text += f'🌍 City ` {cities[i]}\n'
            self.order_text += f'💸 Price ` {prices[i]} dram\n'
            self.order_text += f'🕒 Date&time ` {datesandtimes[i]}'