from public.components.common import *
from zenaura.client.component import Component
from public.constants import input_code
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class

def Card(
    content,
    attrs, 
    default_class="shadow  w-64 me-2 px-2.5 py-0.5 rounded bg-light-white text-light-gray1 dark:text-dark-page1 dark:bg-dark-gray2", 
    ):
    """
      Displays a form input field. 
      args:
        content : card content of zenaura components or elements.
        attrs: card attributes.
        default_class: default css class names.
      
    """
    return Builder("div").with_attribute("class", default_class).with_attributes(**attrs).with_children(*content).build()

class CardExample(Component):
  def __init__(self):
    self.active_tab = "1"


  @mutator
  async def toggle_tabs(self, _):
    self.active_tab = "2" if self.active_tab == "1" else "1"
    
  def render(self):
    comp = Card(
      [
        Header1("The yearly Event", "text-light-gray1 text-2xl dark:text-dark-page1"), 
        Paragraph("The yearly event start at July the start of each year!", "text-light-gray1 dark:text-dark-page1")
      ], 
      {}
    )
    return Div(main_content, [
      StyledComponentPresentation(
        "Card",
        "Displays a card with content - customizable default styles",
        "url",
        comp,
        input_code,
        self.active_tab,
        "card.toggle_tabs"
      )
    ])