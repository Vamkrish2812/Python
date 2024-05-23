from PIL import Image
import numpy as np

img1 = Image.open('D:\\democ1.jpg')
img2 = Image.open('D:\\democ2.jpg')
img3 = Image.open('D:\\democ3.jpg')
img4 = Image.open('D:\\democ4.jpg')

img_arr1 = np.array(img1)
img_arr2 = np.array(img2)
img_arr3 = np.array(img3)
img_arr4 = np.array(img4)

# height_diff = img_arr2.shape[0] - img_arr1.shape[0]
# height_diff1 = img_arr4.shape[0] - img_arr3.shape[0]

# # Pad img_arr1 with zeros at the top (adjust padding location as needed)
# img_arr1_padded = np.pad(img_arr1, ((height_diff, 0), (0, 0), (0, 0)), mode='constant', constant_values=0)
# img_arr3_padded = np.pad(img_arr1, ((height_diff1, 0), (0, 0), (0, 0)), mode='constant', constant_values=0)

h_img_arr1=np.vstack((img_arr1,img_arr2))
h_img_arr2=np.hstack((img_arr3,img_arr4))

v_img_arr1=np.vstack((h_img_arr1,h_img_arr2))

f_im=Image.fromarray(v_img_arr1)
h_img_arr1.show()
