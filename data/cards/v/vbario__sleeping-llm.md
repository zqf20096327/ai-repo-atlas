# vbario/sleeping-llm

⭐ 81 · Python · 推送 2026-10-11 · [GitHub](https://github.com/vbario/sleeping-llm) · 个人维护

**通过睡眠周期将对话事实固化为持久权重记忆的语言模型**

面向研究者的语言模型记忆系统：清醒期用 MEMIT 将对话中的事实直接注入模型权重（无检索、无数据库），睡眠期执行 8 步维护循环，审计并刷新退化记忆，再通过逐事实门控的 LoRA 整合将知识从 MEMIT 缓冲转移到融合权重。基于 MLX（Apple Silicon）与 PyTorch（CUDA）双后端，支持 3B 到 70B 模型，附 5 篇论文、可复现实验脚本与 122 条开发笔记。限制：实验仅用合成三元组事实、MEMIT 仅走原始补全通路、单次实验无误差线。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MEMIT 清醒期权重注入 + 睡眠期零空间约束维护
- LoRA 逐事实分级整合（stage 0-3），MEMIT 编辑按阶段消解以释放容量
- 支持 MLX 与 PyTorch 双后端，覆盖 MacBook Air M3 到 2x H100 硬件
- 提供 5 篇论文 DOI、实验复现脚本与 122 条开发笔记

## 适用场景

- 在本地模型中形成并维护对话持久记忆
- 研究知识编辑与持续学习的整合机制
- 复现清醒容量阈值与睡眠收敛实验

## 场景标签

`Agent 记忆` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L3: A language model that forms persistent memories from conversation and consolidates them through sleep.
> L5: During **wake**, facts are injected directly into model weights via MEMIT — no retrieval, no database, no context st
> L74: |1|**Sleep-Wake Consolidation for Lifelong Conversational Memory in Local Language Models** — LoRA sleep-wake on 3B

## 星数曲线

```mermaid
xychart-beta
    title "vbario/sleeping-llm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-28 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `211df75eeebb` · [字段定义](../../DATASET.md)*
