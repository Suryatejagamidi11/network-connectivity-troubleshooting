import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrow

fig, ax = plt.subplots(figsize=(6.5, 10))

steps = [
    ("1", "Physical", "Link light on NIC & switch port;\ncable seated; cable tester if down", "#4C72B0"),
    ("2", "Physical", "show interface status —\nport up/up, correct speed/duplex", "#4C72B0"),
    ("3", "Data Link", "show interface counters errors —\nCRC, collisions, runts", "#55A868"),
    ("4", "Data Link", "VLAN assignment matches design\n(show vlan brief / switchport)", "#55A868"),
    ("5", "Data Link", "Spanning-tree state — forwarding,\nnot blocking/err-disabled", "#55A868"),
    ("6", "Network", "IP config, gateway reachability\n(ping, arp -a)", "#DD8452"),
    ("7", "Network", "End-to-end path (traceroute) if\ngateway reachable but destination isn't", "#DD8452"),
]

box_w, box_h = 5.6, 1.05
gap = 0.35
top = len(steps) * (box_h + gap)

for i, (num, layer, desc, color) in enumerate(steps):
    y = top - i * (box_h + gap) - box_h
    ax.add_patch(patches.FancyBboxPatch((0.7, y), box_w, box_h,
                                          boxstyle="round,pad=0.05,rounding_size=0.08",
                                          facecolor=color, edgecolor="black", alpha=0.9))
    ax.text(1.0, y + box_h - 0.22, f"Step {num} — {layer}", fontsize=9.5,
            fontweight="bold", color="white", va="top")
    ax.text(1.0, y + 0.18, desc, fontsize=8, color="white", va="bottom")
    if i < len(steps) - 1:
        ax.annotate("", xy=(0.7 + box_w/2, y - gap*0.15), xytext=(0.7 + box_w/2, y),
                     arrowprops=dict(arrowstyle="-|>", color="black", lw=1.5))

ax.set_xlim(0, 7)
ax.set_ylim(-0.3, top + 0.4)
ax.axis("off")
ax.set_title("Layer-Based Troubleshooting Methodology\n(worked bottom-up; each layer confirmed before moving to the next)",
              fontsize=11, pad=14)

plt.tight_layout()
plt.savefig("diagrams/troubleshooting-methodology.png", dpi=170)
print("Methodology diagram generated.")
