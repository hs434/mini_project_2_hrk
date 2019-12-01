from Calculator.statistics.Mean import Mean
from Calculator.statistics.Sd import Sd

def Pop_correlation_coefficient(my_population, my_population2):
    mean1, mean2 = Mean(my_population), Mean(my_population2)
    sd1, sd2 = Sd(my_population), Sd(my_population2)
    correlation = 0
    for i in range(0,len(my_population)):
        factor_a = (my_population[i] - mean1)/sd1
        factor_b = (my_population2[i] - mean2) / sd2
        correlation = correlation + (factor_a * factor_b)
    pop_correlation_coefficient = correlation / len(my_population)
    return pop_correlation_coefficient
