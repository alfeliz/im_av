#!/usr/bin/env python
# Read 8 images from Cordin camera, and calculate a modifier of the intensity in percentage.
# The files MUST be named "FinalFocusCam*nn*.bmp" where *nn* is a number between 01 and 08.


import scipy.misc #Import adequate commands for reading images

import pickle

import numpy as np 


mat_im = {} #Dictionary with the processed data images.

for i in range(1,9): #For images named 1-8 in the number
	archivo = "FinalFocusCam0"+str(i)+".bmp" #Make the filename
	mat = scipy.misc.imread(archivo) #Read the file and transform it in a scipy ndarray with three dimensions: [Height, Width, 0-2{Chanel, original image RBG}]
	mat_im[i-1] = sum( mat[:,:,i] for i in range(len(mat[1,1,:])) )	


mat_aver =  sum(image for image in mat_im.itervalues() ) / len(mat_im) #Making the average of the matrices. ".itervalues()" creates an iterator in the values of the dictionary.

mat_dif = {} #Dictionary with the difference from the average.

for i in range(len(mat_im)): #Range to make an iterable object, integers are not.
	mat_dif[i] = np.mean(abs(mat_aver - mat_im[i])) #One number proportional to the relative illumination for every image.
	
value = mat_dif[0]
for i in range(len(mat_dif)):
	mat_dif[i] = abs(mat_dif[i]/value - 1) * 100 #To normalize with the first image
	print "Imagen "+str(i+1)+" valor relativo(%): "+str(mat_dif[i])

#Saving the data in a file:
salvado = open("CORDIN_intensity.txt",'w')    

for key, value in mat_dif.items():
	salvado.write("{0} {1:7.2f}\n".format("Imagen_0"+str(key), value) )
           
salvado.close()  
	
	
#And tha... tha... that`s all, folks!!
	

