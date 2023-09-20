#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""
from timeit import timeit
from sys import argv
from geo.point import Point
from ldc import *
#from tycat import *
#from segment import *


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

    def testing(point1, point2):

        """ Cette fonction retourne 1 si la distance entre les deux points
        est inférieure à la distance donnée en argument dans composants() """

        test = Point.distance_to(point1, point2) <= distance

        return test
    

    def get_cell(pt, d):

        """ gets the cell"""

        return (int(pt.coordinates[0]*(2**(1/2))/d), int(pt.coordinates[1]*(2**(1/2))/d))
    

    def is_in(cell, dic):

        """ checks whether the cell is in the dic or not """
        try:
            dic[cell]
            return True
        except KeyError:
            return False
        

    def neighbor(cell, dic):
        """ gets list of neighbors """

        def adjacency1(cell1, cell2, dic):

            """ checks adjacency for two cells """

            pts1 = dic[cell1]
            pts2 = dic[cell2]

            for pt1 in pts1:
                for pt2 in pts2:
                    if testing(pt1, pt2):
                        return True
            return False

        a = [(cell[0]+i, cell[1]+j) for i in range(-2, 3) for j in range(-2, 3) if i!= 2 or j !=2]

        return [x for x in a if (is_in(x, dic) and adjacency1(cell, x, dic))]



    def diff(set1, set2):

        """ algebrical difference between two sets """

        return [x for x in set1 if x not in set2]



    cells = {}

    for pt in points:
        a = get_cell(pt, distance)
        try:
            cells[a].append(pt)
        except KeyError:
            cells[a] = [pt]


    
    dic_cell_to_index = {}
    dic_index_to_cell = {}
    for i, a in enumerate(cells.keys()):
        dic_cell_to_index[a] = i
        dic_index_to_cell[i] = a


    i = 0

    conn = []
    seen = set()



    while i != len(cells):

        pile = [dic_index_to_cell[i]]
        seen.add(dic_index_to_cell[i])


        long = len(cells[dic_index_to_cell[i]])
        while pile :


            a = neighbor(pile[-1], cells)

            if not a:
                
                pile.pop(-1)

            else:

                a = diff(a, seen)
    
                if not a:
                
                    pile.pop(-1)
    
                else:
                    i += 1
                    pile.append(a[0])
                    seen.add(a[0])
                    long += len(cells[a[0]])
    
                    j = dic_cell_to_index[a[0]]
    
                    dic_index_to_cell[i], dic_index_to_cell[j] = dic_index_to_cell[j], dic_index_to_cell[i]
                    dic_cell_to_index[dic_index_to_cell[i]], dic_cell_to_index[dic_index_to_cell[j]] = dic_cell_to_index[dic_index_to_cell[j]], dic_cell_to_index[dic_index_to_cell[i]]



        i += 1

        conn.append(long)
    conn.sort(reverse=True)
    print(f"{conn}")        

        



def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


if __name__ == "__main__":
    main()
 



