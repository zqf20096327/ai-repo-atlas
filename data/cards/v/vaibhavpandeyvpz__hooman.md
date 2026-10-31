# vaibhavpandeyvpz/hooman

⭐ 15 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/vaibhavpandeyvpz/hooman) · [官网](https://vaibhavpandey.com/hooman/) · 个人维护

**本地优先的开源 AI agent 运行时，覆盖 CLI/VS Code/多渠道**

MIT 许可的全栈 agent 运行时，提供 CLI（有状态 TUI、一次性 exec、daemon 频道自动化）、VS Code 扩展、ACP 协议接入与 Design 模式（HTML→Figma/Sketch/PDF/PPTX）。它读取代码库、编辑文件、运行命令，配置与会话存储于 ~/.hooman，无账号与遥测。本地优先：首跑 setup 可选 llama.cpp(GGUF) 与 Apple Silicon MLX，权重按需下载，也支持 BYOK 与 OpenAI 兼容自定义端点。支持 MCP(stdio/http/sse+OAuth)、技能、子代理、审批与后台 shell 作业。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多运行表面共享同一运行时与本地配置：CLI、VS Code、ACP、daemon、Design 模式
- 本地推理：llama.cpp (GGUF) 与 Apple Silicon MLX，权重按需下载，无需 API key 即可启动
- MCP 支持 stdio/streamable-http/sse，含 OAuth、懒加载工具发现与可选 Playwright 浏览器 MCP
- 14 个推理 provider 适配（anthropic/azure/bedrock/google/groq/llama-cpp/minimax/mlx/moonshot/ollama/openai/openrouter/xai）

## 适用场景

- 在终端或 VS Code 中运行可读写代码库的 AI agent
- 通过 Slack/Telegram 等 daemon 频道做自动化任务
- 在内网或离线环境用 llama.cpp/MLX 跑 agent 而不出网
- 用 ACP 协议在 Zed 等编辑器中接入同一 agent 运行时

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L24: Hooman is a mature, local-first AI agent runtime for teams that want the full stack — not a thin chat wrapper. It r
> L78: - **Full-stack, not single-surface** — CLI, VS Code, ACP, daemon channels, and Design mode share one runtime and on

## 星数曲线

```mermaid
xychart-beta
    title "vaibhavpandeyvpz/hooman 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `35f8eb7d2fe8` · [字段定义](../../DATASET.md)*
