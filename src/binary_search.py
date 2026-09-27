import itertools

def objective(x1, x2) :
    return (-(3*x1) - (5*x2) - (4*x1*x2))

best_value = objective(0, 0)
for i in itertools.product([0, 1], repeat=2) :
    cur_value = objective(i[0],i[1])
    cur_state = i

    if (cur_value >= best_value) :
        best_value = cur_value
        best_state = cur_state

print(best_state ,best_value)