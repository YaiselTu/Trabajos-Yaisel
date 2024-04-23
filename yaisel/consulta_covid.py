from pyswip import Prolog

nombre = input('Por favor, ingresa tu nombre para realizar un diagnóstico complementario: ')
dolor_garganta = input('¿Sientes dolor de garganta? (si o no): ')
fiebre = input('¿Tienes fiebre? (si o no): ')
dolor_muscular = input('¿Tienes dolor muscular? (si o no): ')
dificultad_respiratoria = input('¿Tienes dificultad para respirar? (si o no): ')
fatiga = input('¿Tienes fatiga? (si o no): ')

prolog = Prolog()
prolog.consult("diagnostico_covid.pl")

result = bool(list(prolog.query(f"diagnostico_covid('{nombre}', '{dolor_garganta}', '{fiebre}', '{dolor_muscular}', '{dificultad_respiratoria}', '{fatiga}')")))
