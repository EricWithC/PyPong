from . import tools
import pygame as pg
from . import setup

class MenuManager:
    def __init__(self):
        self.selected_index = 0
        self.last_option = None

    def draw_menu(self):
        for i, opt in enumerate(self.rendered["des"]):
            opt[1].center = (setup.SCREEN_RECT.centerx, self.from_bottom + i * self.spacer)
            if i == self.selected_index:
                rend_img, rend_rect = self.rendered["sel"][i]
                rend_rect.center = opt[1].center
                setup.SCREEN.blit(rend_img, rend_rect)
            else:
                setup.SCREEN.blit(opt[0], opt[1])
    
    def update_menu(self):
        # self.mouse_hover_sound()
        self.change_selected_option()

    def get_event_menu(self, event):
        if event.type == pg.KEYDOWN:
            if event.key in [pg.K_UP, pg.K_w]:
                self.change_selected_option(-1)
            elif event.key in [pg.K_DOWN, pg.K_s]:
                self.change_selected_option(1)
            elif event.key == pg.K_RETURN:
                self.select_option(self.selected_index)
        self.mouse_menu_click(event)
    
    # def mouse_hover_sound(self):
    #     '''Play sound when selected option changes'''
    #     for i, opt in enumerate(self.rendered["des"]):
    #         if opt[1].collidepoint(pg.mouse.get_pos()):
    #             if self.last_option != opt:
    #                 self.button_hover.sound.play()
    #                 self.last_option = opt
    
    def mouse_menu_click(self, event):
        '''Select menu option'''
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            for i, opt in enumerate(self.rendered["des"]):
                if opt[1].collidepoint(pg.mouse.get_pos()):
                    self.selected_index = i
                    self.select_option(i)
                    break
    
    def pre_render_options(self):
        '''Render menu options based on selected or deselected'''
        font_deselect = tools.Font.load('8bitOperatorPlus-Regular.ttf', 50)
        font_selected = tools.Font.load('8bitOperatorPlus-Regular.ttf', 75)

        rendered_msg = {"des": [], "sel": []}
        for option in self.options:
            d_rend = font_deselect.render(option, 1, (255, 255, 255))
            d_rect = d_rend.get_rect()
            s_rend = font_selected.render(option, 1, (255, 255, 0))
            s_rect = s_rend.get_rect()
            rendered_msg["des"].append((d_rend, d_rect))
            rendered_msg["sel"].append((s_rend, s_rect))
        self.rendered = rendered_msg

    def select_option(self, i):
        '''Select menu options via keys or mouse'''
        if i == len(self.next_list):
            self.quit = True
        else:
            # self.button_sound.sound.play()
            self.next = self.next_list[i]
            self.done = True
            self.selected_index = 0
    
    def change_selected_option(self, op=0):
        '''Change highlighted menu option'''
        for i, opt in enumerate(self.rendered["des"]):
            if opt[1].collidepoint(pg.mouse.get_pos()):
                self.selected_index = i
        if op:
            # self.button_hover.sound.play()
            self.selected_index += op
            max_ind = len(self.rendered["des"])-1
            if self.selected_index < 0:
                self.selected_index = max_ind
            elif self.selected_index > max_ind:
                self.selected_index = 0