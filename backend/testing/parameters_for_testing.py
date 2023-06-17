#=======================================TEST TABLE_MODEL=======================================#
tableModelIncorrectTypeParamsForCategory = [100, 24.5, ['a','b'], ("String",),False]
tableModelIncorrectTypeParamsForProductWithoutDescribe = [(None,100),(2.5,"Name"),("id",("String",)),(True,None),(10,[]),(object,False),]
tableModelIncorrectTypeParamsForProductWithDescribe = [(None,100,None),(2.5,"Name",False),("id",("String",),str),(True,None,"Describe"),(10,[],10.5),(object,False,100_000_000)]
tableModelCorrectTypeParamsForProductAmount = [(1,1_00),(00,1465),(1_0,0)]
tableModelIncorrectTypeParamsForProductAmount = [("1","1_00"),("23",1465),(int,int)]
tableModelIncorrectTypeParamsForPersons = [
    ("","","",""),
    (0,"Kowalski","123-123-123","Kielce"),
    ("Jan",0,"123123","Kielce"),
    ("Jan","Kowalski",123123,"Kielce"),
    ("Jan","Kowalski","123-123-123",None),
    ("Jan","Kowalski",123-123-123,None),
    (str,object,str,False),
    (("Jan",),str,int,False),
]
tableModelIncorrectTypeParamsForClients = [("0","20"),("a",10_0),(1_0,int)]
tableModelIncorrectTypeParamsForWorkplaceAndRole = [0,str,False,None,object,{}]
tableModelIncorrectTypeParamsForEmployees = [("1","100",2),(00,1465,""),("X","Y","Z"),(10,int,10),(False,True,False)]
tableModelIncorrectTypeParamsForLoginData = [(100,"100",100),(None,1465,True),("X@login.pl","Yyyy",None),(str,str,bool),(False,True,False)]
tableModelIncorrectTypeParamsForOtp = [("0",123123),("login",None),(None,str),(False,False)]

#=======================================TEST ENDPOINTS=======================================#

readCategoryData = [{'name': 'Electronics', 'id': 1}, {'name': 'Books', 'id': 2}, {'name': 'Clothing', 'id': 3}, {'name': 'Home and Garden', 'id': 4}, {'name': 'Beauty', 'id': 5}]
readCategoryDataById = {'name': 'Books', 'id': 2}
createCategoryData = [{'name':'Test'}, {'name':'Test with id','id':7}]
updateCategoryData = {'name':'Test'}

readProductData = [{'category': 'Electronics', 'product_name': 'Smartphone', 'describe': 'Lorem ipsum dolor sit amet.', 'product_id': 1}, {'category': 'Electronics', 'product_name': 'Laptop', 'describe': 'Lorem ipsum dolor sit amet.', 'product_id': 2}, {'category': 'Books', 'product_name': '1984', 'describe': 'Lorem ipsum dolor sit amet.', 'product_id': 3}, {'category': 'Books', 'product_name': 'To Kill a Mockingbird', 'describe': 'Lorem ipsum dolor sit amet.', 'product_id': 4}, {'category': 'Clothing', 'product_name': 'T-Shirt', 'describe': 'Lorem ipsum dolor sit amet.', 'product_id': 5}, {'category': 'Clothing', 'product_name': 'Jeans', 'describe': 'Lorem ipsum dolor sit amet.', 'product_id': 6}, {'category': 'Home and Garden', 'product_name': 'Furniture Set', 'describe': 'Lorem ipsum dolor sit amet.', 'product_id': 7}, {'category': 'Beauty', 'product_name': 'Perfume', 'describe': 'Lorem ipsum dolor sit amet.', 'product_id': 9}, {'category': 'Beauty', 'product_name': 'Makeup Kit', 'describe': 'Lorem ipsum dolor sit amet.', 'product_id': 10}]
readProductDataById = {'category': 'Books', 'product_name': 'To Kill a Mockingbird', 'describe': 'Lorem ipsum dolor sit amet.', 'product_id': 4}
createProductData = [{'id_category': 1, 'name': 'Iphone', 'describe': 'Lorem ipsum dolor sit amet.', 'amount':15},{'id_category': 3, 'name': 'Hat', 'describe': 'Lorem ipsum dolor sit amet.', 'amount':150}]
updateProductData = {'id_product':1,'amount':15}

readPersonData = [{'name': 'John', 'surname': 'Doe', 'phone': '123456789', 'address': '123 Main St.', 'id': 1}, {'name': 'Jane', 'surname': 'Doe', 'phone': '987654321', 'address': '456 High St.', 'id': 2}, {'name': 'Bob', 'surname': 'Smith', 'phone': '555123456', 'address': '789 Elm St.', 'id': 3}, {'name': 'Alice', 'surname': 'Jones', 'phone': '888999000', 'address': '1010 Oak Ave.', 'id': 4}, {'name': 'Chris', 'surname': 'Brown', 'phone': '111222333', 'address': '1313 Maple St.', 'id': 5}, {'name': 'David', 'surname': 'Johnson', 'phone': '777888999', 'address': '1414 Cedar St.', 'id': 6}, {'name': 'Lisa', 'surname': 'Davis', 'phone': '444555666', 'address': '1515 Birch Ave.', 'id': 7}, {'name': 'Michael', 'surname': 'Garcia', 'phone': '222333444', 'address': '1616 Oak St.', 'id': 8}, {'name': 'Karen', 'surname': 'Wilson', 'phone': '999000111', 'address': '1717 Maple Ave.', 'id': 9}, {'name': 'Robert', 'surname': 'Anderson', 'phone': '666777888', 'address': '1818 Elm St.', 'id': 10}]
readPersonByIdData = {'name': 'John', 'surname': 'Doe', 'phone': '123456789', 'address': '123 Main St.', 'id': 1}
createPersonData = {'name': 'Test', 'surname': 'testowy', 'phone': '098765432', 'address': 'No kielce'}

readEmployeeData = [{'Name': 'David Johnson', 'Workplace': 'Biuro Główne', 'Role': 'Manager', 'Employee_id': 1}, {'Name': 'Lisa Davis', 'Workplace': 'Biuro Główne', 'Role': 'Pracownik', 'Employee_id': 2}, {'Name': 'Michael Garcia', 'Workplace': 'Oddział 1', 'Role': 'Asystent', 'Employee_id': 3}, {'Name': 'Karen Wilson', 'Workplace': 'Oddział 1', 'Role': 'Pracownik', 'Employee_id': 4}, {'Name': 'Robert Anderson', 'Workplace': 'Magazyn', 'Role': 'Manager', 'Employee_id': 5}]
readEmployeeByIdData = {'Name': 'Michael Garcia', 'Workplace': 'Oddział 1', 'Role': 'Asystent', 'Employee_id': 3}
createEmployeeData = {'id_persons':5,'id_workplace':1,'id_role':2}
updateEmployeeData = {'id_persons':2,'id_workplace':2,'id_role':1}

readRoleData = [{'name': 'Manager', 'id': 1}, {'name': 'Pracownik', 'id': 2}, {'name': 'Asystent', 'id': 3}]
readRoleByIdData = {'name': 'Manager', 'id': 1}
createAndUpdateRoleData = {'name': 'Rektor'}

readUser = 'test@test.pl'
createUserData = {'login':'test2@test.pl','password':'test','id_employee':2}
otpCodeData = {'username':'test@test.pl','password':'qwerty'}
tokenData = {'username':'test@test.pl','password':'qwerty', "client_secret": '000000' }
