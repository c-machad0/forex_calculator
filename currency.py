import pandas as pd

def find_currency(from_currency, to_currency):
    table = pd.read_csv('physical_currency_list.csv')

    # Verifica se ambos os códigos de moeda estão na coluna 'currency code'
    exists_from = not table.loc[table['currency code'] == from_currency].empty
    exists_to = not table.loc[table['currency code'] == to_currency].empty

    # Retorna True se ambos os códigos forem encontrados; caso contrário, retorna False
    return exists_from and exists_to