if __name__ == '__main__':
    import sys
    import webbrowser
    print('''   \033[1;33m###    ##    ## ##     ##    ###    ##    ## 
  ## ##    ##  ##  ###   ###   ## ##   ###   ## 
 ##   ##    ####   #### ####  ##   ##  ####  ## 
##     ##    ##    ## ### ## ##     ## ## ## ## 
#########    ##    ##     ## ######### ##  #### 
##     ##    ##    ##     ## ##     ## ##   ### 
##     ##    ##    ##     ## ##     ## ##    ##
\033[1;36m===============================================\033[1;m \033[1;31m
########  ##      ## ##     ## 
##     ## ##  ##  ## ###   ### 
##     ## ##  ##  ## #### #### 
##     ## ##  ##  ## ## ### ## 
##     ## ##  ##  ## ##     ## 
##     ## ##  ##  ## ##     ## 
########   ###  ###  ##     ## \033[34;1m[0]\033[1;32m:\033[35;1m EXIT
\033[1;33m[\033[34;1m*\033[1;33m]\033[1;31mWelcom on\033[35;1m{\033[1;32mtool-pr\033[35;1m}\033[1;31m Programmable by[\033[34;1mAyman Belhaj\033[1;31m]
\033[34;1m[10]\033[1;32m:\033[35;1m Follow my account {\033[1;31mfacebook\033[35;1m}
\033[34;1m[20]\033[1;32m:\033[35;1m Follow my account on {\033[1;32mgithub\033[35;1m}
\033[34;1m[30]\033[1;32m:\033[35;1m Follow my account on {\033[1;33minstagram\033[35;1m}
\033[34;1m[\033[1;32m7777\033[34;1m]\033[1;32m:\033[35;1m Follow The officiel page of\033[1;31m DEEP WEB MAROC\033[35;1m in fb
\033[1;36m|==============================================\033[1;36m| 
\033[1;36m|  \033[1;33m       thanks for the best groups:          \033[1;36m| 
\033[1;36m|  \033[34;1m [ DWM +18 ] [ HK-G ] [ TM78 ] [MCT] [MKT] \033[1;36m |  
\033[1;36m|==============================================| ''')
    print("\033[1;31mthis tool it's for the people who want to\033[1;31m ")
    print("\033[1;31mget closer to their goals and see their future\033[1;31m")
    print("\033[1;32mnow you are in 1bac\033[1;32m")
    print("\033[34;1m[1]\033[1;32m:\033[35;1mSMB     \033[34;1m[3]\033[1;32m:\033[35;1mPC")
    print("\033[34;1m[2]\033[1;32m:\033[35;1mSMA     \033[34;1m[4]\033[1;32m:\033[35;1mSVT")
    print("\033[34;1m[5]\033[1;32m:\033[35;1mI am in 2bac")
    x = int(input("choose ==>"))
    #my accounts
    def open_my_facebook_account():
        webbrowser.open_new("https://www.facebook.com/ayman.belhaj.10")
        print("\033[1;31mthanks for visiting my facebook account \n\033[1;32mGood Bye\033[1;32m")
    def open_my_github_account():
        webbrowser.open_new("https://github.com/ayman1902")
        print("\033[1;31mthanks for visiting my github account \n\033[1;32mGood Bye\033[1;32m")
    def open_my_instagram_account():
        webbrowser.open_new("https://www.instagram.com/ayman.bell.10/")
        print("\033[1;31mthanks for visiting my instagram account \n\033[1;32mGood Bye\033[1;32m")
    def open_the_officiel_page_of_DWM_in_fb():
        webbrowser.open_new("https://www.facebook.com/dwebmaroc/")
        print("\033[1;31mthanks for visiting the officiel page of DWM in fb \n\033[1;32mGood Bye\033[1;32m")
    if x == 10:
        open_my_facebook_account()
    if x == 20:
        open_my_github_account()
    if x == 30:
        open_my_instagram_account()
    if x == 7777:
        open_the_officiel_page_of_DWM_in_fb()
    #2BAC éxaman nationnal
    if x == 5:
        moyen_de_rejional0 = float(input("your note of rejionnal exam:"))
        moyen_des_semestres = float(input("your note of semesters:"))
        print("\033[1;32mnow you are in 2bac\033[1;32m")
        print("\033[34;1m[1]\033[1;32m:\033[35;1mSMB     \033[34;1m[3]\033[1;32m:\033[35;1mPC")
        print("\033[34;1m[2]\033[1;32m:\033[35;1mSMA     \033[34;1m[4]\033[1;32m:\033[35;1mSVT")
        y = int(input("choose ==>"))
        if y == 0:
            print("\033[1;36mError please retry the process")
            sys.exit()
        if y != 0 and y != 1 and y != 2 and y != 3 and y != 4 :
            print("\033[1;36mError please retry the process")
            sys.exit()
        else:
            print('''\033[34;1m=============================================== \033[1;36m''')
        if y == 1:
            # 2bac éxaman nationnal SMB
            maths = (float(input("note de maths:")) * 9)
            pc = (float(input("note de pc:")) * 7)
            si = (float(input("note se sI:")) * 3)
            philo = (float(input("note de philo:")) * 2)
            anglais = (float(input("note d'anglais:")) * 2)
            moyen_de_nationnale = (maths + pc + si + philo + anglais) / 23
            print("\033[1;32m===============================================\033[1;32m")
            print("\033[1;33mton note d'éxaman nationnale est " + str(moyen_de_nationnale))
            # la moyen général pour entrer à une classs
            moyen_géneral_re = ((moyen_de_rejional0 * 25) + (moyen_des_semestres * 25) + (moyen_de_nationnale * 50))/100
            moyen_géneral1 = (moyen_de_rejional0 + (moyen_de_nationnale * 3)) / 4
            print("\033[1;33mton moyen d'éxaman réjional est" + str(moyen_de_rejional0))
            print("\033[1;33mton moyen générale est " + str(moyen_géneral_re))
            print("\033[1;33mton moyen d'acceptabilité dans les écoles est " + str(moyen_géneral1))
        elif y == 2:
            # 2bac éxaman nationnal SMA
            maths = (float(input("note de maths:")) * 9)
            pc = (float(input("note de pc:")) * 7)
            svt = (float(input("note se svt:")) * 3)
            philo = (float(input("note de philo:")) * 2)
            anglais = (float(input("note d'anglais:")) * 2)
            moyen_de_nationnale = (maths + pc + svt + philo + anglais) / 23
            print("\033[1;32m===============================================\033[1;32m")
            print("\033[1;33mton moyen d'éxaman nationnal est " + str(moyen_de_nationnale))
            # la moyen général pour entrer à une classs)
            moyen_géneral_re = ((moyen_de_rejional0 * 25) + (moyen_des_semestres * 25) + ( moyen_de_nationnale * 50)) / 100
            moyen_géneral1 = (moyen_de_rejional0 + (moyen_de_nationnale * 3)) / 4
            print("\033[1;33mton moyen d'éxaman réjional est" + str(moyen_de_rejional0))
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
            print('''\033[35;1m=============================================== \033[34;1m''')
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
            print("\033[1;32mgood luck :)")
            sys.exit()
        elif y == 3:
            # 2bac éxaman nationnal pc
            maths = (float(input("note de maths:")) * 7)
            pc = (float(input("note de pc:")) * 7)
            svt = (float(input("note se svt:")) * 5)
            philo = (float(input("note de philo:")) * 2)
            anglais = (float(input("note d'anglais:")) * 2)
            moyen_de_nationnale = (maths + pc + svt + philo + anglais) / 23
            print("\033[1;32m===============================================\033[1;32m")
            print("\033[1;33mton moyen d'éxaman nationnal est " + str(moyen_de_nationnale))
            # la moyen général pour entrer à une classs)
            moyen_géneral_re = ((moyen_de_rejional0 * 25) + (moyen_des_semestres * 25) + ( moyen_de_nationnale * 50)) / 100
            moyen_géneral2 = (moyen_de_rejional0 + (moyen_de_nationnale * 3)) / 4
            print("\033[1;33mton moyen d'éxaman réjional est" + str(moyen_de_rejional0))
            print("\033[1;33mton moyen générale est " + str(moyen_géneral_re))
            print("\033[1;33mton moyen d'acceptabilité dans les écoles est " + str(moyen_géneral2))
            # les seuil des écoles pour spc
        ENSA = 15.4
        ENCG = 15.5
        ENSAM = 16.8
        MEDECIN = 17
        DENTISTE = 16
        ingénieurie = 16
        if y == 3:
            # acceptabiliter pour les écoles
            print('''\033[35;1m=============================================== \033[34;1m''')
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
            print("\033[1;32mgood luck :)")
            sys.exit()
        elif y == 4:
            # 2bac éxaman nationnal SVT
            maths = (float(input("note de maths:")) * 7)
            pc = (float(input("note de pc:")) * 5)
            svt = (float(input("note se svt:")) * 7)
            philo = (float(input("note de philo:")) * 2)
            anglais = (float(input("note d'anglais:")) * 2)
            moyen_de_nationnale = (maths + pc + svt + philo + anglais) / 23
            print("\033[1;32m===============================================\033[1;32m")
            print("\033[1;33mton moyen d'éxaman nationnal est " + str(moyen_de_nationnale))
            # la moyen général pour entrer à une classs)
            moyen_géneral_re = ((moyen_de_rejional0 * 25) + (moyen_des_semestres * 25) + ( moyen_de_nationnale * 50)) / 100
            moyen_géneral3 = (moyen_de_rejional0 + (moyen_de_nationnale * 3)) / 4
            # les seuil des écoles pour spc
            print("\033[1;33mton moyen d'éxaman réjional est" + str(moyen_de_rejional0))
            print("\033[1;33mton moyen générale est " + str(moyen_géneral_re))
            print("\033[1;33mton moyen d'acceptabilité dans les écoles est " + str(moyen_géneral3))
            ENSA = 16.5
            ENCG = 15.6
            ENSAM = 16.80
            MEDECIN = 16
            DENTISTE = 16
            if y == 4:
                # acceptabiliter pour les écoles
                print('''\033[35;1m=============================================== \033[34;1m''')
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
                print("\033[1;32mgood luck :)")
                sys.exit()
    elif x == 0:
        print("\033[1;36mGood Bye")
        sys.exit()
    if x!= 0 and x != 1 and x != 2 and x != 3 and x != 4 and x != 5 and x != 10 and x != 20 and x != 30 and x != 7777:
        print("\033[1;36mError please retry the process")
        sys.exit()
        # 1bac éxaman réjonnal
    elif x == 1 or x == 2 or x == 3 or x == 4:
     print('''\033[34;1m=============================================== \033[1;36m''')
     francais = float(input("note de francais:")) * 2
     arabe = float(input("note d'arabe:"))
     eis = float(input("note de eis:"))
     hg = float(input("note de hg:"))
     moyen_de_rejional = (francais + arabe + eis + hg) / 5
     print("\033[1;33mton note d'éxaman réjonnal est " + str(moyen_de_rejional))
     moyen_des_semestres = float(input("your note of semesters:"))
     print('''\033[1;31m=============================================== \033[1;36m''')
