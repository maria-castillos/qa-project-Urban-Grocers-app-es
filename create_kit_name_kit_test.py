import sender_stand_request
import data


# Función para cambiar el valor del parámetro name en el cuerpo de la solicitud
def get_kit_body(name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_body

# Función de prueba positiva
def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    # Comprueba si el código de estado es 201
    assert response.status_code == 201
    # Comprueba que el campo name está en la respuesta y contiene un valor
    assert response.json()["name"] == kit_body["name"]  #CORRECCION SE TENIA ANTERIORMENTE QUE ["name] =! name

# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si el código de estado es 400
    assert response.status_code == 400

#Prueba 1.Kit creado con exito.El parametro name contiene 1 caracter
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert(data.kit_body_prueba_1)

#Prueba 2.Kit creado con exito.El parametro name contiene 511 caracteres
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(data.kit_body_prueba_2)

#Prueba 3.Error.El parámetro name NO contiene carácteres
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_code_400(data.kit_body_prueba_3)

#Prueba 4.Error. El parametro name contiene 512 caracteres
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400(data.kit_body_prueba_4)

#Prueba 5.Kit creado con exito.El parametro name contiene caracteres especiales
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert(data.kit_body_prueba_5)

#Prueba 6.Kit creado con extio.El parametro name contiene un string con espacio
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(data.kit_body_prueba_6)

#Prueba 7.Kit creado con exito.El parametro name contiene un string de digitos
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert(data.kit_body_prueba_7)

#Prueba 8.Error. Falta el parametro name en la solicitud.
def test_create_kit_no_name_get_error_response():
    negative_assert_code_400(data.kit_body_prueba_8)

#Prueba 9.Error.El tipo de parametro name: Numero
def test_create_kit_numer_type_name_get_error_response():
    negative_assert_code_400(data.kit_body_prueba_9)