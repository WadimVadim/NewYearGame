#Импорт библиотек
import pygame, random, time, sys

#---Меню
def Menu():
	#Размеры окна
	ScreenX = 700
	ScreenY = 500

	screen = pygame.display.set_mode([ScreenX, ScreenY])
	pygame.display.set_caption("Новогодний подарок")

	#Инициализация pygame
	pygame.init()

	#Количество подарков
	gifts = 0

	#Назначение переменных
	running = True
	FPS = 60
	timer = pygame.time.Clock()

	#Изображения
	background = pygame.image.load('Assets/d1.png')
	d2 = pygame.image.load('Assets/d2.png')
	d3 = pygame.image.load('Assets/d3.png')
	ng = pygame.image.load('Assets/ng.png')

	#Кнопки
	b1 = pygame.image.load('Buttons/Begin.png')
	b2 = pygame.image.load('Buttons/Newgame.png')
	b3 = pygame.image.load('Buttons/Help.png')
	b4 = pygame.image.load('Buttons/Exit.png')

	b1_click = pygame.image.load('Buttons/Begin_click.png')
	b2_click = pygame.image.load('Buttons/Newgame_click.png')
	b3_click = pygame.image.load('Buttons/Help_click.png')
	b4_click = pygame.image.load('Buttons/Exit_click.png')

	b1v = b1 
	b2v = b2
	b3v = b3
	b4v = b4
	ngv = ng

	#ng = pygame.transform.scale(ng, (290, 75))

	#Основной цикл
	while running:
		for event in pygame.event.get():
			#Выключения игры
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.MOUSEMOTION:
				(x1,y1)= event.pos
				if  (x1>=13 and x1<=297) and (y1>=140 and y1<=194):
					b1v = b1_click
				elif  (x1>=13 and x1<=297) and (y1>=210 and y1<=264):
					b2v = b2_click
				elif  (x1>=13 and x1<=297) and (y1>=280 and y1<=334):
					b3v = b3_click
				elif  (x1>=13 and x1<=297) and (y1>=350 and y1<=404):
					b4v = b4_click
				else:
					b1v = b1 
					b2v = b2
					b3v = b3
					b4v = b4

			elif event.type == pygame.MOUSEBUTTONDOWN:
				(x1,y1)= event.pos
				if  (x1>=13 and x1<=297) and (y1>=140 and y1<=194):
					Loadgame(ScreenX, ScreenY, running, FPS, timer, gifts)
				elif  (x1>=13 and x1<=297) and (y1>=210 and y1<=264):
					Game1(ScreenX, ScreenY, running, FPS, timer, gifts)
				elif  (x1>=13 and x1<=297) and (y1>=280 and y1<=334):
					Help(ScreenX, ScreenY, running, FPS, timer)
				elif  (x1>=13 and x1<=297) and (y1>=350 and y1<=404):
					running = False

		screen.blit(background, [0,0])
		pygame.draw.rect(screen, [255,255,255], (0, 0, 700, 3))
		pygame.draw.rect(screen, [255,255,255], (0, 497, 700, 3))
		pygame.draw.rect(screen, [255,255,255], (695, 0, 5, 500))
		pygame.draw.rect(screen, [255,255,255], (0, 0, 2, 500))

		screen.blit(ngv, (30, 40))
		screen.blit(b1v, (13,140))
		screen.blit(b2v, (13,210))
		screen.blit(b3v, (13,280))
		screen.blit(b4v, (13,350))

		screen.blit(d2, (360,400))
		screen.blit(d3, (380,300))


		#Счётчик FPS
		timer.tick(FPS)

		#Обновление содержимого окна
		pygame.display.flip()

	#Выключение игры
	pygame.quit()

