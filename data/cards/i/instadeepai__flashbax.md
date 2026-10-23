# instadeepai/flashbax

⭐ 281 · Python · Apache-2.0 · 推送 2026-08-27 · [GitHub](https://github.com/instadeepai/flashbax) · [官网](https://instadeepai.github.io/flashbax/) · 组织维护

**面向 JAX 强化学习的加速经验回放缓冲区库**

InstaDeep 维护的 Python 库，为强化学习提供可在 jax.jit/jax.pmap 完全编译函数中使用的经验回放缓冲区，包括 Flat Buffer、Trajectory Buffer、Item Buffer、Prioritised 变体与 FIFO 队列。缓冲区均以轨迹缓冲区为基座构建，要求按时间步顺序添加数据；提供 Vault 机制将缓冲区按时间轴切片持久化到磁盘以支持离线 RL，并附多个 Colab 示例（DQN/PPO/Anakin 等）。通过 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Flat/Trajectory/Item Buffer 及 Prioritised 变体，兼容 jax.jit 与 jax.pmap
- Vault 将缓冲区切片写入磁盘，支持离线 RL 的大容量经验存储
- FIFO 队列结构可用于 on-policy 算法
- 提供 Colab 示例（DQN、PPO、Anakin 架构等）

## 适用场景

- 在 JAX 中构建端到端 jit 编译的 RL 训练循环并使用回放缓冲区
- 离线强化学习中将大规模经验数据持久化到磁盘并按需载入
- R2D2 等循环网络算法中采样多步轨迹

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L31: Flashbax is a library designed to streamline the use of experience replay buffers within the context of reinforceme
> L33: Flashbax provides an implementation of various different types of buffers, such as Flat Buffer, Trajectory Buffer, 

## 星数曲线

```mermaid
xychart-beta
    title "instadeepai/flashbax 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 280 --> 282
    line [281, 281]
```

2026-10-18 281 → 2026-10-23 281（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `05a834fb809f` · [字段定义](../../DATASET.md)*
