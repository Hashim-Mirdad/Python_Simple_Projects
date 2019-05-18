#       ******** Calculator  ********


class calculator:
    def __init__(self, val1=None, val2=None, result=None, choice=None):
        self.val1 = float(input("Please Enter the first Value:  "))
        self.val2 = float(input("Please Enter the Second Value:  "))
        self.choice = input("Please Select your choice: 1/2/3/4  ")
        self.result = result
        if self.choice == "1":
            self.result = self.val1 + self.val2
            print(self.result)
                
        elif self.choice == "2":
            self.result = self.val1 - self.val2
            print(self.result)
        elif self.choice == "3":
            self.result = self.val1 * self.val2
            print(self.result)
        elif self.choice == "4":
            self.result = self.val1 / self.val2
            print(self.result)
        elif self.choice == "0" or self.choice >= "5":
            if self.choice == "0":
                try:
                    print("Please Select Number between 1 and 4")

                except ValueError:
                    print("Value error", ValueError)
            elif self.choice >= "4":
                try:
                    print("please try again")
                except ValueError:
                    return ValueError
        else:
            print("good Bye")

    def __str__(self):
        return " value1 {} value2 {} is eqaul to {}".format(self.val1, self.val2, self.result)

def main():
    calculator()

if __name__=="__main__":
    main()