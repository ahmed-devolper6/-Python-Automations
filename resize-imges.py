from turtle import width
from PIL import Image
import os
fit_size = int(input("Type i size: "))
outpout_floder = input("Type i name of output floder: ")
if not os.path.exists(outpout_floder):
    os.mkdir(outpout_floder)
for filename in os.path.listdir("."):
    if filename.endswith((".jpg" , ".png")):
        continue
    image = Image.open(filename)
    hegit , witdh = Image.size
    if witdh > fit_size and hegit > fit_size:
        if witdh > hegit:
            hegit = int((fit_size/hegit)*witdh)
            width = fit_size
        else:
            witdh = int((fit_size/width)*hegit)
            hegit = fit_size
        image = image.resize(width,hegit)
        image = image.save(outpout_floder , filename)
        print(".....................")

print("done")



