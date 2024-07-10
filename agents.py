from crewai import Agent
from textwrap import dedent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools
load_dotenv()
class TravelAgents:
    
    def __init__(self):
        # self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        # self.Ollama = Ollama(model="openhermes")
        self.gemini15 = ChatGoogleGenerativeAI(model='gemini-pro', verbose= True, temperature= 0.5)

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Especialista em planejamento e logística de viagens. 
                            Tenho décadas de experiência na elaboração de roteiros de viagem"""),
            goal=dedent(f"""Crie um itinerário de viagem de 7 dias com planos detalhados por dia, incluindo orçamento,
                            sugestões de embalagem e dicas de segurança"""),
            tools=[SearchTools.search_internet, CalculatorTools.calculate],
            verbose=True,
            llm=self.gemini15,
            callback=[],
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Especialista em analisar dados de viagens para escolher os destinos ideais"""),
            goal=dedent(f"""Selecione as melhores cidades com base no clima, na estação, nos preços e nos interesses do viajante"""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.gemini15,
        )
        
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Expert",
            backstory=dedent(f"""Guia local experiente com muitas informações sobre a cidade, suas atrações e costumes"""),
            goal=dedent(f"""Fornecer as MELHORES percepções sobre a cidade selecionada"""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.gemini15,
        )
