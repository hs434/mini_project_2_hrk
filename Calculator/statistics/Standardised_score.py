from Calculator.statistics.Mean import Mean
from Calculator.statistics.Sd import Sd

def Standardised_score(my_population):
    my_mean = Mean(my_population)
    my_sd = Sd(my_population)
    standardised_score = list()
    for x in my_population:
        my_score = (x - my_mean) / my_sd
        standardised_score.append(my_score)
    return standardised_score