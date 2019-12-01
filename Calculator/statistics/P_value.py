from scipy.stats import t


def P_value(my_population,confidence_level):
    df = len(my_population) - 1  # degrees of freedom
    a = (1 - confidence_level) / 2
    my_t = t.ppf(confidence_level, df)
    my_p = 1 - t.cdf(my_t,df)
    return my_p
