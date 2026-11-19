from pydantic import BaseModel, Field


# É super importante colocar o tipo do campo
class JustAnwserEasy(BaseModel):
    answer:str = Field(description="Toda a resposta do LLM deve vim aqui nesse campo answer")
