#Realizar un algoritmo que solicite una cadena de texto al usuario. El algoritmo debe determinar si la cadena de texto es un “pangrama”. 
#Un pangrama es un texto que utiliza todas las letras existentes del alfabeto de un idioma (No diferencia entre mayúsculas y minúsculas). 

def es_p(cadena): 
    alfabeto = set(range(ord('a'), ord('z') + 1))  
    letras_a = set()
#explicacion incial
  #DEFINI LA PRIMERA FUNCION, COLOCANDO EN ARGUMENTO EN CADENA (TEXTO) Y GENERANDO EL RANGO DE VALORES DEL AASCII Y PONIENDO MAS UNO PA INCLUIR LA Z Y SET PARA LA ENTRADA DEL ARGMENTO
    for words in cadena:
        if (ord('a') <= ord(words) <= ord('z')) or (ord('A') <= ord(words) <= ord('Z')):
            if ord('A') <= ord(words) <= ord('Z'):
                words = chr(ord(words) + 32)  
            letras_a.add(ord(words))  
    return letras_a == alfabeto
#explicacion intermedia
#se crea un ciclo for para recorrer la cadena de texto y se san dos ifs anidados para saber si es minuscula o mayuscula y se le suma 32 para que se convierta en minuscula
#porque 32 es la diferencia entre mayuscula y minuscula y se le suma 32 a la mayuscula para que se convierta en minuscula
#a la fncion letras_a se le añade las condiciones de las letras del alfabeto
#como no se puede comparar directamente con los alfabetos se usa la funcion set para que se pueda comparar
#Vamos a iterar cada letra del alfabeto y ver si las letras del alfabeto estan en la cadena de texto

texto_solo_letras = input("Ingrese un texto: ")

if es_p(texto_solo_letras):
    print("El texto es un pangrama. Feliceidades.")
else:
    print("El texto no es un pangrama. Intentalo de nuevo.")
#explicacion final
#se le pide al usuario que ingrese su respesta y para la impresion se genera na condificonal
#verifica si es_p, si es verdadero se imprime el texto es un pangrama, si no es verdadero se imprime el texto no es un pangrama