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


### Model 1. [CNN with Quantum Fully Connected Layer](https://github.com/yh08037/quantum-neural-network/tree/master/model1-fc)
Build MNIST multi-label classifiers using classical convolution layers and quantum fully-connected layers.

![](images/model1.png)

<p align="center">
<img src="images/hybrid.png" width="600">
</p>

### Model 2. [CNN with Quantum Convolution Layer](https://github.com/yh08037/quantum-neural-network/tree/master/model2-conv)
Build MNIST multi-label classifiers using quantum convolution layers and classical fully-connected layers.

![](images/model2.png)

![](images/quanv.png)



## References
### Model 1. [model name](url)
- [Utility-scale-quantum-computing (Quantum tokyo)](https://github.com/quantum-tokyo/introduction/blob/main/src/courses/utility-scale-quantum-computing/14_utility_3.pdf)
- [Source name (Type of Source)](Source url)

### Model 2. [CNN with Quantum Convolution Layer](https://github.com/yh08037/quantum-neural-network/tree/master/model2-conv)
- [Quanvolutional Neural Networks (Pennylane demo)](https://pennylane.ai/qml/demos/tutorial_quanvolution.html)
- [arxiv-Quanvolutional Neural Networks: PoweringImage Recognition with Quantum Circuits (arxiv)](https://arxiv.org/pdf/1904.04767.pdf)
