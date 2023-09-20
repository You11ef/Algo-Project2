#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from timeit import timeit
from sys import argv

from geo.point import Point


def load_instance(filename):
    
    """
    loads .pts file.
    returns distance limit and points.
    """
    with open(filename, "r") as instance_file:
        lines = iter(instance_file)
        distance = float(next(lines))
        points = [Point([float(f) for f in l.split(",")]) for l in lines]

    return distance, points


def print_components_sizes(distance, points):

    # On recherche dans un premier temps la matrice d'adjacence du graphe en question
    # Notons qu'une arête existe si elle correspond à une distance inférieure à la distance donnée en argument

    n = len(points)

    def testing(point1, point2):

        """ Cette fonction retourne 1 si la distance entre les deux points
        est inférieure à la distance donnée en argument dans composants() """

        test = Point.distance_to(point1, point2) <= distance

        return test

    adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            adjacency_matrix[i][j], adjacency_matrix[j][i] = testing(points[i], points[j]), testing(points[i], points[j])


    # Cette deuxième partie a pour but de trouver les parties connexes du graphe en utilisant un parcours en profondeur


    def voisins(node, adj):

        """ Fonction donnant une liste des noeuds voisins à celui donnée en argument """

        n = len(adj)
        return [i for i in range(n) if adj[node][i]]

    def diff(l1, l2):

        """ Retourne la différence ensembliste des deux listes. Cette fonction n'est pas symétrique."""

        return [x for x in l1 if x not in l2]


    
    
    ALL = []
    NOT_SEEN = [i for i in range(len(adjacency_matrix))]
    while NOT_SEEN:
        x = NOT_SEEN[0]
        seen = [x]
        pile = [x]
        while pile:
            l = diff(voisins(pile[-1], adjacency_matrix), seen)
            if l:
                seen.append(l[0])
                pile.append(l[0])
            else:
                pile.pop(-1)
        for i in seen:
            if i in NOT_SEEN:
                NOT_SEEN.remove(i)
        ALL.append(seen)
    final = [len(x) for x in ALL]
    final.sort(reverse=True)
    print(f"{final}")


def testing(s):
    distance, points = load_instance(s)
    print_components_sizes(distance, points)
    


def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)

if __name__ == "__main__":
    main()