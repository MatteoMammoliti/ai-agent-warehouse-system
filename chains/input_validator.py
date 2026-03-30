from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from schemas.schemas import ParametriQueryPuliti
load_dotenv()
import sqlite3

def get_categorie() -> list[str]:
    """
    Questa funzione effettua una query nel database
    e restituisce tutte le categorie di oggetti presenti nel magazzino.
    """

    conn = sqlite3.connect(
        r"C:\Users\matti\Desktop\Intelligent-Warehouse---Multi-Agent-Web-App\magazzino.db"
    )

    cur = conn.cursor()

    query = "select categoria from Inventario"
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()

    categorie = []

    for row in rows:
        categorie.append(row[0])

    return categorie


categorie = get_categorie()

llm = ChatGroq(model="llama-3.3-70b-versatile").with_structured_output(ParametriQueryPuliti)

system_prompt = f"""
        Sei un esperto di data entry. Il tuo compito è pulire l'input dell'utente.

        CATEGORIE ESISTENTI NEL DATABASE:
        {", ".join(set(categorie))}

        REGOLE:
        1. Trasforma tutto al singolare.
        2. Se l'utente scrive una categoria simile a una valida, usa quella della lista sopra.
        3. Restituisci None se non trovi riferimenti.
    """

prompt = ChatPromptTemplate.from_messages(
    [
        ('system', system_prompt),
        ('human', 'Domanda dell\'utente: {question}')
    ]
)

validation_chain = prompt | llm