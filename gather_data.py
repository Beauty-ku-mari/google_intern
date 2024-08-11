import tensorflow as tf
from tensorflow.keras import models # type: ignore
import matplotlib.pyplot as plt

# Load the Fashion MNIST dataset
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

# Reshape the data to add a single channel (grayscale)
training_images = training_images.reshape(60000, 28, 28, 1)
training_images = training_images / 255.0
test_images = test_images.reshape(10000, 28, 28, 1)
test_images = test_images / 255.0

# Build the CNN model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(training_images, training_labels, epochs=5)

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test loss: {}, Test accuracy: {}'.format(test_loss, test_acc * 100))

# Print first 100 test labels
print(test_labels[:100])

# Prepare for visualizing activations
f, axarr = plt.subplots(3, 4)  # Create a 3x4 subplot grid

FIRST_IMAGE = 0
SECOND_IMAGE = 23
THIRD_IMAGE = 28
CONVOLUTION_NUMBER = 6

# Extract the outputs of each layer
layer_outputs = [layer.output for layer in model.layers]

# Create a model to return the activations for each layer
activation_model = tf.keras.models.Model(inputs=model.input, outputs=layer_outputs)

# Function to visualize the activations
def visualize_activations(image_index, row):
    for x in range(4):
        # Get the activations for the specified layer
        activations = activation_model.predict(test_images[image_index].reshape(1, 28, 28, 1))[x]
        
        # Plot the activations for the specified convolution number
        axarr[row, x].imshow(activations[0, :, :, CONVOLUTION_NUMBER], cmap='inferno')
        axarr[row, x].grid(False)

# Visualize activations for the first image
visualize_activations(FIRST_IMAGE, 0)

# Visualize activations for the second image
visualize_activations(SECOND_IMAGE, 1)

# Visualize activations for the third image
visualize_activations(THIRD_IMAGE, 2)

# Show the plot
plt.show()
