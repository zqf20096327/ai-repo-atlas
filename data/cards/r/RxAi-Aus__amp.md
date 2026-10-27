# RxAi-Aus/amp

⭐ 31 · JavaScript · NOASSERTION · 推送 2026-10-16 · [GitHub](https://github.com/RxAi-Aus/amp) · [官网](https://amp.rxai.com.au/) · 组织维护

**基于 GitHub 仓库的 AI agent 共享记忆系统**

以单个 GitHub 仓库为载体的多 agent 共享记忆与通信协议：Issues 作为消息收件箱、评论作为回复、GitHub Actions 每 6 小时生成带权重的 INDEX.md 索引，lifecycle hooks 将索引与匹配记录注入每个会话。记忆条目按 Outcome（success/failure/neutral）调整置信权重，成功模式权重上升、失败模式衰减。无需向量数据库或额外服务器，支持 Claude Code、Codex、OpenClaw 等多种 agent 接入，提供 npm run setup 交互式安装向导，目前仅支持 macOS/Linux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Issues 为记忆单元、GitHub Actions 为索引器的仓库即大脑架构
- 基于 Outcome 反馈的置信权重系统：成功记忆增强、失败记忆衰减
- lifecycle hooks 向每个 agent 会话注入 INDEX.md 与匹配记录
- npm run setup 交互式向导自动化安装（仓库创建、标签、MCP server、钩子）

## 适用场景

- 让本机多个 AI agent（Claude Code、Codex、OpenClaw 等）跨会话共享记忆
- 不搭建数据库/服务器，用 GitHub 免费自托管 agent 记忆
- 通过权重衰减机制自动淘汰失效的行为模式

## 场景标签

`Agent 记忆` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: A shared memory and communication system for AI agents (e.g. Claude Cowork, OpenClaw)
> L24: A pattern for letting two or more AI agents share memory across sessions without
> L40: Architecture: agents read and write GitHub Issues; GitHub Actions index them every six hours with weights and decay

## 星数曲线

```mermaid
xychart-beta
    title "RxAi-Aus/amp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-27 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `53061e409963` · [字段定义](../../DATASET.md)*
