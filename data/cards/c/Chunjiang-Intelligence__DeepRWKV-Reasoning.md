# Chunjiang-Intelligence/DeepRWKV-Reasoning

⭐ 26 · Python · GPL-3.0 · 推送 2025-12-07 · [GitHub](https://github.com/Chunjiang-Intelligence/DeepRWKV-Reasoning) · 组织维护

**面向 RWKV 的测试时 MCTS 搜索框架，增强 LLM 推理**

为 RWKV 架构设计的测试时推理框架：以异步 Monte Carlo Tree Search 引擎为核心，部署多个搜索策略（PUCT、KL-UCB、Thompson Sampling）并行探索，通过共识机制汇聚结果。利用 RWKV 固定尺寸状态张量实现低成本的节点克隆与状态切换，支持可选的 MLP ValueHead 学习值函数（带启发式回退），并内置 D3.js 前端的实时搜索树可视化。需要 Python 3.8+、PyTorch 2.0+ CUDA 与 24GB+ 显存的 NVIDIA GPU，需自行下载预训练 RWKV 模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多策略并行 MCTS（PUCT / KL-UCB / Thompson Sampling）+ 共识投票
- 利用 RWKV 固定尺寸状态张量实现高效节点克隆与状态切换
- 可训练的 MLP ValueHead，未训练时回退到启发式评估
- 内置 D3.js 实时 MCTS 搜索树可视化（localhost:5001）

## 适用场景

- 在 RWKV 模型上运行测试时树搜索以增强推理
- 实时观察 MCTS 搜索树与各策略的投票过程
- 用自己的奖励数据训练 Value Head 提升搜索质量

## 场景标签

 · 领域:LLM 推理/搜索算法

## 证据(README 行号)

> L5: DeepRWKV-Reasoning is a framework designed to enhance the reasoning capabilities of Large Language Models through so
> L11: - Parallel Universe MCTS: Deploys multiple MCTS engines, each with a unique search strategy (PUCT, KL-UCB, Thompson
> L15: - Asynchronous & High-Performance: Built on `asyncio` to handle thousands of concurrent simulations, with a design 

## 星数曲线

```mermaid
xychart-beta
    title "Chunjiang-Intelligence/DeepRWKV-Reasoning 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `a8063741b6d3` · [字段定义](../../DATASET.md)*
