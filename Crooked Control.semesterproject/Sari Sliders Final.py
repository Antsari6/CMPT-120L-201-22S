# Final Project for Intro to Programming

import pygame, sys, random

# All defined classes

class Paddles:
	def __init__(self, screen, color, posX, posY, width, height):
		self.screen = screen
		self.color = color
		self.posX = posX
		self.posY = posY
		self.width = width #Different from WIDTH
		self.height = height 
		self.state = 'stopped'
		self.draw()

	def draw(self):
		pygame.draw.rect( self.screen, self.color, (self.posX, self.posY, self.width, self.height) )

	def move(self):
		# moving up
		if self.state == 'up':
			self.posY -= 12

		# moving down
		elif self.state == 'down':
			self.posY += 12

	def clamp(self):
		if self.posY <= 0:
			self.posY = 0

		if self.posY + self.height >= HEIGHT:
			self.posY = HEIGHT - self.height

	def restart_pos(self):
		self.posY = HEIGHT//2 - self.height//2
		self.state = 'stopped'
		self.draw()

class Bomb:
	def __init__(self, screen, color, posX, posY, radius):
		self.screen = screen
		self.color = color
		self.posX = posX
		self.posY = posY
		self.dx = 0
		self.dy = 0
		self.radius = radius
		self.draw()

	def draw(self):
		pygame.draw.circle( self.screen, self.color, (self.posX, self.posY), self.radius )

	def start(self):
		self.dx = 7
		self.dy = 8

	def move(self):
		self.posX += self.dx
		self.posY += self.dy

	def wall_collision(self):
		self.dy = -self.dy

	def paddle_collision(self):
		self.dx = -self.dx

	def restart_pos(self):
		self.posX = WIDTH//2
		self.posY = HEIGHT//2
		self.dx = 0
		self.dy = 0
		self.draw()

