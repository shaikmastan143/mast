import requests
BASE_URL='http://127.0.0.1:8000/'
END_POINT='apijson'
resp=requests.get(BASE_URL+END_POINT)
data=resp.json()
print('data from django application:')
print('#'*100)
print('Employee Number:',data['eno'])
print('Employee Name:',data['ename'])
print('Employee Salary:',data['esal'])
print('Employee Address:',data['eadd'])