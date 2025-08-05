import pygame,fun.objects2 as objects2, fun.fun2 as fun2

pygame.init()

screen=pygame.display.set_mode((1280,840))
running=True
clock=pygame.time.Clock()
dt=0
solar_sys=[]
star=objects2.star()
member=-1
delay=0
toggle=False


while running:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            
            
    keys=pygame.key.get_pressed()
    
    try:
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos_tup=pygame.mouse.get_pos()
            poz=[]
            poz.append(pos_tup[0])
            poz.append(pos_tup[1])
            delay=fun2.spawn(solar_sys,poz,delay)
            member=-1
        # if keys[pygame.K_w]:
        #     solar_sys[member].speed[0]+=1*math.cos(solar_sys[member].rot*(math.pi/180))
        #     solar_sys[member].speed[1]+=1*math.sin(solar_sys[member].rot*(math.pi/180))
        # if keys[pygame.K_s]:
        #     solar_sys[member].speed[0]-=1
        #     solar_sys[member].speed[1]-=1
        # if keys[pygame.K_d]:
        #     solar_sys[member].rot-=0.2
        # if keys[pygame.K_a]:
        #     solar_sys[member].rot+=0.2
        if keys[pygame.K_LSHIFT]:
            solar_sys[member].size+=0.1
        if keys[pygame.K_LCTRL]:
            solar_sys[member].size-=0.1
        if keys[pygame.K_LALT]:
            solar_sys[member].speed[0]=0
            solar_sys[member].speed[1]=0
        if keys[pygame.K_SPACE]:
            if star not in solar_sys:
                solar_sys.append(star)
        if keys[pygame.K_BACKSPACE]:
            if star in solar_sys:
                solar_sys.remove(star)
            
            
            
        if keys[pygame.K_UP]: #mjenja clana liste
            solar_sys[member].color='light blue'
            if member>=len(solar_sys)-1:
                member=0
            else:
                member+=1
            solar_sys[member].color='yellow'
    except:
        pass
    
    delay-=1
    
    
    fun2.colision(screen,solar_sys,dt)
        
    fun2.draw(solar_sys,screen,dt)
                        
    
    pygame.display.flip()
    screen.fill('black')
    
    dt=clock.tick(144)/1000

pygame.quit()

