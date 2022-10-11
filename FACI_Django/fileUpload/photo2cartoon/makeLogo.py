import os
import cv2
import torch
import numpy as np
from fileUpload.photo2cartoon.models import ResnetGenerator
from fileUpload.photo2cartoon.utils import Preprocess
from PIL import Image, ImageOps, ImageFilter
import aspose.words as aw
import os

class Photo2Cartoon:
    def __init__(self):
        self.pre = Preprocess()
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.net = ResnetGenerator(ngf=32, img_size=256, light=True).to(self.device)

        assert os.path.exists(
            'fileUpload/photo2cartoon/models/photo2cartoon_weights.pt'), "[Step1: load weights] Can not find 'photo2cartoon_weights.pt' in folder 'models!!!'"
        params = torch.load('fileUpload/photo2cartoon/models/photo2cartoon_weights.pt', map_location=self.device)
        self.net.load_state_dict(params['genA2B'])
        print('[Step1: load weights] success!')

    def inference(self, img):
        # face alignment and segmentation
        face_rgba = self.pre.process(img)
        if face_rgba is None:
            print('[Step2: face detect] can not detect face!!!')
            return None

        print('[Step2: face detect] success!')
        face_rgba = cv2.resize(face_rgba, (256, 256), interpolation=cv2.INTER_AREA)
        face = face_rgba[:, :, :3].copy()
        mask = face_rgba[:, :, 3][:, :, np.newaxis].copy() / 255.
        face = (face * mask + (1 - mask) * 255) / 127.5 - 1

        face = np.transpose(face[np.newaxis, :, :, :], (0, 3, 1, 2)).astype(np.float32)
        face = torch.from_numpy(face).to(self.device)

        # inference
        with torch.no_grad():
            cartoon = self.net(face)[0][0]

        # post-process
        cartoon = np.transpose(cartoon.cpu().numpy(), (1, 2, 0))
        cartoon = (cartoon + 1) * 127.5
        cartoon = (cartoon * mask + 255 * (1 - mask)).astype(np.uint8)
        cartoon = cv2.cvtColor(cartoon, cv2.COLOR_RGB2BGR)
        print('[Step3: photo to cartoon] success!')
        return cartoon

def makeBlack(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return_value, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return threshold_image

def makeLimpidity(image_path):
    im = Image.open(image_path).convert('RGB')
    im_inv = ImageOps.invert(im)
    im_inv_L = im_inv.convert('L')
    im.putalpha(im_inv_L)

    im.save(image_path, 'PNG')

def makeSvg(image_path):
    doc = aw.Document()

    builder = aw.DocumentBuilder(doc)

    shape = builder.insert_image(image_path)

    saveOptions = aw.saving.ImageSaveOptions(aw.SaveFormat.SVG)

    os.remove(image_path)
    image_path = image_path.replace('png', 'svg')
    shape.get_shape_renderer().save(image_path, saveOptions)

def makeLogo(img_path, filename):
    filename = filename[0:-4]
    image_path = 'static/logo/' + filename + '.png'
    print(img_path, "이미지경로")
    img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
    c2p = Photo2Cartoon()
    cartoon = c2p.inference(img)

    cartoon = makeBlack(cartoon)
    if cartoon is not None:
        cv2.imwrite(image_path, cartoon)
        #print('Cartoon portrait has been saved successfully!')

    makeLimpidity(image_path)
    makeSvg(image_path)

    name = filename
    return filename


