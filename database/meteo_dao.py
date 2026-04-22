from database.DB_connect import DBConnect
from model.situazione import Situazione


class MeteoDao():

    @staticmethod
    def get_all_situazioni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.Localita, s.Data, s.Umidita
                        FROM situazione s 
                        ORDER BY s.Data ASC"""
            cursor.execute(query)
            for row in cursor:
                result.append(Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"]))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def tornaUmidita(mese, giorno, localita):
        cnx = DBConnect.get_connection()
        result = []
        cursor = cnx.cursor()
        query = """SELECT Umidita, Data
                FROM situazione
                WHERE MONTH(Data)=%s AND Day(Data)=%s AND Localita=%s"""
        cursor.execute(query, [mese, giorno, localita])
        element = cursor.fetchone()
        cursor.close()
        cnx.close()
        print(element)
        return element
    @staticmethod
    def valoriMedi(mese):
        cnx = DBConnect.get_connection()
        result = []
        cursor = cnx.cursor()
        query = """SELECT Localita, MONTH(Data) as mese, AVG(Umidita)
        FROM situazione
        WHERE MONTH(Data)=%s
        GROUP BY Localita, MONTH(Data)"""
        cursor.execute(query, [mese])
        for element in cursor:
            result.append(element)
        cursor.close()
        cnx.close()
        return result


