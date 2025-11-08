# quantum-communication   
## Simulation of GHZ state generation  
### Overview

This repo studies how small-world style shortcuts on a ring topology affect the effective circuit depth for generating GHZ states. We use:

hubgraph.py to visualize hub shortcuts (one center node connecting to many),
graph_pairs.py to visualize arbitrary pairs as shortcuts,
nbits_GHZ_simulation_2.ipynb to run a simple spreading model as a proxy for GHZ depth, comparing boxplots across shortcut counts.

Key finding:

Hub network:
With a few shortcuts (≈ 10 lines), the average distance drops quickly.
However, it shows larger variance, indicating unstable efficiency.

Random network:

As the number of shortcuts increases (≈ 50–100 lines), it achieves lower average steps and more stable results than the hub model.

→ The hub topology accelerates early spreading, while random connections achieve globally shorter paths when shortcuts are dense.


### [Team "Connect-Quantum-Soulmate"](https://github.com/Nevaseme/Connect-Quantum-Soulmate)
| name | github | role |
|-------|--------|---------|
|Daiki Murata|[@daimurat](https://github.com/daimurat)|IBM Mentor|
|Soichiro Imamura|[@soichiro524](https://github.com/soichiro524)|Student Mentor|
|Yuta Kimura|[@yutaki0702](https://github.com/yutaki0702)|Code development|
|Naoya Kawata|[@naokawa1211-lab](https://github.com/naokawa1211-lab)|Code development|
|Tseng YuChih|[@alkaid7777](https://github.com/alkaid7777)|Code development|
|Takumi Okubo|[@Nevaseme](https://github.com/Nevaseme)|Code development|
