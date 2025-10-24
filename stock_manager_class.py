import requests, config

class stock_manager:
    url = config.endpoints['stock_endpoint']
    headers = {
        "Content-Type": "application/json",
        "Authorization": config.WB_TOKEN_POST
    }
    data = {
        "skus": [config.item_barcode]
    }

    def __init__(self):
        self.update_remaining()

    def get_remaining_text(self):
        self.update_remaining()
        if self.remaining:
            itemoritems = 'item' if self.remaining==1 else 'items'
            text = f'{self.remaining} {itemoritems} left in stock. 📦'
        else:
            text = self.get_no_remaining_text()
        return text
            
    @staticmethod
    def get_no_remaining_text():
        return 'There are no more goods in stock, don\'t forget to restock. ✍️'
    
    def is_remaining_products(self):
        self.update_remaining()
        return self.remaining
    
    def update_remaining(self):
        response = requests.post(self.url, headers=self.headers, json=self.data)
        data = response.json()
        self.remaining = data['stocks'][0]['amount']