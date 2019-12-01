from scipy.stats import t
from Calculator.statistics.Sd import Sd

def Confidence_interval(my_population,confidence_level):
    df = len(my_population) - 1 #degrees of freedom
    a = (1 - confidence_level) / 2
    my_t = t.ppf(confidence_level, df)
    my_sd = Sd(my_population)
    confidence_interval = my_t * ((my_sd / (len(my_population) ** 0.5)))
    return confidence_interval # gives more accurate confidence interval as it gets the t-critical value; normally people take 1.960 as t-critical for 95%

# Reference: https://www.mathsisfun.com/data/confidence-interval.html,
# Reference: https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/confidence-interval/