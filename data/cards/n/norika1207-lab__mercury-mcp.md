# norika1207-lab/mercury-mcp

⭐ 43 · Python · 推送 2026-10-23 · [GitHub](https://github.com/norika1207-lab/mercury-mcp) · [官网](https://github.com/norika1207-lab/mercury-mcp) · 个人维护 · 中文 README

**面向 MCP agent 的 23 个 LLM 跨架构内部观测数据库**

在消费级硬件（一台 Mac mini 与一台 NVIDIA DGX Spark）上采集的 23 个 LLM、13 个架构家族的内部观测数据库，以 Model Context Protocol 工具形式提供给 Claude Code、Cursor、Cline、Goose 等 agent。观测分两层：Tier-A 输出层 logit 钩子做候选信号筛选，Tier-B 逐层残差流指纹做验证，含跨架构逐层对齐矩阵与锚定维度数据。提供 7 个 MCP 工具，如逐层指纹查询、跨架构等价层查找、能力组合配方生成。数据以 mmap-able 二进制 cell grid 存储，代码 MIT、数据 CC-BY-4.0。Tier-B 已完成 12/23 个模型，部分早期发现（dim 11 普遍性）正被重新定性为候选信号，方法论注意事项在论文草稿中公开修订。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 23 个 LLM、13 个架构家族的两层观测数据（Tier-A 筛选 / Tier-B 残差流验证）
- 7 个 MCP 工具：模型列表、锚定维度、逐层指纹、跨架构等价层、能力组合配方等
- 12 个 Tier-B 模型的 84 组跨架构逐层对齐矩阵（qwen-7B L15 对 falcon-7B L16 相似度 0.868）
- 数据以 mmap-able 二进制 cell grid 存储（约 24MB–840MB/模型），单模型采集约 4 小时无需 GPU

## 适用场景

- 机制可解释性研究者查询跨架构逐层功能对齐与锚定维度
- 模型合并/ Frankenstein 玩家查找功能可互换的中间层
- 应用开发者判断微调目标模型与能力所在层
- 在 Claude Code / Cursor 等 agent 中直接对话查询观测数据

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L8: Mercury MCP exposes a 23-LLM cross-architecture observation database to any agent that speaks the Model Context Prot
> L21: The agent calls Mercury MCP tools; Mercury answers from precomputed observation data.
> L61: |Family|Models|Tier-B done|

## 星数曲线

```mermaid
xychart-beta
    title "norika1207-lab/mercury-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-25 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `315eb51dbd32` · [字段定义](../../DATASET.md)*
