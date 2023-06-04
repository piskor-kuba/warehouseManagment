#=======================================TEST DATABASE=======================================#
databaseCorrectUrlParams = "sqlite:///./database/warehouseManagment.db"
databaseIncorrectUrlParams = ["mySql:///./database/warehouseManagment.db", "sqlite:///./database/warehouse.db", "sqlite:///./database/", r'"sqlite:///\./database/warehouseManagment\.db"']

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

#=======================================TEST CRUD=======================================#