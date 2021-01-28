import tweepy
import os
import datos_ripio as d
import ripio_api as r
import time

def create_api():
    auth = tweepy.OAuthHandler(os.environ.get('API_KEY'), os.environ.get('API_SECRECT_KEY'))
    auth.set_access_token(os.environ.get('ACCESS_TOKEN'), os.environ.get('ACCESS_SECRET'))
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
    except Exception as e:
        print(f'Error al crear la API: {e}')
    return api
    
def twittear(mensaje, api):
    try:
        api.update_status(mensaje)
    except tweepy.TweepError as e:
        error = str(e)
        if '187' in error: #Status is duplicate        
            api.update_status(mensaje+'\nD')
        else:
            print(f'Error al enviar el Tweet: {e}')

if  __name__ == '__main__':
    api = create_api()
    while True:
        mensaje = r.precios(d.URL_BASE)
        twittear(mensaje, api)
        time.sleep(60*30)