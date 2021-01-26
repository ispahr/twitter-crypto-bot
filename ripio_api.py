import datos_ripio as r
import requests

def precios (url_base) -> str:
    pairs = ['BTC_USDC', 'BTC_ARS', 'ETH_USDC', 'ETH_ARS', 'USDC_ARS']
    datos = []
    for pair in pairs:
        obtener_todas = url_base+f'rate/{pair}/'
        res = requests.get(obtener_todas, headers = {'Content-Type': 'application/json'}).json()
        datos.append(f"{res['pair'].ljust(17)}{res['last_price'].ljust(17)}{res['variation']}")
    
    message = f"""{'Pair'.ljust(24)}{'Last Price'.ljust(16)}Variation
{datos[0]}
{datos[1]}
{datos[2]}
{datos[3]}
{datos[4]}"""
    return message