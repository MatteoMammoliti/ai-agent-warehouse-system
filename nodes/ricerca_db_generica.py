from schemas.schemas import GraphState
import sqlite3


def ricerca_generica(state: GraphState):

    print("-- NODO DI RICERCA GENERICA NEL DB --")

    tipologia_query = state["tipologia_query"]

    print(f"-- EFFETTUO LA SEGUENTE TIPOLOGIA DI RICERCA: {tipologia_query} ")

    conn = sqlite3.connect(
        r"C:\Users\matti\Desktop\Intelligent-Warehouse---Multi-Agent-Web-App\magazzino.db"
    )
    cur = conn.cursor()

    if tipologia_query == "ricerca":
        query = "select * from Inventario"
        cur.execute(query)

    elif tipologia_query == "esaurimento":
        query = "select * from Inventario where quantita_oggetto < quota_esaurimento"
        cur.execute(query)

    rows = cur.fetchall()
    conn.close()

    d = {}

    for row in rows:
        d.update({row[1]: row[2]})

    return {"risposta_query": d}
