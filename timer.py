import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

frame_rate = 60
total_time = 90  # sec

pygame.init()

screen_size = [700, 500]
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Escape Room")

clock = pygame.time.Clock()
font = pygame.font.SysFont('Calibri', 50, True, False)
text = font.render('00:00', True, WHITE)
text_offset = [text.get_width() / 2, text.get_height() / 2]

# Call user event every 1 sec
pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

done = False
pause = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.USEREVENT + 1 and not pause:
            if total_time:
                total_time -= 1
            else:
                total_time = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = False

    screen.fill(BLACK)

    minutes = total_time // 60
    seconds = total_time % 60

    output_str = '{0:02}:{1:02}'.format(minutes, seconds)

    if minutes >= 1:
        text_color = WHITE
    else:
        text_color = RED

    text = font.render(output_str, True, text_color)

    screen.blit(text, [screen_size[0] / 2 - text_offset[0],
                       screen_size[1] / 2 - text_offset[1]])

    clock.tick(frame_rate)

    pygame.display.flip()

pygame.quit()
