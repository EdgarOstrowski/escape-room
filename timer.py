import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class EscapeRoomTimer(object):
    def __init__(self, total_time):
        pygame.init()
        pygame.display.set_caption("Escape Room")

        self.screen = pygame.display.set_mode([700, 500])
        self.clock = pygame.time.Clock()
        self._frame_rate = 60
        self.total_time = total_time

    def _draw_clock(self):
        font = pygame.font.SysFont('Calibri', 50, True, False)
        # Calculate text area size for '00:00' so that the
        # text does not float around when time value is changing.
        # Maybe it would be better to use a fixed-width font.
        text = font.render('00:00', True, WHITE)
        text_offset = [text.get_width() / 2, text.get_height() / 2]

        minutes = self.total_time // 60
        seconds = self.total_time % 60

        output_str = '{0:02}:{1:02}'.format(minutes, seconds)

        if minutes >= 1:
            text_color = WHITE
        else:
            text_color = RED

        text = font.render(output_str, True, text_color)

        self.screen.blit(text, [self.screen.get_width() / 2 - text_offset[0],
                                self.screen.get_height() / 2 - text_offset[1]])

    def run(self):
        # Call user event every 1 sec
        pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

        done = False
        pause = True

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.USEREVENT + 1 and not pause:
                    if self.total_time:
                        self.total_time -= 1
                    else:
                        self.total_time = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = False

            self.screen.fill(BLACK)
            self._draw_clock()
            self.clock.tick(self._frame_rate)

            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    timer = EscapeRoomTimer(total_time=90)
    timer.run()
