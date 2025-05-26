
#department infromation


# class department:
#     def __init__(self,deparment_id,dname,dlocation,dhod):
#         self.deparment_id="04"
#         self.dname="ece"
#         self.dlocation="hyderabad"
#         self.dhod="nagesh"
#     def display_department_info(self):
#          print("department information: ")
#          print("-------------")
#          print(f"department_id:{self.deparment_id}")
#          print(f"dname: {self.dname}")
#          print(f"dlocation: {self.dlocation}")
#          print(f"dhod:{self.dhod}")

# department1 = department("04","ece","hyd","nagesh")
# department1.display_department_info()



#department count
# class department:
#     department_count = 0
#     def __init__(self,deparment_id,dname,dlocation,dhod):
#         self.deparment_id="04"
#         self.dname="ece"
#         self.dlocation="hyderabad"
#         self.dhod="nagesh"
#         department.department_count += 1
#     def display_department_info(self):
#          print("department information: ")
#          print("-------------")
#          print(f"department_id:{self.deparment_id}")
#          print(f"dname: {self.dname}")
#          print(f"dlocation: {self.dlocation}")
#          print(f"dhod:{self.dhod}")
#     @classmethod
#     def get_total_department(cls):
#           return cls.department_count
# department1 = department("4", "ece", "hyd" , "nagesh")
# department.display_department_info()
# print(f"Total department: {department.get_total_department()}")


#taking inputs 
# class department:
#     department_count = 0
#     def __init__(self,deparment_id,dname,dlocation,dhod):
#         self.deparment_id="04"
#         self.dname="ece"
#         self.dlocation="hyderabad"
#         self.dhod="nagesh"
#         department.department_count += 1
#     def display_department_info(self):
#          print("department information: ")
#          print("-------------")
#          print(f"department_id:{self.deparment_id}")
#          print(f"dname: {self.dname}")
#          print(f"dlocation: {self.dlocation}")
#          print(f"dhod:{self.dhod}")
#     @classmethod
#     def get_total_department(cls):
#           return cls.department_count
# print("Enter details for Department 1")
# department_id = input("Enter department ID: ")
# dname = input("Enter department name: ")
# dlocation = input("Enter department location: ")
# dhod = input("Enter HOD name: ")
# department1 = department(department_id, dname, dlocation , dhod)
# department.display_department_info()
# print(f"Total department: {department.get_total_department()}")


# code for department for loop no of departments

# class department:
#     department_count = 0  
#     def __init__(self, department_id, dname, dlocation, dhod):
#         self.deparment_id = department_id
#         self.dname = dname
#         self.dlocation = dlocation
#         self.dhod = dhod
#         department.department_count += 1  
#     def display_department_info(self):
#         print("\nDepartment Information:")
#         print("------------------------")
#         print(f"Department ID : {self.deparment_id}")
#         print(f"Name          : {self.dname}")
#         print(f"Location      : {self.dlocation}")
#         print(f"HOD           : {self.dhod}")
#         print(f"Total Departments Created: {department.get_total_department()}")
#     @classmethod
#     def get_total_department(cls):
#         return cls.department_count
# num = int(input("How many departments do you want to enter? "))
# for i in range(num):
#     print(f"\nEnter details for Department {i + 1}")
#     department_id = input("Enter department ID: ")
#     dname = input("Enter department name: ")
#     dlocation = input("Enter department location: ")
#     dhod = input("Enter hod name: ")
#     dept = department(department_id, dname, dlocation, dhod)
#     dept.display_department_info()

# displaying in list

# class department:
#     department_count = 0
#     department_list=[]  
#     def __init__(self, department_id, dname, dlocation, dhod):
#         self.department_id = department_id
#         self.dname = dname
#         self.dlocation = dlocation
#         self.dhod = dhod
#         department.department_count += 1
#         department.department_list.append({  #this is for adding deptinfo as a dict into list
#             "Department ID": self.department_id,
#             "Name": self.dname,
#             "Location": self.dlocation,
#             "HOD": self.dhod
#         })  
#     def display_department_info(self):
#         print("\nDepartment Information:")
#         print(f"Department ID : {self.department_id}")
#         print(f"Name          : {self.dname}")
#         print(f"Location      : {self.dlocation}")
#         print(f"HOD           : {self.dhod}")
#         print(f"Total Departments Created: {department.get_total_department()}")
#     @classmethod
#     def get_total_department(cls):
#         return cls.department_count
#     @classmethod
#     def display_all_departments(cls):
#         print("All Departments Information:")
#         index = 1
#         for dept in cls.department_list:
#             print(f"\nDepartment {index}:")
#             for key, value in dept.items():
#                 print(f"{key:15}: {value}")
#             index += 1
#         print(f"\nTotal Departments Created: {cls.get_total_department()}")
# num = int(input("How many departments do you want to enter? "))
# for i in range(num):
#     print(f"\nEnter details for Department {i + 1}")
#     department_id = input("Enter department ID: ")
#     dname = input("Enter department name: ")
#     dlocation = input("Enter department location: ")
#     dhod = input("Enter hod name: ")
#     dept = department(department_id, dname, dlocation, dhod)
#     dept.display_department_info()
# department.display_all_departments()




#for sreaching department details whether they are present are not

class department:
    department_count = 0
    department_list=[]  
    def __init__(self, department_id, dname, dlocation, dhod):
        self.department_id = department_id
        self.dname = dname
        self.dlocation = dlocation
        self.dhod = dhod
        department.department_count += 1
        department.department_list.append({  #this is for adding deptinfo as a dict into list
            "Department ID": self.department_id,
            "Name": self.dname,
            "Location": self.dlocation,
            "HOD": self.dhod
        })  
    def display_department_info(self):
        print("\nDepartment Information:")
        print(f"Department ID : {self.department_id}")
        print(f"Name          : {self.dname}")
        print(f"Location      : {self.dlocation}")
        print(f"HOD           : {self.dhod}")
        print(f"Total Departments Created: {department.get_total_department()}")
    @classmethod
    def get_total_department(cls):
        return cls.department_count
    @classmethod
    def display_all_departments(cls):
        print("All Departments Information:")
        index = 1
        for dept in cls.department_list:
            print(f"\nDepartment {index}:")
            for key, value in dept.items():
                print(f"{key:15}: {value}")
            index += 1  
        print(f"\nTotal Departments Created: {cls.get_total_department()}")
    @classmethod
    def search_by_id(cls, dept_id):
        print(f"\nSearching for ID: {dept_id}")
        for dept in cls.department_list:
            if dept["Department ID"] == dept_id:
                print("Found Department:")
                for k, v in dept.items():
                    print(f"{k}: {v}") 
                return
        print("\nDepartment ID not found.")

                

    @classmethod
    def search_by_name(cls, name):
        print(f"\nSearching for Name: {name}")
        for dept in cls.department_list:
            if dept["Name"].lower() == name.lower():
                print("Found Department:")
                for k, v in dept.items():
                    print(f"{k}: {v}")
                return
        print("Department not found.")

num = int(input("How many departments do you want to enter? "))
for i in range(num):
    print(f"\nEnter details for Department {i + 1}")
    department_id = input("Enter department ID: ")
    dname = input("Enter department name: ")
    dlocation = input("Enter department location: ")
    dhod = input("Enter hod name: ")
    dept = department(department_id, dname, dlocation, dhod)
    dept.display_department_info()
department.display_all_departments()
# Search by ID
search_id = input("\nSearch by Department ID: ")
department.search_by_id(search_id)

# Search by Name
search_name = input("\nSearch by Department Name: ")
department.search_by_name(search_name)


