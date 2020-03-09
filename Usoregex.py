# Pregunta un dato hasta que la validacion sea correcta utilizando expresiones regulares.
# Importa el módulo que es necesario para usar expresiones regulares.
import re

def main():
  # Ciclo infito que seguira asi mientras no se presente un descanso que se representa con break.
  #El dato sera preguntado mientras que no se cumpla con el patron de la expresion regular.

  while True:
    strRFC = input("Dame el RFC: ")
    coincide = re.search("^[A-Z]{4}-[0-9]{6}-[A-Z0-9]{3}$", strRFC)
    if (coincide):
      print("RFC Correcto!")
      break
    else:
      print("RFC incorrecto. Intenta de nuevo.")