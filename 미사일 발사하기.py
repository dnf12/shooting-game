#미사일 발사하기3


drawObject(fighter,x,y)  #비행기를 게임 화면의(x,y) 좌표에 그림

#미사일 발사 화면에 그리기
if len(missileXY) !=0:
    for i, bxy in enumerate(missileXY): #미사일 요소에 대해 반복함
        bxy[1] -=10
        missileXY[i][1] = bxy[1]

        if bxy[1] <= 0: #미사일이 화면 밖을 벗어나면
            try:
                missileXY.remove(bxy) #미사일 제거
            except:
                pass

if len(missileXY) != 0:
    for bx, by in missileXY:
        drawObject(missile, bx, by)

pygame.display.update() #게임화면을 다시그림
