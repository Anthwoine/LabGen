import random
from Joueur import Joueur

def genetique(joueurs):
    fitness_joueurs = fitness(joueurs)
    fitness_joueurs.sort(key=lambda x: x[1], reverse=True)
    
    parents_list = []
    for joueur, point in fitness_joueurs:
        print(joueur, point)
        parents_list.append(joueur)
    
    print("----------------")
    print("----------------")
    print("----------------")
    print("----------------")


    nouvelle_population = []
    while len(nouvelle_population) < len(joueurs):
        parent1, parent2 = random.sample(parents_list[:20], 2)
        enfant = croiser(parent1, parent2)
        enfant = muter(enfant)
        nouvelle_population.append(enfant)
        
    print(len(nouvelle_population))
    return nouvelle_population



def fitness(joueurs):
    joueur_fitness = []
    for joueur in joueurs:
        distance_arrivé = abs(joueur.posX - joueur.labyrinthe.fin[0]) + abs(joueur.posY - joueur.labyrinthe.fin[1])
        nbr_explored = len(joueur.explored)
        estArrive = distance_arrivé == 0

        point = nbr_explored / 2 - distance_arrivé + (0 if estArrive else 100)
        joueur_fitness.append((joueur, point))

    return joueur_fitness

def croiser(parent1, parent2):
    seq1 = parent1.sequence
    seq2 = parent2.sequence
    new_seq = []
    for i in range(len(seq1)):
        new_seq.append(seq1[i] if random.random() < 0.5 else seq2[i])
    
    return Joueur(parent1.labyrinthe, new_seq)

def muter(individu, proba_mutation=0.1):
    for i in range(len(individu.sequence)):
        if random.random() < proba_mutation:
            individu.sequence[i] = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
        return individu



