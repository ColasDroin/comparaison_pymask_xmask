#################### Imports ####################
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

#################### Functions ####################
def plot_all(tw_part, tw_other=None, name_1="beam 1", name_2="beam_2"):
    # Build figure
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True)
    fig.append_trace(
        go.Scatter(
            x=tw_part["s"],
            y=tw_part["betx"],
            mode="lines",
            showlegend=True,
            name=r"$\beta_x \text{{{}}}$".format(" " + name_1),
            # legendgroup="1",
        ),
        row=1,
        col=1,
    )

    fig.append_trace(
        go.Scatter(
            x=tw_part["s"],
            y=tw_part["bety"],
            mode="lines",
            showlegend=True,
            name=r"$\beta_y \text{{{}}}$".format(" " + name_1),
            visible="legendonly",
            # legendgroup="1",
        ),
        row=1,
        col=1,
    )

    if tw_other is not None:
        fig.append_trace(
            go.Scatter(
                x=tw_other["s"],
                y=tw_other["betx"],
                mode="lines",
                showlegend=True,
                name=r"$\beta_x \text{{{}}}$".format(" " + name_2),
                # legendgroup="1",
            ),
            row=1,
            col=1,
        )

        fig.append_trace(
            go.Scatter(
                x=tw_other["s"],
                y=tw_other["bety"],
                mode="lines",
                showlegend=True,
                name=r"$\beta_y \text{{{}}}$".format(" " + name_2),
                visible="legendonly",
                # legendgroup="1",
            ),
            row=1,
            col=1,
        )

    fig.append_trace(
        go.Scatter(
            x=tw_part["s"],
            y=tw_part["x"],
            mode="lines",
            showlegend=True,
            name=r"$x \text{{{}}}$".format(" " + name_1),
            xaxis="x",
            yaxis="y2",
            # legendgroup="2",
        ),
        row=2,
        col=1,
    )

    fig.append_trace(
        go.Scatter(
            x=tw_part["s"],
            y=tw_part["y"],
            mode="lines",
            showlegend=True,
            name=r"$y \text{{{}}}$".format(" " + name_1),
            xaxis="x",
            yaxis="y2",
            visible="legendonly",
            # legendgroup="2",
        ),
        row=2,
        col=1,
    )
    if tw_other is not None:
        fig.append_trace(
            go.Scatter(
                x=tw_other["s"],
                y=tw_other["x"],
                mode="lines",
                showlegend=True,
                name=r"$x \text{{{}}}$".format(" " + name_2),
                xaxis="x",
                yaxis="y2",
                # legendgroup="2",
            ),
            row=2,
            col=1,
        )

        fig.append_trace(
            go.Scatter(
                x=tw_other["s"],
                y=tw_other["y"],
                mode="lines",
                showlegend=True,
                name=r"$y \text{{{}}}$".format(" " + name_2),
                xaxis="x",
                yaxis="y2",
                visible="legendonly",
                # legendgroup="2",
            ),
            row=2,
            col=1,
        )

    fig.append_trace(
        go.Scatter(
            x=tw_part["s"],
            y=tw_part["dx"],
            mode="lines",
            showlegend=True,
            name=r"$D_x \text{{{}}}$".format(" " + name_1),
            xaxis="x",
            yaxis="y3",
            # legendgroup="3",
        ),
        row=3,
        col=1,
    )

    fig.append_trace(
        go.Scatter(
            x=tw_part["s"],
            y=tw_part["dy"],
            mode="lines",
            showlegend=True,
            name=r"$D_y \text{{{}}}$".format(" " + name_1),
            xaxis="x",
            yaxis="y3",
            visible="legendonly",
            # legendgroup="3",
        ),
        row=3,
        col=1,
    )
    if tw_other is not None:
        fig.append_trace(
            go.Scatter(
                x=tw_other["s"],
                y=tw_other["dx"],
                mode="lines",
                showlegend=True,
                name=r"$D_x \text{{{}}}$".format(" " + name_2),
                xaxis="x",
                yaxis="y3",
                # legendgroup="3",
            ),
            row=3,
            col=1,
        )

        fig.append_trace(
            go.Scatter(
                x=tw_other["s"],
                y=tw_other["dy"],
                mode="lines",
                showlegend=True,
                name=r"$D_y \text{{{}}}$".format(" " + name_2),
                xaxis="x",
                yaxis="y3",
                visible="legendonly",
                # legendgroup="3",
            ),
            row=3,
            col=1,
        )

    # Update overall layout
    title_1 = (
        r"$q_{x_1} = "
        + f'{tw_part["qx"]:.5f}'
        + r"\hspace{0.5cm}"
        + r" q_{y_1} = "
        + f'{tw_part["qy"]:.5f}'
        + r"\hspace{0.5cm}"
        + r"Q'_{x_1} = "
        + f'{tw_part["dqx"]:.2f}'
        + r"\hspace{0.5cm}"
        + r" Q'_{y_1} = "
        + f'{tw_part["dqy"]:.2f}'
        + r"\hspace{0.5cm}"
        + r" \gamma_{tr_1} = "
        + f'{1/np.sqrt(tw_part["momentum_compaction_factor"]):.2f}'
    )
    title_2 = (
        r"\\ q_{x_2} = "
        + f'{tw_other["qx"]:.5f}'
        + r"\hspace{0.5cm}"
        + r" q_{y_2} = "
        + f'{tw_other["qy"]:.5f}'
        + r"\hspace{0.5cm}"
        + r"Q'_{x_2} = "
        + f'{tw_other["dqx"]:.2f}'
        + r"\hspace{0.5cm}"
        + r" Q'_{y_2} = "
        + f'{tw_other["dqy"]:.2f}'
        + r"\hspace{0.5cm}"
        + r" \gamma_{tr_2} = "
        + f'{1/np.sqrt(tw_other["momentum_compaction_factor"]):.2f}'
        + r"$"
    )
    title = title_1 + r"$"
    if tw_other is not None:
        title = title_1 + title_2
    fig.update_layout(
        title_text=title,  # "Transverse dynamics evolution with crossing angle",
        title_x=0.5,
        showlegend=True,
        xaxis_showgrid=True,
        yaxis_showgrid=True,
        # xaxis_title=r'$s$',
        # yaxis_title=r'$[m]$',
        width=1000,
        height=1000,
        legend_tracegroupgap=200,
        # dragmode="pan",
        template="plotly_white",
        # uirevision="Don't change",
    )

    # Update yaxis properties
    fig.update_yaxes(
        title_text=r"$\beta_{x,y}$ [m]", row=1, col=1
    )  # , range=[0, 10000], row=1, col=1)
    fig.update_yaxes(
        title_text=r"(Closed orbit)$_{x,y}$ [m]", row=2, col=1
    )  # , range=[-0.05, 0.05], row=2, col=1)
    fig.update_yaxes(
        title_text=r"$D_{x,y}$ [m]", range=[-1.5, 2.5], row=3, col=1
    )  # , row=3, col=1)
    fig.update_xaxes(title_text=r"$s$", row=3, col=1)
    # fig.update_yaxes(fixedrange=True)

    # # Add range slider
    # fig.update_layout(
    #     xaxis=dict(
    #         rangeslider=dict(visible=True),
    #         type="linear",
    #         range=(10, 20),
    #     )
    # )

    return fig
