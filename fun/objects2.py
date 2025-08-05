import pygame,math

class star:# ovo je jedna od zadnjih stvari sta san doda pa san je implementira na nacin da sta manje minjan orginalni kod
    def __init__(self):
        self.poz=[600,400]
        self.speed=[0,0]
        self.size=57
        self.color='red'
        self.hitbox=[self.poz[0]+10,self.poz[0]-10,self.poz[1]+10,self.poz[1]-10]
        
    def render(self,screen,dt,lst):
        pygame.draw.circle(screen,self.color,self.poz,15)

    def refresh(self):
        self.speed=[0,0]
        self.poz=[600,400]
        self.color='red'
        
    def hitboxRefresh(self):
        pass
    def speedMaintenance(self,dt):
        pass
    
    

class celestialObjects:
    def __init__(self,pos):
        self.speed=[0,0]
        self.rot=90 #stupnjevi
        self.poz=pos
        self.size=4
        self.acl=0
        self.trail=[self.poz]
        self.destroyed=[False,100]
        self.color='yellow'
        self.hitbox=[self.poz[0]+self.size-1,self.poz[0]-self.size-1,self.poz[1]+self.size-1,self.poz[1]-self.size-1]
        self.gravityForce=[self.poz[0]+4*self.size,self.poz[0]-4*self.size,self.poz[1]+4*self.size,self.poz[1]-4*self.size]
    
    
    def render(self,screen,dt,lst):
        for x in range(len(self.trail)):
            pygame.draw.circle(screen,(51,51,51),self.trail[x],self.size/2)
        pygame.draw.circle(screen,self.color,self.poz,self.size)
            
    def speedMaintenance(self,dt):
        if len(self.trail)>40:
            self.trail.pop(0)
        self.trail.append(self.poz[:])
        
        
        
        self.poz[0]+=self.speed[0]*dt
        self.poz[1]-=self.speed[1]*dt
        
        
        
    def refresh(self):# i rotacije
        self.hitbox=[self.poz[0]+self.size,self.poz[0]-self.size,self.poz[1]+self.size,self.poz[1]-self.size]
        self.gravityForce=[self.poz[0]+4*self.size,self.poz[0]-4*self.size,self.poz[1]+4*self.size,self.poz[1]-4*self.size]
        
        if self.rot>360:
            self.rot=0
        elif self.rot<0:
            self.rot=360
            
    
    def destroyedF(self,screen,dt):
        scatter=[]
        for x in range(20):
            x=self.poz[:]
            scatter.append(x)
        
        rot=0
        for x in scatter:
            x[0]+=self.speed* math.cos(rot*(math.pi/180))*dt
            x[1]-=self.speed* math.sin(rot*(math.pi/180))*dt
            rot+=18
            pygame.draw.circle(screen,'light blue',x,self.size/3)
            
        self.destroyed[1]-=1

