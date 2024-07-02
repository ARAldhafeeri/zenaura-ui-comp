from public.components.common import *
from zenaura.client.component import Component
from public.constants import input_code
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class

def Input(
    label_text,
    attrs, 
    default_input_class="w-full p-2 border border-gray-300 rounded bg-light-white text-light-gray1 dark:text-dark-page1 hover:bg-light-green dark:bg-dark-gray2 dark:hover:bg-dark-gray1", 
    default_label_class="block mb-2 text-light-gray1 dark:text-dark-page1",
    default_wrapper_class="p-4"
    ):
    """
      Displays a form input field. 
      args:
        attrs: python dictionary trasfrom into html attributes.
        label: label_text : input label text.
        default_input_class : default input css class names
        default_label_class : default label css class names
        default_wrapper_class : default input wrapper css class names
      
    """
    return Div(default_wrapper_class, [
      Builder("label").with_attribute("class", default_label_class).with_text(label_text).build(),
      Builder('input').with_attribute("class", default_input_class).with_attributes(
        **attrs
      ).build(),
    ])

class InputExample(Component):
  def __init__(self):
    self.active_tab = "1"
    self.state = {"email" : ""}

  def update_state(self, field, value):
    self.state[field] = value

  def handle_input(self, event):
    field = event.target.name
    value = event.target.value
    self.update_state(field, value)

  @mutator
  async def toggle_tabs(self, _):
    self.active_tab = "2" if self.active_tab == "1" else "1"
    
  def render(self):
    input = Input(
      "Email: ",
      {
        "name": "email",
        "py-change": "input.change", # instache name input = InputExample()
        "type": "email",
        "placeholder": "enter email.."
      }
    )
    return Div(main_content, [
      StyledComponentPresentation(
        "Input",
        "Displays input form field with custom sytles, event handler",
        "https://araldhafeeri.github.io/Zenaura/api/ui/input/",
        input,
        input_code,
        self.active_tab,
        "input.toggle_tabs"
      )
    ])