import numpy as np

monkeys = []

class Monkey(object):
    def __init__(self, items, op, test, outs):
        inspected = 0
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})
        
    def eval_items(self):
        global monkeys
        for i in self.items:
            self.inspected += 1
            inp = self.op.replace("old", str(i))
            n_i = eval(inp, {'__builtins__':None}) // 3
            
            monkeys[self.outs[0 if n_i % self.test == 0 else 1]].items.append(n_i)

        self.items = []
            
def parse_all(monkeys):
    with open('/mnt/c/Users/felix/workspace/adventOfCode/11/in.txt') as f:
        line = f.readline()
        while line:
            if line.startswith("Monkey"): #not actually neseccary
                items = [int(x) for x in f.readline()[18:-1].split(", ")]
                op = f.readline()[19:-1]
                test = int(f.readline()[21:-1])
                outs = [int(f.readline()[29:-1]), int(f.readline()[30:-1])]
                monkeys.append(Monkey(items, op, test, outs))
            f.readline()
            line = f.readline()
    
def main():
    global monkeys
    parse_all(monkeys)
    
    for _ in range(20):
        [m.eval_items() for m in monkeys]
                
    print(np.prod(sorted([m.inspected for m in monkeys])[-2:]))

if __name__ == '__main__':
    main()