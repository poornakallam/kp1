# score=int("70")
# if score>=90:
#    print("score" + "is an A.") 
# else:
#     if score>=80:
#        print("score" + "is a B.")
#     else:
#         if score>=70:
#            print(str(score) + "is a C.")
#         else:
#             print("score" + "is a D.")

student=90
university=yes

if student>=90:
   if university==yes:
      print("eligible for this university due to secured" +  str(student) + "%")
   else:
          print("not eligible for this university who secured below 90%")
else:
    print("student seccured below 80%")