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
from public.components.breadcrumbs import BreadcrumbsExample
from public.components.button import ButtonExample
from public.components.input import InputExample
from public.components.select import SelectExample
from public.components.form import FormExample
from public.components.badge import BadgeExample
from public.components.card import CardExample
from public.components.popover import PopoverExample
from public.components.modal import ModalExample

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
breadcrumbs = BreadcrumbsExample()
button = ButtonExample()
input = InputExample()
select = SelectExample()
form = FormExample()
badge = BadgeExample()
card = CardExample()
popover = PopoverExample()
modal = ModalExample()

routes = [
  (
    "menu component",
    ClientRoutes.menu.value,
    Page([menu])
  ), 
  (
    "breadcrumbs component",
    ClientRoutes.breadcrumbs.value,
    Page([breadcrumbs])
  ),
  (
    "button component",
    ClientRoutes.button.value,
    Page([button])
  ),
  (
    "input component",
    ClientRoutes.input.value,
    Page([input])
  ), 
  (
    "select component",
    ClientRoutes.select.value,
    Page([select])
  ),
  (
    "form component",
    ClientRoutes.form.value,
    Page([form])
  ),
  (
    "badge component",
    ClientRoutes.badge.value,
    Page([badge])
  ),
  (
    "card component",
    ClientRoutes.card.value,
    Page([card])
  ),
  (
    "popover component",
    ClientRoutes.popover.value,
    Page([popover])
  ),
  (
    "modal component",
    ClientRoutes.modal.value,
    Page([modal])
  ),
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

event_loop.run_until_complete(router.navigate("/menu"))

