# remembra-ai/remembra

⭐ 16 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/remembra-ai/remembra) · [官网](https://remembra.dev) · 组织维护

**跨工具跨机器的编码 agent 会话交接工具（MCP server + CLI）**

面向使用多个编码 agent（Claude Code、Codex、Gemini CLI、Qwen Code、Kimi Code、Cursor 等）的开发者：agent 会话结束时通过 session hooks 从 git（及 Claude Code/Codex 的会话转录）提取已做/未做/失败事项并生成 handoff，下一个 agent 启动时以约 1,500 token 的简报接续；项目按 git remote 识别，可跨机器跨厂商。事实来自 git 与转录，不经 LLM，agent 自报内容标记为未核验。支持自托管（Docker Compose 起 Remembra+Qdrant+Ollama），云服务另收费；转录文件不上传，敏感信息按模式脱敏。Crew mode 可按 zones.yml 划分仓库区域并在写入前拦截冲突。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- handoff 事实从 git 与会话转录构建，不经 LLM，agent 摘要与事实对照核验
- 同一仓库跨机器、跨厂商 agent 接续，按 git remote 识别项目
- 6 种 agent 的 session hooks 适配（部分已验证，Cursor 未验证）
- Crew mode：zones.yml 划区、写入前拦截持区冲突，含 git hooks 拦截 commit/push

## 适用场景

- 我换用或并行使用多个编码 agent，想让下一个直接接上上一个的进度
- 在笔记本、服务器、worktree 间切换时保持 agent 会话上下文
- 多个 agent 同时在一个仓库工作，避免互相覆盖工作区

## 场景标签

`Agent 记忆` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L57: 2. **Brief.** When the next session starts, in the same tool or another, `remembra-relay brief` (run by the verifie
> L72: |Any other MCP agent|none|MCP tools|

## 星数曲线

```mermaid
xychart-beta
    title "remembra-ai/remembra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3ee635bf20e1` · [字段定义](../../DATASET.md)*
