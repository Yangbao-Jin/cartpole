from test import test_agent

def main_test():
    # 已训练模型的文件路径
    model_path = "ppo_cartpole_model"

    # 提示用户
    print("Starting model testing...")
    print(f"Loading model from: {model_path}")

    # 调用测试函数
    test_agent(model_path)

    print("Testing complete!")

if __name__ == "__main__":
    main_test()
