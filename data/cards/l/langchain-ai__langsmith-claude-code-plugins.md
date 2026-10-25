# langchain-ai/langsmith-claude-code-plugins

⭐ 72 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/langchain-ai/langsmith-claude-code-plugins) · [官网](https://langchain.com) · 组织维护

**将 Claude Code 会话追踪上报 LangSmith 的插件**

LangChain 官方维护的 Claude Code 插件：把每轮对话、工具调用输入输出、token 用量与子代理结构作为 trace 发送到 LangSmith 项目，供回读 agent 实际执行过程。默认关闭，需配置 API key 启用；支持按会话 mute 内容、上传前脱敏（API key/JWT/PEM 等）、管理员托管文件锁定配置。Mac 平台插件自带构建，其余平台需 Node.js 20+。通过 Claude Code 的 /plugin 命令安装。

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

- 追踪模型调用、工具与技能调用、子代理嵌套结构至 LangSmith
- 上传前默认脱敏（API key、JWT、PEM、Authorization 等模式）
- 单会话 mute 与 defaultMuted 全局内容隐藏，保留结构占位
- 管理员可通过 managed.json 托管文件锁定用户配置

## 适用场景

- 在 LangSmith 中回看 Claude Code agent 每步做了什么
- 按技能统计 agent 使用情况与 token 消耗
- 团队管理员统一锁定追踪与脱敏策略

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: Sends your Claude Code conversations to LangSmith so you can read back what the agent actually did.
> L41: Each model call carries the conversation so far and the assistant's reply. You also get the model name, provider an

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/langsmith-claude-code-plugins 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 71 --> 74
    line [73, 72, 72]
```

2026-10-18 73 → 2026-10-25 72（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `d116e553ca13` · [字段定义](../../DATASET.md)*
