from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Anser the questions below
here is the conversation history: {context}

Question: {question}

Answer: 
"""

model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    while True:
        question = input("Question: ")
        if question == "exit":
            break
        
        result = chain.invoke({"context": context, "question": question})
        print(result)
        context += f"\n{question}\n{result}"
        #

if __name__ == '__main__':
    handle_conversation()