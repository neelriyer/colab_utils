import PIL
import matplotlib.pyplot as plt

__all__ = ['combine_images_side_by_side']

def combine_images_side_by_side(img1, img2, title):

  images = [PIL.Image.open(img1), PIL.Image.open(img2)]
  widths, heights = zip(*(i.size for i in images))

  total_width = sum(widths)
  max_height = max(heights)

  new_im = PIL.Image.new('RGB', (total_width, max_height))

  x_offset = 0
  for im in images:
    new_im.paste(im, (x_offset,0))
    x_offset += im.size[0]

  plt.imshow(new_im)
  plt.title(title)
  plt.show()
