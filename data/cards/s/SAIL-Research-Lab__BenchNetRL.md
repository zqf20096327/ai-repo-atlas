# SAIL-Research-Lab/BenchNetRL

⭐ 40 · Python · MIT · 推送 2026-01-22 · [GitHub](https://github.com/SAIL-Research-Lab/BenchNetRL) · [官网](https://arxiv.org/abs/2505.15040) · 组织维护

**强化学习中神经网络架构的基准测试套件：横评 PPO 变体**

面向科研用户的 RL 架构基准：在同一 PPO 训练框架下实现并对比 vanilla PPO、LSTM/GRU、Transformer-XL/GTrXL、Mamba/Mamba-2 等骨干网络，在 Atari、MuJoCo、MiniGrid、OpenAI Gym 等多类环境的 9 个任务上度量步速、训练时间、推理延迟与 GPU 显存占用，提供可复现脚本与自定义实验入口。安装走源码 clone + pip 依赖，CUDA 为推荐配置；Mamba/SSM 模块需单独安装且要求 Linux 与特定 CUDA 驱动。附 arXiv 2025 论文引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 PPO 框架下实现 8 种骨干架构（PPO/LSTM/GRU/TrXL/GTrXL/Mamba/Mamba-2）
- 9 个环境上的步速/训练时间/推理延迟/GPU 显存指标对比
- scripts/ours/ 提供可复现基准脚本
- 附 2025 年 arXiv 论文引用条目

## 适用场景

- 为我的 RL 任务选择合适的网络骨干架构
- 复现论文中的跨架构基准实验结果
- 对比序列模型在部分可观测环境下的表现

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L140: ## 📈 Performance Metrics - Average Across 9 Environments
> L105: Use the provided scripts under `scripts/ours/` to launch our experiments. For example:

## 星数曲线

```mermaid
xychart-beta
    title "SAIL-Research-Lab/BenchNetRL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-26 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `9ba129963a46` · [字段定义](../../DATASET.md)*
