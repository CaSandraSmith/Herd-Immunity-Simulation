import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        self.logger = Logger("logger.py")
        
        # TODO: Store the virus in an attribute
        self.virus = virus
        
        # TODO: Store pop_size in an attribute
        self.pop_size = pop_size
        
        # TODO: Store the vacc_percentage in a variable
        self.vacc_percentage = vacc_percentage
        
        # TODO: Store initial_infected in a variable
        self.initial_infected = initial_infected
        
        # You need to store a list of people (Person instances)
        # Some of these people will be infected some will not. 
        # Use the _create_population() method to create the list and 
        # return it storing it in an attribute here. 
        # TODO: Call self._create_population() and pass in the correct parameters.
        population = self._create_population(pop_size, initial_infected, virus)
        self.population = population
        
        self.newly_infected = []

    def _create_population(self, pop_size, initial_infected, virus):
        # TODO: Create a list of people (Person instances). This list 
        # should have a total number of people equal to the pop_size. 
        # Some of these people will be uninfected and some will be infected.
        # The number of infected people should be equal to the the initial_infected
        # TODO: Return the list of people
        people = []
        
        # range stops at number before stop so adding 1 to get same number of people as pop size 
        for i in range(1, pop_size + 1):
            # check if there are more people who need to be infected
            is_infected = initial_infected > 0
            
            # if yes, five them the virus
            if is_infected:
                new_person = Person(i, False, virus)
            else: new_person = Person(i, False)
            
            people.append(new_person)

            # subtract from number of peopl who need to be infected
            initial_infected -= 1
            
        return people

    def _simulation_should_continue(self):
        # This method will return a booleanb indicating if the simulation 
        # should continue. 
        # The simulation should not continue if all of the people are dead, 
        # or if all of the living people have been vaccinated. 
        # NOTE: Added simulation end if the virus has been eradicated
        # TODO: Loop over the list of people in the population. Return True
        # if the simulation should continue or False if not.
        looking_for_vaccination = None
        is_virus_dead = True
        end_sim = True
        
        # loop through all people
        for person in self.population:
            vaccinated = person.is_vaccinated
            
            # check if we still haven't found someone with the virus
            if is_virus_dead:
                # if we waven't check if the current person has the virus
                if isinstance(person.infection, Virus) or person.infection is True:
                    # if they have the virus, it isn't dead on this round
                    is_virus_dead = False

            # the first person we encounter will tell us if we're looking
            # to see if everyone has died or if everyone is vaccinated
            if looking_for_vaccination == None:
                looking_for_vaccination = vaccinated
                continue
            
            # check if the person has the same status as the looking_for_vaccination variable
            if not (vaccinated == looking_for_vaccination):
                # if yes, we can't end sim early
                end_sim = False
        
        # print("dead virus", is_virus_dead)
        # print("end sim?", end_sim)
        
        if is_virus_dead or end_sim: return False
        else: return True
        

    def run(self):
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 

        time_step_counter = 0
        should_continue = True

        while should_continue:
            # TODO: Increment the time_step_counter
            time_step_counter += 1
            
            # TODO: for every iteration of this loop, call self.time_step() 
            self.time_step()
            
            # Call the _simulation_should_continue method to determine if 
            # the simulation should continue
            print(time_step_counter)
            # self.print_infected()
            should_continue = self._simulation_should_continue()
            
            if time_step_counter == 20: break
            

        # TODO: Write meta data to the logger. This should be starting 
        # statistics for the simulation. It should include the initial
        # population size and the virus. 
        
        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 

    def time_step(self):
        # This method will simulate interactions between people, calulate 
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # TODO: Loop over your population
        for person in self.population:
            # For each person if that person is infected
            if isinstance(person.infection, Virus) or person.infection == True:
                # have that person interact with 100 other living people 
                for index in range(100):
                    # keep looping until we find someone who is not the current person or dead
                    random_person = self.pick_random_person(person)
                    
                    # Run interactions by calling the interaction method below. That method
                    # takes the infected person and a random person
                    self.interaction(person, random_person)
                    
                person.did_survive_infection(self.virus)
                
        self._infect_newly_infected()    
        
    
    def pick_random_person(self, current_person):
        current_random_person = random.choice(self.population)
        
        while current_random_person == current_person or not current_random_person.is_alive:
            current_random_person = random.choice(self.population)

        return current_random_person
        

    def interaction(self, infected_person, random_person):
        # TODO: Finish this method.
        
        if (infected_person.is_vaccinated == True):
            return
        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
        if random_person.is_vaccinated == True:
            return
        
            # random_person is already infected:
            #     nothing happens to random person.
        elif isinstance(random_person.infection, Virus):
            return
        
            # random_person is healthy, but unvaccinated:
        else:
            # generate a random number between 0.0 and 1.0.
            random_number = random.random()
            
            # If that number is smaller
            # than repro_rate, add that person to the newly infected array
            if random_number < self.virus.repro_rate:
            #     Simulation object's newly_infected array, so that their infected
            #     attribute can be changed to True at the end of the time step.
                self.newly_infected.append(random_person)
        # TODO: Call logger method during this method.




    def _infect_newly_infected(self):
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for person in self.newly_infected:
            person.infection = True
        
        self.newly_infected = []
        
        
    # def print_infected(self):
    #     infected = 0
    #     noninfected = 0
    #     vaccinate = 0
    #     nonVacinated = 0
    #     for person in self.population:
    #         if isinstance(person.infection, Virus) or person.infection == True:
    #             infected += 1
    #         else: noninfected += 1
            
    #         if person.is_vaccinated:
    #             vaccinate += 1
    #         else: nonVacinated += 1
        
    #     print(f"infected: {infected}")
    #     print(f"noninfected: {noninfected}")
    #     print(f"vaccinated: {vaccinate}")
    #     print(f"nonvax: {nonVacinated}")
            
            


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 100

    # Make a new instance of the imulation
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    sim.run()
