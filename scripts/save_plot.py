# save_plot.py
import os
import matplotlib.pyplot as plt

def save_plot(fig, filename, output_dir='../plots', dpi=300, bbox_inches='tight'):
    """
    Save a matplotlib figure to the specified directory.

    Parameters:
    - fig: matplotlib figure object to be saved
    - filename: name of the output file (e.g., 'plot.png')
    - output_dir: the directory where the plot will be saved (default: '../plots')
    - dpi: resolution of the saved plot (default: 300)
    - bbox_inches: bbox_inches argument passed to plt.savefig for proper formatting (default: 'tight')
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Create the full output path
    output_path = os.path.join(output_dir, filename)
    
    # Save the plot
    fig.savefig(output_path, dpi=dpi, bbox_inches=bbox_inches)
    
    print(f"Plot saved at {output_path}")
