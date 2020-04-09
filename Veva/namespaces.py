input = list(map(lambda _: input().split(' '), range(int(input()))))
g = {'global': {'name': 'global', 'parent': None}}

def create(item):
    new_namespace = {
        'name': item[1],
        'parent': item[2],
    }
    g[item[1]] = new_namespace


def add(item):
    new_namespace = {
        'name': item[2],
        'parent': item[1],
    }
    g[item[1]][item[2]] = new_namespace


def get(item):
    current_namespace = g[item[1]]
    print()
    while (True):

        try:
            current_namespace[item[2]]
            return current_namespace['name']
        except:
            if g[current_namespace['parent']]["parent"] == None:
                current_namespace = g[current_namespace['parent']]


for command in input:
    print("Iter")
    if command[0] == 'create':
        create(command)
    elif command[0] == 'add':
        add(command)
    elif command[0] == 'get':
        get(command)

print(g)