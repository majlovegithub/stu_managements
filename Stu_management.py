
#学院信息在线管理系统
'''
1.信息的输入输出
2.常用数据类型的使用
3.分支结构
4.循环结构
5.函数的定义与使用

'''
#定义一个用于存放学员信息的列表变量

stulist=[{'name':'zhangsan','age':20,'classid':'pythom02'},
        {'name':'lisi','age':25,'classid':'pythom03'},
        {'name':'wangwu','age':28,'classid':'pythom04'}
   ]
#定义一个学生信息的输出函数
def showStu(stulist):
   if len(stulist)==0:
       print("===========没有学员信息可以输出===========")
   print("|{0:<5}| {1:<10}| {2:<5}|{3:<10}|".format("sid","name","age","classid"))
   print("-"*40)
   for i in range(len(stulist)):
       print("|{0:<5}| {1:<10}| {2:<5}|{3:<10}|".format(i+1,stulist[i]['name'],stulist[i]['age'],stulist[i]['classid']))
   
#输出初始界面
while True:          #一个死循环
   print("="*12,"学院管理系统","="*14)
   print("{0:1}{1:13}{2:15}".format(" ","1. 查看学员信息","2. 添加学员信息"))
   print("{0:1}{1:13}{2:15}".format(" ","3. 删除学员信息","4. 退出系统"))
   print("="*48)
   key = input("请输入对应的选择： ")
   #根据键盘输入，判断并执行对应的选择
   if key == "1":
      print("="*12,"学员信息浏览","="*14)
      showStu(stulist)
      input("按回车键继续：")
   elif key == "2":
      print("="*12,"学员信息添加","="*14)
      stu={}
      stu['name']=input("请输入要添加的姓名：")
      stu['age']=input("请输入要添加的年龄：")
      stu['classid']=input("请输入要添加的班级号：")
      stulist.append(stu)
      showStu(stulist)
      input("按回车键继续：")
   elif key == "3":
      print("="*12,"学员信息删除","="*14)
      showStu(stulist)
      sid = input("请输入你要删除的信息id号: ")
      del stulist[int(sid)-1]
      showStu(stulist)
      input("按回车键继续：")
   elif key == "4":
      print("="*12,"再见","="*14)
      break
   else:
      print("=========无效的键盘输入============")
