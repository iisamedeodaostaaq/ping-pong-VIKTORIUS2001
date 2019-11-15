## Prof.: Non ci sono commenti: codice non manutenibile
## Prof.: comment anche le funzioni: cosa fanno?
r=0
g=0
b=0
r2=0
g2=0
b2=0
xrac1=330
## Prof.: non è chiaro perchè -25
yrac1=600-25
xrac2=330
yrac2=0
## Prof.: usa nomi di variabili significativi
xrad=50
yrad=50
xrad2=0
yrad2=0
xpos=0;
ypos=0;
xVers=1
yVers=-1
score1=0
score2=0

def setup():
    global xpos,ypos
    xpos=200
    ypos=200
    size(800,600)
## Prof.: Disegnare nel setup non ha molto senso
    background(62)
    fill(0,255,0)
    rect(60,4,100,140)
    fill(255,255,255)
    rect(160,4,100,140)
    fill(255,0,0)
    rect(260,4,100,140)
    fill(255,215,255)
    triangle(210,10,170,80,250,80)
    fill(205,0,0)
    rect(20,4,40,300)
    
    
def tocca_rac1(xpos,ypos,xrac1,yrac1,yVers):
## Prof.: Fai riferimento alle variabili
    if(ypos>=yrac1-25 and (xpos+25>xrac1 and xpos-25<xrac1+100) ):
        return(True)
    else:
        return(False)
        
def tocca_rac2(xpos,ypos,xrac2,yrac2,yVers):
    if(ypos<=yrac2+50 and (xpos+25>xrac2 and xpos-25<xrac2+100) ):
        return(True)
    else:
        return(False)
    
def rac1_rac2_confini(xrac1,xrac2):
## Prof.: Le racchette escono dal campo verso destra e rientrano a sinistra 
    if (xrac1>=width) or (xrac1<=0):
        xrac1=0
    
    if (xrac2>=width) or (xrac2<=0):
        xrac2=0
        
def draw():
    global xpos,ypos,xVers,yVers,r,g,b,r2,b2,g2,xrad,yrad,xrad2,yrad2,xrac1,yra1,xrac2,score1,score2
    xpos=xpos+xVers*4
    ypos=ypos+yVers*4
    background(62)
    r=r2
    g=g2
    b=b2
    fill(r,g,b)
    ellipse(xpos,ypos,xrad,yrad)
    if(xpos>width-xrad/2 or xpos<0+xrad/2):
        xVers*=-1
        r2=random(0,255)
        g2=random(0,255)
        b2=random(0,255)
        
    if(ypos>height-xrad/2 or ypos<0+xrad/2):
        yVers*=-1
        r2=random(0,255)
        g2=random(0,255)
        b2=random(0,255)
        
    if tocca_rac1(xpos,ypos,xrac1,yrac1,yVers):
        yVers*=-1
    
    if tocca_rac2(xpos,ypos,xrac2,yrac2,yVers):
        yVers*=-1
        
    if (xrac1>=width) or (xrac1<=0):
        xrac1=0
    
    if (xrac2>=width) or (xrac2<=0):
        xrac2=0
    
    rac1_rac2_confini(xrac1,xrac2) 
   

    fill(255,255,255)    
    rect(xrac1,yrac1,100,25)
    
    textSize(30)
    fill(255,0,0)  
    text(score1,xrac1+10,height-1)     
    
    fill(255,255,255)
    rect(xrac2,yrac2,100,25)
    
    textSize(30)
    fill(255,0,0)  
    text(score2,xrac2+10,24)      
    
    
    if(ypos<=xrad/2):
        score1=score1+1
    if score1 >= 5:
        textSize(50)
        fill(255,255,255)  
        text("giocarore 1 ha vinto",100,height/2)
        textSize(30)
        fill(255,255,255)  
        text("premere E per uscire",100,(height/2)+40)   
        
    
    if(ypos>=height-xrad/2):
        score2=score2+1
    if score2 >= 5:
        textSize(50)
        fill(255,255,255)  
        text("giocarore 2 ha vinto",100,height/2)
        textSize(30)
        fill(255,255,255)  
        text("premere E per uscire",100,(height/2)+40)
        
        
        
        
    

def keyPressed():
    global xrac1,xrac2
    if(keyCode==LEFT):
        xrac1-=15
    if(keyCode==RIGHT):
        xrac1+=15
    if(key=="a"):
        xrac2-=15
    if(key=="d"):
        xrac2+=15
    if(key=="e"):
        exit()
    



    
