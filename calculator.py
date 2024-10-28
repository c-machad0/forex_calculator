import requests

# Decorador que chama as funções auxiliares antes da função principal 'lot_size_calculator_
def setup_calculator(function):
    def wrapper(calc, *args, **kwargs):
        calc.lot_type()
        calc.pip_value()
        return function(calc, *args, **kwargs)
    return wrapper

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
        else:
            self.pattern_lot = 1000

    # Função que calcula o valor do pip, com base na cotação atual
    def pip_value(self):
        url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={self.from_currency}&to_currency={self.to_currency}&apikey=CDSPQWSYJ6J9EXA4'
        response = requests.get(url)

        # Verificando se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Convertendo o resultado para JSON
            data = response.json()
            if self.to_currency == 'JPY':
                pip = 0.01
            else:
                pip = 0.0001
        
            # Extraindo a cotação atual do par de moedas
            exchange_rate = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
            
            self.value = (pip / float(exchange_rate)) * self.pattern_lot
        else:
            print("Falha na requisição")

    # Função que calcula o lote para a operação
    @setup_calculator
    def lot_size_calculator(self, stop_loss):
        lot_size = (self.balance * (self.risk / 100)) / stop_loss * self.value
        return f'Lote sugerido: {lot_size}'
    
if __name__ == '__main__':
    pass