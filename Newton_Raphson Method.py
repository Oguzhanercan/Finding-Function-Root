def f(degree,weights_list,point):
    fx = 0
    for i in range(degree):
        fx = fx + weights_list[i] * (point ** i)
    return fx

delta = float(input("Delta değeri (türev için) : ")) # the amount of change in x
epsilon = float(input("Epsilon değeri : ")) # error value
degree = int(input("Fonksiyonun en büyük derecesini giriniz")) +1 # function degree
weights_list = [] # to storage the weights

for i in range(degree):
    weights_list.append(float(input("Fonksiyonun X üzeri {}. ağırlığı".format(i)))) # inputing the weights , first one bias

initial_value = float(input("başlangıç değeri : ")) #initial value

f(degree,weights_list,(initial_value))
x_new = initial_value - f(degree,weights_list,(initial_value))/((f(degree,weights_list,(initial_value+delta)) - f(degree,weights_list,(initial_value)))/delta)


while abs(x_new-initial_value) >= epsilon:
    initial_value = x_new
    x_new = initial_value - f(degree,weights_list,(initial_value))/((f(degree,weights_list,(initial_value+delta)) - f(degree,weights_list,(initial_value)))/delta)

print(x_new)
