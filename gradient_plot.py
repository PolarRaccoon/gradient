import matplotlib.pyplot as plt
import numpy as np

class ColorStep:
    def __init__(self, rgb, steps):
        self.rgb = rgb
        self.steps = steps

def interpolate_colors(color_steps, total_steps):
    total_color_steps = len(color_steps)
    actual_total_steps = sum(cs.steps for cs in color_steps)
    scaling_factor = total_steps / actual_total_steps
    interpolated_colors = []
    for i in range(total_color_steps - 1):
        color1 = color_steps[i]
        color2 = color_steps[i + 1]
        steps = int((color1.steps + color2.steps) / 2 * scaling_factor)
        r1, g1, b1 = color1.rgb
        r2, g2, b2 = color2.rgb
        r_step = (r2 - r1) / steps
        g_step = (g2 - g1) / steps
        b_step = (b2 - b1) / steps
        for j in range(steps):
            interpolated_colors.append((r1 + j * r_step, g1 + j * g_step, b1 + j * b_step))
    interpolated_colors.append(color_steps[-1].rgb)  # Add the last color
    interpolated_colors_resampled = []
    for i in range(total_steps):
        index = int(i / total_steps * len(interpolated_colors))
        interpolated_colors_resampled.append(interpolated_colors[index])
    return interpolated_colors_resampled

def plot_interpolated_colors(colors):
    num_colors = len(colors)
    fig, ax = plt.subplots(figsize=(10, 1))
    for i, color in enumerate(colors):
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=[val/255 for val in color]))
    ax.set_xlim(0, num_colors - 1)  # Adjusted xlim
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.show()

# Color steps for gradient
color_steps = [
    ColorStep([0, 0, 0], 100),  # Night
    ColorStep([128, 128, 255], 100),  # A-Twilight
    ColorStep([200, 200, 255], 100),  # N-Twilight
    ColorStep([220, 220, 255], 100),  # C-Twilight
    ColorStep([240, 240, 255], 5),  # Sunrise
    ColorStep([255, 220, 220], 10),
    ColorStep([255, 240, 240], 5),  # Sunrise
    ColorStep([255, 255, 255], 500),  # Noon
    ColorStep([255, 240, 240], 5),  # Sunset
    ColorStep([255, 220, 220], 10),
    ColorStep([240, 240, 255], 5),  # Sunset
    ColorStep([220, 220, 255], 100),  # C-Twilight
    ColorStep([200, 200, 255], 100),  # N-Twilight
    ColorStep([128, 128, 255], 100),  # A-Twilight
    ColorStep([0, 0, 0], 100)  # Night
]
total_steps = 1440

interpolated_colors = interpolate_colors(color_steps, total_steps)
plot_interpolated_colors(interpolated_colors)
