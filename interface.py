import pygame

from game_object import GameObject
import config as c


class TextObject:
	def __init__(self,
				 x,
				 y,
				 text_func,
				 color,
				 font_name,
				 font_size):
		self.pos = (x, y)
		self.text_func = text_func
		self.color = color
		self.font = pygame.font.SysFont(font_name, font_size)
		self.bounds = self.get_surface(text_func())

	def draw(self, surface, centralized=False):
		text_surface, self.bounds = \
			self.get_surface(self.text_func())
		if centralized:
			pos = (self.pos[0] - self.bounds.width // 2,
				   self.pos[1])
		else:
			pos = self.pos
		surface.blit(text_surface, pos)

	def get_surface(self, text):
		text_surface = self.font.render(text,
										False,
										self.color)
		return text_surface, text_surface.get_rect()

	def update(self):
		pass

class Button(GameObject):
	def __init__(self,
				 x,
				 y,
				 w,
				 h,
				 text,
				 on_click=lambda x: None,
				 padding=0):
		super().__init__(x, y, w, h)
		self.state = 'normal'
		self.on_click = on_click

		self.text = TextObject(x + padding,
							   y + padding, lambda: text,
							   c.button_text_color,
							   c.font_name,
							   c.font_size)

	def draw(self, surface):
		pygame.draw.rect(surface,
						 self.back_color,
						 self.bounds)
		self.text.draw(surface)

	def handle_mouse_event(self, type, pos):
		if type == pygame.MOUSEMOTION:
			self.handle_mouse_move(pos)
		elif type == pygame.MOUSEBUTTONDOWN:
			self.handle_mouse_down(pos)
		elif type == pygame.MOUSEBUTTONUP:
			self.handle_mouse_up(pos)

	def handle_mouse_move(self, pos):
		if self.bounds.collidepoint(pos):
			if self.state != 'pressed':
				self.state = 'hover'
		else:
			self.state = 'normal'

	def handle_mouse_down(self, pos):
		if self.bounds.collidepoint(pos):
			self.state = 'pressed'

	def handle_mouse_up(self, pos):
		if self.state == 'pressed':
			self.on_click(self)
			self.state = 'hover'

	@property
	def back_color(self):
		return dict(normal=c.button_normal_back_color,
					hover=c.button_hover_back_color,
					pressed=c.button_pressed_back_color)[self.state]

	def create_menu(self):
		for i, (text, handler) in enumerate((('PLAY', on_play),
										 ('QUIT', on_quit))):
			b = Button(c.menu_offset_x,
					   c.menu_offset_y + (c.menu_button_h + 5) * i,
					   c.menu_button_w,
					   c.menu_button_h,
					   text,
					   handler,
					   padding=5)
			self.objects.append(b)
			self.menu_buttons.append(b)
			self.mouse_handlers.append(b.handle_mouse_event)
