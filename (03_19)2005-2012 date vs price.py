//testing
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_stata('C:/Users/user/Desktop/dataset.dta')
county = df["fakod"]
price = df["pris"]
date = df["kontraktsdatum"]
tax = df["taxeringsvrde"]
s_price = []
s_date = []
s_tax = []

for i in range(len(county)):
    if county[i] == 1:
        s_price.append(price[i])
        s_date.append(date[i])
        s_tax.append(tax[i])

data = sorted(zip(s_date, s_price, s_tax))

data_list = np.array(data).tolist()
year_list = []
for i in range(len(data_list)):
    year_list.append(data_list[i][0][:4])

year_code = []


def assign(args):
    for k in range(len(args)):
        if args[k] == '2005':
            year_code.append(0)
        elif args[k] == '2006':
            year_code.append(1)
        elif args[k] == '2007':
            year_code.append(2)
        elif args[k] == '2008':
            year_code.append(3)
        elif args[k] == '2009':
            year_code.append(4)
        elif args[k] == '2010':
            year_code.append(5)
        elif args[k] == '2011':
            year_code.append(6)
        elif args[k] == '2012':
            year_code.append(7)


assign(year_list)

year05 = []
price05 = []
tax05 = []
year06 = []
price06 = []
tax06 = []
year07 = []
price07 = []
tax07 = []
year08 = []
price08 = []
tax08 = []
year09 = []
price09 = []
tax09 = []
tax10 = []
year10 = []
price10 = []
tax11 = []
price11 = []
year11 = []
year12 = []
price12 = []
tax12 = []

price0601 = []
price0602 = []
price0603 = []
price0604 = []
price0605 = []
price0606 = []
price0607 = []
price0608 = []
price0609 = []
price0610 = []
price0611 = []
price0612 = []
price0701 = []
price0702 = []
price0703 = []
price0704 = []
price0705 = []
price0706 = []
price0707 = []
price0708 = []
price0709 = []
price0710 = []
price0711 = []
price0712 = []
price0801 = []
price0802 = []
price0803 = []
price0804 = []
price0805 = []
price0806 = []
price0807 = []
price0808 = []
price0809 = []
price0810 = []
price0811 = []
price0812 = []

tax0601 = []
tax0602 = []
tax0603 = []
tax0604 = []
tax0605 = []
tax0606 = []
tax0607 = []
tax0608 = []
tax0609 = []
tax0610 = []
tax0611 = []
tax0612 = []
tax0701 = []
tax0702 = []
tax0703 = []
tax0704 = []
tax0705 = []
tax0706 = []
tax0707 = []
tax0708 = []
tax0709 = []
tax0710 = []
tax0711 = []
tax0712 = []
tax0801 = []
tax0802 = []
tax0803 = []
tax0804 = []
tax0805 = []
tax0806 = []
tax0807 = []
tax0808 = []
tax0809 = []
tax0810 = []
tax0811 = []
tax0812 = []

############### Delete missing value (only tax has missing value)
for k in range(len(data_list)):
    if data_list[k][2] == 0:
        data_list.remove(data_list[k])
