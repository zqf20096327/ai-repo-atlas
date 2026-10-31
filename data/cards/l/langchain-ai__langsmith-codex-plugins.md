# langchain-ai/langsmith-codex-plugins

⭐ 14 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/langchain-ai/langsmith-codex-plugins) · [官网](https://langchain.com) · 组织维护

**把 OpenAI Codex 的会话与工具调用发送到 LangSmith 的追踪插件**

面向 OpenAI Codex CLI 的插件，将每轮对话、模型调用（含模型名、provider、token 数）、工具调用、shell 命令、文件读取、网络搜索与子代理线程上传到 LangSmith 平台供查看。通过 codex plugin 命令或插件浏览器安装，需信任 hooks 并在配置文件中开启 tracing。支持 API key 或 CLI 登录认证、密钥脱敏、会话静音、多目标副本发送、managed file 管理员锁定配置（可配合 MDM 分发）。Mac 自带构建无需 Node，Windows/Linux 需 Node.js 22+，要求 Codex 0.153.4+ 与 LangSmith 账号。MIT 许可。

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

- 追踪模型调用、工具调用、shell 命令与子代理线程到 LangSmith
- 上传前脱敏 API key、JWT、PEM 等凭据模式
- managed file 可由管理员锁定配置并通过 MDM 分发
- 支持 replicas 将同一 trace 发送到多个项目/工作区

## 适用场景

- 在 LangSmith 中查看 Codex agent 每轮实际做了什么
- 团队统一为组织成员部署与锁定追踪配置
- 需要敏感凭据脱敏后再上传的会话审计

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L1: # LangSmith Tracing Plugin for OpenAI Codex
> L3: Sends your Codex turns, tool calls and subagent threads to LangSmith so you can see what the agent actually did.
> L106: Each model call includes the conversation so far and the reply along with the model name, provider, stop reason an

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/langsmith-codex-plugins 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `003426e634e4` · [字段定义](../../DATASET.md)*
