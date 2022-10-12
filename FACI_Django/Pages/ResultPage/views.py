from django.shortcuts import render
import fileUpload.photo2cartoon.makeLogo as ml
from django.core.files.storage import FileSystemStorage
import threading
import time

word = {'사랑스러운' : ['#FFD2D2', '#FAB7B7', '#F4A0A0'],
         '정열적인' : ['#B90000', '#B22222', '#BA52A2'],
         '클래식한' : ['#8B4513', '#8B4F1D', '#8B5927'],
         '몽환적인' : ['#A390EE', '#AD9AEE', '#B7A4EE'],
         '신비로운' : ['#A390EE', '#AD9AEE', '#B7A4EE'],
         '화사한' : ['#FFA6CF', '#FFCAD', '#FFFA78'],

         '상큼한' : ['#FFFA78', '#FFB914', '#FF7F50'],
         '순수한' : ['#E1F6FA', '#EBFBFF', '#FFFFFF'],
         '쾌활한' : ['#FF3CBB', '#FF9614', '#FFEB46'],
         '차가운' : ['#46BEFF' , '#50C8FF', '#5AD2FF'],
         '발랄한' : ['#FFC0CB', '#FFC314', '#FFEB46'],
         '깔끔한' : ['#FFFFFF', '#B4E5FF', '#87CEEB'],

         '다정한' : ['##FFBC9B', '#FFB937', '#FFC7AD'],
         '개구진' : ['#9EF048', '#FFFA78', '#48DAD'],
         '우아한' : ['#FFFFFF', '#FDF5E6', '#F0E68C'],
         '귀여운' : ['#FFC5D0', '#FFCAD', '#FFC0CB'],
         '단아한' : ['#FDF5E6', '#9BDADC', '#B9E2FA'],
         '청초한' : ['#CCE1FF', '#A4C3FF', '#AECDF'],

         '로맨틱한' : ['#CD426B', '#FF7A85', '#DDA0DD'],
         '부드러운' : ['#FAFABE', '#FAFAAA', '#FAFAB4'],
         '차분한' : ['#957745', '#9F814F', '#A48654'],
         '따뜻한' : ['#FFAF00', '#FF8200', '#FFE13C'],
         '투명한' : ['#FFFFFF','#E8F5FF', '#DCEBFF'],
         '산뜻한' : ['#82EB5A', '#FFDC3C', '#FFA374'],

         '편안한' : ['#AAEBAA', '#006400', '#7BA87B'],
         '시크한' : ['#000000', '#646464', '#323232'],
         '지적인' : ['#3C5A91', '#D2E1FF', '#1E3269'],
         '싱그러운' : ['#9EF048', '#A8F552', '#B2FA5C'],
         '밝은' : ['#FFEB46', '#FFBCB9', '#FFCD28'],
         '청량한' : ['#52E4DC', '#79FFCE', '#32AAFF'],

         '단정한' : ['#000069', '#1E3269', '#323C73'],
         '화려한' : ['#FF1493', '#B9062F', '#B9062F'],
         '깨끗한' : ['#FFFFFF', '#FAFAD2', '#FDF5D2'],
         '고급스러운' : ['#F6C17B', '#C29F6D', '#906D3B'],
         '강렬한' : ['#FF0000', '#EB0000', '#CD0000'],
         '명량한' : ['#52E4DC', '#000069', '#FFC81E']}

list = ['사랑스러운', '정열적인', '클래식한', '몽환적인',
            '신비로운', '화사한', '상큼한', '순수한',
            '쾌활한', '차가운', '발랄한', '깔끔한',
            '다정한', '개구진', '우아한', '귀여운', '단아한', '청초한',
            '로맨틱한', '부드러운', '차분한', '따뜻한', '투명한', '산뜻한',
            '편안한', '시크한', '지적인', '싱그러운', '밝은', '청량한', '단정한', '화려한',
            '깨끗한', '고급스러운', '강렬한', '명량한']

check = False
img_url = ''
color = ''
choice = ''

def logoMaking(uploaded_file_url, filename):

    global check
    global img_url
    img_url = ml.makeLogo(uploaded_file_url, filename)
    check = True

def loading(request):
    global color
    global choice

    if request.method == 'GET':
        choice = request.GET["choice"]
        color = word[choice]

    return render(request, 'archone/loading.html')

def result(request):
    global check
    global color
    global img_url
    global choice

    while (True):
        time.sleep(1)
        if check:
            check = False
            break
    img_url = "/static/logo/" + img_url + ".svg"
    return render(request, 'archone/result.html',
                    {'color1': color[0], 'color2': color[1], 'color3': color[2], 'img_url': img_url, 'choice' : choice})

def color(request):
    global check
    global img_url

    if request.method == 'POST':
        img = request.FILES["chooseFile"]
        fs = FileSystemStorage(location='media/screening_ab1', base_url='media/screening_ab1')
        filename = fs.save(img.name, img)
        uploaded_file_url = fs.url(filename)
        thread = threading.Thread(target=logoMaking, args=(uploaded_file_url, filename))
        thread.start()

    return render(request, 'archone/color.html',{'list' : list})

def imgtool(request):

    return render(request, 'archone/imgtool.html',{'color1': color[0], 'color2': color[1], 'color3': color[2], 'img_url': img_url, 'choice' : choice})

