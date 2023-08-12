# Used list as main data structure and created n*n population
# Used dictoray to find {population : fitness}
# Sorted the dictonary by its fitness

import random

f = open("genetic_input.txt", "r")
case = int(f.readline())
data = f.readlines()

temp = []
for i in data:
    a = int(i[1:])
    if i[0] == "l":
        temp.append(-a)  # lend as -Ve
    else:
        temp.append(a)  # Diposite as +Ve

initial = {}  # Main data of the problem
for i in range(case):
    initial[i] = temp[i]


def create_cromosome(data):  # Creating cromosome
    temp = []
    for i in range(case):
        x = random.randint(
            0, case - 1
        )  # taking key numbrs of the initial dictionaty as cromosome so that we can track our value
        temp.append(str(x))
    a = "".join(temp)

    exp = []  # removing the probabilty of finding all 0's
    for i in range(case):
        exp.append(str(0))
    exp = "".join(exp)
    if a != exp:
        return a
    else:
        create_cromosome()


def index_value(string):
    temp = []
    for i in string:
        temp.append(initial(int(i)))
    return temp


wrw = index_value("4444444")


def create_population():  # Creating population
    population = []
    for i in range(case):
        x = create_cromosome(initial)
        x = index_value(x)
        population.append(x)
    return population


def fitness_function(cromosome):  # Fitness function
    fit = 0
    for i in cromosome:
        fit += initial[int(i)]
    return abs(fit)


def crossover(x, y):  # crossover function
    child_1, child_2 = "", ""
    point = random.randint(0, case - 1)
    child_1 = x[0:point] + y[point:]
    child_2 = y[0:point] + x[point:]

    return child_1, child_2


def mutation(cromosome):  # mutation function
    cromo = list(cromosome)
    index = random.randint(0, case - 1)
    value = random.randint(0, case - 1)
    cromo[index] = str(value)
    cromo = "".join(cromo)
    return cromo


def get_ans(cromosome):
    ans = []
    for i in cromosome:
        ans.append(initial[int(i)])
    temp = ""
    for i in ans:
        if i < 0:
            temp += "0"
        else:
            temp += "1"
    return None


data = create_population()


def genetic_algo(population):
    n_max = 1000
    while n_max > 0:
        fit = []
        for i in population:
            fit.append(fitness_function(i))

        compare = dict(zip(population, fit))  # key as population and fitness as value
        temp = sorted(compare.items(), key=lambda x: x[1])
        compare = dict(temp)  # sorted dictionary {population : fitness}

        key_population = compare.keys()
        value_fitness = compare.values()

        if 0 in value_fitness:
            return get_ans(key_population)  # return's ans if fitness is 0
        else:
            worst = list(compare)[-1]  # removing worst fistness
            compare.pop(worst)

            new_population = list(compare)
            next_gen = []
            for i in range(1, len(new_population), 2):
                x = new_population[i]
                y = new_population[i - 1]
                temp = list(crossover(x, y))  # crossover
                for j in temp:
                    next_gen.append(j)
            new_popu = []
            for i in next_gen:
                new_popu.append(mutation(i))  # mutation

        n_max -= 1
    else:
        return -1


# print(genetic_algo(data))
