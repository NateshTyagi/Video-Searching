import cloudinary
import cloudinary.uploader
import cloudinary.api
import requests
import time
import urllib 
import json
l=[[],[]]
l1=[[],[]]
da=[]
da1=[]
val=''
d1=[]
dic={'1':False}
def transcript():
  cloudinary.config( 
    cloud_name = "mohit612", 
    api_key = "349572799681323", 
    api_secret = "8ImKC8q4JdpPOSitKmL85c8_spA" 
  )
  #global dic={'public_id': 'xefeepxjtrdpynzkqlwx', 'version': 1561360022, 'signature': '21ee28fc48bd6b4f7880eec6fcaa40564ff8db90', 'width': 640, 'height': 360, 'format': 'mp4', 'resource_type': 'video', 'created_at': '2019-06-24T07:07:02Z', 'tags': [], 'pages': 0, 'bytes': 4030014, 'type': 'upload', 'etag': '00aad0c6b970c4a1138428af40bd8910', 'placeholder': False, 'url': 'http://res.cloudinary.com/mohit61297/video/upload/v1561360022/xefeepxjtrdpynzkqlwx.mp4', 'secure_url': 'https://res.cloudinary.com/mohit61297/video/upload/v1561360022/xefeepxjtrdpynzkqlwx.mp4', 'info': {'raw_convert': {'google_speech': {'status': 'pending', 'data': {'formats': ['srt', 'vtt']}}}}, 'audio': {'codec': 'aac', 'bit_rate': '95999', 'frequency': 44100, 'channels': 2, 'channel_layout': 'stereo'}, 'video': {'pix_format': 'yuv420p', 'codec': 'h264', 'level': 30, 'profile': 'Constrained Baseline', 'bit_rate': '273332', 'dar': '16:9'}, 'is_audio': False, 'frame_rate': 29.97002997002997, 'bit_rate': 371643, 'duration': 86.749751, 'rotation': 0, 'original_filename': 'videoplayback'}
  global dic
  dic=cloudinary.uploader.upload("C:/Users/lenovo/Downloads/videoplayback.mp4",
    resource_type = "video", 
    raw_convert = "google_speech") 
  print(dic)
fileRet = False
def f_http(idt):
  a1= "C:/Users/lenovo/"
  a="https://res.cloudinary.com/mohit612/raw/upload/"
  #url=a+"v"+str(dic['version']+1)+"/"+dic['public_id']+".transcript"
  try:
    url=a+"v"+str(dic['version']+idt)+"/"+dic['public_id']+".transcript"
    print(url)
    urllib.request.urlretrieve(url, dic['public_id']+".transcript")
    return '111'
  except:
    return '000'
def file1():
  idt=1
  while f_http(idt)=='000':
    time.sleep(500)
    idt=idt+1
    f_http(idt)
  a1= "C:/Users/lenovo/"
  f= open(a1+dic['public_id']+".transcript","r+")
  contents=f.read()
  global d1
  d1=json.loads(contents)
  val=input("enter the string to be searched : ")
def enterval():
    global val,da,l
    val=input("value to be checked : ")
    l=[[],[]]
    val.lower()
    da=val.split()
def searchit1():
    global l
    i=0
    j=0
    k=0
    while j<len(d1):
        if(val in d1[j]['transcript']):
            i=0
            while i<len(d1[j]['words']):
                k=0
                if(d1[j]['words'][i]['word']==da[k]):
                    k=1
                    while(k<len(da)):
                        if(d1[j]['words'][i+k]['word']==da[k]):
                            k=k+1
                        else:
                            break
                    if(k==len(da)):
                        l[0].append([j,i])
                        l[1].append(d1[j]['words'][i]['start_time'])
                        i=i+k
                i=i+1
        j=j+1
def searchit():
    global l,l1
    print(l)
    l1=[[],[]]
    i1=0
    while i1<len(l):
        j=l[0][i1][0]
        i=l[0][i1][1]
        if i<len(d1[j]['words'])-1:
            i=i+1
        else:
            if j<len(d1)-1:
                j=j+1
                i=0
            else:
                return 0
        k=0
        print(d1[j]['words'][i]['word'])
        if(d1[j]['words'][i]['word']==da1[k]):
            k=1
            while(k<len(da1)):
                if(d1[j]['words'][i+k]['word']==da1[k]):
                    k=k+1
                else:
                    break
            if(k==len(da1)):
                l1[0].append([j,i])
                l1[1].append(d1[j]['words'][i]['start_time'])
                i=i+k
        i1=i1+1
    l=l1
    check()
def check():
    if not(len(l[1])):
        print('string not found')
        val3=input("1 to run again with other value : ")
        if(int(val3)==1):
            enterval()
            searchit1()
    if len(l[1])>1:
        val1=input("word appeared more than once select 1 to add more data or select 2 to chose one of the time")
        if int(val1)==1:
            global da1,da
            l1=l
            i=0
            val2=input("enter more string after \"{0}\" to check : ".format(val))
            da1=val2.split()
            da=da+val2.split()
            as1=searchit()
            if not as1:
                print("last element cannot search further")
        if int(val1)==2:
            print("lets see")
def searchdata():
  enterval()
  searchit1()
  check()

transcript()
file1()
searchdata()
  