import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
original_img = Image.open('D:\\b.jpg')
original_img_arr = np.array(original_img)
flipped_lr_array1=np.flipud(original_img_arr)
#fI=Image.fromarray(flipped_lr_array1)
fI=np.rot90(original_img_arr)
# Assuming 'original_img' and 'flipped_ud_img' are your loaded images as NumPy arrays

# Create a subplot with 1 row and 2 columns


# Get references to the subplots using unpacking
fig, axs = plt.subplots(1,2) 

# Display the original image in the first subplot
axs[0].imshow(original_img)
axs[0].set_title('Original')  # Set title for the first subplot

# Display the flipped image in the second subplot
axs[1].imshow(fI)
axs[1].set_title('Flipped (UpDown)')  # Set title for the second subplot

# Display the entire plot
plt.show()