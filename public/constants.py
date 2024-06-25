
menu_component_code = """
from zenaura.ui.commons import *
from zenaura.ui.menu import Menu
from zenaura.client.component import Component
from zenaura.client.mutator import mutator

def with_theme_colors(class_name):
  return f"{class_name} text-light-gray1 hover:text-light-green dark:text-dark-page1 dark:hover:text-dark-gray2"

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
    return Menu(
      main_btn, 
      [custom_profile_btn, *regular_menu_btns],
      self.open
    )

"""

breadcrumbs_code = """
from zenaura.ui.commons import *
from zenaura.ui.breadcrumbs import BreadCrumbs
from zenaura.client.component import Component
from zenaura.client.mutator import mutator

class BreadcrumbsExample(Component):
  def __init__(self):
    self.active_tab = "1"

  @mutator
  async def toggle_tabs(self, _):
    self.active_tab = "2" if self.active_tab == "1" else "1"

  def render(self):
    return BreadCrumbs(
      [
        ("Docs", "nav.docs"),
        ("Components", "nav.Components"),
        ("BreadCrumbs", "nav.BreadCrumbs")
      ]
    )
"""

btn_code = """
from zenaura.ui.commons import *
from zenaura.ui.button import Button
from zenaura.client.component import Component
from zenaura.client.mutator import mutator
btn_one_class = " inline-flex items-center justify-center whitespace-nowrap text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 text-primary-foreground shadow h-9 px-4 py-2 rounded-[6px] m-1 bg-light-gray1 text-light-white hover:bg-light-green dark:text-dark-page1 dark:bg-dark-black dark:hover:bg-dark-gray2 "
class ButtonExample(Component):
  def render(self):
    return Button(
      btn_one_class,
      "Click me",
      "compnentInstance.methodName"
    )
"""

input_code = """
from zenaura.ui.commons import *
from zenaura.ui.input import Input
from zenaura.client.component import Component
from zenaura.client.mutator import mutator

class InputExample(Component):
  def __init__(self):
    self.state = {"email" : ""}

  def update_state(self, field, value):
    self.state[field] = value

  def handle_input(self, event):
    field = event.target.name
    value = event.target.value
    self.update_state(field, value)
    
  def render(self):
    return  Input(
        "Email: ",
        {
          "name": "email",
          "py-change": "input.change", # instache name input = InputExample()
          "type": "email",
          "placeholder": "enter email.."
        }
    )
"""