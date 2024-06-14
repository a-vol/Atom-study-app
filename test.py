import pygame
import sys
import time
from time import sleep, time
from datetime import datetime
import calendar as cld

pygame.init()  # initiates pygame and its audio module
# pygame.mixer.init()

width, height = 800, 600  #sets the window with dimensions, title and icon
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption('Atom')
programIcon = pygame.image.load('E:\\School\\Computer Science\\A LEVEL NEA CS\\pygame\\images\\atom.png')
pygame.display.set_icon(programIcon)
clock = pygame.time.Clock()
current_month, current_year = datetime.now().month, datetime.now(
).year  #get current month and year

# rgb colours dictionary
rgbDict = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'darkspace': (14, 36, 51),
    'lightspace': (114, 136, 151),
    'darkgrey': (52, 53, 59),
    'lightgrey': (81, 82, 92),
    'grey': (200, 200, 200),
    'lightpurple': (105, 105, 195),
    'darkpurple': (50, 20, 71),
    'poople': (75, 0, 130),
    'deepblue': (0, 0, 50)
}

font_size = 15  # initialise the fonts
font_color = rgbDict['white']
font = pygame.font.Font('E:\\School\\Computer Science\\A LEVEL NEA CS\\pygame\\fonts\\nasalization-rg.otf', font_size)


