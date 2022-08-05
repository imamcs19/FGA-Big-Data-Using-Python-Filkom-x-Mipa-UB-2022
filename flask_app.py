# Rencana Pembelajaran FGA Big Using Python Kelas A Fakultas Ilmu Komputer (Filkom),
# Universitas Brawijaya (UB) 2022 Instruktur:

# 1. Imam Cholissodin, S.Si., M.Kom. | email: imamcs@ub.ac.id | FIlkom UB
# 2. Nur Silviyah Rahmi | email: silviyahrahmi@ub.ac.id | Mipa UB

# Link Free Buku Ajar tentang "Big Data Dengan Java/Scala/Python"
# dari saya (Pak Imam Cholissodin) : http://bit.ly/2FMLnfw
#
# Tgl 12 Juli 2022 - 3 September 2022
# Kolaborasi Instruktur Filkom x Mipa UB 2022
# Di Bawah Naungan Kominfo Pusat x Cisco Academy x lainnya dlm FGA
# Asisten Kelas A: Yusron Yogatama

from flask import Flask,render_template,flash, Response, redirect,url_for,session,logging,request,jsonify
from flask import make_response, json
# from flask_ngrok import run_with_ngrok # Alternatif Ngrok => Heroku / PythonAnywhere / https://labs.play-with-docker.com / AWS / GCP / Azure/ eval_js dari Colab (agak terbatas) / etc
import sqlite3
from flask_cors import CORS

from requests.packages.urllib3.exceptions import ProtocolError
from collections import OrderedDict
from operator import itemgetter
from textblob import TextBlob

# from tweepy import OAuthHandler, API, Stream
from tweepy.streaming import StreamListener

import tweepy
import re
import string
import datetime
import json


import joblib


from flask import send_file
from io import BytesIO

from flask_wtf.file import FileField
from wtforms import SubmitField
# from flask_wtf import Form
from flask_wtf import FlaskForm

# import json
import os

app = Flask(__name__, static_folder='static')
# run_with_ngrok(app)  # Start ngrok when app is run
# CORS(app)
CORS(app, resources=r'/api/*')
# CORS(app, resources=r'/*')
# CORS(app)

# app.debug = False
app.secret_key = 'fga^&&*(&^(filkom#BJH#G#VB#Bey89nkGBGUY_ap938255bnub'

# app.secret_key = secrets.token_bytes(32) # used to cryptographically sign session cookies

############ Flask routes general: ############

# # ================ awal - dasar ke-2 ===============
# #

# # buat input dari url, untuk penjumlahan misal 2 bilangan
# @app.route('/add/<a>/<b>')
# def add_ab(a,b):
#     c = int(a) + float(b)
#     return 'a + b = ' + str(c)
#     # return 'a + b = %s' % c
# # https://bigdatafga.pythonanywhere.com/add/1/2.5
# # hasil => a + b = 3.5

# #
# # buatlah halaman post sekaligus get
# # nilai a dan b, lalu ditambahkan
# # dengan return kode html dalam flask python Web App
# @app.route('/post_add2', methods=["POST", "GET"])
# def inputkan_ab():
#     # membuat penjumlahan 2 bilangan

#     if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /post_add2

#         a_in = float(request.form['a'])
#         b_in = float(request.form['b'])
#         c = a_in + b_in

#         return '''
#         <html>
#             <head>
#             </head>
#             <body>
#               <form method="post">
#                 <input type="text" name="a" value="%s" />
#                 <input type="text" name="b" value="%s" />
#                 <input type="submit" value="Hitung a + b"/>

#               </form>
#               <h2>Hasil a + b = %s + %s = %s </h2>
#             </body>
#         </html>
#         ''' % (a_in, b_in, a_in, b_in, c)

#     else: # untuk yang 'GET' data awal untuk di send ke /post_add2
#         return '''
#             <html>
#                 <head>
#                 </head>
#                 <body>
#                   <form action="/post_add2" method="post">
#                     Masukkan nilai a = <input type="text" name="a" value="" />
#                     <br>
#                     Masukkan nilai b = <input type="text" name="b" value="" />
#                     <input type="submit" value="Hitung a + b"/>
#                   </form>
#                 </body>
#             </html>
#         '''

# #
# # buatlah halaman post sekaligus get
# # nilai a dan b, lalu ditambahkan
# # dengan return file "form_add3.html" dalam folder "mysite/templates", flask python Web App
# @app.route('/post_add3', methods=["POST", "GET"])
# def inputkan_ab3():
#     # membuat penjumlahan 2 bilangan
#     if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /post_add2

#         a_in = float(request.form['a'])
#         b_in = float(request.form['b'])
#         c = a_in + b_in

#         return render_template('form_add3.html', a_save = a_in, b_save = b_in, c_save = c)

#     else: # untuk yang 'GET' data awal untuk di send ke /post_add3
#         return render_template('form_add3.html')


# # ================ akhir - dasar ke-2 ===============

# ================ awal - dasar ke-1 ===============
# #
# @app.route('/')
# def hello_world():
#     return 'Hello Big Data Using Python from Flask - FGA x Cisco Academy 2022 x Filkom UB!'

