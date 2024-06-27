from public.components.common import *
from zenaura.client.component import Component
from public.constants import popover_code
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class
from public.components.card import Card

def Popover(
    content,
    over_content,
    show=False,
    position="bottom-0"
    ):
    """
      Displays a button and popover appears when button is hovered over. 
      args:
        content : popover content
        attrs: card attributes.
        default_class: default css class names for content
        over_content: content that popover appear when overed over
        show: when user hover over over_content content card will be visible, elease will be hidden
        position: position of content to over_content, left-0, right-0, top-0, bottom-0 relative position
    """
    return Div(
        "relative",
      [
         over_content,
        Div(f"absolute z-10  {position}" + (" hidden" if not show else ""), [
         content
        ]),
      ]
      )

class PopoverExample(Component):
  def __init__(self):
    self.active_tab = "1"
    self.show = False


  @mutator
  async def toggle_tabs(self, _):
    self.active_tab = "2" if self.active_tab == "1" else "1"
  
  @mutator
  async def mouse_enter(self, _):
    self.show = True

  @mutator
  async def mouse_exit(self, _):
    self.show = False

  def render(self):
    comp = Popover(
      Card(
      [
        Header1("The yearly Event", "text-light-gray1 text-2xl dark:text-dark-page1"), 
        Paragraph("The yearly event start at July the start of each year!", "text-light-gray1 dark:text-dark-page1")
      ], 
      {}
    ), 
    Button(btn_one_class, "hover me", attrs={
      "py-mouseover": "popover.mouse_enter",
      "py-mouseleave": "popover.mouse_exit"
    }), 
    self.show
    )
    return Div(main_content, [
      StyledComponentPresentation(
        "Popover",
        "Displays a content that toggle popover on mouse enter, mouse leave",
        "url",
        comp,
        popover_code,
        self.active_tab,
        "popover.toggle_tabs"
      )
    ])