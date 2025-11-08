# -*- coding: utf-8 -*-
# 例:
#   python graph.py                     -> N=22, ショートカットなし
#   python graph.py -N 23 --targets 5 12 17 20
#   python graph.py -N 22 --targets 4 8 13 17
#   python graph.py -N 22 --center 5 --targets 7 12 18
import argparse
import sys
import matplotlib.pyplot as plt
import networkx as nx

def parse_args():
    p = argparse.ArgumentParser(description="Ring with shortcuts from a center qubit")
    p.add_argument("-N", type=int, default=22, help="number of qubits (nodes)")
    p.add_argument("--center", type=int, default=0, help="shortcut元のビット番号")
    p.add_argument("--targets", type=int, nargs="*", help="ショートカット先のビット番号(複数可)")
    return p.parse_args()

def main():
    args = parse_args()
    N = args.N
    c = args.center

    if N < 3:
        sys.exit("Nは3以上にして。")
    if not (0 <= c < N):
        sys.exit("centerが範囲外。")

    # ターゲット確定
    if args.targets:
        # 重複/範囲/自分自身を除外してクリーンアップ
        T = sorted({t for t in args.targets if 0 <= t < N and t != c})
        if not T:
            sys.exit("有効なtargetsが空。")
    else:
        T = []

    # グラフ構築（リング + ショートカット）
    G = nx.Graph()
    G.add_nodes_from(range(N))
    ring_edges = [(i, (i + 1) % N) for i in range(N)]
    G.add_edges_from(ring_edges)
    shortcut_edges = [(c, t) for t in T]

    # 配置は円周上
    pos = nx.circular_layout(G, scale=1.0)
    pos = {node: (coords[1], -coords[0]) for node, coords in pos.items()}

    # 描画
    plt.figure(figsize=(6, 6), dpi=140)
    # 中心ノードは赤、それ以外は青
    others = [i for i in range(N) if i != c]
    nx.draw_networkx_nodes(G, pos, nodelist=others, node_color='royalblue', node_size=180)
    nx.draw_networkx_nodes(G, pos, nodelist=[c], node_color='red', node_size=220)
    nx.draw_networkx_edges(G, pos, edgelist=ring_edges, width=1.0, edge_color='lightgray')
    nx.draw_networkx_edges(G, pos, edgelist=shortcut_edges, width=2.0, edge_color='purple', alpha=0.7)
    nx.draw_networkx_labels(G, pos, labels={i: str(i) for i in range(N)}, font_size=7)

    plt.title(f"Ring Shortcuts (N={N}, center={c}, targets={T})", fontsize=10)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