# @app.route('/add')
# def add():
#     # membuat penjumlahan 2 bilangan
#     a = 10
#     b = 90
#     c = a + b

#     return str(c)

# # buatlah halaman perkalian
# # antara a*b
# @app.route('/kali')
# def kali():
#     # membuat perkalian 2 bilangan
#     a = 10
#     b = 90
#     c = a * b

#     return str(c)

# # buatlah tampilan indeks looping 1..10
# @app.route('/loop')
# def loop():
#     c = ''
#     for i in range(10): # i = 0,1,..,9
#         c +=str(i+1) + '  '

#     return str(c)

# # buatlah tampilan indeks looping 1 sampai 10
# # yang ganjil
# @app.route('/ganjil')
# def ganjil():
#     c = ''
#     for i in range(10): # i = 0,1,..,9
#         if((i+1)%2!=0):
#             c +=str(i+1) + '  '

#     return str(c)
# # ================ akhir - dasar ke-1 ===============

# ========= untuk Project =================

# @app.route("/")
# def index():
#     return render_template("index.html")
#     return 'Hello FGA Big Data Using Python - Filkom UB 2022 :D'

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route('/menu')
def menugrafkom():
    return render_template('launchpad_menu.html')


@app.route("/login",methods=["GET", "POST"])
def login():
  conn = connect_db()
  db = conn.cursor()
  msg = ""
  if request.method == "POST":
      mail = request.form["mail"]
      passw = request.form["passw"]

      rs = db.execute("SELECT * FROM user WHERE Mail=\'"+ mail +"\'"+" AND Password=\'"+ passw+"\'" + " LIMIT 1")

      conn.commit()

      hasil = []
      for v_login in rs:
          hasil.append(v_login)

      if hasil:
          session['name'] = v_login[3]
          return redirect(url_for("fphome"))
      else:
          msg = "Masukkan Username (Email) dan Password dgn Benar!"

  return render_template("login.html", msg = msg)

@app.route("/register", methods=["GET", "POST"])
def register():
  conn = connect_db()
  db = conn.cursor()
  if request.method == "POST":
      mail = request.form['mail']
      uname = request.form['uname']
      passw = request.form['passw']

      cmd = "insert into user(Mail, Password,Name,Level) values('{}','{}','{}','{}')".format(mail,passw,uname,'1')
      conn.execute(cmd)
      conn.commit()

      # conn = db

      return redirect(url_for("login"))
  return render_template("register.html")

@app.route("/bli", methods=["GET", "POST"])
def bli():
  conn = connect_db()
  db = conn.cursor()

  return render_template("bli.html")

@app.route("/biz", methods=["GET", "POST"])
def biz():
  conn = connect_db()
  db = conn.cursor()

  return render_template("biz.html")


@app.route("/contohfp2_nonspark", methods=["GET", "POST"])
def contohfp2_nonspark():
  # Simple Linear Regression / Klasifikasi / Clustering
  # Importing the libraries
  import numpy as np
  # import matplotlib.pyplot as plt
  import pandas as pd
  import os.path

  BASE_DIR = os.path.dirname(os.path.abspath(__file__))
  url = os.path.join(BASE_DIR, "static/data_contoh/Salary_Data.csv")

  # Importing the dataset => ganti sesuai dengan case yg anda usulkan
  # a. Min. 30 Data dari case data simulasi dari yg Anda usulkan
  # b. Min. 30 Data dari real case, sesuai dgn yg Anda usulkan dari tugas minggu ke-3 (dari Kaggle/UCI Repository)
  # url = "./Salary_Data.csv"
  dataset = pd.read_csv(url)
  X = dataset.iloc[:, :-1].values
  y = dataset.iloc[:, 1].values

  # Splitting the dataset into the Training set and Test set
  # Lib-nya selain sklearn/ Tensorflow/ Keras/ PyTorch/ etc
  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

  # Hitung Mape
  # from sklearn.metrics import mean_absolute_percentage_error

  # Feature Scaling
  """from sklearn.preprocessing import StandardScaler
  sc_X = StandardScaler()
  X_train = sc_X.fit_transform(X_train)
  X_test = sc_X.transform(X_test)
  sc_y = StandardScaler()
  y_train = sc_y.fit_transform(y_train)"""

  # Fitting Simple Linear Regression to the Training set
  from sklearn.linear_model import LinearRegression
  regressor = LinearRegression()
  myModelReg = regressor.fit(X_train, y_train)

  # Simpan hasil model fit
  with open(os.path.join(BASE_DIR, "static/simpan_model_data/myModelReg.joblib.pkl"), 'wb') as f:
    joblib.dump(myModelReg, f, compress=9)

  # Load hasil model fit
  with open(os.path.join(BASE_DIR, "static/simpan_model_data/myModelReg.joblib.pkl"), 'rb') as f:
    myModelReg_load = joblib.load(f)

  # Predicting the Test set results
  #y_pred = regressor.predict(X_test)
  #y_pred2 = regressor.predict(X_train)

  y_pred = myModelReg_load.predict(X_test)
  y_pred2 = myModelReg_load.predict(X_train)

  # Visualising the Training set results
  # plt.scatter(X_train, y_train, color = 'red')
  # plt.plot(X_train, regressor.predict(X_train), color = 'blue')


  # Visualising the Test set results
  # plt.scatter(X_test, y_test, color = 'red')
  # plt.plot(X_train, regressor.predict(X_train), color = 'blue')
  # plt.title('Salary vs Experience (Test set)')
  # plt.xlabel('Years of Experience')
  # plt.ylabel('Salary')
  # plt.show()

  aktual, predict = y_train, y_pred2
  mape = np.sum(np.abs(((aktual - predict)/aktual)*100))/len(predict)

  # return render_template('MybigdataApps.html', y_aktual = list(y_train), y_prediksi = list(y_pred2), mape = mape)
  return render_template('MybigdataAppsNonPySpark.html', y_aktual = list(y_train), y_prediksi = list(y_pred2), mape = mape)

