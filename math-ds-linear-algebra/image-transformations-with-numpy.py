import numpy as np
import matplotlib.pyplot as plt
import codecademylib3

heart_img = np.array([[255,0,0,255,0,0,255],
              [0,255/2,255/2,0,255/2,255/2,0],
          [0,255/2,255/2,255/2,255/2,255/2,0],
          [0,255/2,255/2,255/2,255/2,255/2,0],
              [255,0,255/2,255/2,255/2,0,255],
                  [255,255,0,255/2,0,255,255],
                  [255,255,255,0,255,255,255]])

# Helper: Show images
def show_image(image, name_identifier):
  plt.imshow(image, cmap="gray", vmin=0, vmax=255)
  plt.title(name_identifier)
  plt.axis("off")
  plt.show()
  plt.clf()

# Task: Show heart image
show_image(heart_img, "Original Heart")

# Task: Invert color
heart_inverted = 255 - heart_img
show_image(heart_inverted, "Inverted Heart")

# Task: Rotate heart (90° counterclockwise)
heart_rotated = np.rot90(heart_img, k=1)
show_image(heart_rotated, "Heart Rotated 90° CCW")

# Task: Random Image (7x7 grayscale)
random_img = np.random.randint(0, 256, size=(7, 7))
show_image(random_img, "Random 7x7 Image")

# Task: Solve for heart image (recover from transforms)
# Recover from rotation
heart_recovered_from_rot = np.rot90(heart_rotated, k=3)  # rotate back
show_image(heart_recovered_from_rot, "Recovered from Rotation")

# Recover from inversion
heart_recovered_from_inv = 255 - heart_inverted
show_image(heart_recovered_from_inv, "Recovered from Inversion")
