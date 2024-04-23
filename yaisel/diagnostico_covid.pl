% Diagnóstico de COVID19 basado en síntomas

diagnostico_covid(Nombre, Dolorgarganta, Fiebre, Dolormuscular, Dificultadrespiratoria, Fatiga) :-
    (Dolorgarganta == 'si', Fiebre == 'si', Dolormuscular == 'si', Dificultadrespiratoria == 'si', Fatiga == 'si' ->
        write('Tienes covid19.Mantenga la distancia con sus familiares cercanos y dirijase a un medico, '), write(Nombre), write('.');
        write('No se cumplen suficientes sintomas para un diagnostico de covid19 dirijase al medico para un PCR, '), write(Nombre), write('.')
    ).
