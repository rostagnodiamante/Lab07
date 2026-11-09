import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        print("SONO DENTRO LA POPOLA DROPDOWN")
        # aggiunge le biblioteche
        biblioteche=self._model.get_biblioteche()
        print("DEBUG BIBLIOTECHE:", biblioteche)
        self._view.dd_biblioteca.options.append(
            ft.dropdown.Option("Nessun filtro"))
        for biblio in biblioteche:
            print("Singola biblioteca:", biblio)
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(str(biblio.nome)))

        #aggiunge i generi
        generi=self._model.get_generi()
        print("DEBUG GENERI:", generi)
        self._view.dd_genere.options.append(ft.dropdown.Option("Nessun filtro"))
        for genere in generi:
            if genere:
                self._view.dd_genere.options.append(ft.dropdown.Option(str(genere)))

        self._view.update()


    # CALLBACKS DROPDOWN
    def seleziona_biblioteca(self,e):
        if e.control.value=="Nessun filtro":
            self.biblioteca_selezionata=None
        else:
            self.biblioteca_selezionata= e.control.value

    def seleziona_genere(self,e):
        if e.control.value =="Nessun filtro":
            self.genere_selezionato=None
        else:
            self.genere_selezionato= e.control.value

    # AZIONE: MOSTRA LIBRI
    def handle_mostra_libri(self, e):
    #azione del bottone
        #pulisco la lista di prima
        self._view.list_view.controls.clear()
        #prendo i libri filtrati dal model
        libri= self._model.get_libri_filtrati(
            self.biblioteca_selezionata, self.genere_selezionato
        )

        # se nessun libro soddisfa i criteri mando un allert
        if not libri:
            self._view.alert.show_alert(
                "Nessun libro trovato con i criteri selezionati")
            self._view.update()
            return
        #altrimenti, popola la listview con i libri che ho trovato
        for libro in libri:
            self._view.list_view.controls.append(
                ft.Text(f"{libro.titolo} - {libro.autore} ({libro.anno_pubblicazione}) | Genere: {libro.genere}")
            )
        self._view.update()