############################################
for j in range(len(data_list)):
    if year_code[j] == 0:
        year05.append(data_list[j][0])
        price05.append(int(data_list[j][1]))
        tax05.append(int(data_list[j][2]))
    elif year_code[j] == 1:
        year06.append(data_list[j][0])
        price06.append(int(data_list[j][1]))
        tax06.append(int(data_list[j][2]))
        if data_list[j][0][5:7] == '01':
            price0601.append(int(data_list[j][1]))
            tax0601.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '02':
            price0602.append(int(data_list[j][1]))
            tax0602.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '03':
            price0603.append(int(data_list[j][1]))
            tax0603.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '04':
            price0604.append(int(data_list[j][1]))
            tax0604.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '05':
            price0605.append(int(data_list[j][1]))
            tax0605.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '06':
            price0606.append(int(data_list[j][1]))
            tax0606.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '07':
            price0607.append(int(data_list[j][1]))
            tax0607.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '08':
            price0608.append(int(data_list[j][1]))
            tax0608.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '09':
            price0609.append(int(data_list[j][1]))
            tax0609.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '10':
            price0610.append(int(data_list[j][1]))
            tax0610.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '11':
            price0611.append(int(data_list[j][1]))
            tax0611.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '12':
            price0612.append(int(data_list[j][1]))
            tax0612.append(int(data_list[j][2]))
    elif year_code[j] == 2:
        year07.append(data_list[j][0])
        price07.append(int(data_list[j][1]))
        tax07.append(int(data_list[j][2]))
        if data_list[j][0][5:7] == '01':
            price0701.append(int(data_list[j][1]))
            tax0701.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '02':
            price0702.append(int(data_list[j][1]))
            tax0702.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '03':
            price0703.append(int(data_list[j][1]))
            tax0703.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '04':
            price0704.append(int(data_list[j][1]))
            tax0704.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '05':
            price0705.append(int(data_list[j][1]))
            tax0705.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '06':
            price0706.append(int(data_list[j][1]))
            tax0706.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '07':
            price0707.append(int(data_list[j][1]))
            tax0707.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '08':
            price0708.append(int(data_list[j][1]))
            tax0708.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '09':
            price0709.append(int(data_list[j][1]))
            tax0709.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '10':
            price0710.append(int(data_list[j][1]))
            tax0710.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '11':
            price0711.append(int(data_list[j][1]))
            tax0711.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '12':
            price0712.append(int(data_list[j][1]))
            tax0712.append(int(data_list[j][2]))
    elif year_code[j] == 3:
        year08.append(data_list[j][0])
        price08.append(int(data_list[j][1]))
        tax08.append(int(data_list[j][2]))
        if data_list[j][0][5:7] == '01':
            price0801.append(int(data_list[j][1]))
            tax0801.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '02':
            price0802.append(int(data_list[j][1]))
            tax0802.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '03':
            price0803.append(int(data_list[j][1]))
            tax0803.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '04':
            price0804.append(int(data_list[j][1]))
            tax0804.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '05':
            price0805.append(int(data_list[j][1]))
            tax0805.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '06':
            price0806.append(int(data_list[j][1]))
            tax0806.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '07':
            price0807.append(int(data_list[j][1]))
            tax0807.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '08':
            price0808.append(int(data_list[j][1]))
            tax0808.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '09':
            price0809.append(int(data_list[j][1]))
            tax0809.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '10':
            price0810.append(int(data_list[j][1]))
            tax0810.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '11':
            price0811.append(int(data_list[j][1]))
            tax0811.append(int(data_list[j][2]))
        elif data_list[j][0][5:7] == '12':
            price0812.append(int(data_list[j][1]))
            tax0812.append(int(data_list[j][2]))
    elif year_code[j] == 4:
        year09.append(data_list[j][0])
        price09.append(int(data_list[j][1]))
        tax09.append(int(data_list[j][2]))
    elif year_code[j] == 5:
        year10.append(data_list[j][0])
        price10.append(int(data_list[j][1]))
        tax10.append(int(data_list[j][2]))
    elif year_code[j] == 6:
        year11.append(data_list[j][0])
        price11.append(int(data_list[j][1]))
        tax11.append(int(data_list[j][2]))
    elif year_code[j] == 7:
        year12.append(data_list[j][0])
        price12.append(int(data_list[j][1]))
        tax12.append(int(data_list[j][2]))
################## Divide into months
plt.scatter(tax0601,price0601,sizes = [1])
plt.title(" 2006 Jenuary")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0602,price0602,sizes = [1])
plt.title(" 2006 Feburary")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0603,price0603,sizes = [1])
plt.title(" 2006 March")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0604,price0604,sizes = [1])
plt.title(" 2006 April")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0605,price0605,sizes = [1])
plt.title(" 2006 May")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0606,price0606,sizes = [1])
plt.title(" 2006 June")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0607,price0607,sizes = [1])
plt.title(" 2006 July")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0608,price0608,sizes = [1])
plt.title(" 2006 August")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0609,price0609,sizes = [1])
plt.title(" 2006 September")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0610,price0610,sizes = [1])
plt.title(" 2006 October")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0611,price0611,sizes = [1])
plt.title(" 2006 November")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0612,price0612,sizes = [1])
plt.title(" 2006 December")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0701,price0701,sizes = [1])
plt.title(" 2007 Jenuary")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0702,price0702,sizes = [1])
plt.title(" 2007 Feburary")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0703,price0703,sizes = [1])
plt.title(" 2007 March")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0704,price0704,sizes = [1])
plt.title(" 2007 April")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0705,price0705,sizes = [1])
plt.title(" 2007 May")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0706,price0706,sizes = [1])
plt.title(" 2007 June")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0707,price0707,sizes = [1])
plt.title(" 2007 July")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0708,price0708,sizes = [1])
plt.title(" 2007 August")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0709,price0709,sizes = [1])
plt.title(" 2007 September")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0710,price0710,sizes = [1])
plt.title(" 2007 October")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0711,price0711,sizes = [1])
plt.title(" 2007 November")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0712,price0712,sizes = [1])
plt.title(" 2007 December")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0801,price0801,sizes = [1])
plt.title(" 2008 Jenuary")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0802,price0802,sizes = [1])
plt.title(" 2008 Feburary")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0803,price0803,sizes = [1])
plt.title(" 2008 March")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0804,price0804,sizes = [1])
plt.title(" 2008 April")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0805,price0805,sizes = [1])
plt.title(" 2008 May")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0806,price0806,sizes = [1])
plt.title(" 2008 June")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0807,price0807,sizes = [1])
plt.title(" 2008 July")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0808,price0808,sizes = [1])
plt.title(" 2008 August")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0809,price0809,sizes = [1])
plt.title(" 2008 September")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0810,price0810,sizes = [1])
plt.title(" 2008 October")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0811,price0811,sizes = [1])
plt.title(" 2008 November")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

