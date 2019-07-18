if __name__ == '__main__':
    import sys
    print('''
   \033[1;33m###    ##    ## ##     ##    ###    ##    ## 
  ## ##    ##  ##  ###   ###   ## ##   ###   ## 
 ##   ##    ####   #### ####  ##   ##  ####  ## 
##     ##    ##    ## ### ## ##     ## ## ## ## 
#########    ##    ##     ## ######### ##  #### 
##     ##    ##    ##     ## ##     ## ##   ### 
##     ##    ##    ##     ## ##     ## ##    ##
\033[1;36m===============================================\033[1;m
        \033[1;31m
########  ##      ## ##     ## 
##     ## ##  ##  ## ###   ### 
##     ## ##  ##  ## #### #### 
##     ## ##  ##  ## ## ### ## 
##     ## ##  ##  ## ##     ## 
##     ## ##  ##  ## ##     ## 
########   ###  ###  ##     ## \033[34;1m[0]\033[1;32m:\033[35;1m EXIT  
\033[1;36m|==============================================\033[1;36m| 
\033[1;36m|    \033[1;32m check it my facebook :::: \033[35;1m Ayman Belhaj \033[1;36m | 
\033[1;36m|  \033[34;1m   [ DWM FOR LIFE ]  [ HK-G ]    [ TM78 ] \033[34;1m \033[1;36m |  
\033[1;36m|==============================================| ''')
    print("\033[1;31mthis tool it's for the people who want to\033[1;31m ")
    print("\033[1;31mget closer to their point and see their future\033[1;31m")
    print("\033[1;32mnow you are in 1bac\033[1;32m")
    print("\033[34;1m[1]\033[1;32m:\033[35;1mSMB     \033[34;1m[3]\033[1;32m:\033[35;1mPC")
    print("\033[34;1m[2]\033[1;32m:\033[35;1mSMA     \033[34;1m[4]\033[1;32m:\033[35;1mSVT")
    print("\033[34;1m[5]\033[1;32m:\033[35;1mI am in 2bac")
    x = int(input("choose your branch:"))
    #2BAC éxaman nationnal
    if x == 5:
        moyen_de_rejional0 = float(input("your note of rejionnal exam:"))
        moyen_des_semestres = float(input("your note of semesters:"))
        print("\033[1;32mnow you are in 2bac\033[1;32m")
        print("\033[34;1m[1]\033[1;32m:\033[35;1mSMB     \033[34;1m[3]\033[1;32m:\033[35;1mPC")
        print("\033[34;1m[2]\033[1;32m:\033[35;1mSMA     \033[34;1m[4]\033[1;32m:\033[35;1mSVT")
        y = int(input("choose your branche:"))
        if y == 0:
            print("\033[1;36mError please retry the process")
            sys.exit()
        if y != 0 and y != 1 and y != 2 and y != 3 and y != 4 and y != 5:
            print("\033[1;36mError please retry tht process")
            sys.exit()
            print("088\[1;29m")
        else:
            print('''\033[34;1m=============================================== \033[34;1m''')
        if y == 1:
            # 2bac éxaman nationnal SMB
            print('''\033[1;36m''')
            maths = (float(input("note de maths:")) * 9)
            pc = (float(input("note de pc:")) * 7)
            si = (float(input("note se sI:")) * 3)
            philo = (float(input("note de philo:")) * 2)
            anglais = (float(input("note d'anglais:")) * 2)
            moyen_de_nationnale = (maths + pc + si + philo + anglais) / 23
            print((maths / 9), (pc / 7), (si / 3), (philo / 2), (anglais / 2))
            print("\033[1;33mton note d'éxaman nationnale est " + str(moyen_de_nationnale))
            # la moyen général pour entrer à une classs)
            moyen_géneral_re = ((moyen_de_rejional0 * 25) + (moyen_des_semestres * 25) + (moyen_de_nationnale * 50))/100
            moyen_géneral1 = (moyen_de_rejional0 + (moyen_de_nationnale * 3)) / 4
            print("\033[1;33mton moyen générale est " + str(moyen_géneral_re))
            print("\033[1;33mton moyen d'acceptabilité dans les écoles est " + str(moyen_géneral1))
        elif y == 2:
            # 2bac éxaman nationnal SMA
            print('''\033[1;36m''')
            maths = (float(input("note de maths:")) * 9)
            pc = (float(input("note de pc:")) * 7)
            svt = (float(input("note se svt:")) * 3)
            philo = (float(input("note de philo:")) * 2)
            anglais = (float(input("note d'anglais:")) * 2)
            moyen_de_nationnale = (maths + pc + svt + philo + anglais) / 23
            print((maths / 9), (pc / 7), (svt / 3), (philo / 2), (anglais / 2))
            print("\033[1;33mton moyen d'éxaman nationnal est " + str(moyen_de_nationnale))
            # la moyen général pour entrer à une classs)
            moyen_géneral_re = ((moyen_de_rejional0 * 25) + (moyen_des_semestres * 25) + ( moyen_de_nationnale * 50)) / 100
            moyen_géneral1 = (moyen_de_rejional0 + (moyen_de_nationnale * 3)) / 4
            print("\033[1;33mton moyen générale est " + str(moyen_géneral_re))
            print("\033[1;33mton moyen d'acceptabilité dans les écoles est " + str(moyen_géneral1))
            # les seuil des écoles pour sm
        ENSA = 12
        ENCG = 14.5
        ENSAM = 14.5
        MEDECIN = 15
        DENTISTE = 16
        ingénieurie = 15
        if y == 1 or y == 2:
            # acceptabiliter pour les écoles
            print('''\033[35;1m=============================================== \033[35;1m''')
            print('''\033[34;1m''')
            if moyen_géneral1 >= ingénieurie:
                print("tu es accepter dans l'ingénieurie")
            else:
                print("à la prochaine pour l'ingénieurie")
            if moyen_géneral1 >= MEDECIN:
                print("tu es accepter dans la médecine")
            else:
                print("à la prochaine pour la médcine")
            if moyen_géneral1 >= DENTISTE:
                print("tu es accepter dans la dentiste")
            else:
                print("à la prochaine pour la dentiste")
            if moyen_géneral1 >= ENSAM:
                print("tu es accepter dans l'ensam")
            else:
                print("à la prochaine pour l'ensam")
            if moyen_géneral1 >= ENSA:
                print("tu es accepter dans l'ensa")
            else:
                print("à la prochaine pour l'ensa")
            if moyen_géneral1 >= ENCG:
                print("tu es accepter dans l'encg")
            else:
                print("à la prochaine pour l'encg")
            print("NB: les seuil par rapport à l'anné 2018")
            print("Good Bye")
            sys.exit()
        elif y == 3:
            # 2bac éxaman nationnal pc
            print('''\033[1;36m''')
            maths = (float(input("note de maths:")) * 7)
            pc = (float(input("note de pc:")) * 7)
            svt = (float(input("note se svt:")) * 5)
            philo = (float(input("note de philo:")) * 2)
            anglais = (float(input("note d'anglais:")) * 2)
            moyen_de_nationnale = (maths + pc + svt + philo + anglais) / 23
            print((maths / 7), (pc / 7), (svt / 5), (philo / 2), (anglais / 2))
            print("\033[1;33mton moyen d'éxaman nationnal est " + str(moyen_de_nationnale))
            # la moyen général pour entrer à une classs)
            moyen_géneral_re = ((moyen_de_rejional0 * 25) + (moyen_des_semestres * 25) + ( moyen_de_nationnale * 50)) / 100
            moyen_géneral2 = (moyen_de_rejional0 + (moyen_de_nationnale * 3)) / 4
            print("\033[1;33mton moyen générale est " + str(moyen_géneral_re))
            print("\033[1;33mton moyen d'acceptabilité dans les écoles est " + str(moyen_géneral2))
            # les seuil des écoles pour spc
        ENSA = 15.4
        ENCG = 15.5
        ENSAM = 16.8
        MEDECIN = 17
        DENTISTE = 16
        ingénieurie = 17
        if y == 3:
            # acceptabiliter pour les écoles
            print('''\033[35;1m=============================================== \033[35;1m''')
            print('''\033[34;1m''')
            if moyen_géneral2 >= ingénieurie:
                print("tu es accepter dans l'ingénieurie")
            else:
                print("à la prochaine pour l'ingénieurie")
            if moyen_géneral2 >= MEDECIN:
                print("tu es accepter dans la médecine")
            else:
                print("à la prochaine pour la médcine")
            if moyen_géneral2 >= DENTISTE:
                print("tu es accepter dans la dentiste")
            else:
                print("à la prochaine pour la dentiste")
            if moyen_géneral2 >= ENSAM:
                print("tu es accepter dans l'ensam")
            else:
                print("à la prochaine pour l'ensam")
            if moyen_géneral2 >= ENSA:
                print("tu es accepter dans l'ensa")
            else:
                print("à la prochaine pour l'ensa")
            if moyen_géneral2 >= ENCG:
                print("tu es accepter dans l'encg")
            else:
                print("à la prochaine pour l'encg")
            print("NB: les seuil par rapport à l'anné 2018")
            print("Good Bye")
            sys.exit()
        elif y == 4:
            # 2bac éxaman nationnal SVT
            print('''\033[1;36m''')
            maths = (float(input("note de maths:")) * 7)
            pc = (float(input("note de pc:")) * 5)
            svt = (float(input("note se svt:")) * 7)
            philo = (float(input("note de philo:")) * 2)
            anglais = (float(input("note d'anglais:")) * 2)
            moyen_de_nationnale = (maths + pc + svt + philo + anglais) / 23
            print((maths / 7), (pc / 5), (svt / 7), (philo / 2), (anglais / 2))
            print("\033[1;33mton moyen d'éxaman nationnal est " + str(moyen_de_nationnale))
            # la moyen général pour entrer à une classs)
            moyen_géneral_re = ((moyen_de_rejional0 * 25) + (moyen_des_semestres * 25) + ( moyen_de_nationnale * 50)) / 100
            moyen_géneral3 = (moyen_de_rejional0 + (moyen_de_nationnale * 3)) / 4
            # les seuil des écoles pour spc
            print("\033[1;33mton moyen générale est " + str(moyen_géneral_re))
            print("\033[1;33mton moyen d'acceptabilité dans les écoles est " + str(moyen_géneral3))
            ENSA = 16.5
            ENCG = 15.6
            ENSAM = 16.80
            MEDECIN = 16
            DENTISTE = 16
            if y == 4:
                # acceptabiliter pour les écoles
                print('''\033[35;1m=============================================== \033[35;1m''')
                print('''\033[34;1m''')
                if moyen_géneral3 >= ingénieurie:
                    print("tu es accepter dans l'ingénieurie")
                else:
                    print("à la prochaine pour l'ingénieurie")
                if moyen_géneral3 >= MEDECIN:
                    print("tu es accepter dans la médecine")
                else:
                    print("à la prochaine pour la médcine")
                if moyen_géneral3 >= DENTISTE:
                    print("tu es accepter dans la dentiste")
                else:
                    print("à la prochaine pour la dentiste")
                if moyen_géneral3 >= ENSAM:
                    print("tu es accepter dans l'ensam")
                else:
                    print("à la prochaine pour l'ensam")
                if moyen_géneral3 >= ENSA:
                    print("tu es accepter dans l'ensa")
                else:
                    print("à la prochaine pour l'ensa")
                if moyen_géneral3 >= ENCG:
                    print("tu es accepter dans l'encg")
                else:
                    print("à la prochaine pour l'encg")
                print("NB: les seuil par rapport à l'anné 2018")
                print("Good Bye")
                sys.exit()
    elif x == 0:
        print("\033[1;36mGood Bye")
        sys.exit()
    if x!= 0 and x != 1 and x != 2 and x != 3 and x != 4 and x != 5:
        print("\033[1;36mError please retry tht process")
        sys.exit()
         # 1bac éxaman réjonnal
    elif x == 1 or x == 2 or x == 3 or x == 4:
     print('''\033[34;1m=============================================== \033[34;1m''')
     print('''\033[1;36m''')
     francais = float(input("note de francais:")) * 2
     arabe = float(input("note d'arabe:"))
     eis = float(input("note de eis:"))
     hg = float(input("note de hg:"))
     moyen_de_rejional = (francais + arabe + eis + hg) / 5
     print((francais / 2), arabe, eis, hg)
     print("\033[1;33mton note d'éxaman réjonnal est " + str(moyen_de_rejional))
     moyen_des_semestres = float(input("your note of semesters:"))
     print('''\033[1;31m=============================================== \033[1;31m''')
