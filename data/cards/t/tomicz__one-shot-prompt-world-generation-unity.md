# tomicz/one-shot-prompt-world-generation-unity

⭐ 14 · 推送 2026-10-21 · [GitHub](https://github.com/tomicz/one-shot-prompt-world-generation-unity) · [官网](https://darkounity.com/unity-ai?utm_source=github&utm_campaign=world-generation) · 个人维护

**单条提示驱动 AI 编码代理在 Unity 中生成完整 3D 地形**

面向 Unity 2022.3+ URP 工程的提示词工程仓库：核心是 WORLD-GENERATION-PROMPT.md，其中包含全局规则与 6 个层次提示，让 Claude Code、Cursor、Windsurf、Copilot 等 AI 编码代理自主生成程序化 3D 景观（地形网格、纹理、河流水面、松林、光照后处理、天空云层）。提供两条执行路径：经 Unity MCP 的 execute_code 直接在编辑器内运行代码，或由代理写出 [MenuItem] C# 编辑器脚本供用户手动执行。每次运行按模型名+日期生成独立 run ID 目录以隔离对比多个代理结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 层提示序列驱动代理生成地形/纹理/水面/植被/光照/天空
- 两条执行路径：Unity MCP 直接执行代码或 C# 编辑器脚本
- 按模型名+日期自动生成 run ID，隔离多次运行便于代理间对比
- 关键规则：资产从零生成、层只增不改、道具以射线放置

## 适用场景

- 用一条提示让 AI 代理在 Unity 编辑器内自动搭建程序化 3D 地形
- 对比不同 AI 编码代理（Claude Code/Cursor 等）的生成能力
- 学习面向编辑器代理的提示词工程与 MCP 集成方式

## 场景标签

`提示工程` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L3: A single prompt that drives an AI coding agent to generate a complete procedural 3D landscape inside the Unity Edito
> L47: **Option A — with repo cloned:**

## 星数曲线

```mermaid
xychart-beta
    title "tomicz/one-shot-prompt-world-generation-unity 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `083c71de4c1c` · [字段定义](../../DATASET.md)*
