#! /usr/bin/env python3

from geo.tycat import tycat
from geo.point import Point
from geo.segment import Segment
from sys import argv



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


def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        segments = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if Point.distance_to(points[i], points[j]) <= distance:
                    segments.append(Segment([points[i], points[j]]))
        tycat(points, segments)

main()
