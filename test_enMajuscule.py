import string
import random
from enMajuscule import EnMajuscule

def generation_mot(taille):
    lettres = string.ascii_lowercase
    return ''.join(random.choice(lettres) for i in range(taille))

def test_to_upper():
    test = EnMajuscule()
    nb_reussi=0
    for i in range(10):
        taille_mot = random.randint(1,10)
        random_mot = generation_mot(taille_mot)
        compare = random_mot.upper()
        resultat = test.to_upper(random_mot)
        if compare !=resultat:
            print(f'Test échoué pour to_upper avec {random_mot}')
            print(f'Attendu : {compare}, obtenu : {resultat}')
        else :
            print(f'Test réussi pour to_upper avec {random_mot}')
            nb_reussi+=1
    if nb_reussi == 10:
        print(f'Tous les tests pour to_upper ont réussi.')
    else :
        print(f'Certains tests pour to_upper ont échoué')
