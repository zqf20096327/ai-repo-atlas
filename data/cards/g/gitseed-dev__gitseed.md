# gitseed-dev/gitseed

⭐ 18 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/gitseed-dev/gitseed) · [官网](https://gitseed.dev) · 组织维护

**自托管 AI 编码 Agent 控制平面：沙箱运行且不持有 Git 凭据**

以 Docker Compose / Kubernetes 部署的自托管控制平面，将 Claude Code、Codex、Gemini CLI、Antigravity、OpenCode 五种 agent CLI 运行在无 Git 凭据的沙箱容器中；独立的只读 broker 扫描 diff 中的密钥与受限路径，经人工批准后开 PR，并附 Ed25519 签名的治理凭据。内置五阶段 SDLC 流水线（Ideate→Plan→Execute→Review→Merge）与 Fast-Track 模式，经 LiteLLM 网关支持云 API、本地 Ollama/vLLM/LM Studio 及单用户订阅 OAuth（Personal Mode）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- agent 容器零 Git 凭据，独立 finalize 容器做密钥扫描与受限路径拦截
- 每个 PR 附 Ed25519 签名治理凭据，可离线验证
- 5 阶段 SDLC 流水线与最多 3 个并行模型意见
- LiteLLM 网关统一云 API 与本地 Ollama/vLLM/LM Studio 后端，含硬性美元上限

## 适用场景

- 团队想让 AI 编码 agent 在隔离沙箱中运行且不接触 Git 凭据
- 对 agent 产出的 PR 做密钥扫描、路径策略与人工审批门控
- 离线/内网环境下用本地开源权重模型运行编码 agent
- 在多个 agent CLI 与模型后端之间绑定不同阶段与预算上限

## 场景标签

`编码 Agent` `代码审查` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L7: GitSeed is a self-hosted, open-source control plane for AI coding agents. It runs **Claude Code**, **Codex**, **Gemi
> L62: |**MCP Server**|`http://127.0.0.1:8422/mcp`|Loopback-bound Streamable HTTP & SSE MCP endpoint (65 annotated tools; 
> L117: |**Team & Enterprise Cloud APIs (BYOK / LiteLLM)**|**Anthropic** (Claude), **OpenAI**, **Google Gemini**, **xAI (G


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `7415a3da450c` · [字段定义](../../DATASET.md)*
