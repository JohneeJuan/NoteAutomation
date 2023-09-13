import pytesseract
import glob

global count
count = 1
pngCounter = len(glob.glob1(r'C:\Users\johne_kt82r8o\OneDrive\Desktop\Temporary App',"*.png"))
print(pngCounter)

def fileChange():
    global count
    folderLocation = r'C:\Users\johne_kt82r8o\OneDrive\Desktop\Temporary App'
    global imageFileLocation
    imageFileLocation = (folderLocation + "\yonska" + str(count) + ".png")
    count += 1
    print(imageFileLocation)

def textOuput():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    global firstyonkExtract
    firstyonkExtract = pytesseract.image_to_string(r'C:\Users\johne_kt82r8o\OneDrive\Desktop\Temporary App\firstyonk.png')
    for x in range(2, pngCounter+1):
        fileChange()
        try:
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

            firststringbit = pytesseract.image_to_string(imageFileLocation)
            firstyonkExtract = (firstyonkExtract + "\n" + firststringbit)
        except:
            print("not a png")

textOuput()
global firstyonkExtract
print(firstyonkExtract)









# gong = ""

# def TextChange(counter):
#     tatt = r'C:\Users\johne_kt82r8o\OneDrive\Desktop\Temporary App\yonska1'
#     global gong
#     gong = (tatt + str(counter) + ".png")
#     print(gong)

# # C:\Users\johne_kt82r8o\OneDrive\Desktop\Temporary App

# def extracto():
#     global secondstringbit
#     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
#     secondstringbit = pytesseract.image_to_string(r'C:\Users\johne_kt82r8o\OneDrive\Desktop\Temporary App\firstyonk.png')
#     print(secondstringbit)
#     for i in range(2, 78):
#         TextChange(i)
#         pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
#         global firststringbit
#         firststringbit = pytesseract.image_to_string(gong)
#         secondstringbit = (secondstringbit + "\n" + firststringbit)
#         #print(pytesseract.image_to_string(gong))

# extracto()
# print(secondstringbit)