from public.components.common import *
from zenaura.client.component import Component
from public.constants import input_code
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class
from public.components.card import Card

def Table(data, columns, attrs={}, class_names="min-w-full bg-white shadow-md rounded-xl", td_class_names="py-3 px-4 text-left", th_class_names="py-3 px-4", tr_class_names="border-b border-light-gray dark:border-dark-page1"):
    """
    Creates a table component with given data, columns.
    args:
        data - list of dictionaries of data e.g. [{"key" : 1, "name": "Mike"}]
        columns - list of dictionaries of column names [{"title": "Name", "index": "name"}]
            note index for each column is where data is indexed and displayed, for example
                when index is "name" , for every dictionary in data "name" is fetched and displayed
        class_names - default class name
        attrs table tag attributes dictionary
    """
    names = [Builder("th").with_class(th_class_names).with_text(col["title"]).build() for col in columns]
    indexes = [col["index"] for col in columns]
    rows = []
    for i in range(len(data)):
        row_items = [Builder("td").with_class(td_class_names).with_text(str(data[i][index])).build() for index in indexes]
        rows.append(Builder("tr").with_class(tr_class_names).with_children(
            *row_items
        ).build())
    
    return    Builder("table").with_attributes(**attrs).with_attribute("class", class_names).with_children(
        Builder("thead").with_child(
            Builder("tr").with_class(tr_class_names).with_children(
            *names
        ).build()
        ).build(),
        Builder("tbody").with_children(
            *rows
        ).build()
    ).build()

data = [
    {
        'key': '1',
        'name': 'Mike',
        'age': 32,
        'address': '10 Downing Street',
    },
    {
        'key': '2',
        'name': 'John',
        'age': 42,
        'address': '10 Downing Street',
    },
]

columns = [
    {
        'title': 'Name',
        'index': 'name',
        'key': 'name',
    },
    {
        'title': 'Age',
        'index': 'age',
        'key': 'age',
    },
    {
        'title': 'Address',
        'index': 'address',
        'key': 'address',
    },
]

class TableExample(Component):
    def __init__(self):
        self.active_tab = "1"
        self.show = False

    @mutator
    async def toggle_tabs(self, _):
        self.active_tab = "2" if self.active_tab == "1" else "1"
  

    def render(self):
        comp =  Table(data, columns)
        
        return Div(main_content, [
          StyledComponentPresentation(
            "Table",
            "Displays a table component that receive data, columns then display them",
            "url",
            comp,
            input_code,
            self.active_tab,
            "table.toggle_tabs"
          )
        ])
