#랜덤한 운석 떨어지기3

if len(missileXY) ! = 0:
    for bx, by in missileXY:
        drawObject(missileXY, bx, by)

rockY += rockSpeed   # 운석 아래로 움직임

#운석이 지구로 떨어진 경우
if rockY > padHeight:
#새로운 운석(랜덤)
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0

drawObject(rock, rockX, rockY)   #운석 그리기

pygame.display.update()  #게임화면을 다시 그림
