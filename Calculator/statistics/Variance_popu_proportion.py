from Calculator.statistics.Proportion import Proportion
from Calculator.statistics.Variance import Variance

def Variance_popu_proportion(my_population):
    my_proportion,population_success= Proportion(my_population)
    return Variance(population_success)
