class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        # Define the attributes of your your virus
        self.name = name
        # TODO Define the other attributes of Virus
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    
    # test 1
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    # test 2
    virus = Virus("Bubonic Plague", 0.3, 0.6)
    assert virus.name == "Bubonic Plague"
    assert virus.repro_rate == 0.3
    assert virus.mortality_rate == 0.6
    
    # test 3
    virus = Virus("Mumps", 0.7, 0.1)
    assert virus.name == "Mumps"
    assert virus.repro_rate == 0.7
    assert virus.mortality_rate == 0.1