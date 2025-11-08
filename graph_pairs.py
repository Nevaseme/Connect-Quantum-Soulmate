# -*- coding: utf-8 -*-
# 例:
#   python graph_pairs_tuples.py -N 22 --pairs "[(0,4),(7,12),(15,19),(3,17)]"
#   python graph_pairs_tuples.py -N 50 --pairs "[(2,27),(14,39),(21,45)]"

import argparse
import sys
import ast
import math
import matplotlib.pyplot as plt
import networkx as nx

def parse_pairs_literal(s: str):
    try:
        obj = ast.literal_eval(s)
    except Exception as e:
        sys.exit(f"--pairs の解釈に失敗: {e}")
    if not isinstance(obj, (list, tuple)):
        sys.exit("--pairs は [(u,v), (u,v), ...] のようなリスト/タプルにして。")
    pairs = []
    for item in obj:
        if (isinstance(item, (list, tuple)) and len(item) == 2
            and all(isinstance(x, int) for x in item)):
            u, v = int(item[0]), int(item[1])
            pairs.append(tuple(sorted((u, v))))  # 無向なので正規化
        else:
            sys.exit(f"不正なペア: {item}（(u,v) 形式の整数タプルにして）")
    # 重複除去・ソート
    return sorted(set(pairs))

def circular_positions_with_q0_bottom(N: int):
    # 角度 θ_i = 2π*i/N - π/2 にすることで i=0 が (0,-1)（真下）に来る
    pos = {}
    for i in range(N):
        theta = 2.0 * math.pi * i / N - math.pi / 2.0
        pos[i] = (math.cos(theta), math.sin(theta))
    return pos

def main():
    ap = argparse.ArgumentParser(description="Ring with user-specified shortcut pairs (tuple literal).")
    ap.add_argument("-N", type=int, default=22, help="number of qubits (nodes)")
    ap.add_argument("--pairs",
                    help='ショートカットのペア（Pythonリテラル）。例: "[(0,4),(7,12)]"')
    args = ap.parse_args()

    N = args.N
    if N < 3:
        sys.exit("Nは3以上にして。")

    if args.pairs:
        shortcut_pairs = parse_pairs_literal(args.pairs)
    else:
        shortcut_pairs = []

    # 検証
    for (u, v) in shortcut_pairs:
        if not (0 <= u < N and 0 <= v < N):
            sys.exit(f"範囲外のノード番号: {(u, v)} (0 ≤ node < {N})")
        if u == v:
            sys.exit(f"自己ループは不可: {(u, v)}")

    # リング（隣接ペアは冗長なので警告のみ）
    if shortcut_pairs:
        ring_edges = {(i, (i + 1) % N) if i < (i + 1) % N else ((i + 1) % N, i)
                      for i in range(N)}
        redundant = [e for e in shortcut_pairs if e in ring_edges]
        if redundant:
            print(f"注意: リング隣接を含むペア（ショートカットとして冗長）: {redundant}")

    # グラフ構築
    G = nx.Graph()
    G.add_nodes_from(range(N))
    G.add_edges_from([(i, (i + 1) % N) for i in range(N)])  # リング
    G.add_edges_from(shortcut_pairs)                         # ショートカット

    # 位置: q0を真下に
    pos = circular_positions_with_q0_bottom(N)

    # ショートカットに関与するノードを強調
    sc_nodes = set()
    for u, v in shortcut_pairs:
        sc_nodes.add(u)
        sc_nodes.add(v)
    zero_node = 0
    others = [i for i in range(N) if i not in sc_nodes and i != zero_node]
    hot = [i for i in sorted(sc_nodes) if i != zero_node]

    plt.figure(figsize=(7, 7), dpi=140)
    nx.draw_networkx_nodes(G, pos, nodelist=[zero_node], node_color='royalblue', node_size=240)
    nx.draw_networkx_nodes(G, pos, nodelist=others, node_color='royalblue', node_size=180)
    nx.draw_networkx_nodes(G, pos, nodelist=hot, node_color='royalblue', node_size=220)
    nx.draw_networkx_edges(G, pos, edgelist=[(i, (i + 1) % N) for i in range(N)],
                           width=1.0, edge_color='lightgray')
    nx.draw_networkx_edges(G, pos, edgelist=shortcut_pairs,
                           width=2.4, edge_color='purple', alpha=0.85)
    nx.draw_networkx_labels(G, pos, labels={i: str(i) for i in range(N)}, font_size=7)

    plt.title(f"Ring Shortcuts (N={N})\nPairs: {shortcut_pairs}\n(q0 is at bottom)", fontsize=10)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
