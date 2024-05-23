from PIL import Image
import numpy as np

original_img = Image.open('D:\\b.jpg')

original_img_arr = np.array(original_img)

#print(original_img_arr.size)

#original_img.show()
# print('Rows X cols Count',original_img_arr.shape)
# print('Total elements',original_img_arr.size)
# print('size of each element in bytes',original_img_arr.itemsize)
# print('Total memory occupies',original_img_arr.nbytes/1048576)
# print('Data type',original_img_arr.dtype)
# print('no of Dimensions',original_img_arr.ndim)

#flipped_lr_array=np.fliplr(original_img_arr)

# flipped_lr_array1=np.flipud(original_img_arr)
# fI=Image.fromarray(flipped_lr_array1)

#fi=original_img_arr[:,900:1420]
fi=np.rot90(original_img_arr)

arr=Image.fromarray(fi)
arr.show()