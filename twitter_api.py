import tweepy
import credentials as c
import datos_ripio as d
import ripio_api as r
import time

def create_api():
    auth = tweepy.OAuthHandler(c.API_KEY, c.API_SECRECT_KEY)
    auth.set_access_token(c.ACCESS_TOKEN, c.ACCESS_SECRET)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
    except Exception as e:
        print(f'Error asl crear la API: {e}')
    return api
    
def tweetear(mensaje, api):
    try:
        api.update_status(mensaje)
    except Exception as e:
        print(f'Error al enviar el Tweet: {e}')

if  __name__ == '__main__':
    api = create_api()
    while True:
        mensaje = r.precios(d.URL_BASE)
        tweetear(mensaje, api)
        time.sleep(120)