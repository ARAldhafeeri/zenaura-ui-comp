import asyncio
from zenaura.client.app import Route, App, HistoryNode
from zenaura.client.page import Page
from public.routes import ClientRoutes
from zenaura.client.layout import Layout
from zenaura.client.dom import zenaura_dom
from public.styles import main_content
from public.routes import ClientRoutes
from public.components.sidebar import Sidebar
# styled components in component page
from public.components.menu import MenuExample

try :
    from pyscript import window, document
except ImportError:
    from zenaura.client.mocks import MockWindow
    window = MockWindow()

event_loop = asyncio.get_event_loop()

import asyncio

router = App()

# Instantiate components
side_nav_bar = Sidebar(router)

# styled components page
menu = MenuExample()

# App and routing
menu_page = Page([menu])


routes = [
    (
        "menu component",
        ClientRoutes.menu.value,
        menu_page
    )
]

for title, path, page in routes:
    router.add_route(Route(
        title=title,
        path=path,
        page=page
    ))

my_app_layout = Layout(
    top= [side_nav_bar], 
    routes=router.routes,
    bottom=[]
)


# sync layout component lifecycle methods
router.layout = my_app_layout

