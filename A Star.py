f = open("a_star_input.txt").read().splitlines()
input = []
for line in range(len(f)):
    input.append(f[line].split(" "))

# Getting heuristic value
cites = []
val = []
for i in range(len(input)):
    city = input[i][0]
    cites.append(city)
for i in range(len(input)):
    val.append(int(input[i][1]))
h = dict(zip(cites, val))
h = dict(h)

# Creating adjancy list where key == city , value == destination and cost
temp = []
for i in range(len(input)):
    temp1 = []
    x = input[i]
    x.remove(str(val[i]))
    x.remove(cites[i])
    for j in range(0, len(x), 2):
        y = []
        a, b = x[j], x[j + 1]
        y.append(a)
        y.append(b)
        temp1.append(y)
    temp.append(temp1)
adj_list = zip(cites, temp)
adj_list = dict(adj_list)

start_node = cites[0]
goal_node = cites[-1]


def a_start(start_node, goal_node, adj_list, heuristic):
    open_list = [[start_node, heuristic[start_node]]]  # Arad, 366
    close_list = []

    cost = {start_node: 0}  # initial cost

    while len(open_list) > 0:
        f_n = [i[1] for i in open_list]
        chosen_index = f_n.index(min(f_n))
        node = open_list[chosen_index][0]  # current node
        close_list.append(open_list[chosen_index])  # if all child nodes are visited
        del open_list[chosen_index]

        if close_list[-1][0] == goal_node:  # break the loop if goal is found
            break

        for item in adj_list[node]:
            close_list_item = [x_item[0] for x_item in close_list]
            if item[0] in close_list_item:
                continue
            cost.update(
                {item[0]: int(cost[node]) + int(item[1])}
            )  # add nodes to cost dictionary
            fn_node = (
                int(cost[node]) + heuristic[item[0]] + int(item[1])
            )  # calculate f(n) of current node
            temp = [item[0], fn_node]
            open_list.append(temp)

    trace_node = goal_node
    optimal_sequence = [goal_node]  # optimal node sequence

    for i in range(len(close_list) - 2, -1, -1):
        check_node = close_list[i][0]  # current node

        if trace_node in [children[0] for children in adj_list[check_node]]:
            children_nodes = [i[0] for i in adj_list[check_node]]
            children_costs = [i[1] for i in adj_list[check_node]]

            # check whether h(s) + g(s) = f(s)
            if (
                int(cost[check_node])
                + int(children_costs[children_nodes.index(trace_node)])
                == cost[trace_node]
            ):
                optimal_sequence.append(check_node)
                trace_node = check_node
    optimal_sequence.reverse()  # reverse the optimal sequence as we backtracked

    for i in optimal_sequence:
        print(i, end=" -> ")
    print()
    final_cost = cost[goal_node]
    print(f"Total distance: {final_cost} km")


a_start(start_node, goal_node, adj_list, h)
