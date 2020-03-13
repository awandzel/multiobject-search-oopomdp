# OOPOMDP MultiObject Search

This repository contains the codes for our ICRA 2019 paper. For more details, please refer to the paper: [Arthur Wandzel, Yoonseon Oh, Michael Fishman, Nishanth Kumar, Lawson L.S. Wong, and Stefanie Tellex,  Multi-Object Search using Object-Oriented POMDPs](http://www.ccs.neu.edu/home/lsw/papers/icra2019-mop.pdf)

# Abstract
A core capability of robots is to reason about multiple objects under uncertainty. Partially Observable Markov Decision Processes (POMDPs) provide a means of reasoning under uncertainty for sequential decision making, but are computationally intractable in large domains. In this paper, we propose Object-Oriented POMDPs (OO-POMDPs), which represent the state and observation spaces in terms of classes and objects. The structure afforded by OO-POMDPs support a factorization of the agent’s belief into independent object distributions, which enables the size of the belief to scale linearly versus exponentially in the number of objects. We formulate a novel Multi-Object Search (MOS) task as an OO-POMDP for mobile robotics domains in which the agent must find the locations of multiple objects. Our solution exploits the structure of OO-POMDPs by featuring human language to selectively update the belief at task onset. Using this structure, we develop a new algorithm for efficiently solving OO-POMDPs: Object- Oriented Partially Observable Monte-Carlo Planning (OO- POMCP). We show that OO-POMCP with grounded language commands is sufficient for solving challenging MOS tasks both in simulation and on a physical mobile robot.

*Keywords: multi-object search, grounded language, POMDPs, reinforcement learning*
[Video](https://www.youtube.com/watch?v=ssmez0rjF1Y)



