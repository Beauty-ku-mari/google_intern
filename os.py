# import os
# import zipfile
# import requests

# # Define the URL and the local path for the zip file
# url = 'https://storage.googleapis.com/learning-datasets/horse-or-human.zip'  # Replace with the actual URL
# local_zip = '/tmp/horse-or-human.zip'

# # Download the file if it doesn't exist
# if not os.path.exists(local_zip):
#     print("Downloading file...")
#     response = requests.get(url)
#     with open(local_zip, 'wb') as f:
#         f.write(response.content)
#     print("Download complete.")

# # Extract the zip file
# with zipfile.ZipFile(local_zip, 'r') as zip_ref:
#     zip_ref.extractall('/tmp/horse-or-human')

# # Directory with our training horse pictures
# train_horse_dir = os.path.join('/tmp/horse-or-human/horses')

# # Directory with our training human pictures
# train_human_dir = os.path.join('/tmp/horse-or-human/humans')

# # List first 10 horse images
# train_horse_names = os.listdir(train_horse_dir)
# print("Horse images:", train_horse_names[:10])

# # List first 10 human images
# train_human_names = os.listdir(train_human_dir)
# print("Human images:", train_human_names[:10])

# # Count total horse and human images
# print('Total training horse images:', len(os.listdir(train_horse_dir)))
# print('Total training human images:', len(os.listdir(train_human_dir)))


# import os
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# # Directory with our training horse pictures
# train_horse_dir = os.path.join('/tmp/horse-or-human/horses')

# # Directory with our training human pictures
# train_human_dir = os.path.join('/tmp/horse-or-human/humans')

# # Get the list of image filenames
# train_horse_names = os.listdir(train_horse_dir)
# train_human_names = os.listdir(train_human_dir)

# # Print first 10 filenames to verify
# print(train_horse_names[:10])
# print(train_human_names[:10])

# # Print total number of images in each category
# print('Total training horse images:', len(train_horse_names))
# print('Total training human images:', len(train_human_names))

# # Parameters for our graph; we'll output images in a 5x10 configuration
# nrows = 5
# ncols = 10

# # Index for iterating over images
# pic_index = 0

# # Set up matplotlib fig, and size it to fit 5x10 pics
# fig = plt.gcf()
# fig.set_size_inches(ncols * 4, nrows * 4)

# # Select 25 images from each category
# next_horse_pix = [os.path.join(train_horse_dir, fname) for fname in train_horse_names[pic_index:pic_index+25]]
# next_human_pix = [os.path.join(train_human_dir, fname) for fname in train_human_names[pic_index:pic_index+25]]

# # Plot horse images
# for i, img_path in enumerate(next_horse_pix):
#     sp = plt.subplot(nrows, ncols, i + 1)
#     sp.axis('Off')  # Don't show axes (or gridlines)
#     img = mpimg.imread(img_path)
#     plt.imshow(img)

# # Plot human images
# for i, img_path in enumerate(next_human_pix):
#     sp = plt.subplot(nrows, ncols, i + 26)  # Adjust index to avoid overlapping with horse images
#     sp.axis('Off')  # Don't show axes (or gridlines)
#     img = mpimg.imread(img_path)
#     plt.imshow(img)

# plt.show()
