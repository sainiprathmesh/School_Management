from src.DatabaseConnection import DatabaseConnection


def insert_student(student_class, student_address, student_roll_number, student_fees):
    sql_statement = "Insert Into Student VALUES (%s,%s,%s,%s)"
    values = (student_roll_number, student_class, student_address, student_fees)
    DatabaseConnection.cur.execute(sql_statement, values)
    DatabaseConnection.conn.commit()
    print("Detail Saved Successfully!")


def view_student_details(student_roll_number):
    sql_statement = "SELECT * FROM Student where RollNo = %s"
    sa = (student_roll_number,)
    DatabaseConnection.cur.execute(sql_statement, sa)
    output = DatabaseConnection.cur.fetchall()
    for x in output:
        print(x)


def updateStudent(sclass, saddress, srno, sfee):
    sql_statement = "UPDATE Student SET Address=%s,Class=%s,Fees=%s where RollNo=%s"
    sc = (saddress, sclass, sfee, srno,)
    DatabaseConnection.cur.execute(sql_statement, sc)
    DatabaseConnection.conn.commit()
    print("Detail Updated Sucessfully!!!")


def deleteStudent(srno):
    sql_query = "DELETE FROM Student where RollNo=%s"
    sa = (srno,)
    DatabaseConnection.cur.execute(sql_query, sa)
    DatabaseConnection.conn.commit()
    print("Data deleted successfully!!!")


def insertEmployee(ename, edept, eid):
    sql_statement = "Insert Into Employee VALUES (%s,%s,%s)"
    values = (ename, edept, eid)
    DatabaseConnection.cur.execute(sql_statement, values)
    DatabaseConnection.conn.commit()
    print("Detail Saved Sucessfully!!!")


def viewEmployee(eid):
    sql_statement = "SELECT * FROM Employee where eid = %s"
    sa = (eid,)
    DatabaseConnection.cur.execute(sql_statement, sa)
    output = DatabaseConnection.cur.fetchall()
    for x in output:
        print(x)


def updateEmployee(ename, edept, eid):
    sql_statement = "UPDATE Employee SET ename=%s,edept=%s where eid=%s"
    sc = (ename, edept, eid,)
    DatabaseConnection.cur.execute(sql_statement, sc)
    DatabaseConnection.conn.commit()
    print("Detail Updated Sucessfully!!!")


def deleteEmployee(eid):
    sql_query = "DELETE FROM Employee where eid=%s"
    sa = (eid,)
    DatabaseConnection.cur.execute(sql_query, sa)
    DatabaseConnection.conn.commit()
    print("Data deleted successfully!!!")
