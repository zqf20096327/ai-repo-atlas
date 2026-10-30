# namin/llm-verified-with-monte-carlo-tree-search

⭐ 295 · Jupyter Notebook · MIT · 推送 2026-07-21 · [GitHub](https://github.com/namin/llm-verified-with-monte-carlo-tree-search) · [官网](https://arxiv.org/abs/2402.08147) · 个人维护

**用 MCTS 引导 LLM 合成经形式化验证的代码**

研究原型 VerMCTS：将 LLM 代码生成与蒙特卡洛树搜索结合，在生成已验证程序的搜索空间中探索，每一步调用 Dafny、Coq、Lean、Scala 或 Rust 验证器检查是否在正确轨道上。附带基线、交互式、验证器反馈、PPO/DPO 训练与多样性等多种运行脚本，并支持在 Clover 基准上实验。论文获 NeurIPS 2024 Math-AI 杰出论文奖。依赖 GPU（在双 A100 机器上测试），各验证器为可选安装，Docker/Singularity 沙箱可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- MCTS 搜索空间中逐步调用验证器检查生成轨迹
- 支持 Dafny、Coq、Lean、Scala、Rust 五种验证目标
- 提供 PPO/DPO 训练器与验证器反馈、多样性选择等实验脚本
- 支持 Clover 基准数据集实验与单元测试注入

## 适用场景

- 让较弱模型在验证器辅助下合成可验证程序
- 研究 MCTS+LLM+验证器的程序合成方法
- 复现 VerMCTS 论文实验或在 Clover 基准上评测

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5: This prototype synthesizes verified code with an LLM.
> L7: Using Monte Carlo Tree Search (MCTS), it explores the space of possible generation of a verified program, and it che
> L9: This prototype uses Dafny, Coq, Lean, Scala or Rust.

## 星数曲线

```mermaid
xychart-beta
    title "namin/llm-verified-with-monte-carlo-tree-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 294 --> 296
    line [295, 295]
```

2026-10-18 295 → 2026-10-30 295（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `abd4f874ae80` · [字段定义](../../DATASET.md)*
