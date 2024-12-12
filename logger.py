from datetime import date
from virus import Virus

class Logger(object):
    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

    # The methods below are just suggestions. You can rearrange these or 
    # rewrite them to better suit your code style. 

    # Meta data: This shows the starting situtation including:
    #   population, initial infected, the virus, and the initial vaccinated.
    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num, initial_infected):
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        
        data = [
            "****** SIMULATION START ******\n",
            f"Initial size of the population\t{pop_size}\n",
            f"Initial number of infected people\t{initial_infected}\n",
            f"Name of the virus\t{virus_name}\n",
            f"Mortality Rate\t{mortality_rate * 100}%\n",
            f"Repro rate\t{basic_repro_num * 100}%\n",
            f"Vaccination percentage\t{vacc_percentage* 100}%\n",
            f"Date the simulation was run\t{date.today()}\n"
        ]
        
        outfile = open(self.file_name, "w")
        
        for data_point in data:
            outfile.write(data_point)
            print(data_point.replace("\n", ""))

        outfile.close()

    def log_simulation_end(self, population, total_interactions, total_vacc_interactions):
        # When the simulation concludes you should log the results of the simulation. 
        # This should include: 
        #   The population size, the number of living, the number of dead, the number 
        #   of vaccinated, and the number of steps to reach the end of the simulation. 

        total_living = 0
        total_dead = 0
        total_vaccinated = 0
        
        for person in population:
            if person.is_alive == False:
                total_dead += 1
                continue
            
            if person.is_alive == True:
                total_living += 1
            
            if person.is_vaccinated == True:
                total_vaccinated += 1
                
        if total_vaccinated == total_living:
            reason_sim_end = "Every living person was vaccinated"
        elif total_dead == len(population):
            reason_sim_end = "Everyone died"
        else: reason_sim_end = "Virus burned out"
                
        data = [
            "\n****** SIMULATION END ******\n",
            f"Total living\t{total_living}\n",
            f"Total dead\t{total_dead}\n",
            f"Total vaccinations\t{total_vaccinated}\n",
            f"Why the simulation ended\t{reason_sim_end}\n",
            f"Total interactions\t{total_interactions}\n",
            f"Infections prevented because of vaccination\t{total_vacc_interactions}\n",
        ]
        
        outfile = open(self.file_name, "a")
        
        outfile.write("")
        for data_point in data:
            outfile.write(data_point)
            print(data_point.replace("\n", ""))

        outfile.close()

    def log_iteration(self, time_step_number, number_of_new_infections, number_of_new_fatalities,
                      number_of_interactions, population):
        # What is important is that you log the following information from the simulation:
        # Log interactions. At each step there will be a number of interaction
        # You should log:
        #   The number of interactions, the number of new infections that occured
        # You should log the results of each step. This should inlcude: 
        #   The population size, the number of living, the number of dead, and the number 
        #   of vaccinated people at that step. 
        total_living = 0
        total_dead = 0
        total_vaccinated = 0
        total_infected = 0
        
        for person in population:
            if person.is_alive == False:
                total_dead += 1
                continue
            
            if isinstance(person.infection, Virus) or person.infection == True:
                total_infected += 1
            
            if person.is_alive == True:
                total_living += 1
            
            if person.is_vaccinated == True:
                total_vaccinated += 1
            
        data = [
            f"\n****** Step {time_step_number} ******\n",
            f"New infections\t{number_of_new_infections}\n",
            f"New deaths\t{number_of_new_fatalities}\n",
            f"Interactions\t{number_of_interactions}\n",
            f"Total Living\t{total_living}\n",
            f"Total Dead\t{total_dead}\n",
            f"Total Vaccinated\t{total_vaccinated}\n",
            f"Total Infected\t{total_infected}\n"
        ]
        
        outfile = open(self.file_name, "a")
        
        print("")
        for data_point in data:
            outfile.write(data_point)
            print(data_point.replace("\n", ""))
        print("")

        outfile.close()
        