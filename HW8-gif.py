import os
import imageio

myfile=os.listdir('pics')
images=[]
for i in range(len(myfile)):
    image=imageio.imread('pics/' + myfile[i])
    images.append(image)

imageio.mimsave('pyth.gif', images)