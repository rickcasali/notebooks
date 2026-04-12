import matplotlib.pyplot as plt

def extract_figure_metadata(fig):
    """
    Extracts data, limits, and basic formatting from a Matplotlib figure.
    """
    extracted_data = {
        "canvas_title": fig.canvas.get_window_title() if hasattr(fig.canvas, 'get_window_title') else "Figure",
        "axes": []
    }

    for i, ax in enumerate(fig.axes):
        ax_info = {
            "axis_index": i,
            "title": ax.get_title(),
            "xlabel": ax.get_xlabel(),
            "ylabel": ax.get_ylabel(),
            "xlim": ax.get_xlim(),
            "ylim": ax.get_ylim(),
            "lines": []
        }

        # Extract data from Line2D objects (standard plots)
        for line in ax.get_lines():
            line_data = {
                "label": line.get_label(),
                "xdata": line.get_xdata().tolist(),
                "ydata": line.get_ydata().tolist(),
                "color": line.get_color(),
                "linestyle": line.get_linestyle(),
                "linewidth": line.get_linewidth(),
                "marker": line.get_marker()
            }
            ax_info["lines"].append(line_data)
        
        extracted_data["axes"].append(ax_info)

    return extracted_data

# --- Example Usage ---

# 1. Create a dummy figure
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [10, 20, 10], label='Trend A', color='red', linestyle='--')
ax.plot([1, 2, 3], [5, 15, 25], label='Trend B', color='blue', marker='o')
ax.set_title("Sample Experiment")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Voltage (V)")
fig.show()

# 2. Extract the data
data_dict = extract_figure_metadata(fig)

# 3. Quick check of the output
for ax_data in data_dict['axes']:
    print(f"Axes Title: {ax_data['title']}")
    for line in ax_data['lines']:
        print(f" - Found line '{line['label']}' with {len(line['xdata'])} points.")

# You can now save this as JSON or YAML
import json
# Note: This simple json dump works because we converted numpy arrays to lists (.tolist())

with open('figure_data.json', 'w') as f:
    json.dump(data_dict, f, indent=4)

print("Data successfully saved to figure_data.json")
