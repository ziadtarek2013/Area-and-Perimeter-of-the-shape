import turtle
print("Welcome to shapes program.")
print("You must choose 1 shape from the 4 shapes.")
print("and these shapes are..Square,Triangle,Rhombus,Circle,Rectangle")
shapes=["Square","Triangle","Rectangle","Rhombus","Circle"]
while(1):
 Shape=input("Enter the shape:")

 if(Shape=="Square"):
     Side_Length=int(input("Enter Length:"))
     Perimeter_S=Side_Length*4
     Area_S=Side_Length*Side_Length
     print("The Perimeter of Square = %d" %Perimeter_S ,"cm")
     print("The Area of Square = %d" %Area_S ,"cm^2")

     s=turtle.getscreen()
     zizo=turtle.Turtle()
     zizo.forward(Side_Length)
     zizo.right(90)
     zizo.forward(Side_Length)
     zizo.right(90)
     zizo.forward(Side_Length)
     zizo.right(90)
     zizo.home()

     

 elif(Shape=="Rectangle"):
     Length_R=int(input("Enter Length:"))
     Width=int(input("Enter Width"))
     Perimeter_R=(Length_R+Width)*2
     Area_R=Length_R*Width
     print("The Perimeter of Rectangle = %d" %Perimeter_R ,"cm")
     print("The Area of Rectangle = %d" %Area_R ,"cm^2")



 elif(Shape=="Triangle"):
     Length1=int(input("Enter Length1:"))
     Length2=int(input("Enter Length2:"))
     Length3=int(input("Enter Length3:"))
     base=int(input("Enter Base:"))
     height=int(input("Enter Height:"))
     Perimeter_T=Length1+Length2+Length3;
     Area_T=1/2*base*height;
     print("The Primeter of Triangle = %d" %Perimeter_T)
     print("The Area of Triangle = %d" %Area_T)



 elif(Shape=="Rhombus"):
     Side_Length=int(input("Enter Length:"))
     height=int(input("Enter Height:"))
     base=int(input("Enter Base:"))
     Perimeter_Rh=Side_Length*4
     Area_Rh=height*base;
     print("The Perimeter of Rhombus = %d" %Perimeter_Rh ,"cm")
     print("The Area of Rhombus = %d" %Area_Rh ,"cm^2")



 elif(Shape=="Circle"):
      r= int(input("Enter the radius"))
      pi= 22/7
      cir= 2*pi*r
      print("The circomfrence is",cir)



 else:
    print("Enter again!")
