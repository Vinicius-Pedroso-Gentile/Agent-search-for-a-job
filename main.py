from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_anthropic import ChatAnthropic
from schema import JustAnwserEasy
from tools import tools

load_dotenv()

model = ChatAnthropic(
    model="claude-opus-5-5",
    max_tokens=1024
).bind_tools(
    tools,
    parallel_tool_calls=False,
)

#Estrutura a resposta do LLM 
structured_model = model.with_structured_output(JustAnwserEasy)

if __name__ == "__main__":
    messages = [
        SystemMessage("Use a ferramenta caso queria buscar algo na internet"),
        HumanMessage("qual é a temperatura de Tokyo ?"),
    ]
    
    for _ in range(3):
        response = structured_model.invoke(messages)
        if not response.tool_calls:
            print(response.answer)
            break
        
        
        # Assim eu coloco todas as ferramentas para executar todas se o e llm pedir
        for call in response.tool_calls:
            
            breakpoint()
            
            
    breakpoint()