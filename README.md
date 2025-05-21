# 🤖 FetchReach-PPO (Gymnasium + MuJoCo)

This project uses **Proximal Policy Optimization (PPO)** to train a robotic arm in the `FetchReach-v3` environment to reach randomly placed targets using continuous control. Built with `gymnasium`, `mujoco`, and `stable-baselines3`, and optimized for Apple's M1 GPU with MPS support.

---

## 📌 Overview

- 🎯 Goal-directed robot arm training (reach task)
- 💡 PPO algorithm from Stable-Baselines3
- ⚙️ MuJoCo physics engine (Gymnasium robotics)
- 🧠 Float32-wrapper for Apple Silicon (MPS) compatibility
- 🎥 Optional video recording of agent behavior
- 📉 Reward tracking + progress plots

---

## 🛠 Setup

### 1. Clone & Environment Setup
```bash
git clone https://github.com/Aryan-2602/fetchreach-ppo.git 
cd fetchreach-ppo
conda create -n fetchreach-ppo python=3.10 -y
conda activate fetchreach-ppo
pip install -r requirements.txt
```

### 2. Run Training
```bash
python main.py
```

---

## 🧠 Dependencies

- `gymnasium[robotics]`
- `mujoco`
- `torch` (MPS-compatible)
- `stable-baselines3`
- `matplotlib`, `imageio` (for plotting/video)

See `requirements.txt` for full list.

---

## 📁 Project Structure

```
fetchreach-ppo/
├── src/                  ← training code, wrappers, utilities
├── models/               ← saved PPO models (.zip)
├── assets/               ← training plots, gifs
├── logs/                 ← (optional) logs, TensorBoard
├── main.py               ← entry point
├── README.md             ← this file
├── requirements.txt
└── .gitignore
```

---

## 📈 Training Progress

![Training Reward](assets/training_progress.png)

> Reward curve over training iterations (placeholder until plotted).

---

## 🎥 Trained Agent Demo

![FetchReach Agent](assets/fetchreach_agent.gif)

> The trained PPO agent reaching its target in simulation (placeholder until recorded).

---

## 🔬 Research Relevance

This simulation is a simplified parallel to research involving:
- **Robotic locomotion**
- **Spinal-limb coordination**
- **Goal-conditioned continuous control**

The modular design allows easy extension to more complex environments like `FetchPush`, `Ant`, or custom MuJoCo robots.

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## 🙋‍♂️ Acknowledgments

- [Gymnasium Robotics](https://robotics.farama.org/)
- [Stable-Baselines3](https://stable-baselines3.readthedocs.io/)
- [MuJoCo Physics Engine](https://mujoco.readthedocs.io/)