if x == 1:
    # 2bac éxaman nationnal SMB
    print('''\033[1;36m''')
    maths = (float(input("note de maths:")) * 9)
    pc = (float(input("note de pc:")) * 7)
    si = (float(input("note se sI:")) * 3)
    philo = (float(input("note de philo:")) * 2)
    anglais = (float(input("note d'anglais:")) * 2)
    moyen_de_nationnale = (maths + pc + si + philo + anglais) / 23
    print((maths / 9), (pc / 7), (si / 3), (philo / 2), (anglais / 2))
    # la moyen général pour entrer à une classs)
    moyen_géneral_re = ((moyen_de_rejional * 25) + (moyen_des_semestres * 25) + (moyen_de_nationnale * 50)) / 100
    moyen_géneral1 = (moyen_de_rejional + (moyen_de_nationnale * 3)) / 4
    print("\033[1;33mton moyen générale est " + str(moyen_géneral_re))
    print("\033[1;33mton moyen d'acceptabilité dans les écoles est " + str(moyen_géneral1))
elif x == 2:
    # 2bac éxaman nationnal SMA
    print('''\033[1;36m''')
    maths = (float(input("note de maths:")) * 9)
    pc = (float(input("note de pc:")) * 7)
    svt = (float(input("note se svt:")) * 3)
    philo = (float(input("note de philo:")) * 2)
    anglais = (float(input("note d'anglais:")) * 2)
    moyen_de_nationnale = (maths + pc + svt + philo + anglais) / 23
    print((maths / 9), (pc / 7), (svt / 3), (philo / 2), (anglais / 2))
    print("\033[1;33mton moyen d'éxaman nationnal est " + str(moyen_de_nationnale))
    # la moyen général pour entrer à une classs
    moyen_géneral_re = ((moyen_de_rejional * 25) + (moyen_des_semestres * 25) + (moyen_de_nationnale * 50)) / 100
    moyen_géneral1 = (moyen_de_rejional + (moyen_de_nationnale * 3)) / 4
    print("\033[1;33mton moyen générale est " + str(moyen_géneral_re))
    print("\033[1;33mton moyen d'acceptabilité dans les écoles est " + str(moyen_géneral1))
    #les seuil des écoles pour sm
