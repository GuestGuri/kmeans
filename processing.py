# -*- coding: ISO-8859-1 -*- 
import math
import random

class Point:

    """
    Point class
    """

    def __init__(self, coordonnees):
        self.coordonnees = coordonnees  #list of attributes
        self.n = len(coordonnees)       #dimension
	self.index = 0                #group index (initially, all points are in group 0)

    def __repr__(self):
        return str(self.coordonnees)


class Groupe:

    """
    Group class
    """

    def __init__(self, points):
        if len(points) == 0: 
		raise Exception("Empty group")
        self.points = points                                #points
        self.n = points[0].n                                #dimension 
        for p in points:
            if p.n != self.n: 
		raise Exception("Wrong dimension")       #same dimension of all points
        self.centre = self.calculerCentre()               #group centroid

    def __repr__(self):
        return str(self.points)

    def miseAJour(self, points):
        """
        Distance between old and new centroid
        """
        ancien_centre = self.centre
        self.points = points
        self.centre = self.calculerCentre()
        deplacement_centre = distance_minkowski(ancien_centre, self.centre)
        return deplacement_centre

    def calculerCentre(self):
        """
        Compute centroid
        """
        nombrePoints = len(self.points)        
        coordonnees = [p.coordonnees for p in self.points]          
        unzipped = zip(*coordonnees)                                
        centre_coordonnees = [math.fsum(dList)/nombrePoints for dList in unzipped]   #Compute barycenter
        return Point(centre_coordonnees)


def initialiser_points_iris(points):
	for i in range(0, 50):
		points[i].index = 0
	for i in range(51, 100):
		points[i].index = 1
	for i in range(101, 150):
		points[i].index = 2

		


def kmeans(points, k, critere_arret):
    initial = random.sample(points, k)         #choose k points randomly
    groupes = [Groupe([p]) for p in initial]   #create k groups using the chosen points
    compteur = 0        
    while True:       # Looping until stop
        listes = [ [] for c in groupes]           			       
        compteur_groupe = len(groupes)
        compteur += 1                                                          #begin iterations
        for p in points:                                                       #for every point in sample
            distance_inferieure = distance_minkowski(p, groupes[0].centre)   #compute distance between point and centroid
            indexGroupe = 0                                                    #put the point in this group
            for i in range(compteur_groupe - 1):                               #for the rest of groups
                distance = distance_minkowski(p, groupes[i+1].centre)       #compute distance between point and centroid             
                if distance < distance_inferieure:   #if distance is less than previous distance
                    distance_inferieure = distance   #update distance 
                    indexGroupe = i+1                #update group index for the point
	    p.index = indexGroupe
            listes[indexGroupe].append(p)
        deplacement_maximal = 0.0           
        for i in range(compteur_groupe):    #looping in groups
            deplacement_centre = groupes[i].miseAJour(listes[i])                #compute distance between old and new centroid 
            deplacement_maximal = max(deplacement_maximal, deplacement_centre)  #compute max distance 
        if deplacement_maximal < critere_arret:             #if max distance less then stop criteria then stop iteration
            print "Algorithm converges after %s iterations" % compteur
            break
    return groupes

def distance_minkowski(a, b):
    """Minkowski distance"""
    p = 2 #p = 2 for Euclidean p = 1 for Manhattan
    if a.n != b.n:
        raise Exception("Points have not the same dimension")
    ret = reduce(lambda x,y: x + pow(abs((a.coordonnees[y]-b.coordonnees[y])), p),range(a.n),0.0)
    return pow(ret, 1/float(p))  #math.sqrt(ret)

def distance_tchebychev(a, b):
    """Tchebychev distance"""
    if a.n != b.n:
        raise Exception("Points have not the same dimension")
    ret = max(abs(a.coordonnes[i]-b.coordonnes[i]) for i in range(a.n))
    return ret


def erreurs_iris(points):
	error = 0
	for i in range(0, 50):
		if points[i].index != 0 :
				error +=1
	for i in range(51, 100):
		if points[i].index != 1 :
				error +=1	

	for i in range(51, 100):
		if points[i].index != 2 :
				error +=1

	return error









