class Time :
    def __init__(self,a=0,b=0,c=0):
        self.d = 0
        self .set ( a ,b, c )
        
        
    def get (self):
        while True:            
            try:                  
                self.h=int(input("enter hour   :   "))
                while self.h > 23 :
                     self.h=int(input("enter hour   :   "))
             
                self.m=int(input("enter minute :   "))
                while self.m > 60 :
                     self.m=int(input("enter minute   :   "))
            
                self.s=int(input("enter second :   "))
                while self.s > 60 :
                     self.s=int(input("enter second   :   "))
                break
            except ValueError:
                 print ('error')
              
    def set( self , a=0 , b=0 , c=0 ):
        self.d = 0
        self.h = a
        self.m = b
        self.s = c
        
        self.m += self.s // 60
        self.s %= 60
        
        self.h += self.m // 60
        self.m %= 60
        
        self.d += self.h // 24
        self.h %= 24
        
               
    def __str__ (self):
        return (f"{self.h}:{self.m}:{self.s}")         
           
    def show ( self ):
        if self.d > 0 :
            print ( self.d  , end = " Day ")
        print (self.h , self.m , self.s , sep = ":",end='') 

    def t_to_s ( self ) :
        return ( self.s +  self.m*60  + self.h*3600 + self.d*86400 )

    def __add__ ( self , a ) :
        x = self.t_to_s() + a.t_to_s()
        temp = Time()
        temp.set( 0 , 0 , x )
        return temp
    
    def __sub__ ( self , a ) : 
        return Time( 0 , 0 ,  self.t_to_s() - a.t_to_s())
      
    def __lt__( self ,  a ) :
        return  (self.t_to_s()<  a.t_to_s() )
        
                    