#---Помощь
def Help(ScreenX, ScreenY, running, FPS, timer):

	click = False

	back = pygame.image.load('Buttons/back.png')
	back_click = pygame.image.load('Buttons/back_click.png')
	help_background = pygame.image.load('Assets/help.png')
	
	screen = pygame.display.set_mode([ScreenX, ScreenY])

	#Инициализация pygame
	pygame.init()

	#Основной цикл
	while running:
		for event in pygame.event.get():
			#Выключения игры
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEMOTION:
				(x1,y1)= event.pos
				if  (x1>=210 and x1<=210+284) and (y1>=350 and y1<=350+54):
					click = True
				else:
					click = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				(x1,y1)= event.pos
				if  (x1>=210 and x1<=210+284) and (y1>=350 and y1<=350+54):
					Menu()
					


		screen.blit(help_background, [0,0])

		if click:
			screen.blit(back_click, [210,350])
		else:
			screen.blit(back, [210,350])

		#Счётчик FPS
		timer.tick(FPS)

		#Обновление содержимого окна
		pygame.display.flip()

	#Выключение игры
	pygame.quit()

#---Загрузка сохранённой игры
def Loadgame(ScreenX, ScreenY, running, FPS, timer, gifts):
	with open('Saving.txt') as f:
		level = f.read()

	if level == '0' or level == '1':
		Game1(ScreenX, ScreenY, running, FPS, timer, gifts)
	elif level == '2':
		Game2(ScreenX, ScreenY, running, FPS, timer, gifts)
	elif level == '3':
		Game3(ScreenX, ScreenY, running, FPS, timer, gifts)
	elif level == '4':
		Game4(ScreenX, ScreenY, running, FPS, timer, gifts)

#---Игры

#Баскетбол
def Game1(ScreenX, ScreenY, running, FPS, timer, gifts):

	with open('Saving.txt', 'w') as f:
		f.write('1')

	import random

	xp = 0
	xb = 50
	yb = 0
	xbasket = 590
	ybasket = 100
	speed_bx = 0
	speed_by = 5
	speed = 5
	check = 0
	right = False
	left = False

	font = pygame.font.Font(None, 70)
	screen = pygame.display.set_mode([ScreenX, ScreenY])

	sky = pygame.image.load('Assets/1/sky.png')
	sky = pygame.transform.scale(sky, (700, 500))
	grass = pygame.image.load('Assets/1/grass.png')
	grass = pygame.transform.scale(grass, (60, 60))
	ball = pygame.image.load('Assets/1/ball.png')
	ball = pygame.transform.scale(ball, (40, 40))
	basket = pygame.image.load('Assets/1/basket.png')
	basket = pygame.transform.scale(basket, (120, 170))
	t = pygame.image.load('Assets/t1.png')

	#Инициализация pygame
	pygame.init()

	#Основной цикл
	while running:
		for event in pygame.event.get():
			#Выключения игры
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
				right = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
				left = True
			if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
				right = False
			if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
				left = False

		screen.blit(sky, [0,0])
		for i in range(12):
			screen.blit(grass, [i*60,440])

		if right:
			xp += 7
		if left:
			xp -= 7

		if yb >= 500-37:
			yb = 0
			xb = 50
			speed_by = 0
			speed_bx = 0
			loss = True
			win = False
			Passage1(ScreenX, ScreenY, running, FPS, timer, win, loss, gifts)

		if xb+40 >= 700:
			speed_bx = -speed

		if xb+40 <= 40:
			speed_bx = speed

		if (xp+140 >= xb+20 and xp+71 <= xb+90) and (yb+50 == 480):
			speed_by = -speed 
			speed_bx = speed


		if (xp+70 >= xb+20 and xp <= xb+60) and (yb+50 == 480):
			speed_by = -speed
			speed_bx = -speed 

		if (yb+40 >= ybasket+85 and yb <= ybasket+170) and (xb+40 == xbasket):
			speed_bx = -speed 
			speed_by = -speed

		if yb <= 0:
			speed_by = speed

		if (xbasket <= xb+40 and xbasket+120 >= xb) and (yb+40 >= ybasket+92 and yb+40 <= ybasket+97):
			speed_bx = -1
			speed_by = speed
			check += 1

		yb += speed_by
		xb += speed_bx


		if check >= 3:
			loss = False
			win = True
			gifts += 1
			Passage1(ScreenX, ScreenY, running, FPS, timer, win, loss, gifts)

		text = font.render(str(check), False,(255, 255, 255))
		screen.blit(text, (0, 0))

		screen.blit(t,[80,20])

		screen.blit(ball, [xb,yb])
		screen.blit(basket, [xbasket,ybasket])

		pygame.draw.rect(screen, [121,85,72], (xp, 470, 140, 30))
		pygame.draw.rect(screen, [237,28,36], (0, 497, 700, 3))

		#Счётчик FPS
		timer.tick(FPS)

		#Обновление содержимого окна
		pygame.display.flip()

	#Выключение игры
	pygame.quit()

