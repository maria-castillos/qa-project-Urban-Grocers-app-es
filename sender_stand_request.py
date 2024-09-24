import configuration
import requests
import data

#Funcion para crear un usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

#Funcion para obtener el token de autenticacion
def get_new_user_token():
    user = post_new_user(data.user_body)
    user_json = user.json()
    return user_json['authToken'] #Extrae y devuelve el token de autenticacion


#Funcion para crear un nuevo kit personal para usuario o usuaria
def post_new_client_kit(kit_body): #CORRECION SE AGREGO KIT_BODY DENTRO DE LA FUNCION
    token = get_new_user_token() #CORRECCION
    headers = data.headers.copy() #CORRECCION
    headers['Authorization'] = f'Bearer {token}'
    return requests.post(configuration.URL_SERVICE + configuration.NEW_CLIENTE_KIT_PATH,
                    json= kit_body,
                     headers = headers)  #CORRECION

response = post_new_client_kit(data.kit_body)
print(response.json())
