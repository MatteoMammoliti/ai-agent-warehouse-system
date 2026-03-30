from schemas.schemas import GraphState, ParametriQueryPuliti
from chains.input_validator import validation_chain

def valida_input(state: GraphState) -> dict:

    question = state['question']

    response: ParametriQueryPuliti = validation_chain.invoke(
        {
            'question': question,
        }
    )

    return {
        'oggetto_richiesto': response.nome_oggetto,
        'categoria_oggetto': response.categoria
    }