from crewai import Task
from textwrap import dedent


class TravelTasks:
    def __tip_section(self):
        return "Se você fizer seu MELHOR TRABALHO, eu lhe darei uma comissão de US$ 10.000!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                    **Atividade**: Desenvolver 7 dias de um roteiro de viagem
                    
                    **Descrição**: Expanda o guia da cidade em um itinerário de viagem completo de 7 dias com planos detalhados por dia,
                    incluindo previsões do tempo, lugares para comer, sugestões de como fazer as malas e um orçamento limitado. Você deve sugerir
                    lugares reais para visitar, hotéis reais para se hospedar e restaurantes reais para ir. Esse itinerário deve abranger todos os aspectos 
                    da viagem, desde a chegada até a partida, integrando as informações do guia da cidade com a logística prática da viagem.
                                        
                    **Informações**
                    - Cidade: {city}
                    - Data da Viagem: {travel_dates}
                    - Interesses na viagem: {interests}
                    
                    **Notas**: {self.__tip_section()}
                    """
            ),
            agent=agent,
            expected_output='Os melhores e mais claros e detalhados itinerarios para a viagem'
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
                    **Tarefa**: Identificar a melhor cidade para a viagem
                    
                    **Descrição**: Analisar e selecionar a melhor cidade para a viagem com base em critérios específicos, como padrões climáticos, eventos sazonais
                    e custos de viagem. Essa tarefa envolve a comparação de várias cidades, considerando fatores como condições climáticas atuais, eventos culturais ou sazonais futuros e custos gerais de viagem.
                    eventos culturais ou sazonais e despesas gerais de viagem.
                    Sua resposta final deve ser um relatório detalhado sobre a cidade escolhida, incluindo custos reais de voos, previsão do tempo e atrações.
                    
                    **Informações**
                    - Origem: {origin}
                    - Cidade: {cities}
                    - Data da viagem: {travel_dates}
                    - Interesses na viagem: {interests}
                    
                    **Notas**: {self.__tip_section()}
                    """
            ),
            agent=agent,
            expected_output='As melhores informações das cidades com detalhes e curiosidades'

        )

    def gather_city_info(self, agent, city, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
                    **Tarefa**: Reunir informações detalhadas sobre o guia da cidade
                    
                    **Descrição**: Compilar um guia detalhado da cidade selecionada, reunindo informações sobre as principais atrações, costumes locais,
                        eventos especiais e recomendações de atividades diárias.
                        Esse guia deve fornecer uma visão geral completa do que a cidade tem a oferecer, incluindo joias escondidas,
                        pontos de interesse cultural, pontos de referência obrigatórios, previsões do tempo e custos de alto nível
                    
                    **Informações**
                    - Cidade: {city}
                    - Data da viagem: {travel_dates}
                    - Interesses do viajante: {interests}
                    
                    **Notas**: {self.__tip_section()}
                """
            ),
            agent=agent,
            expected_output='A maior quantidade de informações reunidas e com detalhes.'

        )