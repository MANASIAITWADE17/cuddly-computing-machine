from datetime import datetime,timedelta
class current_time:
    def cur_time(self):
        self.cur_time=datetime.now()
        return(cur_time)
class bread_baking_time:
    def baking_time(self):
        print("1 sweet bread")
        print("2 pizza base bread")
        print("3 french bread")
        print("4 italian bread")
        print("5 ginger_garlic bread")
        ch=int(input("enter your choice"))
        if (ch==1):
            self.b=1
            print("the time required to bake sweet pound bread is=",b)
            return(b)
        elif (ch==2):
            self.b=2
            print("the time required to bake pizza base bread is=",b)
            return(b)
        elif (ch==3):
            self.b=3
            print("the time required to bake french bread is=",b)
            return(b)
        elif (ch==4):
            self.b=4
            print("the time required to bake italian bread is=",b)
            return(b)
        elif (ch==5):
            self.b=5
            print("the time required to bake g_g bread is=",b)
            return(b)
        else:
            return(0)
class all_methods:
    def add_time(ob1,self,b):
        time_required=datetime.datetime.now()+timedelta(hours=b)
        return(time_required)
    def print_time(ob1,ob2,ob3):
        print("current_time",datetime.now())
        b=ob2.baking_time()
        print("baking time",b)
        print("the bread will be ready at",ob3.add_time(ob1,b))


ob1=current_time()
ob2=bread_baking_time()
ob3=all_methods()
ob3.print_time(ob1,ob2,ob3)
             
              

        
                  
                  
