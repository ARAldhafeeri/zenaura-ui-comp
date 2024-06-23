import asyncio
from public.components.common import *
from zenaura.client.component import Component, Reuseable
from public.constants import menu_component_code
from zenaura.client.mutator import mutator
from public.styles import main_content

class MenuExample(Component):
  def __init__(self):
    self.open = False
    self.name = "menu"
    self.active_tab = "1"

  @mutator
  async def toggle_dropdown(self, _):
    self.open = not self.open

  def render(self):
    menu = Menu(
        Button(
              "relative z-10 flex items-center p-2 text-sm text-gray-600 bg-white border border-transparent rounded-md focus:border-blue-500 focus:ring-opacity-40 dark:focus:ring-opacity-40 focus:ring-blue-300 dark:focus:ring-blue-400 focus:ring dark:text-white dark:bg-gray-800 focus:outline-none",
              "open",
              "menu.toggle_dropdown",
        ),
        [
        ButtonWithAttrsChildren(
              with_theme_colors("flex hover:bg-light-hover dark:hover:bg-dark-hover overflow-auto w-full  items-center  items-center p-2 mt-2 text-sm"), {},
            [
              Image(
                  "https://images.unsplash.com/photo-1523779917675-b6ed3a42a561?ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8d29tYW4lMjBibHVlfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=face&w=500&q=200",
                  "jane avatar", "35", "35",
                  "flex-shrink-0 object-cover mx-1 rounded-full w-9 h-9"
              ),
              Div("mx-1 ", [
                  Header1("Jane Doe", "text-sm font-semibold text-gray-700 dark:text-gray-200"),
                  Paragraph("janedoe@exampl.com", "text-sm text-gray-500 dark:text-gray-400")
              ])
            ] 
        ),
        HR(),
        ButtonWithAttrsChildren(
            with_theme_colors("flex hover:bg-light-hover dark:hover:bg-dark-hover overflow-auto w-full  items-center  items-center p-2 mt-2 text-sm"), {},
          [
            Span("text-light-gray1 dark:text-dark-page1", "Settings")
          ] 
        ),
        HR(),
        ButtonWithAttrsChildren(
            with_theme_colors("flex hover:bg-light-hover dark:hover:bg-dark-hover overflow-auto w-full  items-center  items-center p-2 mt-2 text-sm"), {},
          [
            Span("text-light-gray1 dark:text-dark-page1", "Keyboard shortcuts")
          ] 
        ),
        HR(),
        ButtonWithAttrsChildren(
            with_theme_colors("flex hover:bg-light-hover dark:hover:bg-dark-hover overflow-auto w-full  items-center  items-center p-2 mt-2 text-sm"), {},
          [
            Span("text-light-gray1 dark:text-dark-page1", "Company profile")
          ] 
        ),
        ButtonWithAttrsChildren(
            with_theme_colors("flex hover:bg-light-hover dark:hover:bg-dark-hover overflow-auto w-full  items-center  items-center p-2 mt-2 text-sm"), {},
          [
            Span("text-light-gray1 dark:text-dark-page1", "Team")
          ] 
        ),
        ButtonWithAttrsChildren(
            with_theme_colors("flex hover:bg-light-hover dark:hover:bg-dark-hover overflow-auto w-full  items-center  items-center p-2 mt-2 text-sm"), {},
          [
            Span("text-light-gray1 dark:text-dark-page1", "Invite colleagues")
          ] 
        ),
        HR(),
        ButtonWithAttrsChildren(
            with_theme_colors("flex hover:bg-light-hover dark:hover:bg-dark-hover overflow-auto w-full  items-center  items-center p-2 mt-2 text-sm"), {},
          [
            Span("text-light-gray1 dark:text-dark-page1", "Help")
          ] 
        ),
        HR(),
        ButtonWithAttrsChildren(
            with_theme_colors("flex hover:bg-light-hover dark:hover:bg-dark-hover overflow-auto w-full  items-center  items-center p-2 mt-2 text-sm"), {},
          [
            Span( "text-light-gray1 dark:text-dark-page1", "Sign Out")
          ] 
        ),
      ],
      self.open
    )
    return Div(main_content, [
      StyledComponentPresentation(
      "Menu",
      "Display a menu to the user - triggered by py-click",
      "url",
      menu,
      menu_component_code,
      self.active_tab
    )
    ])