import asyncio
from public.components.common import *
from zenaura.client.component import Component, Reuseable
from public.constants import menu_component_code
from zenaura.client.mutator import mutator
from public.styles import main_content

def Menu(main_btn : Button, children: List[ButtonWithAttrsChildren], show : bool) -> "Menu":
	"""
		Display a menu to the user - triggered by py-click

		args : 
			main_btn -> button used to toggle dropdown menu on click.
			children -> menu children 
			show -> used to toggle menu visibility
		return : 
			Togglable menu with options
	"""

	menu = Div(
		"absolute right-0 z-20 w-56 py-2 mt-2 overflow-hidden bg-white rounded-md shadow-xl dark:bg-dark-gray1" + (" hidden" if not show else ""),
		children
	)

	return Div("flex justify-center", [
		Div("relative inline-block mb-20", [
			main_btn, 
			menu

		])
	])

menu_items_cls = with_theme_colors(
   "flex hover:bg-light-hover dark:hover:bg-dark-hover overflow-auto w-full  items-center  items-center p-2 mt-2 text-sm"
)
menu_items_span_cls = "text-light-gray1 dark:text-dark-page1"
menu_items = [
  ( menu_items_cls, {}, menu_items_span_cls, "Settings" ),
  ( menu_items_cls, {}, menu_items_span_cls, "Keyboard shortcuts" ),
  ( menu_items_cls, {}, menu_items_span_cls, "Company profile" ),
  ( menu_items_cls, {}, menu_items_span_cls, "Team" ),
  ( menu_items_cls, {}, menu_items_span_cls, "Help" ),
  ( menu_items_cls, {}, menu_items_span_cls, "Sign out" ),
]

class MenuExample(Component):
  def __init__(self):
    self.open = False
    self.name = "menu"
    self.active_tab = "1"

  @mutator
  async def toggle_dropdown(self, _):
    self.open = not self.open

  @mutator
  async def toggle_tabs(self, _):
    self.active_tab = "2" if self.active_tab == "1" else "1"

  def render(self):

    regular_menu_btns = [ ]

    for class_names, attrs, span_class, span_text in menu_items:
      menu_item =  ButtonWithAttrsChildren(
          class_names, attrs,
        [
          Span( span_class, span_text),
        ]
      ) 
      regular_menu_btns.append(HR())
      regular_menu_btns.append(menu_item)

    main_btn = Button(
              "relative z-10 flex items-center p-2 text-sm text-gray-600 bg-white border border-transparent rounded-md focus:border-blue-500 focus:ring-opacity-40 dark:focus:ring-opacity-40 focus:ring-blue-300 dark:focus:ring-blue-400 focus:ring dark:text-white dark:bg-gray-800 focus:outline-none",
              "open",
              "menu.toggle_dropdown",
        )
    
    custom_profile_btn = ButtonWithAttrsChildren(
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
        )
    menu = Menu(
      main_btn, 
      [custom_profile_btn, *regular_menu_btns],
      self.open
    )
    return Div(main_content, [
      StyledComponentPresentation(
      "Menu",
      "Display a menu to the user - triggered by py-click",
      "https://araldhafeeri.github.io/Zenaura/api/ui/menu/",
      menu,
      menu_component_code,
      self.active_tab,
      "menu.toggle_tabs"
    )
    ])