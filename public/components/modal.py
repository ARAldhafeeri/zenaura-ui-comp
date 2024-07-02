from public.components.common import *
from zenaura.client.component import Component
from public.constants import modal_code
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class
from public.components.card import Card

def Modal(content, close_btn, show_modal=False, class_names="shadow z-40 rounded bg-light-white text-light-gray1 dark:text-dark-page1 dark:bg-dark-gray2"):
    """
    Creates a modal component with given content.
    
    args:
        content: Content to be displayed inside the modal, typically a Component.
        show_modal: Boolean to control the visibility of the modal.
        close_btn: Button to close modal when it's open
        class_names : Default class names
    """
    attrs = {"open": "", "class": class_names} if show_modal else {}
    modal_content = Dialog([
      content,
      close_btn,
    ], attrs)
    
    return modal_content

class ModalExample(Component):
    def __init__(self):
        self.active_tab = "1"
        self.show = False

    @mutator
    async def toggle_tabs(self, _):
        self.active_tab = "2" if self.active_tab == "1" else "1"
  
    @mutator
    async def open(self, _):
        self.show = True

    @mutator
    async def close(self, _):
        self.show = False

    @mutator
    async def save_changes(self, _):
        # Add functionality to save changes
        pass

    def render(self):
        comp =  Div("flex items-center justify-center", [
                    Button(btn_one_class, "Open modal", attrs={
                        "py-click": "modal.open",
                        "data-hs-overlay": "#hs-basic-modal"
                    }),
                Modal(
                  Div("flex flex-col justify-center shadow", [
                      Header1("The yearly Event", "text-light-gray1 text-2xl dark:text-dark-page1"), 
                      Paragraph("The yearly event starts in July at the beginning of each year!", "text-light-gray1 dark:text-dark-page1")
                  ]),
                  Button(btn_one_class, "Close", attrs={
                      "py-click": "modal.close"
                  }),
                  self.show
                )
                ])
        
        return Div(main_content, [
          StyledComponentPresentation(
            "Modal",
            "Displays a content that toggle popover on mouse enter, mouse leave",
            "https://araldhafeeri.github.io/Zenaura/api/ui/modal/",
            comp,
            modal_code,
            self.active_tab,
            "modal.toggle_tabs"
          )
        ])
