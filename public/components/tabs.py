from public.components.common import *
from zenaura.client.component import Component
from public.constants import tabs_code
from zenaura.client.mutator import mutator
from public.styles import main_content
from public.components.card import Card

def TabButton(tab_number, label, active_tab_variable, on_click, class_name, active_class=" me-2 inline-block p-5 border-b-2 border-light-green border-spacing-2 dark:border-dark-page1"):
    class_expression = active_class if tab_number == active_tab_variable else ""
    return ButtonWithAttrsChildren(
        class_name=class_name  + class_expression,
        attrs={
            "py-click": on_click,
            "name": tab_number
        },
        children=[label]
    )

def TabContent(tab_number, active_tab_variable, content):
    is_visible = "block" if tab_number == active_tab_variable else "hidden"
    return Div(
        f"{is_visible} transition-all duration-300 p-4",
        [
         content    
        ]
    )

def Tabs(buttons, content, g_class_names ="bg-gray-100 font-sans", buttons_wrapper_class_names="flex  border-b-2 border-light-green dark:border-dark-black"):
    """
        Create tabs with content for each tab. 
        args:
            buttons : list of TabButton which is a button upon click becomes active and display content
            content : list of TabContent which is the content under each tab.
            g_class_names: global wrapper div class names
            button_wrapper_class_names: button wrapper div class names.
    """
    return Div(
		g_class_names,
		[
			Div(
				"p-8",
				[
					Div(
						"",
						[
							Div(
								buttons_wrapper_class_names,
								buttons
							),
							Div(
								"mt-3", 
                                content
							)
						]
					)
				]
			)
		]
	)

class TabsExample(Component):
    def __init__(self):
        self.active_tab = "1"
        self.show = False
        self.active_tab_example = "1"

    @mutator
    async def toggle_tabs(self, _):
        self.active_tab = "2" if self.active_tab == "1" else "1"
  
    @mutator
    async def active(self, event):
        self.active_tab_example = event.target.name

    def render(self):
        tabs_btns =  [
              TabButton(
                "1", 
                "One", 
                self.active_tab_example, 
                "tabs.active", 
                with_theme_colors_text_no_hover(
                  f"px-4 py-2 transition-all duration-300"
                  )
              ),
              TabButton(
                "2", 
                "two", 
                self.active_tab_example, 
                "tabs.active", 
                with_theme_colors_text_no_hover(
                  f"px-4 py-2 transition-all duration-300"
                  )
                ),
              TabButton(
                "3", 
                "three", 
                self.active_tab_example, 
                "tabs.active", 
                with_theme_colors_text_no_hover(
                  f"px-4 py-2 transition-all duration-300"
                  )
                ),
            ]
        tabs_content = [
          TabContent("1", self.active_tab_example, Header1("one", "")),
          TabContent("2", self.active_tab_example, Header1("two", "")),
          TabContent("3", self.active_tab_example, Header1("three", ""))
        ]
        comp =  Tabs(tabs_btns, tabs_content)
        
        return Div(main_content, [
          StyledComponentPresentation(
            "Tabs",
            "Displays a Tabs component - display content within tabs",
            "url",
            comp,
            tabs_code,
            self.active_tab,
            "tabs.toggle_tabs"
          )
        ])
