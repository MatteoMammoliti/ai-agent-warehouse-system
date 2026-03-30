from langgraph.graph import END, StateGraph
from chains.router_iniziale import chain_router_iniziale
from schemas.schemas import GraphState
from nodes.inizio_ricerca_db import ricerca_nel_db
from nodes.ricerca_db_generica import ricerca_generica
from nodes.generazione_response import generate_response
from nodes.aiuto_documentazione import aiuto_documentazione
from nodes.ricerca_db_specifica import ricerca_specifica
from nodes.input_validator import valida_input

# Costanti rappresentanti i nodi del grafo
RICERCA_NEL_DB = "ricerca_nel_db"
AIUTO_DOCUMENTAZIONE = "aiuto_documentazione"
RICERCA_GENERICA = "ricerca_generica"
RICERCA_SPECIFICA = "ricerca_specifica"
GENERA_RISPOSTA = "genera_risposta"
INPUT_VALIDATOR = "input_validator"


# Funzioni di utilità per gli archi condizionali
def router_iniziale(state: GraphState):
    """
    Questa funzione decreta il primo salto del grafo.
    Se la domanda posta all'agente sarà di ricerca nel db,
    allora faremo:
        START -> RICERCA_NEL_DB

    Altrimenti, se la domanda riguarda una qualsiasi informazione riguardante una documentazione,
    faremo:
        START -> AIUTO_DOCUMENTAZIONE
    """

    question: str = state["question"]

    response = chain_router_iniziale.invoke({"question": question})

    if response.tipologia_domanda == "ricerca":
        return RICERCA_NEL_DB

    elif response.tipologia_domanda == "documentazione":
        return AIUTO_DOCUMENTAZIONE

    return GENERA_RISPOSTA


def router_ricerca(state: GraphState):
    """
    Questa funzione decreta il secondo salto del grafo.
    Se la domanda posta all'agente conterrà una tipologia o un oggetto specifico
    allora faremo:
        START -> RICERCA_SPECIFICA

    Altrimenti, se la query di ricerca sarà generica
    faremo:
        START -> RICERCA_GENERICA
    """

    oggetto = state.get("oggetto_richiesto")
    categoria = state.get("categoria_oggetto")

    if oggetto or categoria:
        return RICERCA_SPECIFICA

    return RICERCA_GENERICA


graph = StateGraph(GraphState)

graph.add_node(RICERCA_NEL_DB, ricerca_nel_db)
graph.add_node(AIUTO_DOCUMENTAZIONE, aiuto_documentazione)

graph.set_conditional_entry_point(
    router_iniziale,
    {
        RICERCA_NEL_DB: RICERCA_NEL_DB,
        AIUTO_DOCUMENTAZIONE: AIUTO_DOCUMENTAZIONE,
        GENERA_RISPOSTA: GENERA_RISPOSTA,
    },
)

graph.add_node(RICERCA_GENERICA, ricerca_generica)
graph.add_node(RICERCA_SPECIFICA, ricerca_specifica)
graph.add_node(INPUT_VALIDATOR, valida_input)

graph.add_conditional_edges(
    RICERCA_NEL_DB,
    router_ricerca,
    {
        RICERCA_GENERICA: RICERCA_GENERICA,
        RICERCA_SPECIFICA: INPUT_VALIDATOR,
    },
)

graph.add_edge(INPUT_VALIDATOR, RICERCA_SPECIFICA)
graph.add_node(GENERA_RISPOSTA, generate_response)
graph.add_edge(RICERCA_GENERICA, GENERA_RISPOSTA)
graph.add_edge(RICERCA_SPECIFICA, GENERA_RISPOSTA)

graph.add_edge(GENERA_RISPOSTA, END)

app = graph.compile()
app.get_graph().draw_mermaid_png(output_file_path="output.png")

if __name__ == "__main__":

    stato = GraphState(
        question="Dammi i 10 oggetti della categoria network in esaurimento",
        categoria_oggetto="",
        oggetto_richiesto="",
        risposta_generata="",
        tipologia_query="",
        risposta_query=None,
    )

    res: GraphState = app.invoke(stato)

    print(res["risposta_generata"])