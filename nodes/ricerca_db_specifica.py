from schemas.schemas import GraphState
import sqlite3


def ricerca_specifica(state: GraphState):

    print('-- NODO RICERCA SPECIFICA --')

    categoria = state.get('categoria_oggetto')
    oggetto = state.get('oggetto_richiesto')
    tipologia_query = state['tipologia_query']

    conn = sqlite3.connect(
        r"C:\Users\matti\Desktop\Intelligent-Warehouse---Multi-Agent-Web-App\magazzino.db"
    )

    cursor = conn.cursor()
    query = "select nome_oggetto, quantita_oggetto from Inventario"
    params = []
    condizioni = []

    if categoria:
        condizioni.append('categoria = ?')
        params.append(categoria)

    if oggetto:
        condizioni.append('nome_oggetto LIKE ?')
        params.append(f"%{oggetto}%")

    if tipologia_query == 'esaurimento':
        condizioni.append('quantita_oggetto < quota_esaurimento')

    if condizioni:
        final_query = f"{query} WHERE {' AND '.join(condizioni)}"
    else:
        final_query = query

    cursor.execute(final_query, params)
    rows = cursor.fetchall()
    conn.close()

    return { 'risposta_query': {row[0]: row[1] for row in rows} }