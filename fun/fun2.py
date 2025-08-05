import fun.objects2 as objects2,math

def conservationOfSpeed(x,y): #stara za skalarnu brzinu
    x.speed=(x.size*x.speed+y.size*y.speed)/(x.size+y.size) #formula za ocuvanje brzine okrenuta za izvuc brzinu nakon sudara
    
    

def boundControll(x,screen,lst):
    if x.poz[1]<0:
        if x:# bez provjere zna se srusit
            lst.remove(x)
    if x.poz[1]>screen.get_height():
        if x:
            lst.remove(x)
    if x.poz[0]<0:
        if x:
            lst.remove(x)
    if x.poz[0]>screen.get_width():
        if x:
            lst.remove(x)
        
        
def middleAngle(angle1,angle2):
    return (angle1+((angle2-angle1+180)%360-180)/2)%360

def objectDistance(x1,x2,y1,y2):
    d=math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
    
    return d

def objectAngle(x1,x2,y1,y2):
    
    angle=math.atan2(y2-x2,y1-x1)
    
    return angle



def pullForce(x,y,dt):# mid af
    
    G=50 #gravitacijska konstanta (random neki broj dok ne proradi)
    r=objectDistance(x.poz[0],x.poz[1],y.poz[0],y.poz[1])
    angle=objectAngle(x.poz[0],x.poz[1],y.poz[0],y.poz[1])
    

    F=G*((y.size*x.size)/(pow(r,2)))
    
    a=F/x.size
    

    if x.speed[0]>1 or x.speed[0]<-1 or x.speed[1]>1 or x.speed[1]<-1:#ako je brzina pre mala dobice novi kut a inace postepeno dobiva, bez ovoga grav. je cudna
        x.rot=middleAngle(x.rot,angle*180/math.pi)
    else:
        x.rot=angle*180/math.pi
        
        
    x.speed[0]+=a*math.cos(x.rot *math.pi/180)*dt
    x.speed[1]+=a*math.sin(x.rot*math.pi/180)*dt
    
    x.poz[0]+=x.speed[0]
    x.poz[1]+=x.speed[1]   
    
   
        

def draw(lst,screen,dt):
    for x in lst:
        x.render(screen,dt,lst)
        x.speedMaintenance(dt)
        boundControll(x,screen,lst)
        
        
def colision(screen,lst,dt):
    for x in lst:
        x.refresh()
    
    
    for x in lst:
        for y in lst:
            if x!=y: 
                if x.color=='red':
                    if x.hitbox[0]>y.hitbox[1] and x.hitbox[1]<y.hitbox[0] and x.hitbox[2]>y.hitbox[3] and x.hitbox[3]<y.hitbox[2]:
                        lst.remove(y)
                    
                pullForce(x,y,dt)          
                

def spawn(lst,pos,delay):
    if delay<0:
        for x in range(len(lst)):
            lst[x].color='light blue'
            
        lst.append(objects2.celestialObjects(pos))
        delay=20
    return delay