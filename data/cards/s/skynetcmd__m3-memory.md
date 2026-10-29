# skynetcmd/m3-memory

⭐ 30 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/skynetcmd/m3-memory) · [官网](https://github.com/skynetcmd/m3-memory) · 个人维护

**给 AI 助手的本地优先持久记忆层，跨会话跨工具共享**

面向 Claude Code、Cursor、Gemini CLI 等 AI 助手的记忆后端：通过 MCP 与 CLI 存取事实、决策、偏好与会话历史，默认 SQLite 单文件存储、完全离线可用。检索采用 BM25 关键词加本地 BGE-M3 语义向量与 MMR 多样性重排，LongMemEval-S 首位命中 91.8%。提供双时间线版本历史、相似度驱动的记忆取代、模型辅助的矛盾检测、知识图谱与后台认知循环维护；支持 PostgreSQL 多机共享与同步。安装仅需 pipx 一条命令，m3 setup 自动发现并接入已装助手。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 服务器与 CLI 共享同一存储，多个助手可共享一份记忆
- BM25 + 本地 BGE-M3 向量 + MMR 混合检索，九个排序信号
- 双时间线历史与相似度取代机制，旧版本不删除可按 as_of 查询
- 默认 SQLite 单文件、完全离线，可选 PostgreSQL 多机共享/同步

## 适用场景

- 换会话或换工具后让 AI 助手记得之前的项目决策与偏好
- 多个 AI 助手（Claude Code/Cursor 等）共享同一份本地记忆
- 合规要求下在自有硬件离线保存与审计 AI 记忆（GDPR 导出/删除）

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L42: m3 is a **memory layer** for AI agents: the AI assistants that work for you, such as
> L154: m3 is a persistent, local-first memory layer for AI agents: an MCP server and a

## 星数曲线

```mermaid
xychart-beta
    title "skynetcmd/m3-memory 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-29"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-29 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `278e94c91c0e` · [字段定义](../../DATASET.md)*
