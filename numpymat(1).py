import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('roasted-beans.jpg')
plt.imshow(img)
plt.axis('off')  
plt.show()
image_array = np.array(img)
