from pydantic import BaseModel, Field
from typing import TypedDict, Optional, Literal

"""
In questo file sono presenti tutte le classi che 
definiscono i formati di risposta e/o stato del grafo dell'agente
"""
class GraphState(TypedDict):
    """
    Questa classe rappresenta lo stato del grafo

    Gli attributi sono:
        - question: domanda dell'utente
    """

    question: str
    categoria_oggetto: str
    oggetto_richiesto: str
    tipologia_query: str
    risposta_query: dict[str, int]
    risposta_generata: str


class RichiestaRicerca(BaseModel):
    """
    Questa classe definisce il formato della risposta della catena
    responsabile di capire se la query dell'utente corrisponde ad una query di ricerca
    nel database, una ricerca nella documentazione relativi a vincoli contrattuali con i fornitori, una domanda
    a cui posso già rispondere perchè sono a conoscenza del risultato.

    Es. "Dimmi i prodotti da ordinare"
    """

    tipologia_domanda: Literal["ricerca", "documentazione", "altro"] = Field(
        description="Descrive cosa l'utente ha richiesto, 'ricerca' significa che per rispondere alla domanda"
        "dell'utente serve guardare nel database, 'documentazione' significa che"
        "per rispondere ho necessità di controllare la documentazione dei fornitori,"
        "'altro' significa che proverà a rispondere con quello che conosco."
    )


class EsisteParametroRicerca(BaseModel):
    """
    Questa classe definisce il formato della risposta della catena
    responsabile di capire se nella query dell'utente sono stati specificati
    parametri utili per la ricerca.

    Es. "Dimmi i prodotti della categoria X da ordinare"
    """

    categoria_oggetto: Optional[str] = Field(
        description="La categoria della merce. Da inserire solo se specificata dall'utente. La categoria deve essere inserita al singolare. "
        "Esempio: se ricevi come categoria 'elettronici', allora la categoria sarà 'elettronica'",
        default=None,
    )

    nome_oggetto: Optional[str] = Field(
        description="Il nome dell'oggetto. Da inserire solo se specificato dall'utente. Il nome dell'oggetto deve essere inserito al singolare."
        "Esempio: se ricevi come nome 'orologi', allora il nome sarà 'orologio'",
        default=None,
    )

    tipologia_query: Literal["esaurimento", "ricerca"] = Field(
        description="Il tipo di intenzione dell'utente: 'esaurimento' se vuole sapere cosa ordinare o cosa manca, 'ricerca' se vuole conoscere la giacenza o info su prodotti specifici."
    )

class ParametriQueryPuliti(BaseModel):

    categoria: Optional[str] = Field(
        description="La categoria corretta presente nel sistema (singolare, prima lettera maiuscola)",
        default=None,
    )

    nome_oggetto: Optional[str] = Field(
        description="Il nome dell'oggetto corretto (singolare, prima lettera maiuscola)",
        default=None,
    )
