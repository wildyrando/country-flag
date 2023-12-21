# country-flags

## Description

This repository contains a collection of country flags in PNG format. The flags are available in three sizes: 100px, 250px, and 1000px.

## Usage

To use the flags, you can download them from the `/flags` directory. The flags have filenames that correspond to the ISO 3166-1 alpha-2 code of each country. For example, the flag of Indonesia has the filename `id.png`.

## Example Usage

Here is an example of how to use the flags:

```python
import matplotlib.pyplot as plt

# Load the flag of Indonesia
flag = plt.imread("100px/id.png")

# Plot the flag
plt.imshow(flag)

# Show the plot
plt.show()
```

