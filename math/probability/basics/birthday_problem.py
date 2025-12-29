n_days = 365

def factorial(num):
    if (num > 0):
        return num if ((num -1) == 0) else num * factorial(num - 1)

prob_none_share_bday = lambda n : factorial(n_days) / (factorial(n_days - n) * (365 ** n))
for i in range (1, 50):
    if (round(prob_none_share_bday(i), 4) <  0.5):
        print(f"Probability of at least 2 people sharing a birthday is {1 - round(prob_none_share_bday(i), 4)} with a minimum number of {i} people required.")
        break