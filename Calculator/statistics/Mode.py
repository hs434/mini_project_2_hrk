def Mode(my_population):
    my_mode = 0
    num_freq = {}
    for item in my_population:
        if item not in num_freq:
         num_freq[item] = 0
        num_freq[item] += 1
    for key, value in num_freq.items():
        if value == max(num_freq.values()):
           my_mode = key
    return (my_mode)



