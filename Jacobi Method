epsilon = float(input("Epsilon değeri : "))  # error value

degreeg = int(input("Fonksiyonun en büyük derecesini giriniz")) + 1  # function degree
degreeh = int(input("Fonksiyonun en büyük derecesini giriniz")) + 1  # function degree
weights_listg = []  # to storage the weights
weights_listh = []  # to storage the weights

for i in range(degreeg):
    weights_listg.append(
        float(input("Fonksiyonun X üzeri {}. ağırlığı".format(i))))  # inputing the weights , first one bias

for i in range(degreeh):
    weights_listh.append(
        float(input("Fonksiyonun X üzeri {}. ağırlığı".format(i))))  # inputing the weights , first one bias

g_value = float(input("başlangıç değeri : "))  # initial value

hx = 1
gx = 0

while hx != 0 and abs(gx - hx) >= epsilon:
    hx = 0
    gx = 0
    for i in range(degreeg):
        gx = gx + weights_listg[i] * (g_value ** i)

    for i in range(degreeh):
        hx = hx + (weights_listh[i] * (gx ** i))
    hx = hx ** (1 / 2)

    g_value = hx



print(g_value)



