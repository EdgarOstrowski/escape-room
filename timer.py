import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()


screen_width = 700
screen_height = 500
size = [screen_width, screen_height]

screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False
clock = pygame.time.Clock()
font = pygame.font.SysFont('Calibri', 50, True, False)

frame_count = 0
frame_rate = 60
start_time = 90  # sec

pause = True

text = font.render('00:00', True, WHITE)
width_offset = text.get_width() / 2
height_offset = text.get_height() / 2

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = False

    screen.fill(BLACK)

    total_time = start_time - (frame_count // frame_rate)
    if total_time < 0:
        total_time = 0

    minutes = total_time // 60
    seconds = total_time % 60

    output_str = '{0:02}:{1:02}'.format(minutes, seconds)

    if minutes >= 1:
        text_color = WHITE
    else:
        text_color = RED

    text = font.render(output_str, True, text_color)

    screen.blit(text, [screen_width / 2 - width_offset,
                       screen_height / 2 - height_offset])

    if not pause:
        frame_count += 1

    clock.tick(frame_rate)

    pygame.display.flip()

pygame.quit()
