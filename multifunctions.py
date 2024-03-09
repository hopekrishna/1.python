class multifunction():
            def subfields():
                    print("sub-fields in AI are:") 
                    list=["Machine Learning","Neural Network","vision","Robotics","Speech Processing","Natural Language Processing"]
                    for temp in list:
                        print(temp)
             

            def oddEven():
                num=int(input("Enter a Number:"))
                if(num%2==0):
                     print(num,"is Even Number")
                     msg="Even Number"
                else:
                     print(num,"is odd Number")
                     msg="Odd Number"
                return msg


            def marriageelg():
                sex=input("Enter ur sex(female,male,f,m):")
                age=int(input("Enter ur age:"))
                if(sex.lower()in("female","f")):
                    if(age>=18):
                        print("Eligible")
                    else:
                        print("Not Eligible")
                elif(sex.lower()in("male","m")):
                    if(age>=21):
                        print("Eligible")
                    else:
                        print("Not Eligible")        



            def percentage():
                sub1=int(input("subject1:"))
                sub2=int(input("subject2:"))
                sub3=int(input("subject3:"))
                sub4=int(input("subject4:"))
                sub5=int(input("subject5:"))
                total=sub1+sub2+sub3+sub4+sub5
                print("Total:",total)
                per=total/500*100
                percentage=per
                return percentage
            


            def triangle():
                height=int(input("Height:"))
                breadth=int(input("Breadth:"))
                area=(height*breadth)/2
                print("Area of Triangle:",area)
                height1=int(input("Height1:"))
                height2=int(input("Height2:"))
                breadth=int(input("Breadth:"))
                perimeter=height1+height2+breadth
                print("Perimeter of Triangle:",perimeter)

       








 



          
    