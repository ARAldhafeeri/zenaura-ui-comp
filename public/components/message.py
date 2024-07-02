from public.components.common import *
from zenaura.client.component import Component
from public.constants import message_code
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class

def Message(content, close, show, class_names="fixed top-0 px-4 py-4 right-0 mt-2  shadow z-40 rounded bg-light-white dark:bg-dark-black"):
    """
    Creates a closeable message notification
    
    args:
        text: content of message
        close: close handler
        class_names : Default class names
        show : boolean show or hide message
    """
    main = "relative" if show else "hidden"
    return Div(main, [
        Div(class_names, [
            Div("relative", [
                content,
                Button("fixed top-0 right-0 dark:text-dark-page1 ", "X", attrs={
                "py-click": close
                })
            ])
        ])
    ])

class MessageExample(Component):
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
        comp =  Div("", [
                    Button(btn_one_class, "show message", attrs={
                        "py-click": "message.open",
                        "data-hs-overlay": "#hs-basic-modal"
                    }),
                    Message(Paragraph("this is a message", "text-light-white dark:text-dark-page1"), "message.close", self.show)
                ])
        
        return Div(main_content, [
          StyledComponentPresentation(
            "Message",
            "Displays a temp message on the screen with exit button",
            "https://araldhafeeri.github.io/Zenaura/api/ui/message/",
            comp,
            message_code,
            self.active_tab,
            "message.toggle_tabs"
          )
        ])
