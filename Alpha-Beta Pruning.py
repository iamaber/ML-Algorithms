import random
bracu_id = input('Enter your student ID:')

#Replacing 0's in student Id
lst = list(bracu_id)
for i in range(len(lst)):
    if lst[i] == '0':
        lst[i] = '8'
bracu_id = ''.join(lst)

#Initializing variables
min_pont = int(bracu_id[4])
rev_last  = bracu_id[7] + bracu_id[6] 
max_pont = int(int(rev_last) * 1.5)
total_point_to_win = int(rev_last)
shuffels = int(bracu_id[3]) 
minimum, maximum = -10000, 10000 # As -infinite and +infinite

#Genarate random points
points = random.sample(range(min_pont, max_pont), 8) 

#Alpha-beta pruning algorithm
def alpha_beta(depth, node, flag, data, alpha, beta): #min max as flag
    if depth == 3: # depth = level - 1
        return data[node]
    if flag == True:  
        best = minimum
        for i in range(2):
            value = alpha_beta(depth+1 , node*2+i, False, data, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = maximum
        for i in range(2):
            value = alpha_beta(depth+1 , node*2+i, True, data, alpha, beta)
            best = min(best, value)
            alpha = min(alpha, best)
            if beta <= alpha:
                break
        return best


#Task-1
print('Task-1:')
result = alpha_beta(0,0,True,points,minimum,maximum)
print(f'Generated 8 random points between the minimum and maximum pointlimits:{points}')
print(f'Total points to win:{total_point_to_win}')
print(f'Achieved point by applying alpha-beta pruning:{result}')
if result > total_point_to_win:
    print('The winner is Optimus Prime\n')
else:
    print('The winner is Megatron\n')
print('========================================================')


#Task-2
print('Task-2:')
suffle_result = []
for i in range(shuffels):
    new_points = points.copy()
    random.shuffle(new_points)
    val = alpha_beta(0,0,True,new_points,minimum,maximum)
    suffle_result.append(val)
print('After the shuffle:')
print(f'List of all points values from each shuffles:{suffle_result}')
print(f'The maximum value of all shuffles:{max(suffle_result)}')
count = 0
for i in suffle_result:
    if i > total_point_to_win:
        count += 1 
print(f'Won {count} times out of {shuffels} number of shuffles')


