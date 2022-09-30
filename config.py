class APIConfig:
    def __init__(self):
        self.api_key = "cr0JzXI38aKZUS2OA3"
        self.api_secret = "O4Yjn3vVuJt7hnIv26xVi0wY3hkyI8Gh7D4T"
        self.api_passphrase = "YOUR_API_PASSPHRASE"
        self.api_url = "https://api.pro.coinbase.com"
        self.api_websocket = "wss://ws-feed.pro.coinbase.com"
    
    def get_api_key(self):
        return self.api_key
    
    def get_api_secret(self):
        return self.api_secret
    
    def get_api_passphrase(self):
        return self.api_passphrase
    
    def get_api_url(self):
        return self.api_url