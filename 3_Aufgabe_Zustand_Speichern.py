"""
1. Baue die Datenklasse Task{id: INTEGER (PRIMARY KEY) text:String, done:Boolean}.
2. Mach die DB_Service fertig mit den Methoden: insert(task), update(task), delete(task) und fetchAll() : List<Task>.
3. Endkommentiere nach und nach die unten stehenden Tests.
4. Mach das alle Tests funktionieren.
"""
import sqlite3
from dataclasses import dataclass




class DB_Service:

    def __init__(self):
        # todo baue verbindung zur Datenbank auf
        # todo stelle sicher das auch eine Tabelle vorhanden ist
        # Hinweis: CREATE TABLE IF NOT EXISTS
        pass

    def insert(self, task):
        # todo Soll einen Task in der Datenbank hinzufügen
        pass

    def update(self, task):
        # todo Soll einen Task in der Datenbank aktualisieren
        pass

    def delete(self, task):
        # todo Soll einen Task aus der Datenbank entfernen
        pass

    def fetchAll(self):
        # todo Soll eine Liste von Tasks returnieren
        pass


# Testen aller Methoden
if __name__ == "__main__":

    def zeigeDB(db_service):
        tasks = db_service.fetchAll()
        for task in tasks:
            print(task)

    db_service = DB_Service()

    # # Test: Insert
    # print("Einfügen von Aufgaben...")
    # task1 = Task(text="Einkaufen gehen", done=False)
    # task2 = Task(text="Hausaufgaben machen", done=True)
    # db_service.insert(task1)
    # db_service.insert(task2)
    #
    # # Test: FetchAll
    # print("Alle Aufgaben aus der Datenbank:")
    # zeigeDB(db_service)
    # #
    # # Test: Update
    # print("\nAufgabe aktualisieren (1. Aufgabe als erledigt markieren)...")
    # updated_task = Task(text="Einkaufen gehen", done=True)
    # db_service.update(updated_task)
    #
    # # Nach dem Update alle Tasks abrufen
    # print("Aktualisierte Aufgaben:")
    # zeigeDB(db_service)
    #
    # # Test: Delete
    # print("\nAufgabe löschen (2. Aufgabe löschen)...")
    # db_service.delete(updated_task)
    #
    # # Nach dem Löschen alle Tasks abrufen
    # print("Übrig gebliebene Aufgaben nach dem Löschen:")
    # zeigeDB(db_service)
    #
