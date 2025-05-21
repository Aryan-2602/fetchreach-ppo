import gymnasium as gym
import numpy as np

class Float32Wrapper(gym.ObservationWrapper):
    def __init__(self, env):
        super().__init__(env)

        # Update each sub-space in the Dict to float32
        original_spaces = self.observation_space.spaces
        self.observation_space = gym.spaces.Dict({
            k: gym.spaces.Box(
                low=np.float32(v.low),
                high=np.float32(v.high),
                dtype=np.float32
            ) if isinstance(v, gym.spaces.Box) else v
            for k, v in original_spaces.items()
        })

    def observation(self, observation):
        return {
            k: v.astype(np.float32) if isinstance(v, np.ndarray) and v.dtype != np.float32 else v
            for k, v in observation.items()
        }