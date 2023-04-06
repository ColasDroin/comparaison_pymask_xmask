#################### Imports ####################
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Get seaborn color palette as list of hex colors
COLORS = px.colors.qualitative.Plotly
#################### Functions ####################
def add_scatter_trace(
    fig, x, y, name, row, col, xaxis, yaxis, visible=None, color=None, legendgroup=None
):
    fig.append_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="lines",
            showlegend=True,
            name=name,
            xaxis=xaxis,
            yaxis=yaxis,
            visible=visible,
            line=dict(color=color),
            # Deactivate legendgroup for now as it doesn't work
            # legendgroup=legendgroup,
        ),
        row=row,
        col=col,
    )
    return fig


def plot_all(
    tw_pm_b1, tw_xm_b1=None, tw_xm_b2=None, name_1="PM B1", name_2="XM B1", name_3="XM B2"
):
    # Build figure
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True)

    # Add traces for beta functions
    fig = add_scatter_trace(
        fig,
        tw_pm_b1["s"],
        tw_pm_b1["betx"],
        r"$\beta_x \text{{{}}}$".format(" " + name_1),
        1,
        1,
        "x",
        "y",
        color=COLORS[0],
        legendgroup="beta",
    )
    fig = add_scatter_trace(
        fig,
        tw_pm_b1["s"],
        tw_pm_b1["bety"],
        r"$\beta_y \text{{{}}}$".format(" " + name_1),
        1,
        1,
        "x",
        "y",
        visible="legendonly",
        color=COLORS[1],
        legendgroup="beta",
    )
    if tw_xm_b1 is not None:
        fig = add_scatter_trace(
            fig,
            tw_xm_b1["s"],
            tw_xm_b1["betx"],
            r"$\beta_x \text{{{}}}$".format(" " + name_2),
            1,
            1,
            "x",
            "y",
            color=COLORS[2],
            legendgroup="beta",
        )
        fig = add_scatter_trace(
            fig,
            tw_xm_b1["s"],
            tw_xm_b1["bety"],
            r"$\beta_y \text{{{}}}$".format(" " + name_2),
            1,
            1,
            "x",
            "y",
            visible="legendonly",
            color=COLORS[3],
            legendgroup="beta",
        )
    if tw_xm_b2 is not None:
        fig = add_scatter_trace(
            fig,
            tw_xm_b2["s"],
            tw_xm_b2["betx"],
            r"$\beta_x \text{{{}}}$".format(" " + name_3),
            1,
            1,
            "x",
            "y",
            visible="legendonly",
            color=COLORS[4],
            legendgroup="beta",
        )
        fig = add_scatter_trace(
            fig,
            tw_xm_b2["s"],
            tw_xm_b2["bety"],
            r"$\beta_y \text{{{}}}$".format(" " + name_3),
            1,
            1,
            "x",
            "y",
            visible="legendonly",
            color=COLORS[5],
            legendgroup="beta",
        )

    # Add traces for position functions
    fig = add_scatter_trace(
        fig,
        tw_pm_b1["s"],
        tw_pm_b1["x"],
        r"$x \text{{{}}}$".format(" " + name_1),
        2,
        1,
        "x",
        "y2",
        color=COLORS[0],
        legendgroup="position",
    )
    fig = add_scatter_trace(
        fig,
        tw_pm_b1["s"],
        tw_pm_b1["y"],
        r"$y \text{{{}}}$".format(" " + name_1),
        2,
        1,
        "x",
        "y2",
        visible="legendonly",
        color=COLORS[1],
        legendgroup="position",
    )
    if tw_xm_b1 is not None:
        fig = add_scatter_trace(
            fig,
            tw_xm_b1["s"],
            tw_xm_b1["x"],
            r"$x \text{{{}}}$".format(" " + name_2),
            2,
            1,
            "x",
            "y2",
            color=COLORS[2],
            legendgroup="position",
        )
        fig = add_scatter_trace(
            fig,
            tw_xm_b1["s"],
            tw_xm_b1["y"],
            r"$y \text{{{}}}$".format(" " + name_2),
            2,
            1,
            "x",
            "y2",
            visible="legendonly",
            color=COLORS[3],
            legendgroup="position",
        )
    if tw_xm_b2 is not None:
        fig = add_scatter_trace(
            fig,
            tw_xm_b2["s"],
            tw_xm_b2["x"],
            r"$x \text{{{}}}$".format(" " + name_3),
            2,
            1,
            "x",
            "y2",
            visible="legendonly",
            color=COLORS[4],
            legendgroup="position",
        )
        fig = add_scatter_trace(
            fig,
            tw_xm_b2["s"],
            tw_xm_b2["y"],
            r"$y \text{{{}}}$".format(" " + name_3),
            2,
            1,
            "x",
            "y2",
            visible="legendonly",
            color=COLORS[5],
            legendgroup="position",
        )

    # Add traces for dispersion functions
    fig = add_scatter_trace(
        fig,
        tw_pm_b1["s"],
        tw_pm_b1["dx"],
        r"$D_x \text{{{}}}$".format(" " + name_1),
        3,
        1,
        "x",
        "y3",
        color=COLORS[0],
        legendgroup="dispersion",
    )
    fig = add_scatter_trace(
        fig,
        tw_pm_b1["s"],
        tw_pm_b1["dy"],
        r"$D_y \text{{{}}}$".format(" " + name_1),
        3,
        1,
        "x",
        "y3",
        visible="legendonly",
        color=COLORS[1],
        legendgroup="dispersion",
    )
    if tw_xm_b1 is not None:
        fig = add_scatter_trace(
            fig,
            tw_xm_b1["s"],
            tw_xm_b1["dx"],
            r"$D_x \text{{{}}}$".format(" " + name_2),
            3,
            1,
            "x",
            "y3",
            color=COLORS[2],
            legendgroup="dispersion",
        )
        fig = add_scatter_trace(
            fig,
            tw_xm_b1["s"],
            tw_xm_b1["dy"],
            r"$D_y \text{{{}}}$".format(" " + name_2),
            3,
            1,
            "x",
            "y3",
            visible="legendonly",
            color=COLORS[3],
            legendgroup="dispersion",
        )
    if tw_xm_b2 is not None:
        fig = add_scatter_trace(
            fig,
            tw_xm_b2["s"],
            tw_xm_b2["dx"],
            r"$D_x \text{{{}}}$".format(" " + name_3),
            3,
            1,
            "x",
            "y3",
            visible="legendonly",
            color=COLORS[4],
            legendgroup="dispersion",
        )
        fig = add_scatter_trace(
            fig,
            tw_xm_b2["s"],
            tw_xm_b2["dy"],
            r"$D_y \text{{{}}}$".format(" " + name_3),
            3,
            1,
            "x",
            "y3",
            visible="legendonly",
            color=COLORS[5],
            legendgroup="dispersion",
        )

    # Add horizontal lines for ip1 and ip5
    fig.add_vline(
        x=float(tw_xm_b1.rows["ip1"].cols["s"].to_pandas().s),
        line_width=1,
        line_dash="dash",
        line_color="grey",
        annotation_text="IP 1",
        annotation_position="top right",
    )

    fig.add_vline(
        x=float(tw_xm_b1.rows["ip5"].cols["s"].to_pandas().s),
        line_width=1,
        line_dash="dash",
        line_color="grey",
        annotation_text="IP 5",
        annotation_position="top right",
    )

    # Update overall layout
    title_1 = (
        r"$\text{{{}}}".format(name_1 + ": ")
        + r"q_{x_{pm_1}} = "
        + f'{tw_pm_b1["qx"]:.5f}'
        + r"\hspace{0.5cm}"
        + r" q_{y_{pm_1}} = "
        + f'{tw_pm_b1["qy"]:.5f}'
        + r"\hspace{0.5cm}"
        + r"Q'_{x_{pm_1}} = "
        + f'{tw_pm_b1["dqx"]:.2f}'
        + r"\hspace{0.5cm}"
        + r" Q'_{y_{pm_1}} = "
        + f'{tw_pm_b1["dqy"]:.2f}'
        + r"\hspace{0.5cm}"
        + r" \gamma_{tr_{pm_1}} = "
        + f'{1/np.sqrt(tw_pm_b1["momentum_compaction_factor"]):.2f}'
    )
    title_2 = (
        r"\\ \text{{{}}}".format(name_2 + ": ")
        + r"q_{x_{xm_1}} = "
        + f'{tw_xm_b1["qx"]:.5f}'
        + r"\hspace{0.5cm}"
        + r" q_{y_{xm_1}} = "
        + f'{tw_xm_b1["qy"]:.5f}'
        + r"\hspace{0.5cm}"
        + r"Q'_{x_{xm_1}} = "
        + f'{tw_xm_b1["dqx"]:.2f}'
        + r"\hspace{0.5cm}"
        + r" Q'_{y_{xm_1}} = "
        + f'{tw_xm_b1["dqy"]:.2f}'
        + r"\hspace{0.5cm}"
        + r" \gamma_{tr_{xm_1}} = "
        + f'{1/np.sqrt(tw_xm_b1["momentum_compaction_factor"]):.2f}'
    )
    title_3 = (
        r"\\ \text{{{}}}".format(name_3 + ": ")
        + r"q_{x_{xm_2}} = "
        + f'{tw_xm_b2["qx"]:.5f}'
        + r"\hspace{0.5cm}"
        + r" q_{y_{xm_2}} = "
        + f'{tw_xm_b2["qy"]:.5f}'
        + r"\hspace{0.5cm}"
        + r"Q'_{x_{xm_2}} = "
        + f'{tw_xm_b2["dqx"]:.2f}'
        + r"\hspace{0.5cm}"
        + r" Q'_{y_{xm_2}} = "
        + f'{tw_xm_b2["dqy"]:.2f}'
        + r"\hspace{0.5cm}"
        + r" \gamma_{tr_{xm_2}} = "
        + f'{1/np.sqrt(tw_xm_b2["momentum_compaction_factor"]):.2f}'
        + r"$"
    )
    title = title_1 + r"$"
    if tw_xm_b1 is not None:
        title = title_1 + title_2 + r"$"
    if tw_xm_b2 is not None:
        title = title_1 + title_2 + title_3

    fig.update_layout(
        title_text=title,
        title_x=0.5,
        showlegend=True,
        xaxis_showgrid=True,
        yaxis_showgrid=True,
        # xaxis_title=r'$s$',
        # yaxis_title=r'$[m]$',
        width=1000,
        height=1000,
        legend_tracegroupgap=200,
        template="plotly_white",
    )

    # Update yaxis properties
    fig.update_yaxes(title_text=r"$\beta_{x,y}$ [m]", row=1, col=1)
    fig.update_yaxes(title_text=r"(Closed orbit)$_{x,y}$ [m]", row=2, col=1)
    fig.update_yaxes(title_text=r"$D_{x,y}$ [m]", row=3, col=1)
    # fig.update_xaxes(title_text=r"$s$", row=1, col=1)
    # fig.update_xaxes(title_text=r"$s$", row=2, col=1)
    fig.update_xaxes(title_text=r"$s$", row=3, col=1)

    return fig
