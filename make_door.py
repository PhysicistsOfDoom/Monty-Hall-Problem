import pygame 

class Door:
    def __init__(self, x, y, open_image, closed_image) -> None:
        self.x = x
        self.y = y
        self.closed_image = pygame.image.load(closed_image)
        self.open_image = pygame.image.load(open_image)
        self.image = self.closed_image
        self.rec = self.image.get_rect(center=(self.x, self.y))

    def toggle(self, door_open):
        if not door_open:
            self.image = self.open_image
        else:
            self.image = self.closed_image
        self.rec = self.image.get_rect(center=(self.x, self.y))