import numpy as np
import matplotlib.pyplot as plt
import json
import xtrack as xt
import xpart as xp


path = "xsuite_lines/line_bb_for_tracking.json"
with open(path) as fid:
    dd = json.load(fid)
p_co = xp.Particles.from_dict(dd["particle_on_tracker_co"])
line = xt.Line.from_dict(dd)
line.particle_ref = xp.Particles.from_dict(dd["particle_on_tracker_co"])
line.build_tracker()
tw = line.twiss()

# Set knob for 'on_bb_charge'
for i, x in enumerate(tw.to_pandas().name):
    if "bb_lr" in x or "bb_ho" in x:
        line.element_refs[x].scale_strength = line.vars["on_bb_charge"]


fp0 = line.get_footprint(nemitt_x=2.5e-6, nemitt_y=2.5e-6)

fp_polar = line.get_footprint(
    nemitt_x=2.5e-6,
    nemitt_y=2.5e-6,
    linear_rescale_on_knobs=[xt.LinearRescale(knob_name="on_bb_charge", v0=0.0, dv=0.1)],
)


fp_ua = line.get_footprint(
    nemitt_x=2.5e-6,
    nemitt_y=2.5e-6,
    mode="uniform_action_grid",
    linear_rescale_on_knobs=[xt.LinearRescale(knob_name="on_bb_charge", v0=0.0, dv=0.1)],
)


plt.close("all")

fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111)
fp0.plot(ax=ax1, label="no rescale bb")
plt.suptitle("Polar mode (default) - no rescale on beambeam")

plt.savefig("footprint_1.png")

fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111, sharex=ax1, sharey=ax1)
fp_polar.plot(ax=ax2, label="rescale bb")
plt.suptitle("Polar mode (default) - linear rescale on beambeam")

plt.savefig("footprint_2.png")

fig3 = plt.figure(3)
ax3 = fig3.add_subplot(111, sharex=ax1, sharey=ax1)
fp_ua.plot()
plt.suptitle("Uniform action grid mode - linear rescale on beambeam")

plt.savefig("footprint_3.png")

# plt.show()
