
while True:
    from src.Database_Helper import insertStudent, deleteStudent, updateStudent, viewStudent, insertEmployee, \
        deleteEmployee, updateEmployee, viewEmployee
    from src.Db_connection import db_connection
    print("_______________________________SCHOOL MANAGEMENT SYSTEM_______________________________")
    print("1.Student\n2.Employee\n3.Exam\n4.Fees")
    a = int(input("Enter Your Choice: "))
    if a == 1:
        print("1.Addmission\n2.Deletion\n3.Update\n4.View")
        b = int(input("Enter your choice: "))
        if b == 1:
            srno = int(input("Enter roll no.: "))
            sclass = int(input("enter Class: "))
            saddress = input("Enter Address: ")
            sfee = int(input("Enter amount of fees deposited: "))
            insertStudent(sclass, saddress, srno, sfee)
        elif b == 2:
            srno = input("Enter Roll No. of student you want to delete: ")
            deleteStudent(srno)
        elif b == 3:
            srno = int(input("Enter Roll No.: "))
            sclass = int(input("Enter New class: "))
            saddress = input("Enter New address: ")
            sfee = int(input("Enter updated amount of fees: "))
            updateStudent(sclass, saddress, srno, sfee, )
        elif b == 4:
            srno = input("1.Enter Roll No.: ")
            viewStudent(srno)
        else:
            pass

    if a == 2:
        print("1.New Joining\n2.Delete data\n3.Update Data\n4.View")
        c = int(input("Enter Your Choice: "))
        if c == 1:
            eid = int(input("Enter employee id: "))
            ename = input("enter employee name: ")
            edept = input("enter department of employee: ")
            insertEmployee(ename, edept, eid)
        elif c == 2:
            eid = int(input("enter employee id you want to delete:"))
            deleteEmployee(eid)
        elif c == 3:
            eid = int(input("enter old id of employee:"))
            ename = input("enter new name of employee: ")
            edept = input("enter new department of employee: ")
            updateEmployee(ename, edept, eid)
        elif c == 4:
            eid = int(input("enter employee id whhich you want to see detail: "))
            viewEmployee(eid)
        else:
            pass

    if a == 3:
        d = input("Enter roll no.: ")
        sql_statement = "select fees from Student where RollNo=%s"
        sf = (d,)
        db_connection.cur.execute(sql_statement, sf)
        output = db_connection.cur.fetchone()
        if output[0] >= 10000:
            print("Eligible for exam!!!!")
        else:
            print("Fees Remaining! Complete it to write exam paper.")

    if a == 4:
        d = int(input("Enter roll no.: "))
        sql_statement = "select fees from Student where RollNo=%s"
        sf = (d,)
        db_connection.cur.execute(sql_statement, sf)
        output = db_connection.cur.fetchone()
        if output[0] >= 10000:
            print("Completely Deposited!!!")
        else:
            print("Fees Remaining! Complete it as soon as possible.")
