from calculator import Calculator
from currency import find_currency

class Menu:
    def __init__(self):
        self.balance = None
        self.risk = None
        self.stoploss = None
        self.currency = None

    # Definindo o balance
    def get_balance(self):
        try:
            self.balance = float(input('Informe o balance de sua conta (ex: 5000): '))

            if not isinstance(self.balance, float):
                raise ValueError('A entrada deve conter numeros')
    
        except ValueError as error:
            print(f'Erro: {error}')

    # Definindo o risco de cada operação
    def get_risk(self):
        try:
            self.risk = float(input('Informe a porcentagem do balance que deseja arriscar (ex: 0.25): '))

            if not isinstance(self.risk, float):
                raise ValueError('A entrada deve conter numeros')
    
        except ValueError as error:
            print(f'Erro: {error}')

    # Definindo qual o tamanho do stoploss
    def get_stoploss(self):
        try:
            self.stoploss = int(input('Informe o valor do stop (em pips. Ex: 40): '))

            if not isinstance(self.stoploss, int):
                raise ValueError('A entrada deve conter numeros')
            
        except ValueError as error:
            print(f'Erro: {error}')

    # Definindo de qual moeda queremos buscar a cotação
    def get_currency(self):
        try:
            self.currency = str(input('Informe o par de moeda (ex: EURUSD): '))

            if not self.currency.isalpha():
                raise ValueError('A entrada so deve conter letras')

            if not len(self.currency) == 6:
                raise ValueError('A string deve conter 6 caracteres')
                
            from_currency = self.currency[:3].upper()
            to_currency = self.currency[3:].upper()

            if find_currency(from_currency, to_currency):
                lot_size_app = Calculator(from_currency, to_currency, self.balance, self.risk)
                resultado_lot = lot_size_app.lot_size_calculator(self.stoploss)

                print(resultado_lot)
            else:
                exit()

        except ValueError as e:
            print(f'Erro: {e}')

    # Menu de opções
    def show_option(self):
        print('1. Calcular')
        print('2. Sair')

    # Executando as opções
    def execute_options(self, option):
        # A opção 1 chama todas as funções na ordem exata que precisa ser calculada
        if option == '1':
            self.get_balance()
            self.get_risk()
            self.get_stoploss()
            self.get_currency()
        elif option == '2':
            print('Saindo...')
        else:
            print('Opção inválida')
            return True
        
    def run_menu(self):
        while True:
            self.show_option()
            option = input('Informe a sua escolha: ')
            if not self.execute_options(option):
                break

if __name__ == '__main__':
    menu = Menu()
    menu.run_menu()