@app.route("/contohfp2_spark", methods=["GET", "POST"])
def contohfp2_spark():
  # MLLIB dari Pyspark Simple Linear Regression /Klasifikasi / Clustering
  # Importing the libraries
  import numpy as np
  import matplotlib.pyplot as plt
  import pandas as pd
  import os

  BASE_DIR = os.path.dirname(os.path.abspath(__file__))
  url = os.path.join(BASE_DIR, "static/data_contoh/Salary_Data.csv")

  import findspark
  findspark.init()
#   import findspark
#   findspark.init("/home/imamcs/spark-3.1.2-bin-hadoop3.2")

  #os.environ["SPARK_HOME"] ="/home/imamcs/mysite/FGA-Big-Data-Using-Python-Filkom-x-Mipa-UB-2021/spark-2.0.0-bin-hadoop2.7"
  #os.environ["PYTHONPATH"] ="/home/imamcs/mysite/FGA-Big-Data-Using-Python-Filkom-x-Mipa-UB-2021/spark-2.0.0-bin-hadoop2.7/python/"
  #os.environ["PYTHONPATH"] +=":/home/imamcs/mysite/FGA-Big-Data-Using-Python-Filkom-x-Mipa-UB-2021/spark-2.0.0-bin-hadoop2.7/python/lib/py4j-0.10.1-src.zip"

  #os.environ["PYTHONPATH"] = "/spark-2.4.1-bin-hadoop2.7/python/"
  #os.environ["PYTHONPATH"] += ":/spark-2.4.1-bin-hadoop2.7/python/lib/py4j-0.10.7-src.zip"

#   print(os.environ["SPARK_HOME"])

#   print(os.environ["PYTHONPATH"])

#   !echo $PYTHONPATH

  from pyspark.sql import SparkSession
  spark = SparkSession.builder.appName("Linear Regression").config("spark.executor.memory", "512m").getOrCreate()

  from pyspark.ml.regression import LinearRegression
  from pyspark.ml.linalg import Vectors
  from pyspark.ml.feature import VectorAssembler
  from pyspark.ml.feature import IndexToString, StringIndexer
  from pyspark.ml import Pipeline, PipelineModel

  from pyspark import SQLContext, SparkConf, SparkContext
  from pyspark.sql import SparkSession
  #sc = SparkContext.getOrCreate()
  sc = spark.sparkContext
  if (sc is None):
      #sc = SparkContext(master="local[*]", appName="Linear Regression")

      spark = SparkSession.\
        builder.\
        appName("Linear Regression").\
        master("local[*]").\
        config("spark.executor.memory", "512m").\
        getOrCreate()

      sc = spark.sparkContext

      # ------------------
  spark = SparkSession(sparkContext=sc)
  # sqlcontext = SQLContext(sc)

  # Importing the dataset => ganti sesuai dengan case yg anda usulkan
  # a. Min. 30 Data dari case data simulasi dari yg Anda usulkan
  # b. Min. 30 Data dari real case, sesuai dgn yg Anda usulkan dari tugas minggu ke-3 (dari Kaggle/UCI Repository)
  # url = "./Salary_Data.csv"

  sqlcontext = SQLContext(sc)
  data = sqlcontext.read.csv(url, header = True, inferSchema = True)

  #from pyspark.ml.feature import VectorAssembler
  # mendifinisikan Salary sebagai variabel label/predictor
  dataset = data.select(data.YearsExperience, data.Salary.alias('label'))
  # split data menjadi 70% training and 30% testing
  training, test = dataset.randomSplit([0.7, 0.3], seed = 100)
  # mengubah fitur menjadi vektor
  assembler = VectorAssembler().setInputCols(['YearsExperience',]).setOutputCol('features')
  trainingSet = assembler.transform(training)
  # memilih kolom yang akan di vektorisasi
  trainingSet = trainingSet.select("features","label")

  #from pyspark.ml.regression import LinearRegression
  # fit data training ke model
  lr = LinearRegression()
  lr_Model = lr.fit(trainingSet)

  # Simpan hasil model fit
  #import tempfile
  #path = tempfile.mkdtemp()
  #path = os.path.join(BASE_DIR, "myModel_Spark")
  path_myModel_Spark = os.path.join(BASE_DIR, "myModel_Spark")
  #lr_Model.write.save(os.path.join(BASE_DIR, "myModelReg_Spark"))
  #lr_Model.save(spark, path_myModel_Spark)
  #lr_Model.save(path_myModel_Spark)
  lr_Model.write().overwrite().save(path_myModel_Spark)
  #write().overwrite().save(path_myModel_Spark)

  #save(sc, path)

  # Load hasil model fit
  #myModelReg_Spark_load = PipelineModel.load(os.path.join(BASE_DIR, "myModelReg_Spark"))
  #myModelReg_Spark_load = lr.load(spark, path_myModel_Spark)
  myModelReg_Spark_load = lr.load(path_myModel_Spark)


  # assembler : fitur menjadi vektor
  testSet = assembler.transform(test)
  # memilih kolom fitur dan label
  testSet = testSet.select("features", "label")

  # fit testing data ke model linear regression
  #testSet = lr_Model.transform(testSet)
  testSet = myModelReg_Spark_load.transform(testSet)

  # testSet.show(truncate=False)

  from pyspark.ml.evaluation import RegressionEvaluator
  evaluator = RegressionEvaluator()
  # print(evaluator.evaluate(testSet, {evaluator.metricName: "r2"}))

  y_pred2 = testSet.select("prediction")
  # y_pred2.show()


  return render_template('MybigdataAppsPySpark.html', y_aktual = y_pred2.rdd.flatMap(lambda x: x).collect(), y_prediksi = y_pred2.rdd.flatMap(lambda x: x).collect(), mape = evaluator.evaluate(testSet, {evaluator.metricName: "r2"}))

