from http.client import responses

import configuration
import requests
import data
from data import headers, kit_body


#Funcion para crear un usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

#Funcion para obtener el token de autenticacion
def authe_token():
    user = post_new_user(data.user_body)
    user_json = user.json()
    return user_json ['authToken'] #Extrae y devuelve el token de autenticacion

token = authe_token()

#Funcion para crear un nuevo kit personal para usuario o usuaria
def post_new_client_kit():
    headers_kit = data.headers.copy()
    headers_kit.update({"Authorization":f'Bearer {token}'})
    return requests.post(configuration.URL_SERVICE + configuration.NEW_CLIENTE_KIT_PATH,
                    json= kit_body,
                     headers = headers_kit)

response = post_new_client_kit()
print(response.json())