plt.scatter(tax0812,price0812,sizes = [1])
plt.title(" 2008 December")
plt.xlabel("Tax value")
plt.ylabel("House price")
plt.xlim((0,10000000))
plt.ylim((0,10000000))
plt.show()

##########################################

plt.scatter(price05,tax05,sizes = [1])
plt.title(" 2005 Price v.s. Tax")
plt.xlabel("House price")
plt.ylabel("Tax value")


plt.scatter(price06,tax06,sizes = [0.5],c = ['grey'])
plt.title(" 2006 Price v.s. Tax")
plt.xlabel("House price")
plt.ylabel("Tax value")


plt.scatter(price07,tax07,sizes = [0.5], c = 'dodgerblue')
plt.title(" 2007 Price v.s. Tax")
plt.xlabel("House price")
plt.ylabel("Tax value")


plt.scatter(price08,tax08,sizes = [0.5], c = 'turquoise')
plt.title(" 2006 ~ 2008 Price v.s. Tax")
plt.xlabel("House price")
plt.ylabel("Tax value")
red_patch = mpatches.Patch(color='grey', label='2006')
blue_patch = mpatches.Patch(color='dodgerblue', label='2007')
grey_patch = mpatches.Patch(color='turquoise', label='2008')
plt.legend(handles=[red_patch,blue_patch,grey_patch])


plt.scatter(price09,tax09,sizes = [0.5],c = 'grey')
plt.title(" 2009 Price v.s. Tax")
plt.xlabel("House price")
plt.ylabel("Tax value")


plt.scatter(price10,tax10,sizes = [0.5],c = 'dodgerblue')
plt.title(" 2010 Price v.s. Tax")
plt.xlabel("House price")
plt.ylabel("Tax value")


plt.scatter(price11,tax11,sizes = [0.5],c = 'turquoise')
plt.title(" 2009 ~ 2011 Price v.s. Tax")
plt.xlabel("House price")
plt.ylabel("Tax value")

red_patch = mpatches.Patch(color='grey', label='2009')
blue_patch = mpatches.Patch(color='dodgerblue', label='2010')
grey_patch = mpatches.Patch(color='turquoise', label='2011')
plt.legend(handles=[red_patch,blue_patch,grey_patch])


plt.scatter(price12,tax12,sizes = [1])
plt.title(" 2012 Price v.s. Tax")
plt.xlabel("House price")
plt.ylabel("Tax value")


################################################
plt.scatter(price06,tax06,sizes = [0.1],c = ['red'])
plt.scatter(price07,tax07,sizes = [0.1], c = 'red')
plt.scatter(price08,tax08,sizes = [0.1], c = 'red')
plt.scatter(price09,tax09,sizes = [0.1],c = 'blue')
plt.scatter(price10,tax10,sizes = [0.1],c = 'blue')
plt.scatter(price11,tax11,sizes = [0.1],c = 'blue')
plt.title(" 2006 ~ 2008 v.s. 2009 ~ 2011")
plt.xlabel("House price")
plt.ylabel("Tax value")

red_patch = mpatches.Patch(color='red', label='2006 ~ 2008')
blue_patch = mpatches.Patch(color='blue', label='2009 ~ 2011')
plt.legend(handles=[red_patch,blue_patch])

##############################################
plt.scatter(year05, price05, sizes=[1.3])
new_ticks = np.linspace(0, 2800, 6)
plt.xticks(new_ticks)
plt.scatter(year06, price06, sizes=[1.3])
plt.xticks(new_ticks)
plt.scatter(year07, price07, sizes=[1.3])
plt.xticks(new_ticks)
plt.scatter(year08, price08, sizes=[1.3])
plt.xticks(new_ticks)
plt.scatter(year09, price09, sizes=[1.3])
plt.xticks(new_ticks)
plt.scatter(year10, price10, sizes=[1.3])
plt.xticks(new_ticks)
plt.scatter(year11, price11, sizes=[1.3])
plt.xticks(new_ticks)
plt.scatter(year12, price12, sizes=[1.3])
plt.xlabel("date")
plt.ylabel("price")
plt.title("2005-2012 date vs price")
plt.show()