@app.route("/bigdataApps", methods=["GET", "POST"])
def bigdataApps():
  if request.method == 'POST':
    import pandas as pd
    import numpy as np
    import os.path

    #BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    #url = os.path.join(BASE_DIR, "dataset_dump.csv")

    dataset = request.files['inputDataset']
    # url = "./dataset_dump.csv"

    persentase_data_training = 90
    banyak_fitur = int(request.form['banyakFitur'])
    banyak_hidden_neuron = int(request.form['banyakHiddenNeuron'])
    dataset = pd.read_csv(dataset, delimiter=';', names = ['Tanggal', 'Harga'], usecols=['Harga'])
    # dataset = pd.read_csv(url, delimiter=';', names = ['Tanggal', 'Harga'], usecols=['Harga'])
    # dataset = dataset.fillna(method='ffill')
    minimum = int(dataset.min()-10000)
    maksimum = int(dataset.max()+10000)
    new_banyak_fitur = banyak_fitur + 1
    hasil_fitur = []
    for i in range((len(dataset)-new_banyak_fitur)+1):
      kolom = []
      j = i
      while j < (i+new_banyak_fitur):
        kolom.append(dataset.values[j][0])
        j += 1
      hasil_fitur.append(kolom)
    hasil_fitur = np.array(hasil_fitur)
    data_normalisasi = (hasil_fitur - minimum)/(maksimum - minimum)
    data_training = data_normalisasi[:int(persentase_data_training*len(data_normalisasi)/100)]
    data_testing = data_normalisasi[int(persentase_data_training*len(data_normalisasi)/100):]

    #Training
    bobot = np.random.rand(banyak_hidden_neuron, banyak_fitur)
    bias = np.random.rand(banyak_hidden_neuron)
    h = 1/(1 + np.exp(-(np.dot(data_training[:, :banyak_fitur], np.transpose(bobot)) + bias)))
    h_plus = np.dot(np.linalg.inv(np.dot(np.transpose(h),h)),np.transpose(h))
    output_weight = np.dot(h_plus, data_training[:, banyak_fitur])

    #Testing
    h = 1/(1 + np.exp(-(np.dot(data_testing[:, :banyak_fitur], np.transpose(bobot)) + bias)))
    predict = np.dot(h, output_weight)
    predict = predict * (maksimum - minimum) + minimum

    #MAPE
    aktual = np.array(hasil_fitur[int(persentase_data_training*len(data_normalisasi)/100):, banyak_fitur])
    mape = np.sum(np.abs(((aktual - predict)/aktual)*100))/len(predict)

    print("predict = ", predict)
    print("aktual =", aktual)
    print("mape = ", mape)

    # return render_template('bigdataApps.html', data = {'y_aktual' : list(aktual),'y_prediksi' : list(predict),'mape' : mape})
    return render_template('bigdataApps.html', y_aktual = list(aktual), y_prediksi = list(predict), mape = mape)


    # return "Big Data Apps " + str(persentase_data_training) + " banyak_fitur = " + str(banyak_fitur) + " banyak_hidden_neuron = " + str(banyak_hidden_neuron) + " :D"
  else:
    return render_template('bigdataApps.html')

def connect_db():
    import os.path

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "data.db")
    # with sqlite3.connect(db_path) as db:

    return sqlite3.connect(db_path)

