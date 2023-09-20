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



def print_components_sizes_amel(distance, points):

    def testing(point1, point2):

        """ Cette fonction retourne 1 si la distance entre les deux points
        est inférieure à la distance donnée en argument dans composants() """

        test = Point.distance_to(point1, point2) <= distance

        return test

    def adding(liste, point):

        """ fonction intermédiaire qui part d'une liste d'ensembles, où chaque ensemble contient des points de même composante connexe,
            et ajoute le point passé en argument à cette liste en effectuant les changements nécessaires pour garder la caractéristique des
            ensembles en question """
        
        if not liste:
            liste.append({point})
        else:
            concerned = []
            cache = liste[:]
            for i, ens in enumerate(cache):
                for pt in ens:
                    if testing(pt, point):
                        concerned.append(ens)
                        liste.remove(ens)
                        break
            a = set().union(*concerned)
            a.add(point)
            liste.append(a)
    
    l = []
    for point in points:
        adding(l, point)
    m = [len(x) for x in l]
    m.sort(reverse=True)
    print(sum(m), f"{m}")


def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes_amel(distance, points)

if __name__ == "__main__":
    main()