
class Rod:
    def __init__(self, name_):
        self.stack = []
        self.name = name_ 
    
    def push(self, disk_num):
        '''
        disk_num = size of the disk | it should be unique
        '''
        if self.size() > 0:
            if self.top() > disk_num:
                self.stack.append(disk_num)
            else:
                print("ERROR! Can't put disk with larger size on smaller sized disk")
                print("Note: The size of the disk is the disk number")
        else: 
            self.stack.append(disk_num)

    def pop(self):
        '''
        removes top element
        '''
        try:
            self.stack.pop()    
        except Exception as e:
            print(f"ERROR : {e}")

    def top(self) -> int:
        '''
        returns the top element in the stack
        '''
        if self.size() == 0: print("top operation can't be performed : The stack is Empty"); return -1
        return self.stack[-1]
    
    def size(self) -> int:
        '''
        returns size of the stack
        '''
        return len(self.stack)

class Run:
    def __init__(self, n):
        self.A = Rod("A")
        self.B = Rod("B")
        self.C = Rod("C")
        self.n = n
        self.no_of_moves = (1 << n) - 1

        for i in range(n, 0, -1):
            self.A.push(i)
        
        self.TowerOfHanoi()
        

    def TowerOfHanoi(self):

        print("-------------Running Tower of Hanoi (iterative approach)---------------")

        t = int(input("Enter 1 (iterative) / 0 (recursive) : "))

        if t == 0:
            self.recursive_method(self.n, self.A, self.C, self.B)
        else:
            self.iterative_approach()
        
    def iterative_approach(self):
        if self.n % 2 == 1:
            pairs = [(self.A, self.C), (self.A, self.B), (self.B, self.C)]
        else:
            pairs = [(self.A, self.B), (self.A, self.C), (self.B, self.C)]

        for i in range(1, self.no_of_moves + 1):
            rod1, rod2 = pairs[(i - 1) % 3]
            self.moveDisk(rod1, rod2)

    def recursive_method(self, n, src, dest, aux):
        if n == 0:
            return
        self.recursive_method(n - 1, src, aux, dest)
        self.moveDisk(src, dest)
        self.recursive_method(n - 1, aux, dest, src)
        
        

    def moveDisk(self, rod1, rod2):
        if(rod2.size() == 0): 
            val = rod1.top(); rod1.pop(); rod2.push(val)
            self.display(rod1, rod2, val)
        elif rod1.size() == 0 : 
            val = rod2.top(); rod2.pop(); rod1.push(val)
            self.display(rod2, rod1, val)
        elif(rod1.top() > rod2.top()): 
            val = rod2.top(); rod2.pop(); rod1.push(val)
            self.display(rod2, rod1, val)
        elif(rod1.top() < rod2.top()): 
            val = rod1.top(); rod1.pop(); rod2.push(val)
            self.display(rod1, rod2, val)
    
    def display(self, rod1, rod2, val):
        print(f"{val} : {rod1.name}-> {rod2.name}")
        


def main():
    no_of_disks = int(input("Enter the number of disks: "))
    orchestrator = Run(no_of_disks)

if __name__ == '__main__':
    print("Tower Of Hanoi - Simulation")
    main()
