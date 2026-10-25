# microsoft/Mnemis

⭐ 107 · Python · MIT · 推送 2026-04-14 · [GitHub](https://github.com/microsoft/Mnemis) · 组织维护

**论文官方仓库：面向 LLM 长期记忆的双路检索框架**

ACL 2026 论文 Mnemis 的官方代码仓库，作者来自 Microsoft。框架将记忆组织为基础图与层次图，提供 System-1 相似检索与 System-2 全局选择两条互补检索路径，在 LoCoMo（93.9）与 LongMemEval-S（91.6）基准上报告评测结果（使用 GPT-4.1-mini）。实现基于 Graphiti，全局选择代码在 global_selection 目录，评测结果与生成的记忆上下文存于 results 目录。仓库当前提供论文复现相关材料，未给出安装运行命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- System-1 相似检索与 System-2 全局选择双路检索机制
- 基于基础图与层次图的记忆组织结构
- 基于 Graphiti 实现，含全局选择代码与评测结果数据
- LoCoMo 93.9 / LongMemEval-S 91.6 评测报告

## 适用场景

- 复现论文中的长期记忆检索实验
- 研究图结构与层次化检索在 LLM 记忆中的应用
- 在 LoCoMo/LongMemEval-S 基准上对比记忆框架表现

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L17: This is official repostory of paper "Mnemis: Dual-Route Retrieval on Hierarchical Graphs for Long-Term LLM Memory"
> L19: > **Abstract**: AI Memory, specifically how models organizes and retrieves historical messages, becomes increasingl
> L54: We implement Mnemis based on Graphiti. The core prompts used in our system are provided in the Appendix of the pape

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/Mnemis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 106 --> 108
    line [107, 107]
```

2026-10-18 107 → 2026-10-25 107（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ecd1ceb131b0` · [字段定义](../../DATASET.md)*
