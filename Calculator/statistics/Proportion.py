from Calculator.statistics.Mean import Mean


def Proportion(my_population):
    # Any number 20% above or 20% below the mean is being considered as outlier.
    # This function returns the proportion of the population which is outlier.
    my_mean = Mean(my_population)
    lower_limit = 0.8 * my_mean
    higher_limit = 1.2 * my_mean
    count = 0
    proportion_success = list()
    for i in my_population:
        if (i>higher_limit) or (i< lower_limit):
            count = count + 1
            proportion_success.append(i)
    p = (count/float(len(my_population)))
    return p,proportion_success