degree = int(input("Fonksiyonun en büyük derecesini giriniz")) +1 # function degree
weights_list = [] # to storage the weights

epsilon = float(input("epsilon değeri : "))

for i in range(degree):
    weights_list.append(float(input("Fonksiyonun X üzeri {}. ağırlığı".format(i)))) # inputing the weights , first one bias

left_border = float(input("Küçük x sınır değeri : "))
right_border = float(input("büyük x sınır değeri : "))

fl = 0
for i in range(degree):
    fl = fl + weights_list[i] * (left_border ** i)  # calculating the function according to left x
fr = 0
for i in range(degree):
    fr = fr + weights_list[i] * (right_border ** i)  # calculating the function according to right x

central = left_border -((right_border-left_border)/(fr-fl)*fl)
fc = 0

for i in range(degree):
    fc = fc + weights_list[i] * (central  ** i)  # calculating the function according to central x
print(fr,fc)
central_new = central +2*epsilon
if fr*fc < 0 :
    while fc != 0 and abs(central_new - central) >= epsilon :
        central_new = central

        central = central_new -((right_border-central_new)/(fr-fc)*fc)

        fc = 0

        for i in range(degree):
            fc = fc + weights_list[i] * (central ** i)  # calculating the function according to central x

if fr * fc < 0:
    while fc != 0 and abs(central_new - central) >= epsilon:
        central_new = central

        central = central_new - ((right_border - central_new) / (fr - fc) * fc)

        fc = 0

        for i in range(degree):
            fc = fc + weights_list[i] * (central ** i)  # calculating the function according to central x

        print(central)

if fl * fc < 0:
    while fc != 0 and abs(central_new - central) >= epsilon:
        central_new = central

        central = central_new - ((left_border - central_new) / (fl - fc) * fc)

        fc = 0

        for i in range(degree):
            fc = fc + weights_list[i] * (central ** i)  # calculating the function according to central x

        print(central)
