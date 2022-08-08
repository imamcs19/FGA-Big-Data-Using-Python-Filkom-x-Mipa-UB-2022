# FGA-Big-Data-Using-Python-Filkom-x-Mipa-UB-2022
Rencana Pembelajaran FGA Big Using Python Kelas A
Fakultas Ilmu Komputer (Filkom), Universitas Brawijaya (UB) 2022
Instruktur: 
1. Imam Cholissodin, S.Si., M.Kom. | email: imamcs@ub.ac.id | FIlkom UB
2. Nur Silviyah Rahmi, S.Si., M.Stat. | email: silviyahrahmi@ub.ac.id | Mipa UB

Link Free Buku Ajar tentang "Big Data Dengan Java/Scala/Python" dari saya (Pak Imam Cholissodin) : http://bit.ly/2FMLnfw
Tgl 12 Juli 2022 - 3 September 2022
Kolaborasi Instruktur Filkom x Mipa UB 2022
Di Bawah Naungan Kominfo Pusat x Cisco Academy x lainnya dlm FGA
Asisten Kelas A: Yusron Yogatama

Screenshot Hasil Running Big Data App Using Python:
![Ngrok x Flask on Google Colab - Login & Register - BigDataApps Rev2.1](https://github.com/imamcs19/FGA-Big-Data-Using-Python-Filkom-x-Mipa-UB-2021/blob/main/Ngrok%20x%20Flask%20on%20Google%20Colab%20-%20Login%20%26%20Register%20-%20BigDataApps%20Rev2.1.png)
--> Ngrok x Flask on Google Colab - Login & Register - BigDataApps Rev2.1 --> Alternatif Migrasi ke PythonAnywhere/ lainnya

![Halaman Upload dan List Files Upload - Flask x SQLite - PythonAnywhere](https://github.com/imamcs19/FGA-Big-Data-Using-Python-Filkom-x-Mipa-UB-2021/blob/main/Halaman%20Upload%20dan%20List%20Files%20Upload%20-%20Flask%20x%20SQLite%20On%20PythonAnywhere.png)
--> Halaman Upload dan List Files Upload - Flask x SQLite - PythonAnywhere

![Data Processing Using PySpark x Flask x SQLite - PythonAnywhere](https://github.com/imamcs19/FGA-Big-Data-Using-Python-Filkom-x-Mipa-UB-2021/blob/main/Data%20Processing%20Using%20PySpark%20On%20PythonAnywhere.png)
05:31 ~ $ pyspark
Python 3.9.5 (default, May 27 2021, 19:45:35)                                                                                                    
[GCC 9.3.0] on linux                                                                                                                             
Type "help", "copyright", "credits" or "license" for more information.                                                                           
22/08/08 05:31:17 WARN Utils: Your hostname, green-liveconsole15 resolves to a loopback address: 127.0.0.1; using 10.0.0.57 instead (on interface ens5)                                                                                                                                           
22/08/08 05:31:17 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address                                                          
22/08/08 05:31:18 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable   
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties                                                                  
Setting default log level to "WARN".                                                                                                             
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).                                                     
Welcome to                                                                                                                                       
      ____              __                                                                                                                       
     / __/__  ___ _____/ /__                                                                                                                     
    _\ \/ _ \/ _ `/ __/  '_/                                                                                                                     
   /__ / .__/\_,_/_/ /_/\_\   version 3.1.2                                                                                                      
      /_/                                                                                                                                        
                                                                                                                                                 
Using Python version 3.9.5 (default, May 27 2021 19:45:35)                                                                                       
Spark context Web UI available at http://ip-10-0-0-57.ec2.internal:4040                                                                          
Spark context available as 'sc' (master = local[*], app id = local-1659936679899).                                                               
SparkSession available as 'spark'.                                                                                                               
>>> def add1(x): return x+1                                                                                                                      
...                                                                                                                                              
>>> list(map(add1,[1,2,3]))                                                                                                                      
[2, 3, 4]                                                                                                                                        
>>> def isOdd(x): return x%2==1                                                                                                                  
...                                                                                                                                              
>>> list(filter(isOdd, range(1,10)))                                                                                                             
[1, 3, 5, 7, 9]                                                                                                                                  
>>> list(range(1,5))                                                                                                                             
[1, 2, 3, 4]                                                                                                                                     
>>> def add(x,y): return x+y                                                                                                                     
...                                                                                                                                                     
>>> from functools import reduce                                                                                                                 
>>> reduce(add,range(1,5))                                                                                                                       
10
>>> (lambda x:2*x)(3)
6
>>> map(lambda x:2*x,[1,2,3])
<map object at 0x7f6363d73fd0>
>>> list(map(lambda x:2*x,[1,2,3]))                                                                                                              
[2, 4, 6]
>>> list(map(lambda t:t[0],[(1,2),(3,4),(5,6)]))
[1, 3, 5]
>>> reduce(lambda x,y:x+y,[1,2,3])
6
>>> reduce(lambda x,y:x+y,map(lambda t:t[0],[(1,2),(3,4),(5,6)]))
9
>>> 
05:39 ~ $ 

--> Data Processing Using PySpark x Flask x SQLite - PythonAnywhere

![Data Processing Using Scikit-learn x Flask x SQLite - PythonAnywhere](https://github.com/imamcs19/FGA-Big-Data-Using-Python-Filkom-x-Mipa-UB-2021/blob/main/Data%20Processing%20Using%20Scikit-learn%20On%20PythonAnywhere.png)
--> Data Processing Using Scikit-learn x Flask x SQLite - PythonAnywhere

![Simple API to Integrated System Between Big Data App and Non Big Data App - PythonAnywhere](https://github.com/imamcs19/FGA-Big-Data-Using-Python-Filkom-x-Mipa-UB-2021/blob/main/Simple%20API%20to%20Integrated%20System%20Between%20Big%20Data%20App%20and%20Non%20Big%20Data%20App.png)
--> Simple API to Integrated System Between Big Data App and Non Big Data App - PythonAnywhere

![SQLite Studio - Membuat db untuk Support Compute Engine dalam Ekosistem Big Data App - PythonAnywhere](https://github.com/imamcs19/FGA-Big-Data-Using-Python-Filkom-x-Mipa-UB-2021/blob/main/SQLite%20Studio%20-%20Membuat%20db%20untuk%20Support%20Compute%20Engine%20dalam%20Ekosistem%20Big%20Data%20App%20Using%20Python.png)
--> SQLite Studio - Membuat db untuk Support Compute Engine dalam Ekosistem Big Data App - PythonAnywhere

![Struktur Files Explorer Web App Flask pada PythonAnywhere untuk Prototype Ekosistem Big Data App Using Python](https://github.com/imamcs19/FGA-Big-Data-Using-Python-Filkom-x-Mipa-UB-2021/blob/main/Struktur%20Files%20Explorer%20Web%20App%20Flask%20pada%20PythonAnywhere%20untuk%20Prototype%20Ekosistem%20Big%20Data%20App%20Using%20Python.png)
--> Struktur Files Explorer Web App Flask pada PythonAnywhere untuk Prototype Ekosistem Big Data App Using Python

Semoga Bermanfaat & Sukses untuk Semuanya. Aamiin. :D
