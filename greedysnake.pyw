import pygame,time,sys,random,playsound,shelve,threading
win=pygame.display.set_mode((720,480))
icon=pygame.image.load('GreedySnake.png')
pygame.display.set_icon(icon)
head=(0,0)
body=[(0,1)]
newhead=head
d=0
pygame.display.set_caption('Greedy Snake')
coin=(random.randint(2,25),random.randint(2,16))
def game(var,score=None,scoretype=None):
	shelf=shelve.open('game','w')
	shelf['game']=var
	if score!=None:
		if score<shelf['score'] and scoretype=='highscore':
			pass
		else:
			shelf['score']=score
	shelf.close()
game(True)
def drawText(content):
		pygame.font.init()
		font  =  pygame.font.Font("micross.ttf",100)
		text_sf  =  font.render(content,True,pygame.Color(255,255,255))
		return  text_sf 
def BGM():
	pygame.mixer.init()
	while shelve.open('game')['game']==True:
		pygame.mixer.music.load('bgm.wav')
		pygame.mixer.music.play()
		time.sleep(2.2)
def exit1():
	game(False,score=len(body)-1,scoretype='highscore')
	win.fill((0,0,0))
	win.blit(drawText('You lose!'),(250,50))
	win.blit(drawText('score:'+str(len(body)-1)),(50,200))
	pygame.display.flip()
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
TO=threading.Thread(target=BGM)
TO.start()
def coinsound():
	playsound.playsound('coin.wav')
while True:
   for event in pygame.event.get():
       if event.type==pygame.KEYDOWN:
         if event.key==pygame.K_DOWN:
            d=0
         if event.key==pygame.K_UP:
            d=1
         if event.key==pygame.K_RIGHT:
            d=2
         if event.key==pygame.K_LEFT:
            d=3
   if d==0:
      newhead=(head[0],head[1]+1)
   elif d==1:
      newhead=(head[0],head[1]-1)
   elif d==2:
      newhead=(head[0]+1,head[1])
   else:
      newhead=(head[0]-1,head[1])
   part=[newhead]
   part+=body[:-1]
   if len(body)>0:
      data=body
      body=[head]
      body+=data[:-1]
   else:
      body=[]
   win.fill((100,100,100))
   head=newhead
   data=pygame.image.load('body.png')
   for i in body:
      win.blit(data,(i[0]*25,i[1]*25))
   data=pygame.image.load('head1.png')
   x=head[0]*25
   y=head[1]*25
   if x>720:
      exit1()
   elif x<0 :
      exit1()
   if y>480:
      exit1()
   elif y<0:
      exit1()
   win.blit(data,(x,y))
   data=pygame.image.load('coin.png')
   win.blit(data,(coin[0]*25,coin[1]*25))
   pygame.display.flip()
   if len(part)<100:
      time.sleep((50-len(part))*0.002)
   if coin in part:
				TO=threading.Thread(target=coinsound)
				TO.start()
				while coin in part:
					coin=(random.randint(2,25),random.randint(2,16))
				body.append(body[-1])
