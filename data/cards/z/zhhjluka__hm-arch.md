# zhhjluka/hm-arch

⭐ 19 · Python · Apache-2.0 · 推送 2026-06-24 · [GitHub](https://github.com/zhhjluka/hm-arch) · 个人维护

**给 AI Agent 的类人分层记忆 SDK，本地离线运行**

面向 AI agent 的离线优先 Python SDK，通过单一 HMArch 门面提供 L0-L6 分层记忆：感觉寄存器、工作记忆、情景/语义记忆、长期归档、程序性技能与元记忆。核心行为基于 SQLite 与确定性检索本地运行，默认无需 API key 或网络；支持保留衰减、遗忘与自动巩固（语义抽取、去重合并、冲突消解）。提供 Codex、Claude Code、Hermes、OpenClaw 的 hook 安装器，OpenAI/DeepSeek/ChromaDB 为可选后端，缺失凭据时回退本地行为。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- L0-L6 七层记忆架构（感觉/工作/情景/语义/归档/程序性/元记忆）
- 保留感知检索与遗忘机制：衰减、复习调度、安全删除窗口、显式 forget()
- 自动巩固：抽取语义、合并重复、冲突消解、归档旧记忆
- npm/Python 安装器接入 Codex、Claude Code、Hermes、OpenClaw

## 适用场景

- 为编程 agent 挂载可持续的记忆层，跨会话保留经验
- 在无网络、无 API key 环境下给 agent 配置本地记忆
- 对 agent 记忆做巩固、归档与遗忘管理

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L11: HM-Arch is an offline-first Python SDK that gives agents a layered memory system inspired by human memory. It combi
> L23: - **Agent-ready integration**: packaged Codex and Claude Code hook installers, Hermes diagnostics, and portable hoo

## 星数曲线

```mermaid
xychart-beta
    title "zhhjluka/hm-arch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5b59fb95fb0b` · [字段定义](../../DATASET.md)*
