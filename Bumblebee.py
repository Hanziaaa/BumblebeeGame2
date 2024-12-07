import pgzrun, random
WIDTH=400
HEIGHT=400
TITLE="BEE COLLECTOR"

bg=Actor("background") 
bee=Actor("bee")
bee.x=WIDTH//2
bee.y=HEIGHT//2
flower=Actor("flower")
score = 0

def place_flower():
    flower.x=random.randint(0,400)
    flower.y=random.randint(0,400)


def draw():
    global score 
    screen.clear()
    screen.blit("background",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text(str(score), "SCORE", color="orange")

def update():
    global score 
    if keyboard.left:
        bee.x = bee.x-2
        if bee.x < 0:
            bee.x=10   
    if keyboard.right:
        bee.x = bee.x+2
        if bee.x > WIDTH:
            bee.x=10
    if keyboard.up:
        bee.y -= 2
        if bee.y < 0:
            bee.y = 10
    if keyboard.down:
        bee.y = bee.y+2
        if bee.y > HEIGHT:
            bee.y = 10 
    if bee.colliderect(flower):
        place_flower()
        score=score+10


pgzrun.go()