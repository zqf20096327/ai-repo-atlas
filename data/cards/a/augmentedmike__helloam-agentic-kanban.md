# augmentedmike/helloam-agentic-kanban

⭐ 16 · TypeScript · 推送 2026-05-25 · [GitHub](https://github.com/augmentedmike/helloam-agentic-kanban) · [官网](https://helloam.bot) · 个人维护 · 中文 README

**本地运行的个人自主 AI 智能体系统，用看板管理并执行任务**

AugmentedMe（AM）是一个开源的本地个人 AI agent 系统：通过 Claude Code 完成前三步引导后，AM 自主接管后续工作，管理软件项目、内容、家庭事务与研究等真实任务。核心机制为本地存储的短期+长期记忆（含向量）、带门控转换的看板状态机、每步均可审计的 git 提交执行循环，并支持夜间反思。跨平台（Mac/Linux/Windows），通过安装脚本一键部署，模型推理经 HTTPS 调用 Anthropic 账户，另计划支持 DeepSeek、Kimi、Qwen 等模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地持久记忆：短期上下文 + 长期向量嵌入，数据存于本机
- 看板状态机：任务状态显式、转换有门控
- Git 驱动执行循环：每一步都是可审计的提交
- 跨平台支持 Mac / Linux / Windows 并提供一键安装脚本

## 适用场景

- 让 AI agent 自主接手并跟踪软件项目、内容创作等长期工作
- 在本地硬件上保留 agent 记忆与任务状态，数据不外流
- 通过看板与日历查看 agent 的任务进度与未来排期

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L29: AugmentedMe is a digital worker that doesn't forget you exist between sessions. Not Siri. Not Alexa. Those are stat
> L35: - 🧠 **Persistent memory** — short-term context + long-term embeddings, stored locally

## 星数曲线

```mermaid
xychart-beta
    title "augmentedmike/helloam-agentic-kanban 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `af728c6e5241` · [字段定义](../../DATASET.md)*
