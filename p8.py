import numpy as np
class DataAnalytics():
    def __init__(self,number=None):
        self.__number=number
    def get_array(self):
        return self.__number

    def create_1d(self):
        length=int(input("input element length for 1d array"))
        elem=list(map(int,input(f"input the {length} element for araay seperated by space :::").split()))
        arr=np.array(elem)
        self.__number=arr
        print("1D array created succefully....")
        print(arr)
        return arr

    def create_2d(self):
          rows=int(input("enter the number for rows:: "))
          columns=int(input("enter the number for colums::"))
          elem=list(map(int,input(f"input the  {rows*columns}  element for araay seperated by space :::").split()))
          arr=np.array(elem)
          arr2d=arr.reshape(rows,columns)
          self.__number=arr2d
          print("2D array created succefully....")
          print(arr2d)
          return arr2d

    def create_3d(self,):
         layer=int(input("enter the layer for 3d"))
         rows=int(input("enter the number for rows:: "))
         columns=int(input("enter the number for colums::"))
         elem=list(map(int,input(f"input the  {layer*rows*columns}  element for araay seperated by space :::").split()))      
         arr=np.array(elem)
         arr3d=arr.reshape(layer,rows,columns)
         self.__number=arr3d
         print("3D array created succefully....")
         print(arr3d)
         return arr3d
    
n1=DataAnalytics()

