
class Assignment:
    def __init__(self) -> None:
        self.final_list = []

    def take_input(self):
        # creating an empty list
        initial_list = []
        # number of elements as input
        n = int(input("Enter number of elements : "))
        # iterating till the range
        for i in range(0, n):
            input_value = input()
            initial_list.append(input_value) # adding the element  
        return  initial_list
        
    def operation(self,input_list):
        for x in input_list:
            if x == "D":
                self.calculate_d()
            elif x == "C":
                self.invalidate()
            elif x == "+":
                self.sum()
            else:
                self.add_record(int(x))

    def total_sum(self,final_list):
        total = 0
        for x in final_list:
            total += x
        return total

    def add_record(self,value):
        self.final_list.append(value)
        print("add_record",self.final_list)
        return self.final_list

    def calculate_d(self):
        # value = self.final_list[-1]
        value = 2 * self.final_list[-1]
        self.final_list.append(value)
        print("calculate_d",self.final_list)
        return self.final_list

    def invalidate(self):
        self.final_list.pop()
        print("invalidate",self.final_list)
        return self.final_list

    def sum(self):
        sum_value = 0
        sum = self.final_list[-1] + self.final_list[-2]
        self.final_list.append(sum)
        print("sum",self.final_list)
        return self.final_list

myclass = Assignment()
input_list = myclass.take_input()
myclass.operation(input_list)
total_sum = myclass.total_sum(myclass.final_list)
print(myclass.final_list)
print(total_sum)