class MainMenu:  # first oop defines the main menu, and all sorts of stuff you can do inside the main menu

  def __init__(
      self, screen, settings_rect, calendar_rect
  ):  # When adding a button to the main menu, get the pygame rect (x, y, width, height) of the button
    self.screen = screen
    self.settings_rect = pygame.Rect(settings_rect)
    self.calendar_rect = pygame.Rect(calendar_rect)

  def handle_settings(
      self, events):  # handles events such as clicking on the buttons
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if self.settings_rect.collidepoint(event.pos):
          return 'settings'
        elif self.calendar_rect.collidepoint(event.pos):
          return 'calendar'

  def update(self):
    pygame.display.flip()

  def draw_buttons(self, button, events, text):  # draws the buttons using another class Button, passes events and text to put onto button
    button.drawRect(events)
    button.text(text)

  def draw_logo(self):  # draws logo and name
    font = pygame.font.Font('E:\\School\\Computer Science\\A LEVEL NEA CS\\pygame\\fonts\\nasalization-rg.otf', 50)
    text_surface = font.render('Atom', False, rgbDict['white'])
    text_rect = text_surface.get_rect()
    text_rect.center = (width // 2 + 19, height // 3)
    screen.blit(text_surface, text_rect)

    icon = pygame.image.load('E:\\School\\Computer Science\\A LEVEL NEA CS\\pygame\\images\\atom.png')
    iconResize = pygame.transform.scale(icon, (50, 50))

    screen.blit(iconResize, (width // 2 - 106, height // 3 - 25))

  def change_display(self, colour):
    displayColour(colour)


class Settings:

  def __init__(self, screen, mainmenu_rect):
    self.screen = screen
    self.mainmenu_rect = pygame.Rect(mainmenu_rect)

  def handle_back(self, events):
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if self.mainmenu_rect.collidepoint(event.pos):
          return 'main_menu'

  def update(self):
    pygame.display.flip()

  def draw_buttons(self, button, events, text):
    button.drawRect(events)
    button.text(text)

  def change_display(self, colour):
    displayColour(colour)

  def draw_title(self):
    global width, height
    font = pygame.font.Font('E:\\School\\Computer Science\\A LEVEL NEA CS\\pygame\\fonts\\nasalization-rg.otf', 30)
    settingstext = font.render('Settings', False, (rgbDict['white']))
    settingsrect = settingstext.get_rect()
    settingsrect.center = (width // 2, 60)

    screen.blit(settingstext, (settingsrect))


class Calendar:

  def __init__(self, screen, mainmenu_rect, exit_rect, create_event_rect):
    self.screen = screen
    self.mainmenu_rect = pygame.Rect(mainmenu_rect)
    self.exit_rect = pygame.Rect(exit_rect)
    self.create_event_rect = pygame.Rect(create_event_rect)

  def handle_back(self, events):
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if self.mainmenu_rect.collidepoint(event.pos):
          return 'main_menu'

  def handle_exit(self, events):
      for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.exit_rect.collidepoint(event.pos):
            return 'calendar'
          
  def handle_create(self, events):
      for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.create_event_rect.collidepoint(event.pos):
            return 'createevent'

  def update(self):
    pygame.display.flip()

  def draw_buttons(self, button, events, text):
    button.drawRect(events)
    button.text(text)

  def draw_grid(self):
    global width, height

    m = cld.monthcalendar(current_year, current_month)
    d = datetime.now().day

    for row in range(6):
      for col in range(7):

        for indexx, x in enumerate(m):
          for indexy, y in enumerate(x):
            if y == d:
              pygame.draw.rect(screen, rgbDict['poople'],
                               (60 + (80 * indexy), 140 +
                                (70 * indexx), 80, 70), 2)

            else:
              pygame.draw.rect(screen, rgbDict['lightgrey'],
                               (60 + (80 * col), 140 + (70 * row), 80, 70), 1)

    current_Date = datetime.now()
    current_month_name = current_Date.strftime('%B')

    font = pygame.font.Font('E:\\School\\Computer Science\\A LEVEL NEA CS\\pygame\\fonts\\nasalization-rg.otf', 30)
    calendartext = font.render(
        str(current_month_name) + ' - ' + str(current_year), False,
        (rgbDict['white']))
    calendarrect = calendartext.get_rect()
    calendarrect.center = (560 // 2 + 60, 60)

    screen.blit(calendartext, (calendarrect))
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for col, day in enumerate(days):
      font = pygame.font.Font('E:\\School\\Computer Science\\A LEVEL NEA CS\\pygame\\fonts\\nasalization-rg.otf', 20)
      text = font.render(day, False, (rgbDict['white']))
      screen.blit(text, (col * 80 + 100 +
                         (60 - text.get_width()) // 2 - 30, 140 - 40))

  def draw_boxes(self, events):
    array = (('', '', '', '', '', '', ''), ('', '', '', '', '', '', ''),
             ('', '', '', '', '', '', ''), ('', '', '', '', '', '', ''),
             ('', '', '', '', '', '', ''), ('', '', '', '', '', '', ''))
    columns = 7
    rows = 6
    buttons = [[
        Button(screen, rgbDict['darkgrey'], rgbDict['lightpurple'],
               (i * 80 + 60, j * 70 + 140, 80, 70)) for i in range(7)
    ] for j in range(6)]

    for row in buttons:
      for button in row:
        button.drawRect(events)

    return buttons

  def draw_day(self):
    font = pygame.font.Font('E:\\School\\Computer Science\\A LEVEL NEA CS\\pygame\\fonts\\nasalization-rg.otf', 15)
    month_calendar = cld.monthcalendar(current_year, current_month)
    for row, week in enumerate(month_calendar):
      for col, day in enumerate(week):
        if day != 0:
          text = font.render(str(day), False, rgbDict['white'])
          screen.blit(text,
                      ((col * 80 + 70 // 2) - (text.get_width() // 2) + 64,
                       (row * 70 + 70 // 2) - (text.get_height() // 2) + 140))

  def checkClick(self, buttons, events):
    for index0, row in enumerate(buttons):
      for index1, button in enumerate(row):
        for event in events:
          if event.type == pygame.MOUSEBUTTONDOWN:
            rect = pygame.Rect(button.Rect)
            if rect.collidepoint(event.pos):
              index = [index0, index1]
              return [index0, index1]
            else:
              break

  def change_display(self, colour):
    displayColour(colour)

  def getday_rect(self, index):

    for row in range(6):
      for col in range(7):
        if row == index[0] and col == index[1]:
          return pygame.Rect(col * 80 + 60, row * 70 + 140, 80, 70)
        


class Button:

  def __init__(self, surface, dColour, lColour, rect, width=0):
    self.surface = surface
    self.Rect = rect
    self.rect = pygame.Rect(rect)
    self.dColour = dColour
    self.lColour = lColour
    self.width = width

  def checkClick(self, events):
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if self.rect.collidepoint(event.pos):
          return True

  def checkHover(self, rect, events):
    for event in events:
      if event.type == pygame.MOUSEMOTION:
        hovered = (rect).collidepoint(event.pos)
        return hovered

  def drawRect(self, events):
    for event in events:
      if self.checkHover(self.rect, events):
        pygame.draw.rect(screen, self.lColour, (self.rect))
      else:
        pygame.draw.rect(screen, self.dColour, (self.rect))

  def text(self, text):
    rect = self.rect
    text_surface = font.render(text, False, font_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (rect[2] // 2) + rect[0], (rect[3] // 2) + rect[1]

    screen.blit(text_surface, text_rect)


class RadioButton:

  def __init__(self, x, y, text):
    self.x = x
    self.y = y
    self.text = text
    self.rect = pygame.Rect(self.x, self.y, 20, 20)
    self.selected = False

  def draw(self, screen):
    pygame.draw.circle(screen, rgbDict['white'], self.rect.center, 8)
    pygame.draw.circle(
        screen, rgbDict['darkgrey'] if self.selected else rgbDict['white'],
        self.rect.center, 5)

    text_surface = font.render(self.text, False, rgbDict['white'])
    text_rect = text_surface.get_rect()
    text_rect.center = (self.x - 30, self.y + 10)
    screen.blit(text_surface, text_rect)

  def checkClick(self, events):
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if self.rect.collidepoint(event.pos):
          return True

  def select(self):
    self.selected = True

  def deselect(self):
    self.selected = False


def displayColour(colour=rgbDict['darkspace']):
  screen.fill(colour)

def text_input():
    user_text = ""
    text_input_active = True
    while text_input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    text_input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
        pygame.draw.rect(screen, rgbDict['white'], (630, 214, 160, 25))
        # Render the user's text
        input_surface = font.render(user_text, False, rgbDict['black'])
        screen.blit(input_surface, (640, 220))

        pygame.display.flip()

    return user_text


colour = rgbDict['darkspace']
displayColour(colour)


def main():
  rickroll = pygame.mixer.Sound('E:\\School\\Computer Science\\A LEVEL NEA CS\\pygame\\sounds\\rick-rolled-short-version.mp3')
  colour = rgbDict['darkspace']
  current_interface = 'main_menu'
  next_interface = None
  b1_x, b1_y, b1_width, b1_height = 350, 450, 100, 25
  SettingsB = Button(screen, rgbDict['darkgrey'], rgbDict['lightgrey'],
                     (b1_x, b1_y, b1_width, b1_height))

  b2_x, b2_y, b2_width, b2_height = 50, 50, 80, 25
  MainMenuB = Button(screen, rgbDict['darkgrey'], rgbDict['lightgrey'],
                     (b2_x, b2_y, b2_width, b2_height))

  b3_x, b3_y, b3_width, b3_height = 350, 400, 100, 25
  CalendarB = Button(screen, rgbDict['darkgrey'], rgbDict['lightgrey'],
                     (b3_x, b3_y, b3_width, b3_height))
  
  b4_x, b4_y, b4_width, b4_height = 640, 480, 80, 25
  CalendarExitB = Button(screen, rgbDict['darkgrey'], rgbDict['lightgrey'],
            (b4_x, b4_y, b4_width, b4_height))
  
  b5_x, b5_y, b5_width, b5_height = 630, 214, 160, 25
  CalendarCreateEventB = Button(screen, rgbDict['darkgrey'], rgbDict['lightgrey'],
            (b5_x, b5_y, b5_width, b5_height))

  darkmodeB = RadioButton(110, 150, 'dark')
  lightmodeB = RadioButton(110, 180, 'light')
  specialB = RadioButton(110, 210, '???')

  main_menu = MainMenu(screen,
                       settings_rect=SettingsB.Rect,
                       calendar_rect=CalendarB.Rect)
  settings = Settings(screen, MainMenuB.Rect)
  calendar = Calendar(screen, MainMenuB.Rect, CalendarExitB.Rect, CalendarCreateEventB.Rect)

  change = True
  running = True
  display = False

  darkmodeB.select()
  while running:
    if change:
      displayColour(colour)
      change = False

    events = pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.MOUSEMOTION:
        print(event.pos)

    if current_interface == 'main_menu':
      if not display:
        main_menu.change_display(colour)
        display = True

      main_menu.draw_buttons(SettingsB, events, 'settings')
      main_menu.draw_buttons(CalendarB, events, 'calendar')
      main_menu.draw_logo()

      next_interface = main_menu.handle_settings(events)

    elif current_interface == 'calendar':
      
      exit = Button(screen, rgbDict['darkgrey'], rgbDict['lightgrey'],
            (640, 480, b2_width, b2_height))

      month_calendar = cld.monthcalendar(current_year, current_month)
      if not display:
        calendar.change_display(colour)
        display = True

      calendar.draw_buttons(MainMenuB, events, 'back')
      buttons = calendar.draw_boxes(events)
      calendar.draw_grid()
      calendar.draw_day()
      


      x = calendar.checkClick(buttons, events)
      if x:
        try:
          
          day = month_calendar[list(x)[0]][list(x)[1]]
          if day != 0:

            next_interface = 'calendarevent'
            if next_interface:
              current_interface = next_interface
              eventcreate = False
              display = False



          else:
            pass

        except IndexError:
          pass




    

      next_interface = calendar.handle_back(events)

    elif current_interface == 'calendarevent':
        
        if not display:
            pygame.draw.rect(screen, rgbDict['lightgrey'],
                         (630, 214, 160, 300))
            # pygame.draw.rect(screen, rgbDict['white'], ())
            display = True
              
        calendar.draw_buttons(CalendarExitB, events, 'exit')
        if not eventcreate:
            calendar.draw_buttons(CalendarCreateEventB, events, 'Create event')

        font = pygame.font.Font('E:\\School\\Computer Science\\A LEVEL NEA CS\\pygame\\fonts\\nasalization-rg.otf', 15)
        date_surface = font.render((f"{day}{'th' if 4 <= day % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')}" + ' ' + datetime.now().strftime('%B')), False, rgbDict['white'])
        daterect = date_surface.get_rect()
        daterect.center = (630 + (160//2), 260)
        screen.blit(date_surface, daterect)



        if CalendarCreateEventB.checkClick(events):
          eventcreate = True

        if eventcreate:
          pygame.draw.rect(screen, rgbDict['white'], (CalendarCreateEventB.Rect))

          user_input = text_input()
          print (user_input)

          eventcreate = False






        previous_interface = calendar.handle_exit(events)
        next_interface = calendar.handle_back(events)
        if previous_interface:
          current_interface = previous_interface
          display = False
        
        elif next_interface:
          current_interface = next_interface
          display = False
           
        x = calendar.checkClick(buttons, events)
        if x:
          current_interface = 'calendar'
          display = False


    elif current_interface == 'settings':
      if not display:
        settings.change_display(colour)
        display = True

      next_interface = settings.handle_back(events)
      settings.draw_buttons(MainMenuB, events, 'back')

      lightmodeB.draw(screen)
      darkmodeB.draw(screen)
      specialB.draw(screen)

      settings.draw_title()

      if lightmodeB.checkClick(events):
        lightmodeB.select()
        darkmodeB.deselect()
        specialB.deselect()
        colour = rgbDict['lightspace']
        change = True

      if darkmodeB.checkClick(events):
        colour = rgbDict['darkspace']
        darkmodeB.select()
        lightmodeB.deselect()
        specialB.deselect()
        change = True

      if specialB.checkClick(events):
        specialB.select()
        lightmodeB.deselect()
        darkmodeB.deselect()
        bg = pygame.image.load('E:\\School\\Computer Science\\A LEVEL NEA CS\\pygame\\images\\rick-astley.jpg')

        if not pygame.mixer.get_busy():
            rickroll.play()

        screen.blit(bg, (0, 0))
        change = False

    pygame.display.flip()
    clock.tick(60)

    if next_interface:
      current_interface = next_interface
      display = False

  pygame.quit()
  sys.exit()


if __name__ == '__main__':
  main()
