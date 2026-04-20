# Pragati-Flow: AI-Driven Emergency Green Corridors
Pragati-Flow is an intelligent, decentralized traffic management system designed to restore the "Golden Hour" for emergency vehicles in dense Indian metropolitan areas. By leveraging Multi-Agent Reinforcement Learning (MARL) and real-time C-V2X communication, the system transforms static traffic signals into life-saving adaptive agents.

# 🚑 The "Why" behind the Project
In India, traffic congestion is more than a delay—it is a barrier to survival.

The Crisis: Approximately 30% of emergency deaths in India occur because ambulances cannot reach hospitals within the critical first hour.

The Problem: Current traffic systems use fixed timers that cannot adapt to real-time emergency needs or the chaotic, "lane-less" nature of Indian roads.

The Solution: Pragati-Flow treats every intersection as an intelligent agent that can preemptively clear a "Green Corridor" for ambulances, reducing transit times by an estimated 20–30%.

# 🚀 Key Features
Decentralized Multi-Agent RL: Individual signal controllers (Agents) learn optimal timings using Deep Q-Networks (DQN) while coordinating with neighboring signals to prevent upstream bottlenecks.

Heterogeneous Traffic Perception: Integrated YOLOv11 vision model fine-tuned to detect and weigh different Indian vehicle classes (autos, bikes, buses).

C-V2X Emergency Preemption: Real-time communication protocol allowing ambulances to request priority from signals up to 1km away.

Acoustic Fallback: A CNN-based audio module that detects Indian ambulance sirens, providing a fail-safe during low-visibility conditions like monsoon rain or heavy fog.

Edge-First Architecture: Designed to run locally on NVIDIA Jetson modules, ensuring real-time response even during network outages.

# 🛠️ Tech Stack
Simulation: SUMO (Simulation of Urban MObility)

AI Frameworks: PyTorch, Stable Baselines3

Vision: YOLOv11, OpenCV

Language: Python 3.10+

Connectivity: TraCI (Traffic Control Interface)

# 📂 Project Structure
Pragati-Flow/
├── simulation/            # SUMO net, route, and configuration files
├── src/                   # Core Python implementation
│   ├── agent.py           # RL Decision logic
│   ├── perception.py      # Computer Vision / YOLO logic
│   └── preemption.py      # V2I and Siren Detection logic
├── data/                  # Trained models and log files
├── docs/                  # Technical Proposal and Diagrams
└── README.md
