import matplotlib.pyplot as plt
import numpy as np


def format_value(value):
    formatted_value = f'{value:.1f}'
    if formatted_value.endswith('.0'):
        return str(int(value))
    return formatted_value


def plot_pentagon(desired_qualities, bar_name):

    qualities_labels = list(desired_qualities.keys())
    qualities_values = list(desired_qualities.values())

    qualities_values_legend = [value * 10 for value in qualities_values]

    angles = np.linspace(0, 2 * np.pi, len(qualities_labels), endpoint=False)

    angles += np.pi / 2

    x = np.cos(angles) * qualities_values
    y = np.sin(angles) * qualities_values

    center_x, center_y = np.mean(x), np.mean(y)

    x = np.append(x, x[0])
    y = np.append(y, y[0])

    fig, ax = plt.subplots(figsize=(8, 8))

    for i in range(len(qualities_labels)):
        ax.plot([center_x, x[i]], [center_y, y[i]], linestyle='--',
                label=f'{qualities_labels[i]} - {format_value(qualities_values_legend[i])}')

    ax.plot(x, y, marker='o')

    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)

    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])

    weighted_sum = format_value(np.mean(qualities_values) * 10)
    color = 'green' if float(weighted_sum) >= 5.0 else 'red'
    ax.text(center_x, center_y - 1.2, f'Nota Final: {weighted_sum}', ha='center', va='center', fontsize=12,
            color=color, weight='bold')

    legend = ax.legend(loc='upper left')
    legend.set_bbox_to_anchor((0, 1))

    plt.title(f'Bravas del bar "{bar_name}"')
    plt.show()
