# -*- coding: ISO-8859-1 -*- 
import random
from processing import *

def read_data(filename, skip_first_line = False, ignore_first_column = False, ignore_last_column = True):
    f = open(filename,'r')
    if skip_first_line:
        f.readline()    
    data = []
    for line in f:
        line = line.split(",")
        if ignore_last_column:
            line = line[:len(line)-1]
        line = [ float(x) for x in line ]
        if ignore_first_column:
            line = line[1:]
        point = Point(line)
        data.append(point)
    f.close()
    return data   

def makeRandomPoint(n, minimal, maximal):
    """Make n-dimension random point"""
    p = Point([random.uniform(minimal, maximal) for i in range(n)])
    return p

def generate_random_data(nombre_points, dimension, minimal, maximal):
    data = [makeRandomPoint(dimension, minimal, maximal) for i in xrange(nombre_points)]
    return data

def write_data(data, filename):
    '''
    Writes data in a csv file.

    @param data: a list of lists

    @param filename: the path of the file in which data is written.
        The file is created if necessary; if it exists, it is overwritten.
    '''
    # If you're curious, look at python's module csv instead, which offers
    # more powerful means to write (and read!) csv files.
    f = open(filename, 'w')
    """for item in data:
	for i in item.points:
            f.write(','.join([repr(x) for x in i.coordonnees]+[str(i.index)]))
    	    f.write('\n')
    f.close()"""
    it = 0
    f.write(','.join(["no_point"]+["attribut_"+str(i+1) for i in range(len(data[0].coordonnees))] + ["no_cluster"]))
    f.write('\n')
    for item in data:
           f.write(','.join([str(it+1)]+[repr(x) for x in item.coordonnees]+[str(item.index)]))
	   f.write('\n')
	   it += 1
    f.close()

def write_centre(data, filename):
    f = open(filename, 'w')
    f.write(','.join(["no_centre"]+["attribut_"+str(i+1) for i in range(len(data[0].centre.coordonnees))]))
    f.write('\n')
    it = 0
    for item in data:
	   f.write(','.join([str(it)]+[repr(x) for x in item.centre.coordonnees]))
	   f.write('\n')
           it += 1
    f.close()

