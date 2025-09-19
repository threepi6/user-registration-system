import sqlite3

class Database():
    def __init__(self,dbadd : str):
        self.con = sqlite3.connect(dbadd)
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS MR_Management
                         (Name TEXT, Family TEXT,Phone TEXT , ID_Number TEXT ,Employee_ID TEXT PRIMARY KEY, Gender TEXT,Role TEXT )''')
        self.con.commit()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Inventory
                         (Item_Code TEXT PRIMARY KEY,Quantity INTEGER, Price INTEGER)''')
        self.con.commit()

    def search_login(self, ID_Number, Employee_ID):
        self.cur.execute('''SELECT * FROM  MR_Management WHERE Employee_ID = ? and ID_Number = ?''',(Employee_ID, ID_Number))
        record = self.cur.fetchone()
        if record:
            return record
        else:
            return None

class Mrm_table(Database):
    def __init__(self, dbadd):
        super().__init__(dbadd)
    
    def insert(self,name, family,phone, id_number, employee_id, gender,  role):
        try:
            self.cur.execute('INSERT INTO MR_Management VALUES(?, ?, ?, ?, ?, ?, ?)',
                            (name, family, phone, id_number, employee_id, gender, role))
            self.con.commit()
            return 'Insert successful'
        except Exception as ex:
            return ex
    
    def show(self):
        self.cur.execute('SELECT * FROM MR_Management')
        records = self.cur.fetchall()
        return records
    
    def update(self, name, family, phone, id_number, gender, role, employee_id):
        try:
            self.cur.execute('UPDATE MR_Management SET Name = ?, Family = ?, Phone = ?, ID_Number = ?, Gender = ?, Role = ? WHERE Employee_ID = ?'
                            ,(name, family, phone, id_number, gender, role, employee_id))
            self.con.commit()
            return 'Updete successful'
        except Exception as ex:
            return ex
        
    def delete(self, employee_id):
            try:
                self.cur.execute('DELETE FROM MR_Management WHERE Employee_ID = ?'
                            ,( employee_id,))
                self.con.commit()
                return 'Delete successful'
            except Exception as ex:
                return ex
    
    def search(self,name, family, phone, id_number, employee_id, gender,  role):
                query = 'SELECT * FROM MR_Management WHERE 1=1 '
                entrys = []

                if name:
                    query += 'AND Name = ? '
                    entrys.append(name)
                
                if family:
                    query += 'AND Family = ? '
                    entrys.append(family)

                if phone:
                    query += 'AND Phone = ? '
                    entrys.append(phone)
                
                if id_number:
                    query += 'AND ID_Number = ? '
                    entrys.append(id_number)
                
                if employee_id:
                    query += 'AND Employee_ID = ? '
                    entrys.append(employee_id)

                if gender:
                    query += 'AND Gender = ? '
                    entrys.append(gender)
                
                if role:
                    query += 'AND Role = ? '
                    entrys.append(role) 
                
                self.cur.execute(query, tuple(entrys))
                records = self.cur.fetchall()
                return records

class Inventory_table(Database):
    def __init__(self, dbadd):
        super().__init__(dbadd) 

    def insert(self, item_code, quantity, price):
        try:
            self.cur.execute('INSERT INTO Inventory VALUES(?,?,?)',(item_code, quantity, price))
            self.con.commit()
            return 'Insert successful'
        except Exception as ex:
            return ex

    def show(self):
        self.cur.execute('SELECT * FROM Inventory')
        records = self.cur.fetchall()
        return records
    
    def update(self, item_code, quantity,price):
        try:
            self.cur.execute('UPDATE Inventory SET Quantity = ?, Price = ? WHERE Item_Code = ?',(quantity,price, item_code))
            self.con.commit()
            return 'Update successful'
        except Exception as ex:
            return ex

    def delete(self,item_code):
            try:
                self.cur.execute('DELETE FROM Inventory WHERE Item_Code = ?',(item_code,))
                self.con.commit()
                return 'Delete successful'
            except Exception as ex:
                return ex
    
    def sell_and_buy(self,item_code):
            self.cur.execute('SELECT * FROM Inventory WHERE Item_Code = ?',(item_code,))
            item = self.cur.fetchone()
            
            return item

    def search(self,item_code ,quantity, price):
        query = 'SELECT * FROM Inventory WHERE 1=1 '
        entrys = []

        if item_code:
            query += 'AND Item_Code = ? '
            entrys.append(item_code)
                
        if quantity:
            query += 'AND Quantity = ? '
            entrys.append(quantity)

        if price:
            query += 'AND Price = ? '
            entrys.append(price)
                
        self.cur.execute(query, tuple(entrys))
        records = self.cur.fetchall()
        return records