"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

import os
import pandas as pd
import matplotlib.pyplot as plt


def pregunta_01():

    os.makedirs("files/plots", exist_ok=True)

    df = pd.read_csv("files/input/news.csv", index_col=0)

    plt.figure(figsize=(8, 6))

    plt.plot(df.index, df["Television"], color="dimgray", linewidth=2)
    plt.plot(df.index, df["Newspaper"], color="gray", linewidth=2)
    plt.plot(df.index, df["Internet"], color="#1f77b4", linewidth=3)
    plt.plot(df.index, df["Radio"], color="lightgray", linewidth=2)

    plt.scatter(df.index[-1], df["Television"].iloc[-1], color="dimgray", s=40)
    plt.scatter(df.index[-1], df["Newspaper"].iloc[-1], color="gray", s=40)
    plt.scatter(df.index[-1], df["Internet"].iloc[-1], color="#1f77b4", s=40)
    plt.scatter(df.index[-1], df["Radio"].iloc[-1], color="lightgray", s=40)

    plt.scatter(df.index[0], df["Television"].iloc[0], color="dimgray", s=40)
    plt.scatter(df.index[0], df["Newspaper"].iloc[0], color="gray", s=40)
    plt.scatter(df.index[0], df["Internet"].iloc[0], color="#1f77b4", s=40)
    plt.scatter(df.index[0], df["Radio"].iloc[0], color="lightgray", s=40)

    plt.title("How people get their news", fontsize=20, pad=20)
    plt.suptitle(
        "An increasing proportion cite the internet as their primary news source",
        fontsize=10,
        y=0.88,
    )

    plt.text(df.index[0] - 0.3, df["Television"].iloc[0], "Television 74%", color="dimgray", ha="right", va="center", fontsize=12)
    plt.text(df.index[0] - 0.3, df["Newspaper"].iloc[0], "Newspaper 45%", color="gray", ha="right", va="center", fontsize=12)
    plt.text(df.index[0] - 0.3, df["Radio"].iloc[0], "Radio 18%", color="lightgray", ha="right", va="center", fontsize=12)
    plt.text(df.index[0] - 0.3, df["Internet"].iloc[0], "Internet 13%", color="#1f77b4", ha="right", va="center", fontsize=12)

    plt.text(df.index[-1] + 0.2, df["Television"].iloc[-1], "66%", color="dimgray", va="center", fontsize=12)
    plt.text(df.index[-1] + 0.2, df["Newspaper"].iloc[-1], "31%", color="gray", va="center", fontsize=12)
    plt.text(df.index[-1] + 0.2, df["Internet"].iloc[-1], "41%", color="#1f77b4", va="center", fontsize=12)
    plt.text(df.index[-1] + 0.2, df["Radio"].iloc[-1], "16%", color="lightgray", va="center", fontsize=12)

    plt.xlim(2000.5, 2010.8)
    plt.ylim(10, 85)

    plt.xticks(df.index)
    plt.yticks([])

    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    plt.tight_layout()

    plt.savefig("files/plots/news.png")
    plt.close()