#Заяц и волки
def Game2(ScreenX, ScreenY, running, FPS, timer, gifts):

	with open('Saving.txt', 'w') as f:
		f.write('2')

	level = 2

	wolf = pygame.image.load('Assets/2/wolf.png')
	wolf = pygame.transform.scale(wolf, (50, 50))
	carrot = pygame.image.load('Assets/2/carrot.png')
	carrot = pygame.transform.scale(carrot, (50, 50))
	rabbit = pygame.image.load('Assets/2/rebit.png')
	rabbit = pygame.transform.scale(rabbit, (50, 50))
	background = pygame.image.load('Assets/2/background1.png')
	background = pygame.transform.scale(background, (ScreenX, ScreenY))
	t = pygame.image.load('Assets/t2.png')

	x_rb = 40
	y_rb = 40
	x_w = []
	y_w = []

	x_c = []
	y_c = []

	u = []

	right = left = up = down = False

	speed_rabbit = 5

	k = 5
	l = 0

	value_c = 0

	font = pygame.font.Font(None, 70)

	screen = pygame.display.set_mode([ScreenX, ScreenY])

	#Инициализация pygame
	pygame.init()

	for i in range(3):
		x_w.append(random.randint(50,650))
		y_w.append(random.randint(50,450))

	for i in range(10):
		x_c.append(random.randint(50,650))
		y_c.append(random.randint(50,450))


	#Основной цикл
	while running:
		for event in pygame.event.get():
			#Выключения игры
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
				right = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
				left = True
			if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
				right = False
			if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
				left = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
				up = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
				down = True
			if event.type == pygame.KEYUP and event.key == pygame.K_UP:
				up = False
			if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
				down = False


		if x_rb <= 0:
			x_rb += 5

		if x_rb >= 650:
			x_rb -= 5

		if y_rb <= 0:
			y_rb += 5

		if y_rb >= 450:
			y_rb -= 5

		if right:
			x_rb += speed_rabbit

		elif left:
			x_rb -= speed_rabbit

		elif up:
			y_rb -= speed_rabbit

		elif down:
			y_rb += speed_rabbit 

		for i in range(len(x_w)):
			if x_w[i] != x_rb:
				if x_w[i]>x_rb:
					x_w[i] -= 2
				elif x_w[i]<x_rb:
					x_w[i] += 2
				if y_w[i] != y_rb:
					if y_w[i]>y_rb:
					    y_w[i] -= 2
					if y_w[i]<y_rb:
						y_w[i] += 2

		for i in range(len(x_w)):
			if (x_w[i] <= x_rb+49 and x_w[i]+49 >= x_rb) and (y_w[i] <= y_rb+49 and y_w[i]+49 >= y_rb):
				loss = True
				win = False
				Passage2(ScreenX, ScreenY, running, FPS, timer, win, loss, gifts)

		for i, j in zip(x_c, y_c):
			if (i <= x_rb+49 and i+49 >= x_rb) and (j <= y_rb+49 and j+49 >= y_rb):
				x_c.remove(i)
				y_c.remove(j)
				value_c += 1

		if value_c == 10:
			loss = False
			win = True
			gifts += 1
			Passage2(ScreenX, ScreenY, running, FPS, timer, win, loss, gifts)


		screen.blit(background, [0,0])

		for i in range(len(x_c)):
			screen.blit(carrot,[x_c[i],y_c[i]])

		for i in range(3):
			screen.blit(wolf,[x_w[i],y_w[i]])

		screen.blit(t,[180,20])
		screen.blit(rabbit,[x_rb,y_rb])

		text = font.render(str(value_c), False,(255, 255, 255))
		screen.blit(text, (0, 0))

		#Счётчик FPS
		timer.tick(FPS)

		#Обновление содержимого окна
		pygame.display.flip()

	#Выключение игры
	pygame.quit()

