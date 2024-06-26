from public.components.common import *
from zenaura.client.component import Component
from public.constants import badge_code
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class

def Badge(
    text,
    attrs, 
    default_class="p-2 text-xs font-medium me-2 px-2.5 py-0.5 rounded bg-light-white text-light-gray1 dark:text-dark-page1 dark:bg-dark-gray2", 
    ):
    """
      Displays a form input field. 
      args:
        text : badge text.
        attrs: span attributes.
        default_class: default css class names.
      
    """
    return Builder("span").with_text(text).with_attribute("class", default_class).with_attributes(**attrs).build()

class BadgeExample(Component):
  def __init__(self):
    self.active_tab = "1"


  @mutator
  async def toggle_tabs(self, _):
    self.active_tab = "2" if self.active_tab == "1" else "1"
    
  def render(self):
    badge = Badge("La ilaha illa Allah", {})
    return Div(main_content, [
      StyledComponentPresentation(
        "Badge",
        "Displays a bdage with specific text with customizable default styles",
        "url",
        badge,
        badge_code,
        self.active_tab,
        "badge.toggle_tabs"
      )
    ])