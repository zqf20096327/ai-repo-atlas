# chekiboy/whaat-ai-identity

⭐ — · [GitHub]() · 个人维护

**给 AI agent 提供本地持久记忆与身份连续性的运行时**

Whaat 是一个本地优先的 AI Identity Runtime：将 agent 的记忆、日志、会话历史以 markdown 文件形式存放在本地 Git 仓库中，每次变更记录为 commit，可审阅与回滚。记忆分层存放并带触发条件与随时间衰减的效度评分；通过 Claude Code 插件的 hooks 与 MCP server 在会话开始注入核心与索引、会话结束时写入日志与报告；提供浏览器应用、whaat 命令行与 127.0.0.1 的 JSON API。目前仅支持 macOS，采用 BSL 1.1（source-available）许可，0.1.0 为 Apache 2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- markdown 记忆 + Git commit 版本历史，可审阅、可回滚
- Truthness & Validity 评分：效度每 30 天衰减 0.2，成功使用可回馈
- Claude Code hooks 强制记忆读写经过运行时并记录访问日志
- whaat mcp 使任意 MCP 客户端可作为身份接入

## 适用场景

- 让长期协作的编码 agent 跨会话记住纠正与偏好
- 在本地以纯文件形式检查、修改、回滚 agent 的记忆
- 为多个 agent 身份建立隔离的记忆存储与令牌

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: Whaat is an **AI Identity Runtime**: a local-first system that gives AI agents persistent memory and identity contin
> L22: |Integrations|Claude Code (plugin with skills and hooks); any MCP client that runs servers over stdio|
> L54: - **Any MCP client.** `whaat mcp` serves the same memory, journal and report calls over MCP, so an agent outside Cl

## 星数曲线

```mermaid
xychart-beta
    title "chekiboy/whaat-ai-identity 星数(近 3 点)"
    x-axis ["2026-11-19", "2026-11-22", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-19 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `7d89dc6db02b` · [字段定义](../../DATASET.md)*