#Тир
def Game3(ScreenX, ScreenY, running, FPS, timer, gifts):

	with open('Saving.txt', 'w') as f:
		f.write('3')

	targets = pygame.image.load('Assets/3/targets.png')
	obstacles = pygame.image.load('Assets/3/obstacles.png')
	obstacles = pygame.transform.scale(obstacles, (190, 370))
	check = pygame.image.load('Assets/3/check.png')
	check = pygame.transform.scale(check, (200, 130))
	background_targets = pygame.image.load('Assets/3/background_targets.png') 
	t = pygame.image.load('Assets/t3.png')

	x_o = 0
	y_o = 0

	x1 = 0
	y1 = 0

	speed_o = 20

	target1 = target2 = target3 = False

	screen = pygame.display.set_mode([ScreenX, ScreenY])

	#Инициализация pygame
	pygame.init()

	#Основной цикл
	while running:
		for event in pygame.event.get():
			#Выключения игры
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEMOTION:
				(x1,y1) = event.pos
			if event.type == pygame.MOUSEBUTTONDOWN:
				(x1,y1)= event.pos
				if (x1 >= x_o+219 or x1 <= x_o):
					if (x1 >= 121 and x1 <= 125) and (y1 >= 149 and y1 <= 153):
						target1 = True
					if (x1 >= 351 and x1 <= 357) and (y1 >= 251 and y1 <= 257):
						target2 = True
					if (x1 >= 578 and x1 <= 584) and (y1 >= 152 and y1 <= 158):
						target3 = True

				else:
					loss = True
					win = False
					Passage3(ScreenX, ScreenY, running, FPS, timer, win, loss, gifts)

		if x_o >= 500:
			speed_o = -20
		elif x_o <= 0:
			speed_o = 20

		x_o += speed_o

		screen.fill((255,255,255))

		screen.blit(targets, [0,0])
		screen.blit(background_targets, [0,370])

		screen.blit(t,[170,420])

		if target1:
			pygame.draw.rect(screen, [34,177,76], (117, 146, 13, 13))
			screen.blit(check, [40,70])
		if target2:
			pygame.draw.rect(screen, [34,177,76], (348, 248, 13, 13))
			screen.blit(check, [270,170])
		if target3:
			pygame.draw.rect(screen, [34,177,76], (575, 148, 13, 13))
			screen.blit(check, [500,70])

		if target1 == target2 == target3 == True:
			loss = False
			win = True
			gifts += 1
			Passage3(ScreenX, ScreenY, running, FPS, timer, win, loss, gifts)

		screen.blit(obstacles, [x_o,y_o])

		pygame.draw.rect(screen, [112,146,190], (x1-6, y1-6, 13, 13))

		#Счётчик FPS
		timer.tick(FPS)

		#Обновление содержимого окна
		pygame.display.flip()

	#Выключение игры
	pygame.quit()

