import requests

class Calculator:
    def __init__(self, from_currency, to_currency, balance, risk):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.balance = balance
        self.risk = risk
        self.value = None
        self.pattern_lot = None

    # Decide automaticamente qual é o lote padrão usado, a partir do balance inicial
    def lot_type(self):
        if self.balance > 10000:
            self.pattern_lot = 100000
        elif self.balance >= 1000 and self.balance <= 10000:
            self.pattern_lot = 10000
        elif self.balance < 1000:
            self.pattern_lot = 1000

        return self.pattern_lot

    # Função que calcula o valor do pip, com base na cotação atual
    def pip_value(self, pip=0.0001):
        url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={self.from_currency}&to_currency={self.to_currency}&apikey=CDSPQWSYJ6J9EXA4'
        response = requests.get(url)
        data = response.json()

        # Verificando se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Convertendo o resultado para JSON
            data = response.json()
        
            # Extraindo a cotação atual do par de moedas
            exchange_rate = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        else:
            print("Falha na requisição")

        self.value = (pip / float(exchange_rate)) * self.pattern_lot

        return self.value

    # Função que calcula o lote para a operação
    def lot_size_calculator(self, stop_loss):
        lot_size = (self.balance * (self.risk / 100)) / stop_loss * self.value
        return lot_size
    

if __name__ == '__main__':
    initial_balance = 5000
    percentage_per_trade = 0.25

    lot_size_app = Calculator('EUR', 'USD', initial_balance, percentage_per_trade)
    resultado_pattern_lot = lot_size_app.lot_type()
    resultado_pip = lot_size_app.pip_value()
    resultado_lot = lot_size_app.lot_size_calculator(20)

    print(resultado_pattern_lot)
    print(resultado_pip)
    print(resultado_lot)