#konversi Seq object menjadi array int [a-z], misal menjadi [1-26] => next untuk bahan optimasi penskalaan
def seq2val_space_plus_arr_a_z(seq_):
    #get unik kode atau simbol IUPAC utk nucleotides
    # print(set(seq_.lower()))
    # {'N', 'G', 't', 'M', 'C', 'A', 'g', 'T', 'c', 'R', 'a'}
    # ['n', 'g', 't', 'm', 'c', 'a', 'g', 't', 'c', 'r', 'a']
    # {'a', 'c', 'g', 'm', 'n', 'r', 't'}

    # konversi setiap char kodenya menjadi angka, misal a = 1, c = 2, g = 3, t = 4
    # Di mana konversi ini nantinya dapat juga dicari nilai yang optimal
    seq_ = str(seq_).lower()

    for idx_letter in range(26):
        seq_= seq_.replace(chr(idx_letter+97),str(idx_letter)+" ")

    val_seq_ = seq_.rstrip()
    # print(val_seq_)

    # upper() sequence
    # up_seq_ = seq_.upper()
    # print(up_seq_)

    arr_val_seq_ = np.fromstring(val_seq_,dtype=int,sep=' ')

    return arr_val_seq_

## untuk trendTwit
## mencoba streaming
class StreamListener(tweepy.StreamListener):
    def __init__(self, start_time):
        """
        Initalizes a StreamListener object.
        start_time: the time the stream was connected
        tweets: a dictionary to store processed tweets and their polarity
        """
        tweepy.StreamListener.__init__(self)
        self.start_time = start_time
        self.tweets = {}

    def on_status(self, status):
        """
        Function called when the stream gets connected. Filters the tweets by user and language.
        If 30 seconds have passed since the stream was connected, returns False so stream can disconnect.
        """
        if filter_users.add_user(status) and status.lang == "en":
            self.process_tweet(status)

        #we want to collect tweets every 30 seconds so we set an internal timer inside the class
        if datetime.datetime.now() <= self.start_time + datetime.timedelta(seconds=30):
            return True

        return False

    def process_tweet(self, status):
        """
        Links, mentions, "RT"s, emojis, and stopwords are removed from the tweet. Sentiment anlaysis is performed and
        the clean tweet (sans stopwords) and analysis result is stored in the tweets dict.

        status: a status object

        """
        #remove links, mentions, "RT"s, emojis, non-ascii chars from the tweet
        clean_tweet = re.sub(r"([^\w]?:\@|https?\://)\S+", "", status.text)
        clean_tweet = re.sub(r'[^\x00-\x7F]+'," ", clean_tweet)

        clean_tweet = clean_tweet.replace("RT ", "")

        #remove numbers and punctuation
        translator = str.maketrans("", "", string.punctuation + string.digits)
        clean_tweet = clean_tweet.translate(translator)


        clean_tweet = clean_tweet.lower()

        #https://stackoverflow.com/questions/2400504/easiest-way-to-replace-a-string-using-a-dictionary-of-replacements/2400577#2400577
        slang = re.compile(r'\b(' + '|'.join(settings.SLANG_DICT.keys()) + r')\b')
        clean_tweet = slang.sub(lambda x: settings.SLANG_DICT[x.group()], clean_tweet)
        ####

        polarity = StreamListener.get_polarity(clean_tweet)

        #remove stopwords(using the custom stopwords list in settings.py) to get most important words
        important_words = " ".join([word for word in clean_tweet.split() if word not in settings.STOPWORDS_SET])

        #add the processed tweet into the tweets list
        self.tweets[important_words] = polarity

    @staticmethod
    def get_polarity(tweet):
        """
        Determines the polarity of the tweet using TextBlob.

        tweet: a partially processed tweet (still has stopwords)
        return: int polarity -> 1 if positive, 0 if neutral, -1 if negative

        """

        text_blob = TextBlob(tweet)

        tweet_polarity_float = text_blob.sentiment.polarity

        #greater than 0.05 ->  positive, less than -0.05 -> negative, else neutral
        if tweet_polarity_float >= 0.05:
            polarity = 1
        elif tweet_polarity_float <= -0.05:
            polarity = -1
        else:
            polarity = 0

        return polarity


    def get_tweets(self):
        """
        Returns a copy of the tweets dictionary.
        """
        return self.tweets.copy()

    def on_error(self, status_code):
        """
        Handles errors coming from the Twitter API. If being rate limited,
        Twitter will send a 420 status code and we will disconnect.

        """
        if status_code == 420:
            return False