#Лабиринт
def Game4(ScreenX, ScreenY, running, FPS, timer, gifts):

	with open('Saving.txt', 'w') as f:
		f.write('4')

	screen = pygame.display.set_mode([ScreenX, ScreenY])

	pygame.init()

	character = pygame.image.load('Assets/4/geroy.png')
	wall = pygame.image.load('Assets/4/stena.jpg')
	road = pygame.image.load('Assets/4/doroga.jpg')
	spike = pygame.image.load('Assets/4/priz.png')
	key = pygame.image.load('Assets/4/key.png')
	door = pygame.image.load('Assets/4/exit.jpg')
	t = pygame.image.load('Assets/t4.png')

	font = pygame.font.Font(None, 30)

	nx=0 #Расстояния от края графического окна до лабиринта
	ny=1
	dx=30 #размеры клетки
	dy=30

	speed_c = 1 #Скорость

	points=0 #Изначальное количество ключей
	acces=6 #Необходимое количество ключей



	lab =   [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	        [0,0,3,1,1,1,1,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0],
	        [0,0,4,0,1,0,1,0,1,0,1,1,0,0,5,0,1,0,0,1,0,0,3,0],
	        [0,0,1,0,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,1,1,0,1,0],
	        [0,0,1,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],
	        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,4,0,0],
	        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
	        [0,0,0,0,1,1,4,0,0,1,1,1,3,0,0,1,1,1,1,1,0,0,0,0],
	        [0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0],
	        [0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,4,0,1,0,0,0,1,0],                            
	        [0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,3,0,1,0],
	        [0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,0,0,0,1,0],
	        [0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1,0],
	        [0,0,0,0,0,0,1,0,0,3,0,1,0,1,1,1,1,0,0,0,1,1,0,0],
	        [0,0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,0,1,0,0,0],
	        [0,2,1,1,1,1,1,0,0,1,1,1,0,4,0,0,3,0,0,4,1,0,0,0],
	        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
	        
	        # 0 - стена, 1 - дорога, 2 - персонаж, 3 - шип, 4 - ключ, 5 - дверь

	#Прорисовка лабиринта
	def drawlab(points,acces):
		for i in range(17):
			for j in range(24):
				x=nx+dx*j
				y=ny+dy*i
				if lab[i][j]==0:
					screen.blit(wall,[x,y])
				elif lab[i][j]==1:
					screen.blit(road,[x,y])
				elif lab[i][j]==2:
					screen.blit(character,[x,y])
					ix=i 
					jy=j
				elif lab[i][j]==3:
					screen.blit(spike,[x,y])
				elif lab[i][j]==4:
					screen.blit(key,[x,y])
				elif lab[i][j]==5:
					screen.blit(door,[x,y])

		screen.blit(t,[160,10])
		pygame.display.flip()
		return(ix,jy,font,points,acces)

	#Контроль клавиш
	def analyskey(i,j,ix,jy,speed_c,running,gifts):
		if event.key == pygame.K_UP and lab[ix-1][jy]!=0 and lab[ix-1][jy]!=5 and lab[ix-1][jy]!=3:
			i=ix-speed_c
		elif event.key == pygame.K_DOWN and lab[ix+1][jy]!=0 and lab[ix+1][jy]!=3:
			i=ix+speed_c
		elif event.key == pygame.K_LEFT and lab[ix][jy-1]!=0 and lab[ix][jy-1]!=3:
			j=jy-speed_c
		elif event.key == pygame.K_RIGHT and lab[ix][jy+1]!=0 and lab[ix][jy+1]!=3:
			j=jy+speed_c
		elif lab[ix-1][jy]==5:
			if points == acces:
				loss = False
				win = True
				gifts += 1
				Passage4(ScreenX, ScreenY, running, FPS, timer, win, loss, gifts)
			else:
				print('Не все ключи собраны!')
		elif lab[ix-1][jy]==3 or lab[ix+1][jy]==3 or lab[ix][jy-1]==3 or lab[ix][jy+1]==3:
			loss = True
			win = False
			Passage4(ScreenX, ScreenY, running, FPS, timer, win, loss, gifts)
		return(i,j)

	#Движение
	def movelab(i,j,ix,jy,lab,acces,points,speed_c):
		font = pygame.font.Font(None, 24)
		x=nx+dx*j
		y=ny+dy*i
		xk=nx+dx*jy
		yk=ny+dy*ix
		if lab[i][j]==0:
			ix=i
			jy=j
		if lab[i][j]==1:
			lab[i][j]=2
			lab[ix][jy]=1
			ix=i
			jy=j
		if lab[i][j]==3:
			ix=i
			jy=j
		if lab[i][j]==4:
			lab[i][j]=2
			lab[ix][jy]=1
			ix=i
			jy=j
			points += 1
		if lab[i][j]==6:
			ix=i
			jy=j
			
		return(i,j,ix,jy,lab,acces,points,speed_c)
	ix,jy,font,points,acces = drawlab(points,acces)
	i=ix
	j=jy


	#Основной цикл
	while running:
		for event in pygame.event.get():
			#Контроль выключения игры
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				i,j= analyskey(i,j,ix,jy,speed_c,running,gifts)
				i,j,ix,jy,lab,acces,points,speed_c = movelab(i,j,ix,jy,lab,acces,points,speed_c)
				
		drawlab(points,acces)

		timer.tick(FPS)

		#Обновление содержимого окна
		pygame.display.flip()

	#Выключение игры
	pygame.quit()

