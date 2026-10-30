# bhansconnect/alphazero-pybind11

⭐ 21 · Python · BSD-3-Clause · 推送 2026-07-28 · [GitHub](https://github.com/bhansconnect/alphazero-pybind11) · 个人维护

**C++ 加速核心的 AlphaZero 修改实现，面向强化学习开发者**

AlphaZero 的修改版实现：游戏主循环与 MCTS 搜索用 C++（pybind11 封装）实现以提升性能并降低内存占用，神经网络与数据打包使用 Python/PyTorch。借鉴 Learning From Scratch by Thinking Fast and Slow 论文思路并加入局面缓存等自有修改。通过 uv 管理环境，提供训练、锦标赛、交互对弈与 MCTS 分析入口；新增游戏需实现 game_state 接口并编辑 meson 构建文件后重新编译。支持 Linux/macOS，CUDA 为可选 GPU 路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 游戏循环与 MCTS 用 C++ 实现，Python 负责神经网络
- 提供训练、锦标赛、交互对弈与 MCTS 阈值分析 CLI 入口
- 局面缓存等自有修改，基于 uv 环境管理（Python 3.11 + PyTorch）
- 可通过实现 game_state 接口与编辑 meson 构建添加新游戏

## 适用场景

- 训练 AlphaZero 风格的自博弈强化学习智能体（如 Connect4）
- 让多个训练好的网络进行锦标赛评估
- 交互式对弈与分析 MCTS 搜索阈值

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: This is a modified implementation of AlphaZero. It takes some inspiration from Learning From Scratch by Thinking Fas
> L75:  - `src/train.py`: CLI entry point for training.

## 星数曲线

```mermaid
xychart-beta
    title "bhansconnect/alphazero-pybind11 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `aae00f37cbea` · [字段定义](../../DATASET.md)*
