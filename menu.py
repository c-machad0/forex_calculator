from calculator import Calculator
from currency import find_currency

try:
    initial_balance = float(input('Informe o balance de sua conta (ex: 5000): '))

    if not initial_balance.is_integer():
        raise ValueError('A entrada deve conter numeros')
    
except ValueError as error:
    print(f'Erro: {error}')
    exit()
except Exception:
    print(f'Erro não reconhecido')

try:
    risk_entry = float(input('Informe a porcentagem do balance que deseja arriscar (ex: 0.25): '))

    if not initial_balance.is_integer():
        raise ValueError('A entrada deve conter numeros')
    
except ValueError as error:
    print(f'Erro: {error}')
    exit()
except Exception:
    print(f'Erro não reconhecido')

try:
    option = str(input('Informe o par de moeda (ex: EURUSD): '))

    if not option.isalpha():
        raise ValueError('A entrada so deve conter letras')

    if not len(option) == 6:
        raise ValueError('A string deve conter 6 caracteres')
        
    from_currency = option[:3].upper()
    to_currency = option[3:].upper()

    if find_currency(from_currency, to_currency):
        lot_size_app = Calculator(from_currency, to_currency, initial_balance, risk_entry)
        resultado_lot = lot_size_app.lot_size_calculator(20)

        print(resultado_lot)
    else:
        exit()

except ValueError as e:
    print(f'Erro: {e}')
    exit()
except Exception:
    print(f'Erro não reconhecido')
    exit()