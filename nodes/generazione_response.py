from schemas.schemas import GraphState
from chains.generate_response import generation_chain


def generate_response(state: GraphState) -> dict:
    """
    Questa funzione genera la risposta invocando l'opportuna chain

    Args:
        state (dict): stato corrente del grafo

    Returns:
        state (dict): stato del grafo aggiornato con la risposta generata dal modello LLM
    """

    print("-- GENERAZIONE DELLA RISPOSTA --")

    question = state["question"]
    oggetti = state["risposta_query"]

    response = generation_chain.invoke(
        {"question": question, "oggetti_recuperati": oggetti}
    )

    return {"risposta_generata": response}
