from calculator import Calculator

initial_balance = float(input('Informe o balance de sua conta (ex: 5000): '))
risk_entry = float(input('Informe a porcentagem do balance que deseja arriscar (ex: 0.25): '))

try:
    option = str(input('Informe o par de moeda (ex: EURUSD): '))

    if not option.isalpha():
        raise ValueError('A entrada so deve conter letras')

    if not len(option) == 6:
        raise ValueError('A string deve conter 6 caracteres')
        
    from_currency = option[:3].upper()
    to_currency = option[3:].upper()

    lot_size_app = Calculator(from_currency, to_currency, initial_balance, risk_entry)
    resultado_lot = lot_size_app.lot_size_calculator(20)

    print(resultado_lot)

except ValueError as e:
    print(f'Erro: {e}')