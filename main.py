# p11 part 4: conjugation map checker thing
n = int(input("n: ").strip()) # hard max integer

def map(lhs, k):
    return k if k not in lhs else lhs[(lhs.index(k)+1)%len(lhs)]

def reduce(exp):
    l = []
    v = set()
    for k in range(1, n+1):
        j = k
        p = []
        while j not in v:
            v.add(j)

            jp = j
            for ex in exp[::-1]:
                jp = map(ex, jp)

            if j != jp:
                p.append(j)
                j = jp
            else:
                break
                
        if len(p) > 0: 
            l.append(p)

    return l


# table = [[k for k in range(9)] for j in range(9)]
# P = [[], [1,3], [2,3,4], [1,2,4], [1,2,4,3], [2,4,3], [1,3,2,4], [1,4,3,2]]
# s = set()

# def to_str(r):
#     return ''.join(["("+' '.join([str(d) for d in x])+")" for x in r])

# for r in range(9):
#     for c in range(9):
#         if r == 0 and c == 0: continue
#         red = reduce([P[r-1], P[c-1]])
#         table[r][c] = to_str(red)
#         s.add(table[r][c])
#         print(to_str([P[r-1]]), to_str([P[c-1]]), "-> ", to_str(red))

# for p in P: s.add(to_str([p]))
# print(s, len(s))


# g = [[], [1, 2], [1, 3], [2, 3], [1, 2, 3], [2, 1, 3]]
# e = g[0]
# ginv = [[x for x in g if eval(x, a) == e][0] for a in g]
# exit(0)
import itertools
perms = [k for k in itertools.permutations([1, 2, 3, 4, 5, 6], r=5)]

def toperm(l):
    return '(' + ' '.join([str(k) for k in l]) + ')'

def read(exp):
    parse = lambda a: [int(x) for x in a.replace("(", "").replace(")", "").strip().split(" ")]
    e = [parse(x) for x in exp.split(")(")]
    return e

while True:
    exp = input("$: ")
    exp = read(exp)
    rexp = reduce(exp)
    print(f"-> {''.join(['('+' '.join([str(y) for y in x])+')' for x in rexp])}")
# print(eval([1, 2, 3], [1, 2, 3]))
# exit(0)
# print(f"g: {g}")
# print(f"ginv: {ginv}")

# for i,a in enumerate(g):
#     ainv = ginv[i]
#     ca = [eval(a, eval(x, ainv)) for x in g]
#     pretty = lambda a: str(a).replace(",", "").replace("[", "$(").replace("]", ")$").replace(")$ $(", ")$ & $(")[2:-2]
#     pretty2 = lambda a: str(a).replace(",", "").replace("[", "(").replace("]", ")")

#     print(f"${pretty2(a)}x{pretty2(ainv)}$ & {pretty(ca)} \\\\")

