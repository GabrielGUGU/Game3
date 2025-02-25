import pgzrun
import random

# Ventana de juego
forest = Actor('forest')
cell =   Actor('border')
cell1 =  Actor('grass')
cell2 =  Actor("grass2")
cell3 =  Actor("grass3")

size_w = 9  # Anchura del campo en celdas
size_h = 10  # Altura del campo en celdas
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h

TITLE = "GARDEN PUZZLE"  # Título de la ventana de juego
FPS = 30  # Número de fotogramas por segundo

my_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 1, 2, 1, 3, 1, 1, 0], 
    [0, 1, 1, 1, 2, 1, 1, 1, 0], 
    [0, 1, 3, 2, 1, 1, 3, 1, 0], 
    [0, 1, 1, 1, 1, 3, 1, 1, 0], 
    [0, 1, 1, 3, 1, 1, 2, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1]  # Fila de poder de ataque y salud
]

# Variables
char = Actor('r1')
char.top = cell.height
char.left = cell.width
char.health = 100
char.attack = 5

enemies = []
contador = 0
contador_enemigos = 0
modo = 1

# Crear enemigos
for i in range(5):
    x = random.randint(1, 7) * cell.width
    y = random.randint(1, 7) * cell.height
    enemy = Actor('enemy', topleft=(x, y))
    enemy.health = random.randint(10, 20)
    enemy.attack = random.randint(5, 10)
    enemies.append(enemy)

# Función para dibujar el mapa
def map_draw():
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            if my_map[i][j] == 0:
                cell.left = cell.width * j
                cell.top = cell.height * i
                cell.draw()
            elif my_map[i][j] == 1:
                cell1.left = cell.width * j
                cell1.top = cell.height * i
                cell1.draw()
            elif my_map[i][j] == 2:
                cell2.left = cell.width * j
                cell2.top = cell.height * i
                cell2.draw()
            elif my_map[i][j] == 3:
                cell3.left = cell.width * j
                cell3.top = cell.height * i
                cell3.draw()

# Función para dibujar en pantalla
def draw():
    global modo    
    if modo == 1:
        forest.draw()
        screen.draw.text("Garden Puzzle", center=(210, 50), color='red', fontsize=47)
        screen.draw.text("your mission:", center=(210, 100), color='red', fontsize=35)
        screen.draw.text("take care of the weeds in", center=(210, 135), color='red', fontsize=25)
        screen.draw.text("the least movements possible", center=(210, 160), color='red', fontsize=25)
        screen.draw.text("press ENTER to start", center=(210, 300), color='red', fontsize=30)

        if keyboard.RETURN:
            modo = 2

    if modo == 2:
        screen.fill("#2f3542")
        map_draw()
        char.draw()

        screen.draw.text("Movimientos:", center=(75, 475), color='white', fontsize=20)
        screen.draw.text(str(contador), center=(150, 475), color='white', fontsize=20)

        screen.draw.text("Hierbas eliminadas:", center=(300, 475), color='white', fontsize=20)
        screen.draw.text(str(contador_enemigos), center=(400, 475), color='white', fontsize=20)

        for enemy in enemies:
            enemy.draw()

        if contador_enemigos >= 5:
            forest.draw()
            screen.draw.text("FELICITACIONES", center=(210, 50), color='red', fontsize=47)
            screen.draw.text('Tus movimientos:', center = (210,145),color = 'red', fontsize = 35)
            screen.draw.text(str(contador), center=(210, 175), color='red', fontsize=30)
            screen.draw.text("Puntaje:", center=(210, 250), color='red', fontsize=25)
            screen.draw.text(str(56 - contador), center=(210, 275), color='red', fontsize=30)
            
# Función para detectar teclas
def on_key_down(key):
    global contador, contador_enemigos

    

    if key == keys.RIGHT and char.x + cell.width < WIDTH - cell.width:
        char.x += cell.width
        contador += 1

    elif key == keys.LEFT and char.x - cell.width > cell.width:
        char.x -= cell.width
        contador += 1

    elif key == keys.DOWN and char.y + cell.height < HEIGHT - cell.height * 2:
        char.y += cell.height
        contador += 1

    elif key == keys.UP and char.y - cell.height > cell.height:
        char.y -= cell.height
        contador += 1

    enemy_index = char.collidelist(enemies)
    if enemy_index != -1:
        enemies.pop(enemy_index)
        contador_enemigos += 1
        print(contador_enemigos)


pgzrun.go()