ENSA = 12
ENCG = 14.5
ENSAM = 14.5
MEDECIN = 15
DENTISTE = 16
ingénieurie = 15
if x == 1 or x == 2:
    # acceptabiliter pour les écoles
    print('''\033[35;1m=============================================== \033[35;1m''')
    print('''\033[34;1m''')
    if moyen_géneral1 >= ingénieurie:
        print("tu es accepter dans l'ingénieurie")
    else:
        print("à la prochaine pour l'ingénieurie")
    if moyen_géneral1 >= MEDECIN:
        print("tu es accepter dans la médecine")
    else:
        print("à la prochaine pour la médcine")
    if moyen_géneral1 >= DENTISTE:
        print("tu es accepter dans la dentiste")
    else:
        print("à la prochaine pour la dentiste")
    if moyen_géneral1 >= ENSAM:
        print("tu es accepter dans l'ensam")
    else:
        print("à la prochaine pour l'ensam")
    if moyen_géneral1 >= ENSA:
        print("tu es accepter dans l'ensa")
    else:
        print("à la prochaine pour l'ensa")
    if moyen_géneral1 >= ENCG:
        print("tu es accepter dans l'encg")
    else:
        print("à la prochaine pour l'encg")
    print("NB: les seuil par rapport à l'anné 2018")
    print("Good Bye")
    sys.exit()
