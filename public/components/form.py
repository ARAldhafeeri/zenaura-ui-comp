from public.components.common import *
from zenaura.client.component import Component
from public.constants import form_code
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class
from public.components.input import Input
from public.components.button import Button

def Form(
    attrs,
    fields,
    on_submit,
    default_form_styles="w-full p-2 border border-gray-300 rounded bg-light-white text-light-gray1 dark:text-dark-page1 hover:bg-light-green dark:bg-dark-gray2 dark:hover:bg-dark-gray1", 
    ):
    """
      Displays a form input field. 
      args:
        attrs: python dictionary trasfrom into html attributes.
        default_form_styles : default input css class names for form
        fields: list of zenaura input fields or custom elements
      
    """
    return Builder("form").with_attribute("class", default_form_styles).with_attributes(**attrs).with_children(*fields).with_attribute("py-submit", on_submit).build()


class FormExample(Component):
  def __init__(self):
    self.active_tab = "1"
    self.state = {
      "name": "",
      "email": "",
      "message": ""
    }

  def update_state(self, field, value):
    self.state[field] = value

  def handle_input(self, event):
      field = event.target.name
      value = event.target.value
      self.update_state(field, value)
      print(self.state)

  def submit(self, event):
    event.preventDefault()
    print("Form submitted with:", self.state)

  @mutator
  async def toggle_tabs(self, _):
    self.active_tab = "2" if self.active_tab == "1" else "1"
    
  def render(self):
    form = Form(
      {},
      [
      Input(
        "Name: ",
        {
          "name": "name", "py-change": "form.handle_input", 
          "type": "text", "placeholder": "enter your name.."
        }
      ), 
      Input(
        "Email: ",
        {
          "name": "email", "py-change": "form.handle_input", 
          "type": "text", "placeholder": "enter email.."
        }
      ), 
      Input(
        "Message: ",
        {
          "name": "message", "py-change": "form.handle_input", 
          "type": "text", "placeholder": "enter a message.."
        }
      ),
      Button(btn_one_class, "submit", "form.submit")
      ],
      "form.submit"
    )
    return Div(main_content, [
      StyledComponentPresentation(
        "Form",
        "Displays a form with zenaura data entry components, with a submit",
        "url",
        form,
        form_code,
        self.active_tab,
        "select.toggle_tabs"
      )
    ])