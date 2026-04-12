import matplotlib.pyplot as plt
import json

def rebuild_figure_from_json(json_path):
    # 1. Load the data
    with open(json_path, 'r') as f:
        data = json.load(f)

    # 2. Create the figure
    # We create a subplot for every axis object stored in the JSON
    fig, axes = plt.subplots(len(data['axes']), 1, squeeze=False)
    
    for i, ax_data in enumerate(data['axes']):
        ax = axes[i, 0]
        
        # 3. Plot the lines
        for line in ax_data['lines']:
            ax.plot(
                line['xdata'], 
                line['ydata'], 
                label=line['label'],
                color=line['color'],
                linestyle=line['linestyle'],
                linewidth=line['linewidth'],
                marker=line['marker']
            )
        
        # 4. Apply formatting and axes metadata
        ax.set_title(ax_data['title'])
        ax.set_xlabel(ax_data['xlabel'])
        ax.set_ylabel(ax_data['ylabel'])
        ax.set_xlim(ax_data['xlim'])
        ax.set_ylim(ax_data['ylim'])
        
        # Only show legend if labels were actually provided
        if any(line['label'] and not line['label'].startswith('_') for line in ax_data['lines']):
            ax.legend()

    plt.tight_layout()
    return fig

# --- Example Usage ---
# Assuming 'figure_data.json' exists from your previous extraction
fig = rebuild_figure_from_json('figure_data.json')
plt.show()
