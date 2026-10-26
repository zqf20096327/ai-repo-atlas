# agynio/claude-map-reduce-memory

⭐ 29 · TypeScript · MIT · 推送 2026-04-15 · [GitHub](https://github.com/agynio/claude-map-reduce-memory) · 个人维护

**Claude Code agent 的跨会话全局持久记忆 CLI**

面向 Claude Code 用户的 npm CLI 工具，为 agent 提供全局持久记忆：笔记带自然语言激活条件存储于 ~/.claude-memory/ 的 chunk 文件，PreToolUse hook 在每次工具调用前读取 transcript 并用小 LLM 做相关性检索，仅注入 transcript 中尚不存在的新提示以保持上下文有界。规模化检索采用 scatter-gather map-reduce（每 chunk 一次 Haiku 调用），并利用 prompt caching 降低成本。需要 Anthropic API key，单 CLI 交付，无额外进程或 MCP 服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PreToolUse hook 自动检索并注入按条件激活的记忆提示
- scatter-gather map-reduce 分块并行检索（每 chunk 一次 Haiku 调用）
- 对 transcript 去重，仅注入新提示使上下文保持有界
- 单一 npm CLI 交付，init 一条命令注册 hooks 并写入 CLAUDE.md

## 适用场景

- 让 Claude Code agent 跨会话保留偏好与经验
- 长会话中按相关性自动召回历史决策笔记
- 替代按位置读取的仓库级 MEMORY.md 记忆方式

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: `cmr-memory` replaces that with context-activated retrieval. Notes are stored globally with a plain-language `--when
> L80: 3. **PreToolUse hook**: Reads the transcript and upcoming tool call,

## 星数曲线

```mermaid
xychart-beta
    title "agynio/claude-map-reduce-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5c05285de044` · [字段定义](../../DATASET.md)*
