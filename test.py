import pygame

def text_to_screen(screen, text, x, y, size = 50,
            color = (200, 000, 000), font_type = 'data/fonts/orecrusherexpand.ttf'):
    try:

        text = str(text)
        font = pygame.font.Font(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    except Exception, e:
        print 'Font Error, saw it coming'
        raise \



eFunk.text_to_screen(screen, 'Text {0}'.format(score), xpos, ypos)



Funk.text_to_screen(screen, 'Text', xpos, ypos)