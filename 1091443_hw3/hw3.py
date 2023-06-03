import logomaker

# 設定序列列表和參數
with open("static/example.txt", "r") as f:
    sequences = [line.strip() for line in f]
    print(sequences)
colors ={
    "A": "red",
    "B":"orange",
    "C":"yellow",
    "D":"green",
    "E":"blue",
    "F":"purple",
    "G":"black",
    "H":"grey",
    "I":"pink",
    "J":"brown",
    "K":"c",
    "L":"lime",
    "M":"salmon",
    "N":"navy",
    "O":"plum",
    "P":"violet",
    "Q":"teal",
    "R":"lavender",
    "S":"aqua",
    "T":"m",
    "U":"greenyellow",
    "V":"orchid",
    "W":"tan",
    "X":"beige",
    "Y":"peru",
    "Z":"aquamarine"
}
counts_matrix = logomaker.alignment_to_matrix(sequences)
logo = logomaker.Logo(counts_matrix, color_scheme=colors)

# 設定圖片大小和格式
logo.style_spines(visible=False)
logo.style_xticks(rotation=90, fmt="%s")
logo.ax.set_title("My Sequence Logo")
logo.fig.set_size_inches(6, 4)
logo.fig.savefig("static/my_logo.png", dpi=300)
print("2")