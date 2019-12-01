from pprint import pprint
from Calculator.statistics.Proportion import Proportion
from Calculator.statistics.Variance import Variance

def Variance_sample_proportion(my_population):
    p,proportion_success= Proportion(my_population)
    return Variance(proportion_success)



