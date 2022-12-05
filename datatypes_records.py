# TYPE EmployeeRecord
# DECLARE EmployeeFirstName : STRING
# DECLARE EmployeeFamilyName : STRING
# DECLARE DateEmployed : DATE
# DECLARE Salary : CURRENCY
# END TYPE

# class EmployeeRecord:
#     def __init__(self, EmployeeFirstName='', EmployeeFamilyName='', DateEmployed='', Salary=0):
#         self.EmployeeFirstName = EmployeeFirstName
#         self.EmployeeFamilyName = EmployeeFamilyName
#         self.DateEmployed = DateEmployed
#         self.Salary = Salary
#
#
# jane = EmployeeRecord()
# jane.EmployeeFirstName = "Jannette"
# jane.EmployeeFamilyName = "Michelle"
# jane.DateEmployed = "16/12/2022"
# jane.Salary = 9000
# jane.Extra = 7000
#
#
# print(jane.EmployeeFirstName)
# print(jane.EmployeeFamilyName)
# print(jane.DateEmployed)
# print(jane.Salary)
# print(jane.Extra)

# MaxIndex ← 6
# INPUT SearchValue
# Found ← FALSE
# Index ← -1
# REPEAT
# 	Index ← Index + 1
# 	IF MyList[Index] = SearchValue THEN
# 		Found ← TRUE
# 	ENDIF
# UNTIL Found = TRUE OR Index >= MaxIndex
# IF Found = TRUE THEN
# 	OUTPUT “Value found in location: ” Index
# ELSE
# 	OUTPUT “Value not found”
# ENDIF





def linear_search(list_of_items, search_value):
    MaxIndex = len(list_of_items)
    Found = False
    Index = -1
    while Found == False and Index <= MaxIndex:
        Index = Index + 1
        if list_of_items[Index] == search_value:
            Found = True
    if Found == True:
        print("Value found in location: ", Index)
    else:
        print("Value not found")


MyList = [3, 7, 1, 9, 0, 4, 6]

SearchValue = int(input("Enter search value: "))

linear_search(MyList, SearchValue)




# matrix = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
#
# print(matrix[1][0])
#
#
# for row in matrix:
#     for i in row:
#         print(i)


# TYPE PersonType
# Name : STRING
# DateOfBirth : DATE
# Height : REAL
# NumberOfSiblings : INTEGER
# IsFullTimeStudent : BOOLEAN
# ENDTYPE

# class PersonType:
#     def __init__(self, Name ="", DateOfBirth="", Height=0, NumberOfSiblings=0, IsFullTImeStudent=False):
#         self.Name = Name
#         self.DateOfBirth = DateOfBirth
#         self.Height = Height
#         self.NumberOfSiblings = NumberOfSiblings
#         self.IsFullTImeStudent = IsFullTImeStudent
#
#
# mike = PersonType()
#
# mike.Name = "Michael Mutagana"
# mike.NumberOfSiblings = 9
# print(mike.Name)
# print(mike.NumberOfSiblings)
