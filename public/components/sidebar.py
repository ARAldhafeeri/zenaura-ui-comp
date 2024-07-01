from .common import *
from public.styles import with_theme_colors, with_theme_colors_text_no_hover, main_content
from zenaura.client.component import Component

class Sidebar(Component):
  def __init__(self, router):
    self.active_comp = "menu"
    self.router = router
		
  async def set_active_comp(self, event):
    await self.router.navigate("/" + event.target.name)
		
  def render(self):
    return SidebarPresentational()

nav_item_style = with_theme_colors("px-3 py-2 text-sm")
category_class_name = with_theme_colors_text_no_hover("mb-1 rounded-md px-2 py-1 text-md font-semibold")

def SideBarNavigation():
	return [
		Header1("Navigation", category_class_name),
		NavItemTextNameFactory(
         "javascript:;", 
         "Menu", 
         nav_item_style,
        "side_nav_bar.set_active_comp",
		),
		NavItemTextNameFactory(
		"javascript:;", 
		"Breadcrumb", 
		nav_item_style,
		"side_nav_bar.set_active_comp",
		),
	]

def SideBarDataEntry():
	return [
		# Data Entry
		Header1("Data Entry", category_class_name),
		NavItemTextNameFactory(
         "javascript:;", 
         "Button", 
         nav_item_style,
        "side_nav_bar.set_active_comp"
		),
		NavItemTextNameFactory(
         "javascript:;", 
         "Input", 
         nav_item_style,
         "side_nav_bar.set_active_comp"
		),
		NavItemTextNameFactory(
         "javascript:;", 
         "Select", 
         nav_item_style,
         "side_nav_bar.set_active_comp"
		),
		NavItemTextNameFactory(
         "javascript:;", 
         "Form", 
         nav_item_style,
         "side_nav_bar.set_active_comp"
		),
	]

def SideBarDataDisplay():
	return [
		Header1("Data Display", category_class_name),
		NavItemTextNameFactory(
         "javascript:;", 
         "Badge", 
         nav_item_style,
         "side_nav_bar.set_active_comp"
		),
		NavItemTextNameFactory(
         "javascript:;", 
         "Card", 
         nav_item_style,
         "side_nav_bar.set_active_comp"
		),
		NavItemTextNameFactory(
         "javascript:;", 
         "Popover", 
         nav_item_style,
         "side_nav_bar.set_active_comp"
		),
		NavItemTextNameFactory(
         "javascript:;", 
         "Table", 
         nav_item_style,
         "side_nav_bar.set_active_comp"
		),
		NavItemTextNameFactory(
         "javascript:;", 
         "Tabs", 
         nav_item_style,
         "side_nav_bar.set_active_comp"
		),
	]

def SideBarFeedBack():
  return [
    Header1("Feedback", category_class_name),
		NavItemTextNameFactory(
         "javascript:;", 
         "Modal", 
         nav_item_style,
         "side_nav_bar.set_active_comp"
		),
		NavItemTextNameFactory(
         "javascript:;", 
         "Message", 
         nav_item_style,
        "side_nav_bar.set_active_comp"
		)
  ]

def SideBarOthers():
  return [
  Header1("Others", category_class_name),
		NavItemTextNameFactory(
         "javascript:;", 
         "Affix", 
         nav_item_style,
         "side_nav_bar.set_active_comp"
		)
  ]

def SidebarPresentational():
  print(len(SideBarNavigation()) + len(SideBarDataEntry()) + len(SideBarDataDisplay()) + len(SideBarFeedBack()) +len(SideBarOthers()))
  return Div(
    "flex flex-col float-left space-y-2 w-1/5 h-screen p-2 overflow-y-scroll bg-light-white dark:bg-dark-gray1", 
    # add more nav items here
    [
      # Navigation
      *SideBarNavigation(),
      *SideBarDataEntry(),
      *SideBarDataDisplay(),
      *SideBarFeedBack(),
      *SideBarOthers()
    ]
  )


