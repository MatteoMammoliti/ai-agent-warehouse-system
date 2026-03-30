from schemas.schemas import GraphState, EsisteParametroRicerca
from chains.router_ricerca_db import chain_router_ricerca_db


def ricerca_nel_db(state: GraphState) -> dict:

    print("-- NODO DI RICERCA NEL DB --")
    print("-- VALUTO SE LA RICERCA E' GENERICA O RELATIVA AD UNA TIPOLOGIA --")

    question = state["question"]

    response: EsisteParametroRicerca = chain_router_ricerca_db.invoke(
        {
            "question": question,
        }
    )

    return {
        "tipologia_query": response.tipologia_query,
        "oggetto_richiesto": response.nome_oggetto,
        "categoria_oggetto": response.categoria_oggetto,
    }
