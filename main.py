import pygame, sys, random


size = (width, height) = 600, 380

pygame.init()

win = pygame.display.set_mode(size)
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

s = 10
cols, rows = int(win.get_width()/s), int((win.get_height()-30)/s)

cell_states = [0,1]

grid = [[random.choice(cell_states) for j in range(cols)] for i in range(rows)]

next_step = [[0 for j in range(cols)] for i in range(rows)]

x, y = cols//2, rows//2

#Generation
gen_value = 0
font = pygame.font.Font("freesansbold.ttf", 16)

textX=10
textY=10

def show_gen(x,y):
    gen = font.render("Generation: " + str(gen_value), True, (0,255,0))
    pygame.draw.rect(win, (0, 0, 0), (0, 0, win.get_width(), 30))
    win.blit(gen, (x,y))

def count_live_cells(i,j,grid):
  live_cells = 0
  if i>0 and grid[i-1][j] == 1:
    live_cells += 1
  if i>0 and j>0 and grid[i-1][j-1] == 1:
    live_cells += 1
  if i>0 and j+1<len(grid[0]) and grid[i-1][j+1] == 1:
    live_cells += 1
  if i+1<len(grid) and grid[i+1][j] == 1:
    live_cells += 1
  if i+1<len(grid) and j+1<len(grid[0]) and grid[i+1][j+1] == 1:
    live_cells += 1
  if i+1<len(grid) and j>0 and grid[i+1][j-1] == 1:
    live_cells += 1
  if j>0 and grid[i][j-1] == 1:
    live_cells += 1
  if j+1<len(grid[0]) and grid[i][j+1] == 1:
    live_cells += 1
  return live_cells


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for i in range(cols):
        for j in range(rows):
            xpos = i * s
            ypos = j * s + 30
            if grid[j][i] == 0:
                pygame.draw.rect(win, (0, 0, 0), (xpos, ypos, s, s))
            elif grid[j][i] == 1:
                pygame.draw.rect(win, (255, 255, 255), (xpos, ypos, s, s))
            pygame.draw.line(win, (20, 20, 20), (xpos,ypos), (xpos, height))
            pygame.draw.line(win, (20, 20, 20), (xpos,ypos), (width,ypos))


    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            live_count = count_live_cells(i,j,grid)
            if grid[i][j] == 1 and live_count < 2:
                next_step[i][j] = 0
            elif grid[i][j] == 1 and live_count in [2,3]:
                next_step[i][j] = 1
            elif grid[i][j] == 1 and live_count > 3:
                next_step[i][j] = 0
            elif grid[i][j] == 0 and live_count == 3:
                next_step[i][j] = 1
            else:
                next_step[i][j] = 0
    
    show_gen(textX,textY)
    if next_step != grid:
        gen_value += 1

    grid = next_step
    next_step = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    

    pygame.display.flip()
