held=int(input("Number of Classes held:"))
Attended=int(input("Number of Classes Attended:"))

Percentage_Attended:int= ((Attended/held)*100)
print("Percentage of class attended:",Percentage_Attended)

if Percentage_Attended<75:
    print("Not Allowed to sit in exam")
else:
    print("Allowed to sit in Exam")