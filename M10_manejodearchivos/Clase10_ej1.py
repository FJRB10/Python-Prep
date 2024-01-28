import sys

#print(len(sys.argv))

if len(sys.argv) == 4:
	for i in range(len(sys.argv)):
		if i != 0:
			print(f'EL PAREMTRO NUMERO {i} ES {sys.argv[i]}')
elif len(sys.argv) < 4:
	print('HACEN FALTA PARAMETROS DE ENTRADA RECUERDE QUE SON 3')
else:
	print('SON MAS PARAMETROS DE LOS REQUERIDOS, RECUERDE QUE SON 3')