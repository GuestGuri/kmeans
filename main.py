# -*- coding: ISO-8859-1 -*- 
from data import *
from processing import *

print("**********************************************************")
print("**********************************************************")
print("1 - IRIS Data")
print("2 - Random Data")
mode = input("Your choice: ")
if mode == 1 :
        points = read_data("iris.csv")
	initialiser_points_iris(points)
        critere_arret = input("When to stop ?: ")
	nombre_groupes = input("How many group ?: ")
	print points
	groupes = kmeans(points, nombre_groupes, critere_arret)
	write_data(points, "resultat_iris.csv")
	write_centre(groupes, "centres_iris.csv")
       

elif mode == 2 :
	nombre_points = input("How many point ?: ")
	dimension = input("Dimension of each point ?: ")
        minimal = input("Max value of each attribue ?: ")
        maximal = input("Min value of each attribue ?: ")
        critere_arret = input("When to stop ?: ")
	nombre_groupes = input("How many group ?: ")
	points = generate_random_data(nombre_points, dimension, minimal, maximal)
        print points
        groupes = kmeans(points, nombre_groupes, critere_arret)
	write_data(points, "resultat.csv")
        write_centre(groupes, "centres.csv")


else:
	pass

k = 0
l = 1
for i in groupes:
	count = 0
        for p in i.points:
            print " Groupe: ", k, "\t Point :", p
            count += 1
	print "We have " + str(count) + " point in this group"
        print("\n")
	k += 1

for i in points:
	print str(l) + ": " + str(i.coordonnees) + " in group " + str(i.index)
	l += 1