if x == 1:
    # 2bac éxaman nationnal SMB
    maths = (float(input("note de maths:")) * 9)
    pc = (float(input("note de pc:")) * 7)
    si = (float(input("note se sI:")) * 3)
    philo = (float(input("note de philo:")) * 2)
    anglais = (float(input("note d'anglais:")) * 2)
    moyen_de_nationnale = (maths + pc + si + philo + anglais) / 23
    print("\033[1;32m===============================================\033[1;32m")
    print("\033[1;33mton moyen d'éxaman nationnal est " + str(moyen_de_nationnale))
    # la moyen général pour entrer à une classs)
    moyen_géneral_re = ((moyen_de_rejional * 25) + (moyen_des_semestres * 25) + (moyen_de_nationnale * 50)) / 100
    moyen_géneral1 = (moyen_de_rejional + (moyen_de_nationnale * 3)) / 4
    print("\033[1;33mton note d'éxaman réjonnal est " + str(moyen_de_rejional))
    print("\033[1;33mton moyen générale est " + str(moyen_géneral_re))
    print("\033[1;33mton moyen d'acceptabilité dans les écoles est " + str(moyen_géneral1))
elif x == 2:
    # 2bac éxaman nationnal SMA
    maths = (float(input("note de maths:")) * 9)
    pc = (float(input("note de pc:")) * 7)
    svt = (float(input("note se svt:")) * 3)
    philo = (float(input("note de philo:")) * 2)
    anglais = (float(input("note d'anglais:")) * 2)
    moyen_de_nationnale = (maths + pc + svt + philo + anglais) / 23
    print("\033[1;32m===============================================\033[1;32m")
    print("\033[1;33mton moyen d'éxaman nationnal est " + str(moyen_de_nationnale))
    # la moyen général pour entrer à une classs
    moyen_géneral_re = ((moyen_de_rejional * 25) + (moyen_des_semestres * 25) + (moyen_de_nationnale * 50)) / 100
    moyen_géneral1 = (moyen_de_rejional + (moyen_de_nationnale * 3)) / 4
    print("\033[1;33mton note d'éxaman réjonnal est " + str(moyen_de_rejional))
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
    print('''\033[35;1m=============================================== \033[34;1m''')
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
    print("\033[1;32mgood luck :)")
    sys.exit()
