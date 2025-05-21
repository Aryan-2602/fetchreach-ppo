import gymnasium as gym
import torch
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.monitor import Monitor
from src.wrappers import Float32Wrapper
from stable_baselines3.common.evaluation import evaluate_policy
import os

def train_agent():
    print(f"Using device: {'mps' if torch.backends.mps.is_available() else 'cpu'}")
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

    env = gym.make("FetchReach-v3", render_mode="human")
    env = Float32Wrapper(env)
    env = Monitor(env)
    env = DummyVecEnv([lambda: env])

    model = PPO("MultiInputPolicy", env, verbose=1, device=device)
    model.learn(total_timesteps=50000)

    os.makedirs("models", exist_ok=True)
    model.save("models/ppo_fetchreach_gymnasium")

    mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10)
    print(f"Mean reward: {mean_reward:.2f} ± {std_reward:.2f}")