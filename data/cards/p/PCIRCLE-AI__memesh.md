# PCIRCLE-AI/memesh

⭐ 16 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/PCIRCLE-AI/memesh) · [官网](https://pcircle.com/memesh) · 组织维护 · 中文 README

**为 Claude Code/Codex 提供本地共享记忆与 agent 通信层**

面向 AI 编程 agent 的本地记忆协作层：以插件形式接入 Claude Code 与 Codex，将决策、教训、任务状态等记忆存入单一本地文件 ~/.memesh/knowledge-graph.db，无需云端记忆服务或独立模型。提供 12 个记忆与协调工具（remember/recall/message 等）和 10 个 hook，按相关性/新近度/频率/置信度/召回影响加权排序检索结果；本地运行的 agent 之间可通过持久收件箱交换消息。命令行工具需 Node.js 22.13+，原生投递路径仅支持 macOS/Linux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一本地文件存储记忆，无需云服务或独立模型
- 12 个记忆与协调工具（记忆存取、任务状态、agent 间消息等）
- 加权评分排序：相关性 30%+新近度 25%+频率 18%+置信度 17%+召回影响 10%
- Claude Code 与 Codex 在同一机器上共享同一份记忆

## 适用场景

- 跨会话保存并找回项目决策与经验教训
- 让 Claude Code 和 Codex 共用同一套本地记忆
- 在多个本地 agent 之间交接工作进度与传递消息

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: **Shared local memory for Claude Code and Codex.**
> L7: MeMesh helps your coding agents remember your preferences, project decisions, and lessons from past work, so you spe

## 星数曲线

```mermaid
xychart-beta
    title "PCIRCLE-AI/memesh 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `1935966af41a` · [字段定义](../../DATASET.md)*
