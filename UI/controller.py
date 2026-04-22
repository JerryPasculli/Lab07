import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e, mese):
        self._view.lst_result.controls.clear()
        if mese == None:
            stringa = ft.Text(f"Non hai scelto un mese", color = "red")
            self._view.lst_result.controls.append(stringa)
            self._view.update_page()
            return
        lista = self._model.medie(mese)
        for element in lista:
            print(element)
            stringa = ft.Text(f"{element[0]} : {element[2]}")
            self._view.lst_result.controls.append(stringa)
        self._view.update_page()



    def handle_sequenza(self, e, mese):
        self._view.lst_result.controls.clear()
        if mese == None:
            stringa = ft.Text(f"Non hai scelto un mese", color="red")
            self._view.lst_result.controls.append(stringa)
            self._view.update_page()
            return
        sequenza = self._model.esegui(mese)
        for element in sequenza:
            print(element)
            stringa = ft.Text(f"{element}")
            self._view.lst_result.controls.append(stringa)
        self._view.update_page()

    def read_mese(self, e):
        self._mese = int(e.control.value)

