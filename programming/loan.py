print("please answet this questions with a rating from 1-10")

large=int(input(How large is the loan?))
good=int(input(How good is your credit history?))
high=int(input(How high is your income?))
large=int(input(How large is your down payment?))

should_loan = False

if large >= 5:
    if good >= 7 ad high >= 7:
        should_loan = True
    elif good >= 7 or high >= 7:
            if large >= 5:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
else:
    if good < 4:
        should_loan = False
    else:
        if high >= 7 or large >= 7:
            should_loan = True
        elif high >= 4 and large >= 4:
            should_loan = True
        else:
            should_loan = False

if should_loan:
    print("The decision is yes. This is a good loan.")
else:
    print("The decision is no. You should not loan this money.")