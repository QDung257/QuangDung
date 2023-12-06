import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('diemPython.csv',index_col=0,header = 0)
in_data = array(df.iloc[:,:])
print(in_data)
print('Tong so sinh vien tham du mon hoc la :')
tongsv= in_data[:,1]
print(np.sum(tongsv))
diemAc = in_data[:,2]
diemA = in_data[:,3]
diemBc = in_data[:,4]
diemB = in_data[:,5]
diemCc = in_data[:,6]
diemC = in_data[:,7]
diemDc = in_data[:,8]
diemD = in_data[:,9]
diemF = in_data[:,10]
print('Tong sv:',tongsv)
tongdiemac = np.sum(diemAc)
print("Tong so sinh vien dat diem A+ la: ",tongdiemac)
tongdiema = np.sum(diemA)
print("Tong so sinh vien dat diem A la: ",tongdiema)
tongdiembc = np.sum(diemBc)
print("Tong so sinh vien dat diem B+ la: ",tongdiembc)
tongdiemb = np.sum(diemB)
print("Tong so sinh vien dat diem B la: ",tongdiemb)
tongdiemcc = np.sum(diemCc)
print("Tong so sinh vien dat diem C+ la: ",tongdiemcc)
tongdiemc = np.sum(diemC)
print("Tong so sinh vien dat diem C la: ",tongdiemc)
tongdiemdc = np.sum(diemDc)
print("Tong so sinh vien dat diem D+ la: ",tongdiemdc)
tongdiemd = np.sum(diemD)
print("Tong so sinh vien dat diem D la: ",tongdiemd)
tongdiemf = np.sum(diemF)
print("Tong so sinh vien dat diem F la: ",tongdiemf)
maxd = diemD.max()
i, = np.where(diemD == maxd)
mind = diemD.min()
i, = np.where(diemA == mind)

print('Tong so sinh vien dat diem >=D la: ', np.sum(tongsv)- np.sum(tongdiemf))

lop1=in_data[0,2:10] 
print('Lop 1 co ',np.sum(lop1),'SV dat >=D')
lop2=in_data[1,2:10] 
print('Lop 2 co ',np.sum(lop2),'SV dat >=D')
lop3=in_data[2,2:10] 
print('Lop 3 co ',np.sum(lop3),'SV dat >=D')
lop4=in_data[3,2:10] 
print('Lop 4 co ',np.sum(lop4),'SV dat >=D')
lop5=in_data[4,2:10] 
print('Lop 5 co ',np.sum(lop5),'SV dat >=D')
lop6=in_data[5,2:10] 
print('Lop 6 co ',np.sum(lop6),'SV dat >=D')
lop7=in_data[6,2:10] 
print('Lop 7 co ',np.sum(lop7),'SV dat >=D')
lop8=in_data[7,2:10] 
print('Lop 8 co ',np.sum(lop8),'SV dat >=D')
lop9=in_data[8,2:10] 
print('Lop 9 co ',np.sum(lop9),'SV dat >=D')
#tổng số sinh viên đạt mỗi bài kiểm tra
tongsvdat = np.sum(in_data[:, -5:], axis=0)
# In ra tổng số sinh viên đạt từng bài kiểm tra
print('Tổng số sinh viên đạt từng bài kiểm tra là:')
print('L1 có :', tongsvdat[-5],'đạt')
print('L2 có :', tongsvdat[-4],'đạt')
print('tx1 có :', tongsvdat[-3],'đạt')
print('tx2 có:', tongsvdat[-2],'đạt')
print('Cuối kỳ  có:', tongsvdat[-1],'đạt')

print('lop co nhieu diem D la {0} co {1} sv dat diem D'.format(in_data[i,0],maxd))
print('lop co it diem D la {0} co {1} sv dat diem D'.format(in_data[i,0],mind))
plt.plot(range(len(diemA)),diemA,'r-',label="Diem A")
plt.plot(range(len(diemB)),diemB,'g-',label="Diem B")
plt.plot(range(len(diemC)),diemC,'b-',label="Diem C")
plt.plot(range(len(diemD)),diemD,'y-',label="Diem D")
plt.xlabel('Lơp')
plt.ylabel(' So sv dat diem ')
plt.legend(loc='upper right')
plt.show()

