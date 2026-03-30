from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGroq(model="llama-3.3-70b-versatile")

system_prompt = """
    Sei un assistente utile. Il tuo compito è fornire assistenza ai dipendenti del magazzino.
    Se hai ricevuto dei dati riguardante degli oggetti in un magazzino, 
    li dovrai formattare in una lista leggibile seguendo il seguente modo:
    
    1. Usa SEMPRE questo formato: 📦 [Nome] - Qty: [Quantità]
        2. Se un oggetto ha quantità 0, scrivi (TERMINATO) alla fine.
    
    Se invece, la lista è vuota o non sai la risposta alla domanda, rispondi in modo cordiale che non è possibile fornire,
    aiuto senza dare alcuna spiegazione del perchè. 
    
    Dati dal DB: {oggetti_recuperati}
    Domanda: {question}
"""

prompt = ChatPromptTemplate.from_template(system_prompt)

generation_chain = prompt | llm | StrOutputParser()
