from PIL import Image, ImageFilter
from random import randint
def flash(idx,intensity):
    for i in range(w):
        for j in range(h):
            p = inputImage.getpixel((i,j))
            x = []
            x.append(p[0])
            x.append(p[1])
            x.append(p[2])
            x[idx-1]=x[idx-1]+int(intensity*255/100);
            if x[idx-1] > 255:
                x[idx-1] = 255
            if x[idx-1] < 0:
                x[idx-1] = 0
            p=tuple(x)
            inputImage.putpixel((i,j),p)
            fname = "flash"+str(idx)+".jpg"
    inputImage.save(fname,"JPEG")
    return


def bw():
    inputImage = Image.open('input.jpg', 'r').convert("L")
    w,h = inputImage.size
    
    for i in range(w):
        for j in range(h):
            p = inputImage.getpixel((i,j))
            if p > 128:
                p=255
            else:
                p=0
            inputImage.putpixel((i,j),p)
           
            fname = "bw.jpg"
    inputImage.save(fname,"JPEG")
    return

def bright(intensity):
    inputImage = Image.open('input.jpg', 'r').convert("RGB")
    w,h = inputImage.size
    
    for i in range(w):
        for j in range(h):
            p = inputImage.getpixel((i,j))
            x = []
            x.append(p[0])
            x.append(p[1])
            x.append(p[2])
            
            x[0]=abs(int(x[0]+int((intensity)*33/255)))
            x[1]=abs(int(x[1]+int((intensity)*33/255)))
            x[2]=abs(int(x[2]+int((intensity)*33/255))) 
            p=tuple(x)
            inputImage.putpixel((i,j),p)           
            fname = "bright.jpg"
    inputImage.save(fname,"JPEG")
    return

def enhance(idx):
    image = Image.open('input.jpg')
    if idx==1:
        image = image.filter(ImageFilter.FIND_EDGES)
        image.save('crayon.jpeg') 
    elif idx==2:
        image = image.filter(ImageFilter.SHARPEN)
        image.save('sharpen.jpeg') 
    elif idx==3:
        image = image.filter(ImageFilter.BLUR)
        image.save('blur.jpeg') 
    elif idx==4:
        image = image.filter(ImageFilter.CONTOUR)
        image.save('contour.jpeg') 
    elif idx==5:
        image = image.filter(ImageFilter.DETAIL)
        image.save('detail.jpeg') 
    elif idx==6:
        image = image.filter(ImageFilter.EDGE_ENHANCE)
        image.save('edged.jpeg') 
    elif idx==7:
        image = image.filter(ImageFilter.EMBOSS)
        image.save('embossed.jpeg') 
    elif idx==8:
        image = image.filter(ImageFilter.SMOOTH)
        image.save('smothened.jpeg') 
    return

def grayscale():
    inputImage = Image.open('input.jpg', 'r').convert("L")
    w,h = inputImage.size
    for i in range(w):
        for j in range(h):
            p = inputImage.getpixel((i,j))
            inputImage.putpixel((i,j),p)
            fname = "grayscale.jpg"
    inputImage.save(fname,"JPEG")
    return

def toonish(intensity):
    for i in range(w):
        for j in range(h):
            p = inputImage.getpixel((i,j))
            x = []
            x.append(p[0])
            x.append(p[1])
            x.append(p[2])
            
            x[0]=abs(int(x[0]+int((intensity)*255/100)))%255
            x[1]=abs(int(x[1]+int((intensity)*255/100)))%255
            x[2]=abs(int(x[2]+int((intensity)*255/100)))%255 
            p=tuple(x)
            inputImage.putpixel((i,j),p)
            fname = "toonish.jpg"
    inputImage.save(fname,"JPEG")
    return



def burn(intensity):
    for i in range(w):
        for j in range(h):
            p = inputImage.getpixel((i,j))
            x = []
            x.append(p[0])
            x.append(p[1])
            x.append(p[2])
            x[0]=abs(x[0]-int((3*intensity)))
            x[1]=abs(x[1]-int((3*intensity)))
            x[2]=abs(x[2]-int((3*intensity)))
            if x[0] > 255:
                    x[0] = 255
            if x[1] > 255:
                    x[1] = 255
            if x[2] > 255:
                    x[2] = 255
            if x[0] < 0:
                    x[0] = 0
            if x[1] < 0:
                    x[1] = 0
            if x[2] < 0:
                    x[2] = 0
            p=tuple(x)
            inputImage.putpixel((i,j),p)
            fname ="burn.jpg"
    inputImage.save(fname,"JPEG")
    return

def forefilter(idx,intensity):
    for i in range(w):
        for j in range(h):
            p = inputImage.getpixel((i,j))
            x = []
            x.append(p[0])
            x.append(p[1])
            x.append(p[2])
            if index==7:
                x[0]=abs(int(x[0]+int((0.5*intensity))))  
                x[1]=abs(int(x[1]+int((0.3*intensity))))  
                x[2]=abs(int(x[2]+int((0.2*intensity))))              
            elif index==8:
                x[0]=abs(x[0]+int((0.33*intensity)))
                x[1]=abs(x[1]+int((0.33*intensity)))
                x[2]=abs(x[2]+int((0.33*intensity)))
            elif index==9:
                x[0]=abs(x[0]-int((0.3*intensity)))
                x[1]=abs(x[1]-int((0.3*intensity)))
                x[2]=abs(x[2]-int((0.3*intensity)))
            if x[0] > 255:
                    x[0] = 255
            if x[1] > 255:
                    x[1] = 255
            if x[2] > 255:
                    x[2] = 255
            if x[0] < 0:
                    x[0] = 0
            if x[1] < 0:
                    x[1] = 0
            if x[2] < 0:
                    x[2] = 0
            p=tuple(x)
            inputImage.putpixel((i,j),p)
            fname = str(idx)+".jpg"
    inputImage.save(fname,"JPEG")
    return

inputImage = Image.open('input.jpg', 'r').convert("RGB")
w,h = inputImage.size
index = 1
while index!=0:
    print("1.RedFlash \t 2.GreenFlash \t 3.BlueFlash \n4. BW \t 5. Crayon \t 6. Bright \n7. Warm \t 8.White-ish \t 9.Black-ish \n10.Grayscale \t 11. Toonish \t12. Burn \n13.Sharpen \t14.Blur \t15.Contour \n16.Detailed \t17.Edged \t18.Embossed \n19.Smooth")
    index = int(input("Enter id:"))
    if index>=1 and index<=3 :
        intensity = int(input("Enter Intensity:"))
        flash(index,intensity)
    elif index==4:
        bw()
    elif index==5:
        enhance(1)
    elif index==6:
        intensity = int(input("Enter Intensity:"))
        bright(intensity)
    elif index>=7 and index<=9:
        intensity = int(input("Enter Intensity:"))
        forefilter(index,intensity)
    elif index==10:
        grayscale()
    elif index==11:
        toonish(50)
    elif index==12:
        burn(50)
    elif index==13:
        enhance(2)
    elif index==14:
        enhance(3)
    elif index==15:
        enhance(4)
    elif index==16:
        enhance(5)
    elif index==17:
        enhance(6)
    elif index==18:
        enhance(7)
    elif index==19:
        enhance(8)

    print("DONE! (press '0' to exit)")