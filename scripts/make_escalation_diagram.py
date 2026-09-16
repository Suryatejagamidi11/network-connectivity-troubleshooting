import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(9, 4.2))

levels = [
    ("Level 1\nSelf-Resolve", "Bad cable, duplex mismatch,\nwrong VLAN on an access port\n(methodology steps 1-5)", "#55A868"),
    ("Level 2\nEscalate", "Issues past the access switch:\ndistribution/core routing, firewall,\nDHCP scope exhaustion\n(after steps 1-6 confirm access layer clean)", "#DD8452"),
    ("Level 3\nChange Control", "Config changes outside a standard fix:\nnew VLAN, trunk changes affecting\nother ports, STP topology changes", "#C44E52"),
]

box_w, box_h = 2.6, 2.6
gap = 0.9
x0 = 0.5

for i, (title, desc, color) in enumerate(levels):
    x = x0 + i * (box_w + gap)
    ax.add_patch(patches.FancyBboxPatch((x, 0.5), box_w, box_h,
                                          boxstyle="round,pad=0.05,rounding_size=0.1",
                                          facecolor=color, edgecolor="black", alpha=0.9))
    ax.text(x + box_w/2, 0.5 + box_h - 0.35, title, ha="center", fontsize=10.5,
            fontweight="bold", color="white")
    ax.text(x + box_w/2, 0.5 + box_h/2 - 0.25, desc, ha="center", va="center",
            fontsize=7.6, color="white")
    if i < len(levels) - 1:
        ax.annotate("", xy=(x + box_w + gap - 0.1, 0.5 + box_h/2),
                     xytext=(x + box_w + 0.1, 0.5 + box_h/2),
                     arrowprops=dict(arrowstyle="-|>", color="black", lw=2))

ax.set_xlim(0, x0 + 3 * box_w + 2 * gap)
ax.set_ylim(0, 3.6)
ax.axis("off")
ax.set_title("Escalation Path", fontsize=12, pad=10)

plt.tight_layout()
plt.savefig("diagrams/escalation-path.png", dpi=170)
print("Escalation diagram generated.")
