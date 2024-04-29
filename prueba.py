def token_string(input_str, i):
    global line, col
    token = ""
    while i < len(input_str):
        char = input_str[i]
        if char == '{' or char == '}' or char in [' ', ';', '"']:
            if token:
                return [token, i]
            else:
                token += char
                i += 1
        elif char == '\n':
            i += 1
            line += 1
            col = 1
        else:
            token += char
            i += 1


# Ejemplo de uso
line = 1
col = 1
input_str = 'InsertarUnico insertadoc = nueva InsertarUnico("NombreColeccion","\n{\n"nombre":"Obra Literaria",\n"autor":"Jorge Luis"\n}\n");\n\nActualizarUnico actualizadoc = nueva ActualizarUnico("NombreColeccion", " \n{ \n"nombre": "Obra Literaria" \n}, \n{ \n$set: {"autor": "Mario Vargas"} \n} \n"); \n\n\nEliminarUnico eliminadoc = nueva EliminarUnico("NombreColeccion", " \n{ \n"nombre": "Obra Literaria" \n} \n"); \n\n\n'
result = token_string(input_str, 0)
print(result)