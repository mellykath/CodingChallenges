digits = input("Enter the four digits from the PIN without any separators: ")
PINs = []
for a in range(4):
    for b in range(4):
        if a != b:
            for c in range(4):
                if c != a and c != b:
                    for d in range(4):
                        if d != a and d != b and d != c:
                            PIN = digits[a]+digits[b]+digits[c]+digits[d]
                            if PIN not in PINs:
                                PINs.append(PIN)
print(PINs)
print("There are",len(PINs),"possible PINs.")
