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

central = ((right_border*fl) - (left_border*fr))/(fl-fr)
fc = 0

for i in range(degree):
    fc = fc + weights_list[i] * (central  ** i)  # calculating the function according to central x


if fl == 0:
    print(left_border)
elif fr == 0 :
    print(right_border)
elif fl*fr >0 :
    print("kök yok")
else :
    while fc != 0 and abs(left_border - right_border) >= epsilon :
        right_border = central

        central = ((right_border * fl) - (left_border * fr)) / (fl - fr)



        fc = 0
        for i in range(degree):
            fc = fc + weights_list[i] * (central ** i)  # calculating the function according to central x

print(central)

