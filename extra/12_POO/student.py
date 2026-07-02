class Student:
    def __init__(self, name, house):           
        self.name = name
        self.house = house
        # self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
    #GET
    @property
    def name(self):
        return self._name

    #SET
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    #GET 
    @property
    def house(self):
        return self._house
    
    #SET
    @house.setter
    def house(self, house):
        if house not in ["Griffindor", "Hufflepuff", "Revenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house
    

    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "🦌"
    #         case "Otter":
    #             return "🦦"
    #         case "Jack Russell terrier":
    #             return "🐶"
    #         case _:
    #             return "🪄"


def main():
    student = Student.get()
    print(student)
    # print ("Expecto Patronum!")
    # print(student.charm())


if __name__ == "__main__":
    main()