class SortData(object):
    data = {}

    def __init__(self, tweets):
        """
        Initializes a SortData object.
        tweets: a dictionary of processed tweets and their polarity
        """
        self.tweets = tweets

    def calculate_frequencies(self):
        """
        Calculates the frequencies of the words in processed tweets
        and creates the data dictionary. A key value pair for the dictionary
        will have the word as the key and a list as its value. The list will include
        the number of times the word has occurred in all the tweets seen so far and
        another list including the number of positive, neutral, and negative tweets
        containing that word.

        """
        #key value pair for the data dictionary -> word:[count, [numPositiveTweets, numNeutralTweets, numNegativeTweets]]

        for tweet, polarity in self.tweets.items():
            for word in tweet.split():
                if word not in self.data:

                    self.data[word] = [0, [0, 0, 0]]

                    self.data[word][0] = 1

                    self.update_polarity_frequency(word, polarity)

                else:
                    self.data[word][0] += 1

                    self.update_polarity_frequency(word, polarity)


    def update_polarity_frequency(self, word, polarity):
        """
        Determines what polarity (positive, neutral, negative) the tweet has
        according to the tweets dictionary and updates the value in the data dictionary.

        """
        if polarity == 1:
            self.data[word][1][0] += 1
        elif polarity == 0:
            self.data[word][1][1] += 1
        else:
            self.data[word][1][2] += 1


    def get_most_common_words(self):
        """
        Removes all the words in the data dictionary that have occurred
        less than two times in all the tweets seen so far. Sorts the data
        dictionary by frequency of the words in descending order.

        return: a JSON object version of the sorted dictionary

        """
        self.calculate_frequencies()

        data_copy = self.data.copy()

        for word in data_copy:
             if self.data[word][0] <= 2:
                 del self.data[word]

        sorted_words = OrderedDict(sorted(self.data.items(), key = itemgetter(1), reverse = True))

        #make sure the dictionary is less than or equal to 15 words so ajax request in javascript
        #doesn't slow down
        while len(sorted_words) >= 15:
            sorted_words.popitem()
        return json.dumps(sorted_words)

def event_stream():
    """
    Connects the stream, sorts and processes the data, and creates
    a dictionary of the most common words found.

    return: a JSON object containing the most common words found in the tweets sample
            and their frequencies and polarity data

    """
    try:
        stream_listener = StreamListener(datetime.datetime.now())
        # stream = tweepy.Stream(auth = api.auth, listener = stream_listener)
        stream = tweepy.Stream(auth, listener = stream_listener)

        # # receive tweets on assigned tracks,
        # # filter them by assigned conditions and send them to port
        # twitter_stream = Stream(auth, Listener(c_socket, api))
        # # twitter_stream.filter(lang=["en"],track=tracks)
        # twitter_stream.filter(track=tracks,languages=["id","en"])

        #we want a lot of tweets so we filter with most used words
        stream.filter(track = settings.COMMON_WORDS, locations = settings.LOCATIONS)
        stream.disconnect()
        sortData = SortData(stream_listener.get_tweets())
        return sortData.get_most_common_words()
    except ProtocolError:
        print("There was an error. Restarting stream...")
    except ConnectionError:
        print("There was an error. Restarting stream...")

@app.route('/twit')
def twit():
    #clear the data dictionary when page is refreshed
    SortData.data.clear()
    # return render_template("twit.html")
    return render_template("twity.html")

@app.route('/stream')
def stream():
    return Response(event_stream(), mimetype="application/json")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html")

# labels_trendTwit = []
# values_trendTwit = []
# @app.route("/trendTwit")
# def chart_trendTwit():
#     global labels_trendTwit,values_trendTwit
#     labels = []
#     values = []
#     return render_template('chart.html', values=values_trendTwit, labels=labels_trendTwit)


# @app.route('/refreshData_trendTwit')
# def refresh_graph_data_trendTwit():
#     global labels_trendTwit, values_trendTwit
#     print("labels now: " + str(labels_trendTwit))
#     print("data now: " + str(values_trendTwit))
#     return jsonify(sLabel=labels_trendTwit, sData=values_trendTwit)


# @app.route('/updateData_trendTwit', methods=['POST'])
# def update_data_post_trendTwit():
#     global labels_trendTwit, values_trendTwit
#     if not request.form or 'data' not in request.form:
#         return "error",400
#     labels_trendTwit = ast.literal_eval(request.form['label'])
#     values_trendTwit = ast.literal_eval(request.form['data'])
#     print("labels received: " + str(labels_trendTwit))
#     print("data received: " + str(values_trendTwit))
#     return "success",201


