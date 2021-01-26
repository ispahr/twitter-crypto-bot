# Crypto Bot

## @parrita_bot

## Funcionamiento
Mediante al API de Ripio Exchange y de Twitter este bot twittea los precios de algunas monedas cada 30 minutos.

Las claves de acceso a la API de Twitter se pasan como variables de entorno con el módulo os.environ con los siguientes nombres:
#
API_KEY =

API_SECRECT_KEY = 

ACCESS_TOKEN

ACCESS_SECRET 
#
## Requirements
Es recomendable crear un entorno virtual para instalar las librerias y así evitar problemas de incompatibilidad.
- Requests
- Tweepy

## Documentación
Documentación a la API de Ripio Exchange: 
Documentación a la API de Twitter:

## Aclaraciones
Los archivos Procfile y runtime.txt son para poder hacer el deploy a Heroku. No son parte del proyecto

