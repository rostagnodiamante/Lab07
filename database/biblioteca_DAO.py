from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_all_biblioteche(self):
        cnx= DBConnect.get_connection()
        result=[]
        if cnx is None:
            print("Connessione al database fallita")
            return result

        cursor=cnx.cursor(dictionary=True)
        query="""SELECT *
               FROM biblioteca"""

        try:
            cursor.execute(query)
            for row in cursor:
                biblioteca=Biblioteca(
                    id=row["id"], nome=row["nome"], indirizzo=row["indirizzo"]
                )
                result.append(biblioteca)
        except Exception as e:
            print(f"Errore durante l'esecuzione della query: {e}")
        finally:
            cursor.close()
            cnx.close()
        return result