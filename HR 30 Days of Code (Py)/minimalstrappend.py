# attempt to create a minimal example where a loop appends chars to a string. Failed, found different solution
S = "HowadereAlter"

for i in range(0, len(S)):
    Sev = ''
    if i % 2 == 0:
        X = S[i].join(Sev)
        print(X)

print("Endegelände")
