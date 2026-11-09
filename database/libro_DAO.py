from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_libri_filtrati(self,biblioteca_nome, genere):
        cnx=DBConnect.get_connection()
        result=[]
        if cnx is None:
            print("connessione al database fallita")
            return result

        cursor=cnx.cursor(dictionary=True)
        query="""
        SELECT l.id, l.titolo, l.autore, l.genere, l.id_biblioteca
        FROM libro l
        WHERE 1=1
        """
        parametri=[]

        # se l'utente ha scelto una biblioteca specifica
        if biblioteca_nome and biblioteca_nome != "Nessun filtro":
            query += "AND b.nome = %s"
            parametri.append(biblioteca_nome)

        # se l'utente ha scelto un genere specifico
        if genere and genere != ("Nessun filtro"):
            query += "AND b.genere=%s"
            parametri.append(genere)

        try:
            cursor.execute(query, tuple(parametri))
            for row in cursor:
                libro=Libro(
                    id=row["id"],
                    titolo=row["titolo"],
                    autore=row["autore"],
                    genere=row["genere"],
                    id_biblioteca=row["id_biblioteca"]
                )
                result.append(libro)
            cursor.close()
            cnx.close()
            return result
        except Exception as e:
            print(f"Errore durante l'esecuzione della query dei libri: {e}")
            if cnx:
                cursor.close()
                cnx.close()
            return result

    def get_all_generi(self):
        cnx=DBConnect.get_connection()
        result=[]
        if cnx is None:
            print("connessione al database fallita")
            return result

        cursor=cnx.cursor(dictionary=True)
        query="""
        SELECT DISTINCT genere
        FROM libro
        WHERE genere IS NOT NULL
        ORDER BY genere"""

        try:
            cursor.execute(query)
            for row in cursor:
                result.append(row["genere"])
            cursor.close()
            cnx.close()
            return result
        except Exception as e:
            print(f"Errore durante il recupero del genere: {e}")
            if cnx:
                cursor.close()
                cnx.close()
            return result