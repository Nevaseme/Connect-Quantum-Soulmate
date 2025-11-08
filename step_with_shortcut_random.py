"""
方法概要：
このプログラムは Qiskit の `CouplingMap` 機能を用いて、
量子ビットが環状（リング状）に接続されたネットワークを生成し、
その上にランダムに「ショートカット」を追加していきます。
各ショートカット数に対して、`CouplingMap.distance_matrix` により
すべての量子ビット間の最短距離を計算し、
その中で最も長い距離（= 最も離れた量子ビット間の距離）を
量子回路の「深さ」の近似値として評価します。
Qiskit の CouplingMap クラスを使うことで、
量子デバイス上の結合関係（隣接関係）を簡単にシミュレートできます。
"""

import numpy as np
import matplotlib.pyplot as plt
import random
from qiskit.transpiler import CouplingMap

# === パラメータ設定 ===
N = 500                         # リング構造のノード（量子ビット）数
shortcut_range = range(0, 100)  # 追加するショートカットの数
trials_per_shortcut = 10        # 各ショートカット数での平均化試行回数

# ヘルパー関数：与えられた2つのノード a, b がリング上で隣接しているかを判定
def are_ring_neighbors(a, b, n):
    d = (a - b) % n
    return d == 1 or d == n - 1

# === メイン処理 ===
avg_depth_steps = []   # 各ショートカット数における平均「最大距離（深さ）」を格納

for num_shortcuts in shortcut_range:
    depth_list = []

    for _ in range(trials_per_shortcut):
        # リング構造の CouplingMap を作成
        cm = CouplingMap.from_ring(N)
        added_undirected = set()

        # ショートカット（双方向エッジ）を追加
        while len(added_undirected) < num_shortcuts:
            a, b = random.sample(range(N), 2)
            if are_ring_neighbors(a, b, N):
                continue  # 元々隣接している場合はスキップ
            key = tuple(sorted((a, b)))
            if key in added_undirected:
                continue  # すでに追加済みのエッジはスキップ
            cm.add_edge(a, b)
            cm.add_edge(b, a)
            added_undirected.add(key)

        # 距離行列を計算し、有限値の中で最大距離を取得（深さの近似）
        dm = cm.distance_matrix
        finite = dm[np.isfinite(dm)]
        max_step = np.nanmax(finite)
        depth_list.append(max_step)

    # 各ショートカット数に対して、平均最大距離を計算
    avg_depth_steps.append(np.mean(depth_list))

# === プロット ===
plt.figure(figsize=(6, 4))
plt.plot(shortcut_range, avg_depth_steps, "o", label="Step (depth)")  # ← 去掉 '-'
plt.xlabel("Number of shortcuts")
plt.ylabel("Step (depth)")
plt.title(f"Small-world effect on circuit depth (N={N})")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()