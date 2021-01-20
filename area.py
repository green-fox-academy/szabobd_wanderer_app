from enemies import Enemies

class Area:
    def __init__(self, grid):
        self.level = 1
        self.enemy_list = []

    def create_enemy_list(self, grid):
        enemies = Enemies(self.level, grid)
        self.enemy_list = enemies.enemy_list

    def draw(self, grid, hero, canvas, background, image_size):
        hero.x = 0
        hero.y = 0
        hero.has_key = False
        hero.killed_boss = False
        grid.draw(canvas, background, image_size)
        hero.draw(canvas, background, image_size)
        self.create_enemy_list(grid)
        for enemy in self.enemy_list:
            enemy.draw(canvas, background, image_size)
        hero.get_stats(canvas)
