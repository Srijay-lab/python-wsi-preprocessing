import matplotlib
matplotlib.use('Agg')

from deephistopath.wsi import slide
from deephistopath.wsi import tiles
from deephistopath.wsi import util
import os

#slide_number = 3
#Continue from 377
for slide_number in range(0,500):
    slide_path = "F:/Projects/HEROHE/Dataset/DataSets/" + str(slide_number) +  ".mrxs"
    if(os.path.exists(slide_path)):
        scaled_image_path = slide.training_slide_to_image(slide_path)
        print(scaled_image_path)
        #scaled_image_path = "C:/Users/Srijay/Desktop/Projects/python-wsi-preprocessing/data/" + str(slide_number) +  ".png"
        tiles.summary_and_tiles(scaled_image_path, slide_path, display=True, save_summary=True, save_data=False, save_top_tiles=True)