from public.components.common import *
from zenaura.client.component import Component
from public.constants import btn_code
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class

class ButtonExample(Component):
  def __init__(self):
    self.active_tab = "1"

  @mutator
  async def toggle_tabs(self, _):
    self.active_tab = "2" if self.active_tab == "1" else "1"
    
  def render(self):
    button = Button(
      btn_one_class,
      "Click me",
      "compnentInstance.methodName"
    )
    return Div(main_content, [
      StyledComponentPresentation(
        "Button",
        "Displays button with custom sytles, event handler",
        "url",
        button,
        btn_code,
        self.active_tab,
        "button.toggle_tabs"
      )
    ])