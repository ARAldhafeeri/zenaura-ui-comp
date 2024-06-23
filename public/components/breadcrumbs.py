import asyncio
from public.components.common import *
from zenaura.client.component import Component, Reuseable
from public.constants import breadcrumbs_code
from zenaura.client.mutator import mutator
from public.styles import main_content

def BreadCrumbs(
    breadcrumbs, 
    seprator=">", 
    span_class="", 
    a_tag_class="opacity-60", 
    li_class="flex cursor-pointer items-center font-sans text-sm font-normal leading-normal antialiased transition-colors duration-300 text-light-gray1 hover:text-light-green dark:text-dark-page1 dark:hover:text-dark-gray2 ", 
    ol_class="flex w-full flex-wrap items-center rounded-md py-2 px-4", 
    sep_class="pointer-events-none mx-2 select-none font-sans text-sm font-normal leading-normal antialiased"
    ) -> "BreadCrumbs":
  """
    Display the path to the current resources as hierarchy of links

    args : 
      breadcrumbs - list of tuples as [("title", "handler"), ...] displayed in order
        handler url to navigate to.
        title is the title of breadcrumb that will be displayed.
      seprator - custom seprator between breadcrumbs default is text >
      span_class - span element classes
      a_tag_class - breadcrumb a tag css calsses
      li_class - breadcrumb li tag css classes
      ol_class - bread crumb ol tag css classes
      sep_class - breadcrumb seprator css classes
  """
  crumbs = []
  sep = Span(sep_class, seprator)
  for title, handler in breadcrumbs:
    crumb = LI(
      A(
        Span(span_class, title),
        {"class": a_tag_class, "href": handler},
      ),
      {"class": li_class}
    )
    crumbs.append(crumb)
    crumbs.append(sep)
  return OL(crumbs, {"class" : ol_class})

class BreadcrumbsExample(Component):
  def __init__(self):
    self.active_tab = "1"

  @mutator
  async def toggle_tabs(self, _):
    self.active_tab = "2" if self.active_tab == "1" else "1"

  def render(self):
    breadcrumbs = BreadCrumbs(
      [
        ("Docs", "nav.docs"),
        ("Components", "nav.Components"),
        ("BreadCrumbs", "nav.BreadCrumbs")
      ]
    )
    return Div(main_content, [
      StyledComponentPresentation(
      "Breadcrumbs",
      "Display a menu to the user - triggered by py-click",
      "url",
      breadcrumbs,
      breadcrumbs_code,
      self.active_tab,
      "breadcrumbs.toggle_tabs"
    )
    ])