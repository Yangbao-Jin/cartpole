import gym
from stable_baselines3 import PPO

def test_agent(model_path):
    # 创建 CartPole 环境，启用人类模式渲染
    env = gym.make("CartPole-v1", render_mode="human")  # 指定 render_mode 为 human

    # 加载训练好的模型
    print("Loading trained model...")
    model = PPO.load(model_path)

    # 测试并渲染
    obs, _ = env.reset()  # 解包元组，提取状态值
    total_reward = 0
    for _ in range(2000):  # 测试 1000 步
        action, _ = model.predict(obs, deterministic=True)  # 确定性策略
        # 修改这里：解包返回值
        obs, reward, terminated, truncated, _ = env.step(action)
        total_reward += reward  
        if terminated or truncated:  # 处理结束状态
            print(f"Episode finished with total reward: {total_reward}")
            obs, _ = env.reset()  # 重新初始化
            total_reward = 0

    env.close()
