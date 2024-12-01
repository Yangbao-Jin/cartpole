CartPole Project
项目描述
本项目基于 OpenAI Gym 提供的 CartPole 环境。
使用 Stable-Baselines3 的 PPO 算法训练智能体，使其能够平衡小车上的杆子。
包含模型的测试和 2D 动画渲染。训练代码另行发布。

项目目录：
複製程式碼
cartpole_project/
├── main_test.py        # 主运行文件
├── test.py             # 模型测试和渲染脚本
├── requirements.txt    # 项目依赖
├── README.md           # 项目说明

克隆项目
在终端中运行以下命令克隆仓库并进入项目目录：
git clone https://github.com/Yangbao-Jin/cartpole](https://github.com/Yangbao-Jin/cartpole/tree/V1.0
cd cartpole

创建虚拟环境并安装依赖
为了确保项目运行环境的一致性，请使用以下命令创建虚拟环境并安装依赖：

Linux/MacOS 终端运行命令:
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

Windows 终端运行命令:
python -m venv env
env\Scripts\activate
pip install -r requirements.txt


运行项目
确保依赖安装完成后，运行以下命令启动项目：
python3 main_test.py
