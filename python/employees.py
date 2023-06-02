'''
berapa banyak karyawan yang berjenis kelamin laki-laki dan perempuan?
Mencari tahu siapa nama manager dengan menggunakan search algorithm?
buatlah perhitungan bonus berdasarkan gaji + bonus jika work_time karyawan diatas 7 jam dan posisi nya bukanlah manager
bonus = salary * work time / 100
total salary = salary + bonus
output : Employee: <employee name> have total salary: <total salary>
'''
employees = [
    {   #1
        "name": "Adam Moore",
        "gender": "male",
        "age": 39,
        "salary": 15_000_000,
        "position": "manager",
        "work_time": 5
    },  
    {   #2
        "name": "Ellis McCoy",
        "gender": "female",
        "age": 31,
        "salary": 10_000_000,
        "position": "supervisor",
        "work_time": 8
    },
    {   #3
        "name": "Mary Jane",
        "gender": "female",
        "age": 24,
        "salary": 25_000,
        "position": "admin",
        "work_time": 8
    },
    {   #4
        "name": "Alex Murphy",
        "gender": "male",
        "age": 35,
        "salary": 10_000,
        "position": "developer","work_time": 12
    },
    {   #5
        "name": "Norman Bourne",
        "gender": "male",
        "age": 18,
        "salary": 5000,
        "position": "developer",
        "work_time": 7.5
    }
]

#----------------------------------------------------------------
#kode Adiweno

print("EMPLOYEES\n\n1 Employee name list\n2 Manager\n3 employees salary\n4 count gender") #menu
input = int(input("Input(1/2/3/4): ")) #input

#cond 1
if input == 1: 
    for i in range(5): 
        employee = employees[i] #variabel yang memuat list employees dari 0 sampai 4 
        print(employee["name"])

#cond 2
elif input == 2:
    def searchManager(employees):   
        for employee in employees:  #untuk mencari employee dari awal hingga akhir list
            if employee["position"] == "manager": 
                return employee["name"]    #return variabel employee menjadi "name"
        return None     #return "None" jika tidak ada manager

    print("Manager: ", searchManager(employees)) #print fungsi
    
elif input == 3:
    totalSalary = ""
    for employee in employees:
        #employee = employees[i]
        managerSalary = employee["position"] == "manager"       #variabel untuk mengecualikan manager
        if employee["work_time"] >= 7 and managerSalary == False: 
            bonus = employee["salary"] * employee["work_time"] / 100    #math
            totalSalary = employee["salary"] + bonus                    #math
        #print manager salary and other salary            
        if managerSalary:
            print("Employee:", employee["name"], "have total salary:", employee["salary"])
        if "manager" not in employee["position"]:
            print("Employee:", employee["name"], "have total salary:", totalSalary) 
        #print(employee["name"])

elif input == 4:
    male = 0
    female = 0

    for i in employees:
        if i["gender"] == "male":
            male += 1
        if i["gender"] == "female":
            female += 1
    print("Male: %d\nFemale: %d" % (male,female))


else:
    print("wrong input")