class Scorecount:
	def __init__(self, screen, points, posX, posY):
		self.screen = screen
		self.points = points
		self.posX = posX
		self.posY = posY
		self.font = pygame.font.SysFont("monospace", 80, bold=True)
		self.label = self.font.render(self.points, 0, WHITE)
		self.show()

	def show(self):
		self.screen.blit(self.label, (self.posX - self.label.get_rect().width // 2, self.posY))

	def increase(self):
		points = int(self.points) + 1
		self.points = str(points)
		self.label = self.font.render(self.points, 0, WHITE)

	def restart(self):
		self.points = '0'
		self.label = self.font.render(self.points, 0, WHITE)

class CollisionManager:
	def between_ball_and_paddle1(self, ball, paddle):
		ballX = ball.posX
		ballY = ball.posY
		paddleX = paddle.posX
		paddleY = paddle.posY

		# y is in collision area?
		if ballY + ball.radius > paddleY and ballY - ball.radius < paddleY + paddle.height:
			# x is in collision area?
			if ballX - ball.radius <= paddleX + paddle.width:
				# collision
				return True

		# no collision
		return False

	def between_ball_and_paddle2(self, ball, paddle):
		ballX = ball.posX
		ballY = ball.posY
		paddleX = paddle.posX
		paddleY = paddle.posY

		# y is in collision?
		if ballY + ball.radius > paddleY and ballY - ball.radius < paddleY + paddle.height:
			# x is in collision?
			if ballX + ball.radius >= paddleX:
				# collision
				return True

		# no collision
		return False

	def between_ball_and_walls(self, ball):
		ballY = ball.posY

		# top collision
		if ballY - ball.radius <= 0:
			return True

		# bottom collision
		if ballY + ball.radius >= HEIGHT:
			return True

		# no collision
		return False

	def between_ball_and_goal1(self, ball):
		return ball.posX + ball.radius <= 0

	def between_ball_and_goal2(self, ball):
		return ball.posX - ball.radius >= WIDTH


def startmenu():
	pygame.init()
	displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption(('Sari Sliders Project'))
	bigfont = pygame.font.SysFont('Times New Roman', 90)
	smallfont = pygame.font.SysFont('Times New Roman', 40)
	titletext = bigfont.render('Sari Sliders', True, 'WHITE')
	starttext = smallfont.render('Press K To Continue', True, 'WHITE')

	running = True
	
	while running:

		displaysurface.fill((116,16,116))
		displaysurface.blit(titletext, (WIDTH/5, 50))
		displaysurface.blit(starttext, (WIDTH/5, 270))
		pygame.display.update()
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
				sys.exit()
			if event.type == pygame.KEYDOWN and event.key != pygame.K_1 and event.key == pygame.K_k:
				objective()


def objective():

	displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Sari Sliders")
	titling = pygame.font.SysFont('Calibri', 45)
	caption = pygame.font.SysFont('Calibri', 30)
	titletext = titling.render('CURRENT MISSION', True, 'WHITE')
	basetext1 = caption.render('Avoid having the grenade enter your side', True, 'WHITE')
	basetext2 = caption.render('First to lose has to smell the winners foot', True, 'WHITE')
	basetext3 = caption.render('W/S and Up/Down keys move your paddle', True, 'WHITE')
	basetext4 = caption.render('Press Q to quit, R to reset', True, 'WHITE')
	basetext5 = caption.render('Press P to continue to the game', True, 'WHITE')
	
	running = True

	while running:

		displaysurface.fill((116, 63, 116))
		displaysurface.blit(titletext, (WIDTH/4, 50))
		displaysurface.blit(basetext1, (WIDTH/4, 100))
		displaysurface.blit(basetext2, (WIDTH/4, 175))
		displaysurface.blit(basetext3, (WIDTH/4, 300))
		displaysurface.blit(basetext4, (WIDTH/4, 375))
		displaysurface.blit(basetext5, (WIDTH/4, 440))
		pygame.display.update()
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
				sys.exit()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
				True


# Colors and Screen Measure

WIDTH, HEIGHT = 900, 500
BLACK = (0, 0, 0)
WHITE = (255, 240, 225)
RED = (245, 0, 0)
BLOOD = (103,16,103)
GREEN = (67, 240, 25)

# Screen Display

pygame.init()
gamescreen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("Sari Sliders")

# Objects and Misc. defined variables

leftpaddle = Paddles( gamescreen, RED, 15, HEIGHT//2 - 60, 20, 120 ) #Left side 
rightpaddle = Paddles( gamescreen, WHITE, WIDTH - 20 - 15, HEIGHT//2 - 60, 20, 120 ) #Right Side
ball = Bomb( gamescreen, GREEN, WIDTH//2, HEIGHT//2, 12 )

score1 = Scorecount( gamescreen, '0', WIDTH//4, 15 )
score2 = Scorecount( gamescreen, '0', WIDTH - WIDTH//4, 15 )
 
bounce = CollisionManager()
FPS = 60
playing = False
clock = pygame.time.Clock()

# Functions needed for filling screen and restarting 

def draw_board():
	gamescreen.fill( BLOOD )
	pygame.draw.line( gamescreen, BLACK, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 5 )

def restart():
	draw_board()
	score1.restart()
	score2.restart()
	ball.restart_pos()
	leftpaddle.restart_pos()
	rightpaddle.restart_pos()

draw_board()

# Main Game Loop


while True:

    #Keyboard movement Input

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p and not playing:
				ball.start()
				playing = True

			if event.key == pygame.K_r and playing:
				restart()
				playing = False

			#Left Paddle movement

			if event.key == pygame.K_w:
				leftpaddle.state = 'up'

			if event.key == pygame.K_s:
				leftpaddle.state = 'down'

			#Right paddle movement

			if event.key == pygame.K_UP:
				rightpaddle.state = 'up'

			if event.key == pygame.K_DOWN:
				rightpaddle.state = 'down'

		if event.type == pygame.KEYUP:
			leftpaddle.state = 'stopped'
			rightpaddle.state = 'stopped'

	#	startmenu()

	if playing:
		
		draw_board()

        # Grenade Movement

		ball.move()
		ball.draw()

		# Paddle Movement 

		leftpaddle.move()
		leftpaddle.clamp()
		leftpaddle.draw()

		rightpaddle.move()
		rightpaddle.clamp()
		rightpaddle.draw()

		# Bottom/Top Wall Bounce

		if bounce.between_ball_and_walls(ball):
			ball.wall_collision()

		# Left Paddle collision c

		if bounce.between_ball_and_paddle1(ball, leftpaddle):
			ball.paddle_collision()

		# Right Paddle collision c

		if bounce.between_ball_and_paddle2(ball, rightpaddle):
			ball.paddle_collision()

		# Right Paddle Score (2)

		if bounce.between_ball_and_goal2(ball):
			draw_board()
			score1.increase()
			print('Right Paddle Survives')
			ball.restart_pos()
			leftpaddle.restart_pos()
			rightpaddle.restart_pos()
			playing = False

		# Left Paddle Scoring (1)

		if bounce.between_ball_and_goal1(ball):
			draw_board()
			score2.increase()
			print('Left Paddle Survives')
			ball.restart_pos()
			leftpaddle.restart_pos()
			rightpaddle.restart_pos()
			playing = False

	score1.show()
	score2.show()

	clock.tick(FPS)
	pygame.display.update()

