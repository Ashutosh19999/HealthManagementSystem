while 1:
    option = 0
    log = 0
    print("\nWelcome to our Health Management System")
    print("Would you like to log or retrieve the medical files.Select the following options:")
    print("1 for Log")
    print("2 for Retrieve")
    print("3-Exit()")
    select = int(input())


    def getdate():
        import datetime
        return datetime.datetime.now()


    # First option
    if select == 1:
        print("Which client would you like to log:")
        print("1-Harry")
        print("2-Rohan")
        print("3-Hammad")
        print("4-exit")
        log = int(input())

        # Harry -Log
        if log == 1:
            print("What would you like to log:'1' for Diet or '2' for  Excercise for Harry?If you want to exit , select '3'")
            option = int(input())
        # Diet
            if option == 1:
             print("Enter the record  in the diet file:")
             diet = str(input())
             f = open("Diet-1.txt", "a")
             f.write(str(getdate()) + '\t')
             f.write(diet+ '\n')
             f.close()
             continue
        # Excercise
            if option == 2:
             print("Enter the record  in the excercise file:")
             excercise = str(input())
             f = open("Excercise-1.txt", "a")
             f.write(str(getdate()) + '\t')
             f.write(excercise+'\n')
             f.close()
             continue

            if option == 3:
             print("Thank you for printing")
             continue

        # Rohan-log
        if log == 2:
            print("What would you like to log:'1' for Diet or '2' for  Excercise for Rohan?If you want to exit , select '3'")
            option = int(input())
        # Diet
            if option == 1:
             print("Enter the record in the diet file:")
             diet = str(input())
             f = open("Diet-2.txt", "a")
             f.write(str(getdate()) + '\t')
             f.write(diet + '\n')
             f.close()
             continue

        # Excercise
            if option == 2:
             print("Enter the record  in the excercise file:")
             excercise = str(input())
             f = open("Excercise-2.txt", "a")
             f.write(str(getdate()) + '\t')
             f.write(excercise+ '\n')
             f.close()
             continue

            if option == 3:
             print("Thank you for printing")
             continue

        # Hammad-log
        if log == 3:
            print("What would you like to log:'1' for Diet or '2' for  Excercise for Hammad?If you want to exit , select '3'")
            option = int(input())
        # Diet
            if option == 1:
             print("Enter the record  in the diet file:")
             diet = str(input())
             f = open("Diet-3.txt", "a")
             f.write(str(getdate()) + '\t')
             f.write(diet+ '\n')
             f.close()
             continue
        # Excercise
            if option == 2:
             print("Enter the record  in the excercise file:")
             excercise = str(input())
             f = open("Excercise-3.txt", "a")
             f.write(str(getdate()) + '\t')
             f.write(excercise + '\n')
             f.close()
             continue

            if option == 3:
             print("Thank you for visiting")
             continue

        if log == 4:
            print("Thank you for visiting!")
            continue
    # Retrieve
    if select == 2:
        print("Which client would you like to retrieve:")
        print("1-Harry")
        print("2-Rohan")
        print("3-Hammad")
        print("4-Exit")
        retrieve = int(input())
        # Harry-retrieve
        if retrieve == 1:
            print("What would you like to retrieve:'1' for Diet or '2' for  Excercise for Harry?If you want to exit , select '3'")
            option = int(input())
            # Diet
            if option == 1:
                f = open("Diet-1.txt", "r")
                v = f.read()
                print(v)
                f.close()
                continue
            # Excercise
            if option == 2:
                f = open("Excercise-1.txt", "r")
                v = f.read()
                print(v)
                f.close()
                continue

            if option == 3:
                print("Thank you for visiting")
                continue
        # Rohan
        if retrieve == 2:
            print("What would you like to retrieve:'1' for Diet or '2' for  Excercise for Rohan?If you want to exit , select '3'")
            option = int(input())
            # Diet
            if option == 1:
                f = open("Diet-2.txt", "r")
                v = f.read()
                print(v)
                f.close()
                continue
            # Excercise
            if option == 2:
                f = open("Excercise-2.txt", "r")
                v = f.read()
                print(v)
                f.close()
                continue

            if option == 3:
                print("Thank you for visiting")
                continue
        # Hammad
        if retrieve == 3:
            print("What would you like to retrieve:'1' for Diet or '2' for  Excercise for Hammad?If you want to exit , select '3'")
            option = int(input())
            # Diet
            if option == 1:
                f = open("Diet-3.txt", "r")
                v = f.read()
                print(v)
                f.close()
                continue
            # Excercise
            if option == 2:
                f = open("Excercise-3.txt", "r")
                v = f.read()
                print(v)
                f.close()
                continue

            if option == 3:
                print("Thank you for visiting")
                continue

        if retrieve == 4:
            print("Thank you for visiting")
            continue

    if select == 3:
        print("Thank you for visiting")
        continue
