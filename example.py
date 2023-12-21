# Import required modules
import requests, io
import matplotlib.pyplot as plt

# Load the flag of Indonesia from the raw link
response = requests.get("https://github.com/wildyrando/country-flag/blob/main/1000px/id.png?raw=true")
image_data = response.content

# Create the plot
plt.figure(figsize=(4, 3))  # Set appropriate figure size
image = plt.imread(io.BytesIO(image_data))

# Display the image
plt.imshow(image)
plt.axis("off")
plt.title("Indonesian Flag")

# Show the plot
plt.show()