elif x == 3:
    # 2bac éxaman nationnal pc
    print('''\033[1;36m''')
    maths = (float(input("note de maths:")) * 7)
    pc = (float(input("note de pc:")) * 7)
    svt = (float(input("note se svt:")) * 5)
    philo = (float(input("note de philo:")) * 2)
    anglais = (float(input("note d'anglais:")) * 2)
    moyen_de_nationnale = (maths + pc + svt + philo + anglais) / 23
    print((maths / 7), (pc / 7), (svt / 5), (philo / 2), (anglais / 2))
    # la moyen général pour entrer à une classs)
    moyen_géneral_re = ((moyen_de_rejional * 25) + (moyen_des_semestres * 25) + (moyen_de_nationnale * 50)) / 100
    moyen_géneral2 = (moyen_de_rejional + (moyen_de_nationnale * 3)) / 4
    print("\033[1;33mton moyen générale est " + str(moyen_géneral_re))
    print("\033[1;33mton moyen d'acceptabilité dans les écoles est " + str(moyen_géneral2))
    # les seuil des écoles pour spc
ENSA = 15.4
ENCG = 15.5
ENSAM = 16.8
MEDECIN = 17
DENTISTE = 16
ingénieurie = 17
if x == 3:
        # acceptabiliter pour les écoles
        print('''\033[35;1m=============================================== \033[35;1m''')
        print('''\033[34;1m''')
        if moyen_géneral2 >= ingénieurie:
            print("tu es accepter dans l'ingénieurie")
        else:
            print("à la prochaine pour l'ingénieurie")
        if moyen_géneral2 >= MEDECIN:
            print("tu es accepter dans la médecine")
        else:
            print("à la prochaine pour la médcine")
        if moyen_géneral2 >= DENTISTE:
            print("tu es accepter dans la dentiste")
        else:
            print("à la prochaine pour la dentiste")
        if moyen_géneral2 >= ENSAM:
            print("tu es accepter dans l'ensam")
        else:
            print("à la prochaine pour l'ensam")
        if moyen_géneral2 >= ENSA:
            print("tu es accepter dans l'ensa")
        else:
            print("à la prochaine pour l'ensa")
        if moyen_géneral2 >= ENCG:
            print("tu es accepter dans l'encg")
        else:
            print("à la prochaine pour l'encg")
        print("NB: les seuil par rapport à l'anné 2018")
        print("Good Bye")
        sys.exit()
