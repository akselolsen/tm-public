import pymongo
import os
import PIL
import os
from PIL import Image
from PIL import ImageChops
from PIL import ImageOps

# list of variable use in the code
list_data = []
#savedid = collection.find_one({'_id':0})
id = 0

#connection to the database
cluster = pymongo.MongoClient("mongodb+srv://aksel:1234@test.ka8c0.mongodb.net/test?retryWrites=true&w=majority")
db = cluster['tm']
collection = db['picture_data']

# add the list of data in the database
def insert_in_database(x):
  collection.insert_many(x)


# ceate a set of data that will be put in the database
def create_dic_picture(pic_id, doc_name, number_pixel, similitude):
  document = {'_id':pic_id,'name':doc_name,'number pink pixel':number_pixel,'amount of similutude': similitude}
  return document
   
# create the name of the document
#def set_name(name):
  #names = os.path.split('.')
  #name = names[0]
  #extensions = names[1]
  #print(name)

#set the id of the document
def set_id(x):
  global id
  id += 1
  return x 


def calculate_similitude(path):# calculate the degre of similitude between image
# the picture refernce picture can be change to an other picture 
#this amout of similitude is represente in euclidian distance between picture
  i = 0
  c1 = 0
  picture = Image.open('/picture/Unknown-4.jpeg')
  picture_gray = ImageOps.grayscale(picture)#ref picture in gray scale( need to adapt the path)
  picture2 = Image.open(path)
  picture_gray2  = ImageOps.grayscale(picture2)# picture in gray scale
  histogram = picture_gray.histogram()#create a histogram of the picture
  histogram1 = picture_gray2.histogram()

  while i<len(histogram) and i<len(histogram1): 
    c1+=(histogram[i]-histogram1[i])**2
    i+= 1
  c1 = c1**(1 / 2) 
  return c1

for i in os.listdir('/picture'):#loop throw the data of the folder the dire can be change 
  data = create_dic_picture(set_id(id), i, 22 , calculate_similitude('/picture/' + i))
  collection.insert_one(data)
  #collection.update_one({'_id':0}, {'$set':{'value_id':id}})


#collection.insert_one({'_id':0 ,'value_id':0})

#the aim no is to implement a fuction that check if the data is in the data base or not
#to store global value in (like id)the data base in order to reuse it.
#find the percentage of similitude between image and
