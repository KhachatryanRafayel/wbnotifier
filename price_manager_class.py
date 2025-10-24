import utilites, textwrap, requests, config as cnfg

class price_manager:
    config = cnfg
    def __init__(self):
        self.update_price_am_both_suppliers()
        self.update_discounds()

    def get_price_text(self):
        self.update_price_am_both_suppliers()
        self.update_price_ru_both_suppliers()

        price_text = textwrap.dedent(f'''
        🟨
        In Armenia 🇦🇲
            - Official supplier price {self.price_am_offic} drams 💸
            - Secondary supplier price {self.price_am_secnd} drams 💸
        In Russia 🇷🇺
            - Official supplier price {self.price_ru_offic} drams 💸
            - Secondary supplier price {self.price_ru_secnd} drams 💸''')
        return price_text

    def get_price_change_text(self):
        new_price_am_secnd = self.get_price('secondary', 'am')
        new_seller_discount, new_wb_discount = self.get_discounts()

        message = textwrap.dedent(f'''
        🟨
        The price has changed. 🔄
        Region - Armenia 🇦🇲         
        It was `  {self.price_am_secnd} drams ({self.seller_disount}% seller {self.wb_discount}% wb) 🏷️
        It became `  {new_price_am_secnd} drams ({new_seller_discount}% seller {new_wb_discount}% wb) 🏷️
        ''')

        self.update_price_am_both_suppliers()
        self.update_discounds()

        return message


    def get_secondary_price_lower_official_price_text(self):

        self.update_price_ru_both_suppliers()

        message = textwrap.dedent(f'''
        🟥
        The new price is lower than the price of the official supplier.՝
        Region - Russia 
        Price of the second supplier՝   {self.price_ru_secnd} 📈 💸
        Price of the official supplier՝ {self.price_ru_offic} 📉 💸
        Raise the price!⬆⬆⬆
        ''')

        return message
    

    def update_price_am_both_suppliers(self):
        self.price_am_secnd = self.get_price('secondary', 'am')
        self.price_am_offic = self.get_price('official', 'am')


    def update_discounds(self):
        discounts = self.get_discounts()
        self.seller_disount = discounts[0]
        self.wb_discount = discounts[1]


    def update_price_ru_both_suppliers(self):
        self.price_ru_secnd = self.get_price('secondary', 'ru')
        self.price_ru_offic = self.get_price('official', 'ru')


    def get_price(self, supplier='secondary', region='am'):
        endpointtemplate = self.config.endpoints[f'price_{region}_template_endpoint']
        item_number = self.config.item_numbers[supplier]
        url = f'{endpointtemplate}' \
        f'{item_number}'
        
        response = requests.get(url)
        data = response.json()

        price_dict = data['products'][0]['sizes'][0]['price']

        price_cents = price_dict['product'] + price_dict['logistics']

        price_dram = price_cents // 100

        return price_dram
    

    def get_discounts(self):
        price = self.price_am_secnd
        url = self.config.endpoints['price_seller_endpoint']
        headers = {"Authorization": self.config.WB_TOKEN,}
        response = requests.get(url, headers=headers)
        data = response.json()
        good = data['data']['listGoods'][0]
        seller_discount = good['discount']
        exchange_rate = utilites.get_exchange_rate('AMD', 'RUB')
        seller_discount_price = good['sizes'][0]['discountedPrice']
        wb_discount = int( (1 - (price*exchange_rate / seller_discount_price) ) * 100 )
        return (seller_discount, wb_discount)
    
    def is_price_changed(self):
        new_price_am_secnd = self.get_price('secondary', 'am')
        return new_price_am_secnd != self.price_am_secnd
    
    def is_secondary_price_lower_official_price(self):
        self.update_price_ru_both_suppliers()
        return self.price_ru_secnd < self.price_ru_offic