#---Переходы

def Passage1(ScreenX, ScreenY, running, FPS, timer, win, loss, gifts):
	screen = pygame.display.set_mode([ScreenX, ScreenY])

	#Инициализация pygame
	pygame.init()

	w = pygame.image.load('Assets/Passage/1_w.png')
	l = pygame.image.load('Assets/Passage/loss.png')
	c = pygame.image.load('Buttons/Continue.png')
	c_click = pygame.image.load('Buttons/Continue_click.png')

	b = c

	#Основной цикл
	while running:
		for event in pygame.event.get():
			#Выключения игры
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.MOUSEMOTION:
				(x1,y1)= event.pos
				if  (x1>=240 and x1<=240+231) and (y1>=450 and y1<=450+43):
					b = c_click
				else:
					b = c

			elif event.type == pygame.MOUSEBUTTONDOWN:
				(x1,y1)= event.pos
				if  (x1>=240 and x1<=240+231) and (y1>=450 and y1<=450+43):
					Game2(ScreenX, ScreenY, running, FPS, timer, gifts)

		if win:
			screen.blit(w, [0,0])
			win = False

		if loss:
			screen.blit(l, [0,0])

		screen.blit(b,[240,450])

		print(gifts)


		#Счётчик FPS
		timer.tick(FPS)

		#Обновление содержимого окна
		pygame.display.flip()

	#Выключение игры
	pygame.quit()

def Passage2(ScreenX, ScreenY, running, FPS, timer, win, loss, gifts):
	screen = pygame.display.set_mode([ScreenX, ScreenY])

	#Инициализация pygame
	pygame.init()

	w1 = pygame.image.load('Assets/Passage/1_w.png')
	w2 = pygame.image.load('Assets/Passage/2_w.png')
	l = pygame.image.load('Assets/Passage/loss.png')
	c = pygame.image.load('Buttons/Continue.png')
	c_click = pygame.image.load('Buttons/Continue_click.png')

	b = c

	#Основной цикл
	while running:
		for event in pygame.event.get():
			#Выключения игры
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.MOUSEMOTION:
				(x1,y1)= event.pos
				if  (x1>=240 and x1<=240+231) and (y1>=450 and y1<=450+43):
					b = c_click
				else:
					b = c

			elif event.type == pygame.MOUSEBUTTONDOWN:
				(x1,y1)= event.pos
				if  (x1>=240 and x1<=240+231) and (y1>=450 and y1<=450+43):
					Game3(ScreenX, ScreenY, running, FPS, timer, gifts)

		if win:
			if gifts == 1:
				screen.blit(w1, [0,0])
			elif gifts == 2:
				screen.blit(w2, [0,0])
			win = False

		if loss:
			screen.blit(l, [0,0])

		screen.blit(b,[240,450])

		print(gifts)


		#Счётчик FPS
		timer.tick(FPS)

		#Обновление содержимого окна
		pygame.display.flip()

	#Выключение игры
	pygame.quit()

def Passage3(ScreenX, ScreenY, running, FPS, timer, win, loss, gifts):
	screen = pygame.display.set_mode([ScreenX, ScreenY])

	#Инициализация pygame
	pygame.init()

	w1 = pygame.image.load('Assets/Passage/1_w.png')
	w2 = pygame.image.load('Assets/Passage/2_w.png')
	w3 = pygame.image.load('Assets/Passage/3_w.png')
	l = pygame.image.load('Assets/Passage/loss.png')
	c = pygame.image.load('Buttons/Continue.png')
	c_click = pygame.image.load('Buttons/Continue_click.png')

	b = c

	#Основной цикл
	while running:
		for event in pygame.event.get():
			#Выключения игры
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.MOUSEMOTION:
				(x1,y1)= event.pos
				if  (x1>=240 and x1<=240+231) and (y1>=450 and y1<=450+43):
					b = c_click
				else:
					b = c

			elif event.type == pygame.MOUSEBUTTONDOWN:
				(x1,y1)= event.pos
				if  (x1>=240 and x1<=240+231) and (y1>=450 and y1<=450+43):
					Game4(ScreenX, ScreenY, running, FPS, timer, gifts)

		if win:
			if gifts == 1:
				screen.blit(w1, [0,0])
			elif gifts == 2:
				screen.blit(w2, [0,0])
			elif gifts == 3:
				screen.blit(w3, [0,0])
			win = False

		if loss:
			screen.blit(l, [0,0])

		screen.blit(b,[240,450])

		print(gifts)


		#Счётчик FPS
		timer.tick(FPS)

		#Обновление содержимого окна
		pygame.display.flip()

	#Выключение игры
	pygame.quit()

