# country-flags

## Description

This repository contains a collection of country flags in PNG format. The flags are available in three sizes: 100px, 250px, and 1000px.

## Usage

To use the flags, you can download them from the `/flags` directory. The flags have filenames that correspond to the ISO 3166-1 alpha-2 code of each country. For example, the flag of Indonesia has the filename `id.png`.

## Example Usage

Here is an example of how to use the flags:

```python
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
```

