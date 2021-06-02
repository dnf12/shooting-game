#파괴한 운석 수와 놓친 운석 수 표시하기1

#운석을 맞춘 개수 계산
def writeScore(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 20)
    text = font.render('파괴한 운석 수:' +str(count), True, (255,255,255))
    gamePad.blit(text,(10,0))



#운석이 화면 아래로 통과한 개수
def writePassed(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 20)
    text = font.render('놓친 운석:' +str(count), True, (255,0,0))
    gamePad.blit(text,(360,0))