def Passage4(ScreenX, ScreenY, running, FPS, timer, win, loss, gifts):
	screen = pygame.display.set_mode([ScreenX, ScreenY])

	#Инициализация pygame
	pygame.init()

	
	w1 = pygame.image.load('Assets/Passage/1_w.png')
	w2 = pygame.image.load('Assets/Passage/2_w.png')
	w3 = pygame.image.load('Assets/Passage/3_w.png')
	w4 = pygame.image.load('Assets/Passage/4_w.png')
	l = pygame.image.load('Assets/Passage/loss.png')
	c = pygame.image.load('Buttons/Continue.png')
	c_click = pygame.image.load('Buttons/Continue_click.png')

	b = c

	#Основной цикл
	while running:
		for event in pygame.event.get():
			#Выключения игры
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.MOUSEMOTION:
				(x1,y1)= event.pos
				if  (x1>=240 and x1<=240+231) and (y1>=450 and y1<=450+43):
					b = c_click
				else:
					b = c

			elif event.type == pygame.MOUSEBUTTONDOWN:
				(x1,y1)= event.pos
				if  (x1>=240 and x1<=240+231) and (y1>=450 and y1<=450+43):
					Finish(ScreenX, ScreenY, running, FPS, timer, gifts)

		if win:
			if gifts == 1:
				screen.blit(w1, [0,0])
			elif gifts == 2:
				screen.blit(w2, [0,0])
			elif gifts == 3:
				screen.blit(w3, [0,0])
			elif gifts == 4:
				screen.blit(w4, [0,0])
			win = False

		if loss:
			screen.blit(l, [0,0])

		screen.blit(b,[240,450])

		print(gifts)


		#Счётчик FPS
		timer.tick(FPS)

		#Обновление содержимого окна
		pygame.display.flip()

	#Выключение игры
	pygame.quit()

#Финал
def Finish(ScreenX, ScreenY, running, FPS, timer, gifts):
	screen = pygame.display.set_mode([ScreenX, ScreenY])

	#Инициализация pygame
	pygame.init()

	g0 = pygame.image.load('Assets/Finish/0.png')
	g1 = pygame.image.load('Assets/Finish/1.png')
	g2 = pygame.image.load('Assets/Finish/2.png')
	g3 = pygame.image.load('Assets/Finish/3.png')
	g4 = pygame.image.load('Assets/Finish/4.png')
	home = pygame.image.load('Buttons/Home.png')
	home_click = pygame.image.load('Buttons/Home_click.png')

	b = home

	#Основной цикл
	while running:
		for event in pygame.event.get():
			#Выключения игры
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.MOUSEMOTION:
				(x1,y1)= event.pos
				if  (x1>=10 and x1<=92) and (y1>=10 and y1<=87):
					b = home_click
				else:
					b = home

			elif event.type == pygame.MOUSEBUTTONDOWN:
				(x1,y1)= event.pos
				if  (x1>=10 and x1<=92) and (y1>=10 and y1<=87):
					Menu()

		print(gifts)
		if gifts == 0:
			screen.blit(g0, [0,0])

		elif gifts == 1:
			screen.blit(g1, [0,0])

		elif gifts == 2:
			screen.blit(g2, [0,0])

		elif gifts == 3:
			screen.blit(g3, [0,0])

		elif gifts == 4:
			screen.blit(g4, [0,0])


		screen.blit(b,[10,10])


		#Счётчик FPS
		timer.tick(FPS)

		#Обновление содержимого окна
		pygame.display.flip()

	#Выключение игры
	pygame.quit()


if __name__ == "__main__":
    Menu()