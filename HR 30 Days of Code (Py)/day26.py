
def fineCalc(dateRet, dateDue):
    fine = 0
    dayFee = 15  # hackos/day
    monthFee = 500  # hackos/month
    annFee = 10000  # hackos fixed
    dayDue = dateDue[0]
    monDue = dateDue[1]
    yeaDue = dateDue[2]

    dayRet = dateRet[0]
    monRet = dateRet[1]
    yeaRet = dateRet[2]

    if yeaRet < yeaDue:
        return fine
    elif yeaRet == yeaDue:  # returned same year/before
        if monRet < monDue:
            return fine
        elif monRet == monDue:
            if dayRet <= dayDue:
                return fine
            else:
                fine = dayFee*(dayRet-dayDue)
                return fine
        else:  # ret month late
            fine = monthFee*(monRet-monDue)
            return fine

    else:  # returned year late
        fine = annFee
        return fine


ret = list(map(int, input().split()))
# da, ma, ya = actually

due = list(map(int, input().split()))
# de, me, ye = expected


print(fineCalc(ret, due))