# cara akses, misal: http://imamcs.pythonanywhere.com/api/fp/3.0/?a=70&b=3&c=2
@app.route("/api/fp/3.0/", methods=["GET"])
def api():
    import os.path
    import sys

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    url = os.path.join(BASE_DIR, "static/data_contoh/dataset_dump_tiny.csv")

    # url = "../GGRM.JK.csv"
    # dataset=pd.read_csv(url)

    import pandas as pd
    import numpy as np
    import json
    # from django.http import HttpResponse
    from flask import Response


    a, b, c = request.args.get('a'), request.args.get('b'),request.args.get('c')
    # print(a,' ',b,' ',c)
    # bar = request.args.to_dict()
    # print(bar)

    # dataset = request.FILES['inputDataset']#'E:/Pak Imam/Digitalent/dataset_dump.csv'
    persentase_data_training = int(a)
    banyak_fitur = int(b)
    banyak_hidden_neuron = int(c)
    # print(persentase_data_training,banyak_fitur,banyak_hidden_neuron)

    dataset = pd.read_csv(url, delimiter=';', names = ['Tanggal', 'Harga'], usecols=['Harga'])
    #dataset = pd.read_csv(url, usecols=['Close'])
    dataset = dataset.fillna(method='ffill')

    # print("missing value", dataset.isna().sum())

    minimum = int(dataset.min())
    maksimum = int(dataset.max())
     # print(minimum,maksimum)
    new_banyak_fitur = banyak_fitur + 1
    hasil_fitur = []
    for i in range((len(dataset)-new_banyak_fitur)+1):
        kolom = []
        j = i
        while j < (i+new_banyak_fitur):
            kolom.append(dataset.values[j][0])
            j += 1
        hasil_fitur.append(kolom)
    hasil_fitur = np.array(hasil_fitur)
        # print(hasil_fitur)
    data_normalisasi = (hasil_fitur - minimum)/(maksimum - minimum)

    data_training = data_normalisasi[:int(
        persentase_data_training*len(data_normalisasi)/100)]
    data_testing = data_normalisasi[int(
        persentase_data_training*len(data_normalisasi)/100):]

    # print(data_training)
    # Training
    is_singular_matrix = True
    while(is_singular_matrix):
        bobot = np.random.rand(banyak_hidden_neuron, banyak_fitur)
        #print("bobot", bobot)
        bias = np.random.rand(banyak_hidden_neuron)
        h = 1 / \
            (1 + np.exp(-(np.dot(data_training[:, :banyak_fitur], np.transpose(bobot)) + bias)))

        #print("h", h)
        #print("h_transpose", np.transpose(h))
        #print("transpose dot h", np.dot(np.transpose(h), h))

        # cek matrik singular
        cek_matrik = np.dot(np.transpose(h), h)
        det_cek_matrik = np.linalg.det(cek_matrik)
        if det_cek_matrik != 0:
            #proceed

        #if np.linalg.cond(cek_matrik) < 1/sys.float_info.epsilon:
            # i = np.linalg.inv(cek_matrik)
            is_singular_matrix = False
        else:
            is_singular_matrix = True


    h_plus = np.dot(np.linalg.inv(cek_matrik), np.transpose(h))

    # print("h_plus", h_plus)
    output_weight = np.dot(h_plus, data_training[:, banyak_fitur])

        # print(output_weight)
        # [none,none,...]

    # Testing
    h = 1 / \
        (1 + np.exp(-(np.dot(data_testing[:, :banyak_fitur], np.transpose(bobot)) + bias)))
    predict = np.dot(h, output_weight)
    predict = (predict * (maksimum - minimum) + minimum)

    # MAPE
    aktual = np.array(hasil_fitur[int(
        persentase_data_training*len(data_normalisasi)/100):, banyak_fitur]).tolist()
    mape = np.sum(np.abs(((aktual - predict)/aktual)*100))/len(predict)
    prediksi = predict.tolist()
    # print(prediksi, 'vs', aktual)
    # response = json.dumps({'y_aktual': aktual, 'y_prediksi': prediksi, 'mape': mape})

    # return Response(response, content_type='text/json')
    # return Response(response, content_type='application/json')
    #return Response(response, content_type='text/xml')


    response = jsonify({'y_aktual': aktual, 'y_prediksi': prediksi, 'mape': mape})


    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    # response.headers.add("access-control-allow-credentials","false")
    # response.headers.add("access-control-allow-methods","GET, POST")


    # r = Response(response, status=200, mimetype="application/json")
    # r.headers["Content-Type"] = "application/json; charset=utf-8"
    return response



# get json data from a url using flask in python
@app.route('/baca_api', methods=["GET"])
def baca_api():
    import requests
    import json
    # uri = "https://api.stackexchange.com/2.0/users?order=desc&sort=reputation&inname=fuchida&site=stackoverflow"
    uri = "http://enterumum.pythonanywhere.com/api/fp/3.0/?a=50&b=3&c=2"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
        return "Terdapat Error Pada Koneksi Anda"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)

    # json.loads(response.get_data().decode("utf-8"))
    # data = json.loads(requests.get(uri).decode("utf-8"))
    # data = json.loads(response.get(uri).get_data().decode("utf-8"))

    # import urllib.request
    # with urllib.request.urlopen("http://imamcs.pythonanywhere.com/api/fp/3.0/?a=90&b=3&c=2") as url:
    #     data = json.loads(url.read().decode())
    #     #print(data)

    # from urllib.request import urlopen

    # import json
    # import json
    # store the URL in url as
    # parameter for urlopen
    # url = "https://api.github.com"

    # store the response of URL
    # response = urlopen(url)

    # storing the JSON response
    # from url in data
    # data_json = json.loads(response.read())

    # print the json response
    # print(data_json)

    # data = \
    #     {
    #   "items": [
    #     {
    #       "badge_counts": {
    #         "bronze": 16,
    #         "silver": 4,
    #         "gold": 0
    #       },
    #       "account_id": 258084,
    #       "is_employee": false,
    #       "last_modified_date": 1573684556,
    #       "last_access_date": 1628710576,
    #       "reputation_change_year": 0,
    #       "reputation_change_quarter": 0,
    #       "reputation_change_month": 0,
    #       "reputation_change_week": 0,
    #       "reputation_change_day": 0,
    #       "reputation": 420,
    #       "creation_date": 1292207782,
    #       "user_type": "registered",
    #       "user_id": 540028,
    #       "accept_rate": 100,
    #       "location": "Minneapolis, MN, United States",
    #       "website_url": "http://fuchida.me",
    #       "link": "https://stackoverflow.com/users/540028/fuchida",
    #       "profile_image": "https://i.stack.imgur.com/kP5GW.png?s=128&g=1",
    #       "display_name": "Fuchida"
    #     }
    #   ],
    #   "has_more": false,
    #   "quota_max": 300,
    #   "quota_remaining": 299
    # }

    # displayName = data['items'][0]['display_name']# <-- The display name
    # reputation = data['items'][0]['reputation']# <-- The reputation

    # y_train = data['y_aktual']
    # y_pred = data['y_prediksi']
    # mape = data['mape']

    return data
    # return str(mape)
    # return render_template('MybigdataAppsNonPySpark.html', y_aktual = list(y_train), y_prediksi = list(y_pred), mape = mape)


