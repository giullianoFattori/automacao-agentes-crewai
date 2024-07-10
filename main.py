import os
from crewai import Crew
from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks

# os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        expert_agent = agents.expert_travel_agent()
        city_agent = agents.city_selection_expert()
        local_agent = agents.local_tour_guide()

        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_agent,
            self.cities,
            self.date_range,
            self.interests,
        )

        identify_city = tasks.identify_city(
            city_agent,
            self.origin,
            self.cities,
            self.interests,
            self.date_range,
        )
        
        gather_city_info = tasks.gather_city_info(
            local_agent,
            self.cities,
            self.date_range,
            self.interests,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_agent, city_agent, local_agent],
            tasks=[plan_itinerary, identify_city, gather_city_info],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Bem-vindo ao Trip Planner Crew")
    print("-------------------------------")
    location = input( dedent("""De qual cidade você esta saindo ou pretende sair?"""))
    cities = input(dedent("""Quais são as opções de cidades que você tem interesse em visitar?"""))
    date_range = input(dedent("""Qual é o intervalo de datas em que você está interessado em viajar?"""))
    interests = input(dedent("""Quais são alguns de seus interesses e hobbies de alto nível?"""))

    trip_crew = TripCrew(location, cities, date_range, interests)
    result = trip_crew.run()
    print("\n\n########################")
    print("## Aqui está o resultado da execução da equipe personalizada:")
    print("########################\n")
    print(result)
