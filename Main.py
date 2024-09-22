# def solution(U, weight):
#     current = [None, None]
#     counter = 0

#     for i in range(len(weight)):
#         if current[0] == None:
#             current[0] = weight[i]
#         elif current[1] == None:
#             current[1] = weight[i]
#         else:
#             current[0] = current[1]
#             current[1] = weight[i]

#         if current[0] != None and current[1] != None:
#             total_weight = current[0] + current[1]
#         else:
#             total_weight = current[0] or current[1]

#         if total_weight > U:
#             counter += 1
#             current[1] = None

#     return counter
# --------

# def solution(U, weight):
#     counter = 0
#     current = [None, None]

#     for i in range(len(weight)):
#         if current[0] is None:
#             current[0] = weight[i]
#         elif current[1] == None:
#             current[1] = weight[i]
#         else:
#             current[0] = current[1]
#             current[1] = weight[i]

#         total_weight = 0
#         if current[0] != None:
#             total_weight += current[0]
#         if current[1] != None:
#             total_weight += current[1]

#         if total_weight > U:
#             counter += 1
#             current[1] = None

#     return counter

# ------

# def solution(U, weight):
#     counter = 0
#     current = [None, None]
#     n = len(weight)

#     for i in range(n):
#         if current[0] != None and current[1] != None:
#             current[0] = current[1]
#             current[1] = None

#         if current[0] == None:
#             current[0] = weight[i]
#         elif current[1] == None:
#             current[1] = weight[i]

#         total_weight = 0
#         if current[0] != None:
#             total_weight += current[0]
#         if current[1] != None:
#             total_weight += current[1]

#         #check weight
#         if total_weight > U:
#             counter += 1
#             current[1] = None

#     return counter


# def solution(U, weight):
#     counter = 0
#     current = []

#     for w in weight:
#         if len(current) < 2:
#             current.append(w)
#         else:
#             current.pop(0)
#             current.append(w)

#         if sum(current) > U:
#             counter += 1
#             current.pop()

#     return counter

# if total_weight > U:
#             counter += 1
#             current.pop()
#             if len(current) == 1:
#                 current[0] = None

#     current = [car for car in current if car is not None]


# def solution(U, weight):
#     counter = 0
#     current = []

#     for w in weight:
#         if len(current) < 2:
#             current.append(w)
#         else:
#             current.pop(0)
#             current.append(w)

#         if len(current) == 2 and sum(current) > U:
#             counter += 1
#             current.pop()

#     return counter


def solution(U, weight):
    counter = 0
    bridge = [None, None]

    bridge[0], bridge[1] = weight[0], weight[1]
    weight.pop()
    weight.pop()

    for i in range(len(weight)):
        if weight[i] + bridge[1] < U:
            bridge[0] = bridge[1]
            bridge[1] = weight[i]
        else:
            counter += 1

    return counter


cars = [7, 6, 5, 2, 7, 4, 5, 4]
U = 7
print(solution(U, cars))