print("Welcome to the Numpy Analyzer!!")
while True:
    print("Choose a Option...")
    print("1.Create a Numpy Array")
    print("2.Perform Mathematical Operations")
    print("3.Combine or Split Arrays")
    print("4.Search,Sort,or Filter Arrays")
    print("5.Compute Aggregates and statistics")
    print("6.Exit")

    choice=int(input("Enter your choice ..."))
    match choice:
        case 1:
            
             print("Select the type of Array for Creation")
             print("1.  1D Array")
             print("2.  2D Array")
             print("3.  3D Array")
             choice2=int(input("Enter your choice..."))
             match choice2:
                 case 1:
                      n1.create_1d()
                 case 2:
                      n1.create_2d()
                 case 3:
                     n1.create_3d()
                     
             while True:


                      print("Choose an Operation...")
                      print("1.Idenxing")
                      print("2.Slicing")
                      print("3.Go Back")
                      choice3=int(input("Enter the Choice...."))
                      match choice3:
                       case 1:
                          arr1=n1.get_array()
                          if arr1.ndim==1:
                           index=int(input("enter the index number for serching element in 1d array "))
                           res=arr1[index]
                           print("------------------------------")
                           print(res)
                           print("------------------------------")
                          elif arr1.ndim==2:
                           row=int(input("enter the row index number for element... "))
                           columns=int(input("enter the columns index number for element... "))
                           res=arr1[row,columns]
                           print("------------------------------")
                           print(res)
                           print("------------------------------")
                          else:
                            depth = int(input("Enter depth index: "))
                            row = int(input("Enter row index: "))
                            column = int(input("Enter column index: "))
                            res=arr1[depth, row, column]
                            print("------------------------------")
                            print(res)
                            print("------------------------------")
                       case 2:
                         arr1=n1.get_array()
                         if arr1.ndim==1:
                            range1=int(input("enter the range number for siling the array ::"))
                            range2=int(input("enter the range number for siling the array ::"))
                            print("------------------------------")
                            print(arr1[range1:range2])
                            print("------------------------------")
                         elif arr1.ndim==2:
                             row_start_range=int(input("enter the start row range number for siling the array ::"))
                             row_end_range=int(input("enter the end  row range number for siling the array ::"))
                             column_start_range=int(input("enter the start column range number for siling the array ::"))
                             column_end_range=int(input("enter the end column range number for siling the array ::"))
                             print("------------------------------")
                             print(arr1[row_start_range:row_end_range,column_start_range:column_end_range])
                             print("------------------------------")
                         else:
                             depth_start_range = int(input("Enter the start depth range number for slicing the array :: "))
                             depth_end_range = int(input("Enter the end depth range number for slicing the array :: "))

                             row_start_range = int(input("Enter the start row range number for slicing the array :: "))
                             row_end_range = int(input("Enter the end row range number for slicing the array :: "))

                             column_start_range = int(input("Enter the start column range number for slicing the array :: "))
                             column_end_range = int(input("Enter the end column range number for slicing the array :: "))
                             print("------------------------------")

                             print(arr1[
                                        depth_start_range:depth_end_range,
                                        row_start_range:row_end_range,
                                        column_start_range:column_end_range
                                        ])
                             print("------------------------------")
                             
                       case 3:
                        break

        case 2:
            while True:
             print("Choose a mathematical operation")
             print("1.Addition")
             print("2.Substration")
             print("3.Multiplication")
             print("4.Division")
             print("5.Go Back")
             choice4=int(input("Enter the choice..."))
             match choice4:
                case 1:
                    print("re-enter same-size element (element separeted by space):")
                    arr1=n1.get_array()
                    if n1.get_array().ndim==1:
                        arr2=n1.create_1d()
                    elif n1.get_array().ndim==2:
                        arr2=n1.create_2d()
                    else:
                        arr2=n1.create_3d()
                    res=arr1 + arr2
                    print("------------------------------")
                    print("result of Addition",res)
                    print("------------------------------")
                   
                    
                    
                    

                case 2:
                    print("re-enter same-size element (element separeted by space):")
                    arr1=n1.get_array()
                    if n1.get_array().ndim==1:
                        arr2=n1.create_1d()
                    elif n1.get_array().ndim==2:
                        arr2=n1.create_2d()
                    else:
                        arr2=n1.create_3d()
                    res=arr1 - arr2
                    print("------------------------------")
                    print("result of substration",res)
                    print("------------------------------")
                    
                case 3:
                    print("re-enter same-size element (element separeted by space):")
                    arr1=n1.get_array()
                    if n1.get_array().ndim==1:
                        arr2=n1.create_1d()
                    elif n1.get_array().ndim==2:
                        arr2=n1.create_2d()
                    else:
                        arr2=n1.create_3d()
                    res=arr1 * arr2
                    print("------------------------------")
                    print("result of multiplication",res)
                    print("------------------------------")
                    
                case 4:
                    print("re-enter same-size element (element separeted by space):")
                    arr1=n1.get_array()
                    if n1.get_array().ndim==1:
                        arr2=n1.create_1d()
                    elif n1.get_array().ndim==2:
                        arr2=n1.create_2d()
                    else:
                        arr2=n1.create_3d()
                    res=arr1 / arr2
                    print("------------------------------")
                    print("result of divison",res)
                    print("------------------------------")
                    
                case 5:
                    break
                    
        case 3:
            arr1=n1.get_array()
            print("Choose a Option....")
            print("1.Combine Array")
            print("2.Split Array")
            choice5=int(input('Enter the choice...'))
            match choice5:
                case 1:
                   print("combine tha array by (hstack//vstack)")
                   print("1.hstcak")
                   print("2.vstack")
                   choice8=int(input("enyter the choice"))
                   match choice8:
                        case 1:
                            print("re-enter same-size element (element separeted by space):")
                            arr1=n1.get_array()
                            if n1.get_array().ndim==1:
                                arr2=n1.create_1d()
                            elif n1.get_array().ndim==2:
                                arr2=n1.create_2d()
                            else:
                                arr2=n1.create_3d()
                            print("------------------------------")
                            print("combine bt hstack::",np.hstack((arr1,arr2)))
                            print("------------------------------")
                        case 2:
                             print("re-enter same-size element (element separeted by space):")
                             arr1=n1.get_array()
                             if n1.get_array().ndim==1:
                                arr2=n1.create_1d()
                             elif n1.get_array().ndim==2:
                                arr2=n1.create_2d()
                             else:
                                 arr2=n1.create_3d()
                             print("------------------------------")
                             print("combine bt vstack::",np.vstack((arr1,arr2)))
                             print("------------------------------")
                    
                case 2:
                    print("split tha array by (hsplit//vsplit)")
                    print("1.hsplit")
                    print("2.vsplit")
                    choice8=int(input("enter the choice"))
                    match choice8:
                        case 1:
                         print("re-enter same-size element (element separeted by space):")
                         arr1=n1.get_array()
                         if n1.get_array().ndim==1:
                            arr2=n1.create_1d()
                         elif n1.get_array().ndim==2:
                            arr2=n1.create_2d()
                         else:
                            arr2=n1.create_3d()
                         parts = int(input("Enter number of parts: "))
                         print("------------------------------")
                         print("split bt hsplit::",np.hsplit(arr1,parts))
                         print("------------------------------")
                         
                        case 2:
                             print("re-enter same-size element (element separeted by space):")
                             arr1=n1.get_array()
                             if n1.get_array().ndim==1:
                              arr2=n1.create_1d()
                             elif n1.get_array().ndim==2:
                              arr2=n1.create_2d()
                             else:
                                arr2=n1.create_3d()
                             parts = int(input("Enter number of parts: "))
                             print("------------------------------")
                             print("split by vsplit::",np.vsplit(arr1,parts))
                             print("------------------------------")
                 
                           
        case 4:
            
            print("Choose a Option....")
            print("1.Search a value ")
            print("2.Sort the array")
            print("3.Filter array")
            choice6=int(input("Enter the choice.... "))
            match choice6:
                case 1:
                    arr1=n1.get_array()
                    search_value=int(input("enter the number for serach"))
                    res=np.where(arr1==search_value)
                    print("------------------------------")
                    print("index of search value::",res)
                    print("------------------------------")
                case 2:
                    print("sort the value in ascending and decending order")
                    print("1.Acending")
                    print("2.Decending")
                    choice9=int(input("enter the choice"))
                    match choice9:
                        case 1:
                            arr1=n1.get_array()
                            res=np.sort(arr1)
                            print("------------------------------")
                            print("sorted array in acending order::",res)
                            print("------------------------------")
                        case 2:
                            arr1=n1.get_array()
                            res=np.sort(arr1)[::-1]
                            print("------------------------------")
                            print("sorted array in decending order::",res)
                            print("------------------------------")
                            
                case 3:
                    
                    print("Filter options")
                    print("1. Even numbers")
                    print("2. Odd numbers")
                    print("3.Greater than value")
                    print("4.less than value")
                    

                    choice10 = int(input("Enter the choice: "))

                    match choice10:
                     case 1:
                      arr1=n1.get_array()
                      print("------------------------------")
                      print(arr1[arr1 % 2 == 0])
                      print("------------------------------")

                     case 2:
                      arr1=n1.get_array()
                      print("------------------------------")
                      print(arr1[arr1 % 2 != 0])
                      print("------------------------------")
                     case 3:
                         value = int(input("Enter value: "))
                         print("------------------------------")
                         print(arr1[arr1 > value])
                         print("------------------------------")
                     case 4:
                         value = int(input("Enter value: "))
                         print("------------------------------")
                         print(arr1[arr1 < value])
                         print("------------------------------")

                     
        case 5:
            print("Choose a aggregate/statistics Option....")
            print("1.Sum")
            print("2.Mean")
            print("3.Median")
            print("4.strandard Deviation")
            print("5.Variance")
            choice7=int(input("Enter the choice.... "))
            match choice7:
                case 1:
                    arr1=n1.get_array()
                    print("------------------------------")
                    print("sum of Array::",np.sum(arr1))
                    print("------------------------------")
                case 2:
                    arr1=n1.get_array()
                    print("------------------------------")
                    print("Mean of array::",np.mean(arr1))
                    print("------------------------------")
                case 3:
                    arr1=n1.get_array()
                    print("------------------------------")
                    print("Median of array::",np.median(arr1))
                    print("------------------------------")
                case 4:
                    arr1=n1.get_array()
                    print("------------------------------")
                    print("standard deviation of array::",np.std(arr1))
                    print("------------------------------")
                case 5:
                    arr1=n1.get_array()
                    print("------------------------------")
                    print("Variance of array::",np.var(arr1))
                    print("------------------------------")
                case 6:
                    arr1 = n1.get_array()
                    print("------------------------------")
                    print("Minimum:", np.min(arr1))
                    print("------------------------------")

                case 7:
                    arr1 = n1.get_array()
                    print("------------------------------")
                    print("Maximum:", np.max(arr1))
                    print("------------------------------")
        case 6:
            print("thank you for using this ")
            break
        case _:
            print("invalid input please re-enter ...")

            

                                 

