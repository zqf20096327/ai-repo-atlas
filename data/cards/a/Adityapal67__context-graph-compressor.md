# Adityapal67/context-graph-compressor

⭐ 35 · MIT · 推送 2026-05-30 · [GitHub](https://github.com/Adityapal67/context-graph-compressor) · 个人维护

**将长 AI 对话压缩为可移植 JSON 上下文图，供跨会话/跨 LLM 接续**

一个 Claude skill：在对话中触发后，把长聊天历史压缩为结构化 JSON 上下文图（compact 模式约 300-500 tokens，readable 模式供人类阅读归档）。图节点分为 fact/decision/problem/goal/code/context 六类，带 h/m/l 重要性标签与状态追踪，输出可下载的 .json 文件。用户将 JSON 粘贴到新会话或 GPT/Gemini/Mistral 等其他 LLM 即可接续原对话。以 Claude.ai 上传 .skill 文件方式安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将对话压缩为 compact/readable 两种模式的 JSON 上下文图，compact 约 300-500 tokens
- 六类节点（fact/decision/problem/goal/code/context）与 h/m/l 重要性标签
- 输出可下载 .json 文件，可粘贴到 Claude 或 GPT/Gemini/Mistral 等其他 LLM
- 在 Claude.ai 对话中用自然语言触发（如 compress this chat）

## 适用场景

- 对话过长时压缩上下文，在新会话中低成本接续
- 把 Claude 对话迁移到 GPT/Gemini 等其他 LLM 继续工作
- 以 readable 模式归档项目历史并与队友分享

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: A Claude skill that compresses any chat conversation into a minimal, portable JSON context graph — so you can contin
> L111: 1. Download `context-graph-compressor.skill`
> L118: - Claude (claude.ai)

## 星数曲线

```mermaid
xychart-beta
    title "Adityapal67/context-graph-compressor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-30 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a8632b0e57ae` · [字段定义](../../DATASET.md)*
