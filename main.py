_G='Player:   '
_F='two_player'
_E='hard'
_D='medium'
_C='easy'
_B=False
_A=True
import pygame,random
pygame.init()
WIDTH,HEIGHT=1000,500
BACKGROUND_COLOR=255,255,255
PADDLE_COLOR=203,155,182
BALL_COLOR=189,189,230
NET_COLOR=0,0,0
BALL_SPEED=7
PADDLE_SPEED=10
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Air Hockey')
paddle_width=15
paddle_height=100
player_paddle=pygame.Rect(50,HEIGHT//2-paddle_height//2,paddle_width,paddle_height)
ai_paddle=pygame.Rect(WIDTH-50-paddle_width,HEIGHT//2-paddle_height//2,paddle_width,paddle_height)
ball=pygame.Rect(WIDTH//2-15,HEIGHT//2-15,30,30)
ball_speed_x=BALL_SPEED*random.choice((1,-1))
ball_speed_y=BALL_SPEED*random.choice((1,-1))
player_score=0
ai_score=0
font=pygame.font.Font(None,36)
EASY_AI_SPEED=2
MEDIUM_AI_SPEED=5
HARD_AI_SPEED=13
difficulty=None
selecting_difficulty=_A
while selecting_difficulty:
	screen.fill(BACKGROUND_COLOR);message='Choose game mode: Easy, Medium, Hard, Two-Player (press E, M, H, T)';text=font.render(message,_A,(0,0,0));text_rect=text.get_rect(center=(WIDTH//2,HEIGHT//2-50));screen.blit(text,text_rect);pygame.display.flip()
	for event in pygame.event.get():
		if event.type==pygame.QUIT:selecting_difficulty=_B
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_e:difficulty=_C;selecting_difficulty=_B
			elif event.key==pygame.K_m:difficulty=_D;selecting_difficulty=_B
			elif event.key==pygame.K_h:difficulty=_E;selecting_difficulty=_B
			elif event.key==pygame.K_t:difficulty=_F;selecting_difficulty=_B
clock=pygame.time.Clock()
def move_ai_paddle(ball,ai_speed):
	B=ai_speed;A=ball
	if ball_speed_x>0 and A.centerx>WIDTH//2:
		if ai_paddle.centery<A.centery:ai_paddle.y+=B
		elif ai_paddle.centery>A.centery:ai_paddle.y-=B
running=_A
while running:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:running=_B
	keys=pygame.key.get_pressed()
	if keys[pygame.K_DOWN]and player_paddle.bottom<HEIGHT:player_paddle.y+=PADDLE_SPEED
	if keys[pygame.K_UP]and player_paddle.top>0:player_paddle.y-=PADDLE_SPEED
	ball.x+=ball_speed_x;ball.y+=ball_speed_y
	if ball.top<=0 or ball.bottom>=HEIGHT:ball_speed_y=-ball_speed_y
	if ball.colliderect(player_paddle)or ball.colliderect(ai_paddle):ball_speed_x=-ball_speed_x
	if ball.left<=0:ai_score+=1;ball=pygame.Rect(WIDTH//2-15,HEIGHT//2-15,30,30);ball_speed_x=BALL_SPEED*random.choice((1,-1));ball_speed_y=BALL_SPEED*random.choice((1,-1))
	if ball.right>=WIDTH:player_score+=1;ball=pygame.Rect(WIDTH//2-15,HEIGHT//2-15,30,30);ball_speed_x=BALL_SPEED*random.choice((1,-1));ball_speed_y=BALL_SPEED*random.choice((1,-1))
	if difficulty==_C:ai_speed=EASY_AI_SPEED
	elif difficulty==_D:ai_speed=MEDIUM_AI_SPEED
	elif difficulty==_E:ai_speed=HARD_AI_SPEED
	else:ai_speed=PADDLE_SPEED
	if difficulty==_F:
		keys2=pygame.key.get_pressed()
		if keys2[pygame.K_s]and ai_paddle.bottom<HEIGHT:ai_paddle.y+=ai_speed
		if keys2[pygame.K_w]and ai_paddle.top>0:ai_paddle.y-=ai_speed
	else:move_ai_paddle(ball,ai_speed)
	screen.fill(BACKGROUND_COLOR);pygame.draw.rect(screen,PADDLE_COLOR,player_paddle);pygame.draw.rect(screen,PADDLE_COLOR,ai_paddle);pygame.draw.ellipse(screen,BALL_COLOR,ball);pygame.draw.aaline(screen,NET_COLOR,(WIDTH//2,0),(WIDTH//2,HEIGHT))
	if difficulty==_F:player_text=font.render('Player 1:   '+str(player_score),_A,PADDLE_COLOR);ai_text=font.render('Player 2:   '+str(ai_score),_A,PADDLE_COLOR)
	elif difficulty==_C:player_text=font.render(_G+str(player_score),_A,PADDLE_COLOR);ai_text=font.render('Easy AI:   '+str(ai_score),_A,PADDLE_COLOR)
	elif difficulty==_D:player_text=font.render(_G+str(player_score),_A,PADDLE_COLOR);ai_text=font.render('Medium AI:   '+str(ai_score),_A,PADDLE_COLOR)
	elif difficulty==_E:player_text=font.render(_G+str(player_score),_A,PADDLE_COLOR);ai_text=font.render('Hard AI:   '+str(ai_score),_A,PADDLE_COLOR)
	screen.blit(player_text,(WIDTH//4,50));screen.blit(ai_text,(3*WIDTH//4-ai_text.get_width(),50));pygame.display.flip();clock.tick(60)
pygame.quit()
