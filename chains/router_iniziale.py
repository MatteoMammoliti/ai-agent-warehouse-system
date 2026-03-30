from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from schemas.schemas import RichiestaRicerca

llm = ChatGroq(model="llama-3.3-70b-versatile").with_structured_output(RichiestaRicerca)

system_prompt = """
                Sei un assistente virtuale utile il cui compito è quello di decidere se per rispondere alla 
                domanda arrivata in input dall'utente, è necessario consultare il database. All'interno del database 
                sono presenti esclusivamente queste informazioni:
                - nome_oggetto: il nome dell'oggetto
                - quantita: la quantita attuale dell'oggetto
                - quota_esaurimento: la quota minima oltre la quale è necessario riordinare l'oggetto dal fornitore
                - categoria: la categoria a cui fa riferimento l'oggetto
                """

prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt), ("human", "Domanda in input dell'utente: {question}")]
)

chain_router_iniziale = prompt | llm