elif x == 3:
    # 2bac éxaman nationnal pc
    maths = (float(input("note de maths:")) * 7)
    pc = (float(input("note de pc:")) * 7)
    svt = (float(input("note se svt:")) * 5)
    philo = (float(input("note de philo:")) * 2)
    anglais = (float(input("note d'anglais:")) * 2)
    moyen_de_nationnale = (maths + pc + svt + philo + anglais) / 23
    print("\033[1;32m===============================================\033[1;32m")
    print("\033[1;33mton moyen d'éxaman nationnal est " + str(moyen_de_nationnale))
    # la moyen général pour entrer à une classs)
    moyen_géneral_re = ((moyen_de_rejional * 25) + (moyen_des_semestres * 25) + (moyen_de_nationnale * 50)) / 100
    moyen_géneral2 = (moyen_de_rejional + (moyen_de_nationnale * 3)) / 4
    print("\033[1;33mton note d'éxaman réjonnal est " + str(moyen_de_rejional))
    print("\033[1;33mton moyen générale est " + str(moyen_géneral_re))
    print("\033[1;33mton moyen d'acceptabilité dans les écoles est " + str(moyen_géneral2))
    # les seuil des écoles pour spc
ENSA = 15.4
ENCG = 15.5
ENSAM = 16.8
MEDECIN = 17
DENTISTE = 16
ingénieurie = 16
if x == 3:
        # acceptabiliter pour les écoles
        print('''\033[35;1m=============================================== \033[34;1m''')
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
        print("\033[1;32mgood luck :)")
        sys.exit()
elif x == 4:
    # 2bac éxaman nationnal SVT
    maths = (float(input("note de maths:")) * 7)
    pc = (float(input("note de pc:")) * 5)
    svt = (float(input("note se svt:")) * 7)
    philo = (float(input("note de philo:")) * 2)
    anglais = (float(input("note d'anglais:")) * 2)
    moyen_de_nationnale = (maths + pc + svt + philo + anglais) / 23
    print("\033[1;32m===============================================\033[1;32m")
    print("\033[1;33mton moyen d'éxaman nationnal est " + str(moyen_de_nationnale))
    # la moyen général pour entrer à une classs)
    moyen_géneral_re = ((moyen_de_rejional * 25) + (moyen_des_semestres * 25) + (moyen_de_nationnale * 50)) / 100
    moyen_géneral3 = (moyen_de_rejional + (moyen_de_nationnale * 3)) / 4
    print("\033[1;33mton note d'éxaman réjonnal est " + str(moyen_de_rejional))
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
        print('''\033[35;1m=============================================== \033[34;1m''')
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
        print("\033[1;32mgood luck :)")
        sys.exit()
