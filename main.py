import flet as ft
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from model.model import Model
from UI.view import View
from UI.controller import Controller


def main(page: ft.Page):
    my_model = Model()
    my_view = View(page)
    my_controller = Controller(my_view, my_model)
    my_view.set_controller(my_controller)
    my_view.load_interface()

    my_controller.popola_dropdown()

ft.run(main)