@app.route('/upload', methods=["GET", "POST"])
def upload():

    form = UploadForm()
    if request.method == "POST":

        if form.validate_on_submit():
            file_name = form.file.data
            database(name=file_name.filename, data=file_name.read() )
            # return render_template("upload.html", form=form)
            return redirect(url_for("dashboard"))

    return render_template("upload.html", form=form)


@app.route('/hapus/file/', methods=["GET"])
def hapus():
    name = request.args.get('name')
    conn = connect_db()
    db = conn.cursor()

    db.execute("DELETE FROM  upload WHERE name =\'"+ name +"\'")
    # mydata
    # for x in c.fetchall():
    #     name_v=x[0]
    #     data_v=x[1]
    #     break

    conn.commit()
    db.close()
    conn.close()

    return redirect(url_for("dashboard"))

@app.route('/unduh/file/', methods=["GET"])
def unduh():
    name = request.args.get('name')
    conn = connect_db()
    db = conn.cursor()

    # c = db.execute(""" SELECT * FROM  upload WHERE name ="""+ name)
    c = db.execute("SELECT * FROM  upload WHERE name =\'"+ name +"\'")
    # mydata
    for x in c.fetchall():
        name_v=x[0]
        data_v=x[1]
        break

    conn.commit()
    db.close()
    conn.close()

    # return render_template('dashboard.html', header = mydata)


    return send_file(BytesIO(data_v), attachment_filename=name_v, as_attachment=True)


@app.route('/download', methods=["GET", "POST"])
def download():

    form = UploadForm()

    if request.method == "POST":
        conn = connect_db()
        db = conn.cursor()

        # conn= sqlite3.connect("fga_big_data_rev2.db")
        # cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = db.execute(""" SELECT * FROM  upload """)

        for x in c.fetchall():
            name_v=x[0]
            data_v=x[1]
            break

        conn.commit()
        db.close()
        conn.close()

        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=True)


    return render_template("upload.html", form=form)



# class LoginForm(FlaskForm):
class UploadForm(FlaskForm):
    file = FileField()
    submit = SubmitField("submit")
    download = SubmitField("download")

def database(name, data):
    conn = connect_db()
    db = conn.cursor()

    # conn= sqlite3.connect("fga_big_data_rev2.db")
    # cursor = conn.cursor()

    db.execute("""CREATE TABLE IF NOT EXISTS upload (name TEXT,data BLOP) """)
    db.execute("""INSERT INTO upload (name, data) VALUES (?,?) """,(name,data))

    conn.commit()
    db.close()
    conn.close()

def query():
    # conn= sqlite3.connect("fga_big_data_rev2.db")
    # cursor = conn.cursor()

    conn = connect_db()
    db = conn.cursor()

    print("IN DATABASE FUNCTION ")
    c = db.execute(""" SELECT * FROM  upload """)

    for x in c.fetchall():
        name_v=x[0]
        data_v=x[1]
        break



    conn.commit()
    db.close()
    conn.close()

    return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=True)

@app.route('/dashboard')
def dashboard():
    # cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cur.execute('SELECT * FROM header')
    # data = cur.fetchall()
    # cur.close()

    conn = connect_db()
    db = conn.cursor()

    # conn= sqlite3.connect("fga_big_data_rev2.db")
    # cursor = conn.cursor()
    print("IN DATABASE FUNCTION ")
    c = db.execute(""" SELECT * FROM  upload """)

    mydata = c.fetchall()
    for x in c.fetchall():
        name_v=x[0]
        data_v=x[1]
        break

    hasil = []
    for v_login in c:
        hasil.append(v_login)

    conn.commit()
    db.close()
    conn.close()

    #return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=True)

    return render_template('dashboard.html', header = mydata)

@app.route('/logout')
def logout():
   # remove the name from the session if it is there
   session.pop('name', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
    #import os
    #os.environ["JAVA_HOME"] ="/usr/lib/jvm/java-8-openjdk-amd64"
    #print(os.environ["JAVA_HOME"])
    #print(os.environ["SPARK_HOME"])
    #print(os.environ["PYTHONPATH"])
    # db.create_all()
    app.run()  # If address is in use, may need to terminate other sessions:
             # Runtime > Manage Sessions > Terminate Other Sessions
  # app.run(host='0.0.0.0', port=5004)  # If address is in use, may need to terminate other sessions:
             # Runtime > Manage Sessions > Terminate Other Sessions
    # socket.run(app, debug=True)