elif x == 4:
    # 2bac éxaman nationnal SVT
    print('''\033[1;36m''')
    maths = (float(input("note de maths:")) * 7)
    pc = (float(input("note de pc:")) * 5)
    svt = (float(input("note se svt:")) * 7)
    philo = (float(input("note de philo:")) * 2)
    anglais = (float(input("note d'anglais:")) * 2)
    moyen_de_nationnale = (maths + pc + svt + philo + anglais) / 23
    print((maths / 7), (pc / 5), (svt / 7), (philo / 2), (anglais / 2))
    # la moyen général pour entrer à une classs)
    moyen_géneral_re = ((moyen_de_rejional * 25) + (moyen_des_semestres * 25) + (moyen_de_nationnale * 50)) / 100
    moyen_géneral3 = (moyen_de_rejional + (moyen_de_nationnale * 3)) / 4
    print("\033[1;33mton moyen générale est " + str(moyen_géneral_re))
    print("\033[1;33mton moyen d'acceptabilité dans les écoles est " + str(moyen_géneral3))
    # les seuil des écoles pour spc
    ENSA = 16.5
    ENCG = 15.6
    ENSAM = 16.80
    MEDECIN = 16
    DENTISTE = 16
    if x == 4:
        # acceptabiliter pour les écoles
        print('''\033[35;1m=============================================== \033[35;1m''')
        print('''\033[34;1m''')
        if moyen_géneral3 >= MEDECIN:
            print("tu es accepter dans la médecine")
        else:
            print("à la prochaine pour la médcine")
        if moyen_géneral3 >= DENTISTE:
            print("tu es accepter dans la dentiste")
        else:
            print("à la prochaine pour la dentiste")
        if moyen_géneral3 >= ENSAM:
            print("tu es accepter dans l'ensam")
        else:
            print("à la prochaine pour l'ensam")
        if moyen_géneral3 >= ENSA:
            print("tu es accepter dans l'ensa")
        else:
            print("à la prochaine pour l'ensa")
        if moyen_géneral3 >= ENCG:
            print("tu es accepter dans l'encg")
        else:
            print("à la prochaine pour l'encg")
        print("NB: les seuil par rapport à l'anné 2018")
        print("Good Bye")
        sys.exit()
