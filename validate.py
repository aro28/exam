def val(x):
    for chr in x:
        if chr[0] != '1' and chr[0] != '2':
            return "cant create"
        else:
            return "can"


print(val('1214463'))