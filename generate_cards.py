import matplotlib.pyplot as plt
import numpy as np

card_height = 3.5
card_width = 2.5
colors = ['#8500ff','#fd7300','#00f6a2']
shapes = ['R','D','E']
numbers = [1,2,3]
shades = ['S','B','T']

def poly_rectangle(center,width=1.25,height=.375):
	poly_points = np.array([
		[center[0]-width/2,center[1]-height/2],
		[center[0]+width/2,center[1]-height/2],
		[center[0]+width/2,center[1]+height/2],
		[center[0]-width/2,center[1]+height/2],
		[center[0]-width/2,center[1]-height/2]]) 
	return poly_points

def poly_diamond(center,width=1.45,height=.425):
	poly_points = np.array([
		[center[0],center[1]-height/2],
		[center[0]+width/2,center[1]],
		[center[0],center[1]+height/2],
		[center[0]-width/2,center[1]],
		[center[0],center[1]-height/2]]) 
	return poly_points

def poly_ellipse(center,a=1.65,b=.15):
	phi = np.linspace(0,np.pi*2,100)	
	r = a*b/np.sqrt(b*np.cos(phi)**2+a*np.sin(phi)**2)
	x = r*np.cos(phi) + center[0]
	y = r*np.sin(phi) + center[1]
	poly_points = np.column_stack((x,y))
	return poly_points


def make_card(col_indx,num,shape,shade):
	# Color
	col = colors[col_indx]
	# Shape
	if shape=='E':	
		poly_fun = poly_ellipse
	elif shape=='R':	
		poly_fun = poly_rectangle
	elif shape=='D':	
		poly_fun = poly_diamond
	# Number
	if num==1:
		y = [0]
	elif num==2:
		y = [-.375,.375]
	elif num==3:
		y = [-.75,0,.75]
	# Fill
	if shade=='B':
		shd = '00'
	elif shade=='S':
		shd = 'ff'
	elif shade=='T':
		shd = '33'
	file_name = shape+'_'+str(num)+'_'+shade+'_'+['p','o','g'][col_indx]+'.svg'
	plt.figure(figsize=(card_width,card_height))
	plt.grid(True)
	for i in range(len(y)):
		polygon = poly_fun(center=[0,y[i]])
		plt.plot(polygon[:,0],polygon[:,1],color=col,lw=3)
		plt.fill(polygon[:,0],polygon[:,1],color=col+shd)
		plt.subplots_adjust(left=0,bottom=0,right=1,top=1)
	plt.xlim(-card_width/2,card_width/2)
	plt.ylim(-card_height/2,card_height/2)
	plt.axis('off')
	plt.savefig('Cards/'+file_name,format='svg',bbox_inches='tight',pad_inches=0)

card_counter = 0
for sp in shapes:
	for sd in shades:
		for cl in range(len(colors)):
			for nm in numbers:
				card_counter = card_counter + 1
				print('Drawing card '+str(card_counter),'\n')
				make_card(col_indx=cl,num=nm,shape=sp,shade=sd)
