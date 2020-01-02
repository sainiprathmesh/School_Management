from src.Db_connection import db_connection


def insertStudent(sclass, saddress, srno, sfee):
    sql_statement = "Insert Into Student VALUES (%s,%s,%s,%s)"
    values = (srno, sclass, saddress, sfee)
    db_connection.cur.execute(sql_statement, values)
    db_connection.conn.commit()
    print("Detail Saved Sucessfully!!!")


def viewStudent(srno):
    sql_statement = "SELECT * FROM Student where RollNo = %s"
    sa = (srno,)
    db_connection.cur.execute(sql_statement, sa)
    output = db_connection.cur.fetchall()
    for x in output:
        print(x)


def updateStudent(sclass, saddress, srno, sfee):
    sql_statement = "UPDATE Student SET Address=%s,Class=%s,Fees=%s where RollNo=%s"
    sc = (saddress, sclass, sfee, srno, )
    db_connection.cur.execute(sql_statement, sc)
    db_connection.conn.commit()
    print("Detail Updated Sucessfully!!!")


def deleteStudent(srno):
    sql_query = "DELETE FROM Student where RollNo=%s"
    sa = (srno,)
    db_connection.cur.execute(sql_query, sa)
    db_connection.conn.commit()
    print("Data deleted successfully!!!")


def insertEmployee(ename, edept, eid):
    sql_statement = "Insert Into Employee VALUES (%s,%s,%s)"
    values = (ename, edept, eid)
    db_connection.cur.execute(sql_statement, values)
    db_connection.conn.commit()
    print("Detail Saved Sucessfully!!!")


def viewEmployee(eid):
    sql_statement = "SELECT * FROM Employee where eid = %s"
    sa = (eid,)
    db_connection.cur.execute(sql_statement, sa)
    output = db_connection.cur.fetchall()
    for x in output:
        print(x)


def updateEmployee(ename, edept, eid):
    sql_statement = "UPDATE Employee SET ename=%s,edept=%s where eid=%s"
    sc = (ename, edept, eid, )
    db_connection.cur.execute(sql_statement, sc)
    db_connection.conn.commit()
    print("Detail Updated Sucessfully!!!")


def deleteEmployee(eid):
    sql_query = "DELETE FROM Employee where eid=%s"
    sa = (eid,)
    db_connection.cur.execute(sql_query, sa)
    db_connection.conn.commit()
    print("Data deleted successfully!!!")