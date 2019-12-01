
def Median(my_population):
    my_population.sort()
    length = len(my_population)
    my_median = 0
    if length%2 == 1:
        my_median = my_population[(length+1)/2]
    else:
        middle_position = int((length)/2)
        my_median1 = my_population[middle_position-1]
        my_median2 = my_population[middle_position]
        my_median = (my_median1+my_median2)/2
    return (my_median)
