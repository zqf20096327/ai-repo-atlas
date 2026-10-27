# hlpun/Train-in-Silence

⭐ 104 · Python · MIT · 推送 2026-08-04 · [GitHub](https://github.com/hlpun/Train-in-Silence) · 个人维护 · 中文 README

**面向 LLM 微调的 GPU 选型 MCP 服务器：算 VRAM 并比价**

以 MCP server / CLI / REST API 三种形式提供的 LLM 微调硬件规划工具：用户描述一次训练任务，它估算所需 VRAM/FLOPs，聚合十余家 GPU 云的实时价格，输出成本-时间的 Pareto 前沿与排序推荐。API key 可选，未提供时自动回退到 GPUHunt/GPUFinder 聚合源或内置样例数据，并标注数据新鲜度来源。可注册为 Claude Code/Claude Desktop 的 MCP 工具。README 声明项目处于实验性开发阶段，估算模型固定、无内置校准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 按任务描述自动估算 VRAM/FLOPs 并生成硬件推荐
- 聚合 Vast.ai、RunPod、AWS、Lambda 等 10+ 云平台实时价格
- 无需 API key，可回退到通用聚合器或样例数据
- 提供 CLI、REST API 与 Claude Code/Desktop MCP 三种使用方式

## 适用场景

- 微调 LLM 前一次性确定满足 VRAM 要求且最省钱的 GPU 方案
- 在 Claude Code 中用自然语言查询跨云 GPU 训练方案
- 避免手工在多个云平台间比价和估算显存

## 场景标签

 · 领域:LLM 训练基础设施

## 证据(README 行号)

> L11: **Train in Silence** is the first **Task-Aware MCP server** for LLM fine-tuning. It doesn't just list prices; it un
> L21: claude mcp add tis --scope user -- tis-mcp
> L72: YAML request -> Estimator -> Market Aggregator -> Optimizer -> Pareto Frontier -> Ranked Output

## 星数曲线

```mermaid
xychart-beta
    title "hlpun/Train-in-Silence 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 103 --> 105
    line [104, 104]
```

2026-10-18 104 → 2026-10-27 104（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `402de092935b` · [字段定义](../../DATASET.md)*
