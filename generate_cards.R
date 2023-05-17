# General functions
polar_to_cartesian <- function(r,phi){
	x <- r*cos(phi)
	y <- r*sin(phi)
	return(list(x=x,y=y))
}

figure_perimeter <- function(shape, center_x, center_y, width, height){
	if(shape=='ellipse'){
		a <- width/2
		b <- height/2
		theta <- seq(0,2*pi,length.out=15)
		radius <- (a*b)/(sqrt((b*cos(theta))^2+(a*sin(theta))^2))
		at_origin <- polar_to_cartesian(radius,theta)
		x <- at_origin$x+center_x 
		y <- at_origin$y+center_y
	}
	else if(shape=='diamond'){
		x <- c(center_x-width/2,center_x,center_x+width/2,center_x,center_x-width/2)
		y <- c(center_y,center_y-height/2,center_y,center_y+height/2,center_y)
	}
	else if(shape=='rectangle'){
		x <- c(center_x-width/2,rep(center_x+width/2,2),center_x-width/2,center_x-width/2)
		y <- c(rep(center_y+c(-1,1)*height/2,each=2),center_y-height/2)
	}
	return(list(x=x,y=y))
}

blank_polygons <- function(perimenters){

}


# Figure testing:
try(dev.off())
x11(width=2.5,height=3.5)
par(mar=rep(2,4),xaxs='i',yaxs='i')
plot(NULL,xlim=c(-1,1),ylim=c(-1,1))
fp <- figure_perimeter('rectangle',center_x=0.25,center_y=-0.5,width=1.5,height=1)
polygon(fp$x,fp$y,border='red',lwd=2,col='#44558889')	


make_card <- function(){
	par(mar=rep(1,4),xaxs='i',yaxs='i')
	plot(NULL,xlim=c(-1,1),ylim=c(-1,1))
	x <- c(-.5,.5,.5,-.5,-.5,-.25,-.25,.25,.25,-.25)
	y <- c(-.5,-.5,.5,.5,-.5,-.25,.25,.25,-.25,-.25)
	polygon(x,y,col='#44589e78',lwd=2,border='#d37834')

	# 0. Choose color ['#color1','#color2','#color3']
	# 1. Fill card with texture ['blank','solid','lines']
	# 2. Draw figure(s) ['ellipse','diamond','rectangle']
	# 	2a. Get figure(s) perimeter coordinates
	# 	2b. Draw blank polygons surrounding figurei(s)
	# 	2c. Draw figure(s) lines

}
png(file='Cards/card.png',width=2.5,height=3.5,units='in',res=500)
make_card()
dev.off()
