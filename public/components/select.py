from public.components.common import *
from zenaura.client.component import Component
from public.constants import select_code
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class

def Select(
    label_text,
    attrs,
    options, 
    default_input_class="w-full p-2 border border-gray-300 rounded bg-light-white text-light-gray1 dark:text-dark-page1 hover:bg-light-green dark:bg-dark-gray2 dark:hover:bg-dark-gray1", 
    default_label_class="block mb-2 text-light-gray1 dark:text-dark-page1",
    default_wrapper_class="p-4",
    ):
    """
      Displays a form input field. 
      args:
        attrs: python dictionary trasfrom into html attributes.
        label: label_text : input label text.
        default_input_class : default input css class names
        default_label_class : default label css class names
        default_wrapper_class : default input wrapper css class names
        options: select options List[Option]
      
    """
    return Div(default_wrapper_class, [
      Builder("label").with_attribute("class", default_label_class).with_text(label_text).build(),
      Builder('select').with_attribute("class", default_input_class).with_attributes(
        **attrs
      ).with_children(*options).build(),
    ])

def Option(
    label,
    attrs,
    default_input_class="w-full p-2 border border-gray-300 rounded bg-light-white text-light-gray1 dark:text-dark-page1 hover:bg-light-green dark:bg-dark-gray2 dark:hover:bg-dark-gray1", 
    ):
    """
      Displays a form input field. 
      args:
        attrs: python dictionary trasfrom into html attributes.
        default_input_class : default input css class names
        default_label_class : default label css class names
        value : text value of option      
    """
    return Builder('option').with_attribute("class", default_input_class).with_attributes(
      **attrs
    ).with_text(label).build()

class SelectExample(Component):
  def __init__(self):
    self.active_tab = "1"
    self.state = {"select" : ""}

  def update_state(self, field, value):
    self.state[field] = value

  def handle_input(self, event):
    field = event.target.name
    value = event.target.value
    self.update_state(field, value)
    print(self.state)

  @mutator
  async def toggle_tabs(self, _):
    self.active_tab = "2" if self.active_tab == "1" else "1"
    
  def render(self):
    select = Select(
      "Email: ",
      {
        "name": "select",
        "py-change": "select.handle_input",
      },
      [
         Option("Volvo", {"value": "volvo"}),
         Option("Saab", {"value": "saab"}),
         Option("Audi", {"value": "audi"})
      ]
    )
    return Div(main_content, [
      StyledComponentPresentation(
        "Select",
        "Displays select with option form field with custom sytles, event handler",
        "url",
        select,
        select_code,
        self.active_tab,
        "select.toggle_tabs"
      )
    ])