# Hace preguntas con diferente tipo de dato cada una, sin que se validen.

# Importa el modulo necesario para poder ingresar el tipo de dato de una fecha.
import datetime
# Los datos que son preguntados, se tienen, se preguntan o se calculan y no necesariamente tienen que ser del mismo tipo de dato.
# Notación que se utiliza:
#   str   string
#   i     int
#   f     float
#   dt    date


def main():
 # Los datos string se preguntan y procesan sin intermediación.
 strDato = input("Dame un dato string: ")
 # Los datos numéricos se preguntan por intermediación.
 _iDato = input("Dame un dato entero: ")
 iDato = int(_iDato)
 _fDato = input("Dame un dato float: ")
 fDato =float(_fDato)
 # Los datos date se preguntan por intermediación.
 _dtDato = input("Dame una fecha yyyy/mm/dd: ")
 anio=_dtDato[0:4]
 mes=_dtDato[5:7]
 dia=_dtDato[-2:]
 print(anio)
 print(mes)
 print(dia)

 dtDato = datetime.datetime(int(anio), int(mes), int(dia))

 print(strDato)
 print(type(strDato))
 print(iDato)
 print(type(iDato))
 print(fDato)
 print(type(fDato))
 print(dtDato)
 print(type(dtDato))