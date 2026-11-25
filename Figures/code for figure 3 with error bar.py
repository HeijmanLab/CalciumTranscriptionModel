import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import matplotlib.patches as mpatches

rcParams['font.family'] = 'Arial'
rcParams['font.size'] = 10
rcParams['font.weight'] = 'bold'

figsize = (17.6 / 2.54, 7 / 2.54)  # 17.6 cm × 7 cm
bar_width = 0.35

# Figure 3A 
groups_A = ['CTR', 'Anti-miR-1', '50 nM miR-1']
exp_data_A = [100, 130.4, 85.3]
sim_data_A = [100.0, 132.9, 81.7]

# Figure 3B 
groups_B = ['CTR', 'Anti-miR-1', 'OE miR-1']
exp_data_B = [100.0, 130.476, 76.190]
sim_data_B = [100.0, 118.4, 69.5]
err_exp_B = [22.857, 23.810, 30.476]
x_pos = np.arange(len(groups_B))

exp_color_A = '#8583A9'   # Rau et al. (2011)
exp_color_B = '#CA8BA8'   # Lu et al. (2015)
SIM_EDGE = '#4D4D4D'
SIM_HATCH = '///'

fig, axes = plt.subplots(1, 2, figsize=figsize)
axA, axB = axes

x_A = np.arange(len(groups_A))
axA.bar(x_A - bar_width/2, exp_data_A, width=bar_width, color=exp_color_A, edgecolor='black')
axA.bar(x_A + bar_width/2, sim_data_A, width=bar_width,
        facecolor='none', edgecolor=SIM_EDGE, hatch=SIM_HATCH, linewidth=1)

axA.set_xticks(x_A)
axA.set_xticklabels(groups_A)
axA.set_ylabel("Relative Ca$_{V}$1.2 Protein Levels\n(% of CTR)", fontsize=12, fontweight='bold')
axA.set_ylim(0, 150)
axA.tick_params(width=1.2, labelsize=10)

x_B = np.arange(len(groups_B))
axB.bar(x_B - bar_width/2, exp_data_B, width=bar_width, color=exp_color_B, edgecolor='black',
    yerr=[np.zeros_like(err_exp_B), err_exp_B], capsize=3, error_kw=dict(lw=1, capthick=1))
axB.bar(x_B + bar_width/2, sim_data_B, width=bar_width,
        facecolor='none', edgecolor=SIM_EDGE, hatch=SIM_HATCH, linewidth=1)

axB.set_xticks(x_B)
axB.set_xticklabels(groups_B)
axB.set_ylabel("Relative Ca$_{V}$β Protein Levels\n(% of CTR)", fontsize=12, fontweight='bold')
axB.set_ylim(0, 170)
axB.tick_params(width=1.2, labelsize=10)

legend_elements = [
    mpatches.Patch(color=exp_color_A, label='Rau et al. (2011)'),
    mpatches.Patch(color=exp_color_B, label='Lu et al. (2015)'),
    mpatches.Patch(facecolor='none', edgecolor=SIM_EDGE, hatch=SIM_HATCH,
                   label='Simulation', linewidth=1),
]

fig.subplots_adjust(left=0.08, right=0.9, top=1, bottom=0.10, wspace=0.45)

fig.legend(
    handles=legend_elements,
    loc='center left',
    bbox_to_anchor=(0.95, 0.50),
    frameon=False,
    fontsize=11
)

fig.canvas.draw()
renderer = fig.canvas.get_renderer()

def ax_bbox_in_fig(ax):
    return ax.get_window_extent(renderer=renderer).transformed(fig.transFigure.inverted())

# A
bboxA = ax_bbox_in_fig(axA)
fig.text(
    bboxA.x0 - 0.14,   
    bboxA.y1 + 0.03,    
    "A",
    ha='left', va='bottom',
    fontweight='bold', fontsize=12
)

# B
bboxB = ax_bbox_in_fig(axB)
fig.text(
    bboxB.x0 - 0.14,
    bboxB.y1 + 0.03,
    "B",
    ha='left', va='bottom',
    fontweight='bold', fontsize=12
)
from pathlib import Path

script_dir = Path(__file__).resolve().parent

output_dir = script_dir / "Output"
output_dir.mkdir(parents=True, exist_ok=True)
save_path = output_dir / "figure3 with error bar.jpg"
plt.savefig(save_path, dpi=300, bbox_inches="tight")
plt.show()

