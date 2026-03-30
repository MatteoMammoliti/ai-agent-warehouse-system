from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from schemas.schemas import EsisteParametroRicerca

llm = ChatGroq(model="llama-3.3-70b-versatile").with_structured_output(
    EsisteParametroRicerca
)

system_prompt = """
                Sei un assistente virtuale utile il cui compito è quello di decidere se nella domanda dell'utente
                è presente un riferimento ad un oggetto o una categoria, utile per indirizzare la ricerca
                """

prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt), ("human", "Domanda in input dell'utente: {question}")]
)

chain_router_ricerca_db = prompt | llm
