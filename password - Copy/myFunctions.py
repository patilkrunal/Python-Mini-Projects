import pyperclip
from database import cursor, db


def add_pswd(accntname, username, password):
    sql = ("INSERT INTO pswd(accntname, username, password) VALUES (%s, %s, %s)")
    cursor.execute(sql, (accntname, username, password,))
    db.commit()
    row_id = cursor.lastrowid
    print(f"Password for account {accntname} added to the database!")

def get_pswds():
    sql = ("SELECT * FROM pswd ORDER BY created DESC")
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row[0], row[1], sep=": ")

def get_pswd(account):
    sql = ("SELECT password FROM pswd WHERE accntname = %s")
    cursor.execute(sql, (account,))
    try:
        result = cursor.fetchone()
    except Exception as e:
        print(e)
    
    if(len(result)):
        pyperclip.copy(result[0])
        print(f"Password for {account} copied to clipboard.")
    else:
     	print(f"No data found with accountname {account}")

def update_pswd(accntname, username, password):
    sql = ("UPDATE pswd SET username = %s WHERE accntname = %s")
    cursor.execute(sql, (username, accntname))
    sql = ("UPDATE pswd SET password = %s WHERE accntname = %s")
    cursor.execute(sql, (password, accntname))
    db.commit()
    print(f"{accntname} data updated!")

def delete_pswd(accntname):
    sql = ("DELETE FROM pswd WHERE accntname = %s")
    cursor.execute(sql, (accntname,))
    db.commit()
    print(f"{accntname} data deleted!")


# add_pswd('gmail1', 'username1', 'Brad')
# add_pswd('fb1', 'username2', 'Jeff')
# add_pswd('yahoo1', 'username', 'Jane')

# get_pswds()
# get_pswd('gmail1')

# update_pswd('fb1', 'username', 'newpassword')
# get_pswds()

# delete_pswd('fb1')
# get_pswds()