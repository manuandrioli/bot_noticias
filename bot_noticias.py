from bs4 import BeautifulSoup
import requests
import re
import tweepy
from twitter_keys import *
import openai
from PIL import Image
import asyncio
from sustituir_funcion import *


########################### autenticación ###################################
autenticador = tweepy.OAuthHandler(API_key, API_key_secret)
auth = tweepy.OAuth2BearerHandler(bearer_token=bearer_token_key)
autenticador.set_access_token(Access_token,Access_token_secret)

api = tweepy.API(autenticador, wait_on_rate_limit=True)
client = tweepy.Client(consumer_key= API_key,consumer_secret= API_key_secret,access_token= Access_token,access_token_secret= Access_token_secret,bearer_token=bearer_token_key)

########################### requests, beautiful soup  ##################################################
HEADERS = { 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }

pagina = requests.get('https://www.infobae.com/ultimas-noticias/',headers=HEADERS).text
soup = BeautifulSoup(pagina, 'lxml')
noticias = soup.find_all('a',class_="feed-list-card")
noticia=soup.find('a',class_='feed-list-card feed-list-card-first')
#titulo = noticia.find('h2', class_='feed-list-card-headline-lean feed-list-card-headline-lean-first').text
#descripcion = noticia.find('div',class_='deck deck-first').text
#imagen = noticia.find('img',class_='feed-list-image feed-list-image-first lazyload').attrs['src']

""" bot_perfil = requests.get('https://twitter.com/bot_noticiasx', headers=HEADERS).text
soup2 = BeautifulSoup(bot_perfil,'lxml')
tweets_bot=soup2.find_all('span',class_='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0') """


##########################################################################

#  OPEN AI
openai.api_key = API_secret_openai

def generar_imagen_openAI(texto): #función para generar una imagen con OpenAI
  res = openai.Image.create(
    prompt=texto,
    n=1,
    size="256x256",
  )
  return res["data"][0]["url"]

######################################################################################

#loop de todas las noticias para comparar la noticia original con la sustituída y evitar que se tuitee una noticia sin modificaciones. si hay una sustitución se tuitea y termina el for, sino se sigue buscando más noticias.
for noti in noticias:
    
    titulo = noti.h2.text
    #descripcion = noti.find('div',class_='deck').text
    descripcion = noti.div.div.text
    link_noti='https://www.infobae.com'+noti['href']
    """ for tweet_bot in tweets_bot:
        print(tweet_bot.text)
        if tweet_bot.text == sustituir(titulo) or tweet_bot.text == sustituir(descripcion):
            continue
        else:
            pass """
    if (not sustituir(titulo) == titulo ) and (not sustituir(descripcion) == descripcion) :
        break
    
###############################################################################################################

texto_tweet = sustituir(titulo) + '\n' + '\n' + sustituir(descripcion) #tweet completo con título y descripción
print(texto_tweet)

try: #try de generar la imagen, ya que en algunas ocasiones los títulos contienen palabras explícitas y OpenAI no permite esos prompts
    url1 = generar_imagen_openAI(sustituir(titulo)) #genera una imagen con la IA de OpenAI, usando el título de prompt
except (openai.InvalidRequestError):
    pass
respuesta = requests.get(url1)

if respuesta.status_code == 200:
        with open('imagen_IA.jpg', 'wb') as image:
            for chunk in respuesta:
                image.write(chunk)

media = api.media_upload(filename='imagen_IA.jpg')




""" if (not sustituir(titulo) == titulo ) and (not sustituir(descripcion) == descripcion): 
    #si hubo un cambio en título y descripción twittea

    if len(texto_tweet) < 280: 
        #si contando el título y la descripción no se pasa caracteres máximos permitidos por twitter, twittea ambos
        tweet = client.create_tweet(text=texto_tweet,media_ids= 
            [media.media_id_string]) 
    else: #sino, twittea sólo el título
        tweet = client.create_tweet(text=sustituir(titulo),media_ids= 
                [media.media_id_string])
        

tweetId = tweet.data['id'] #guarda el id del tweet

client.create_tweet(text=f'Noticia original: {link_noti}', in_reply_to_tweet_id=tweetId) #responde al tweet con la noticia original """