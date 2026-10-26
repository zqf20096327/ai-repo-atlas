# betaHi/copilot-bridge

⭐ 46 · TypeScript · MIT · 推送 2026-07-10 · [GitHub](https://github.com/betaHi/copilot-bridge) · [官网](https://betahi.github.io/copilot-bridge/) · 个人维护

**把 GitHub Copilot 转为本地 OpenAI/Anthropic 兼容 API 的桥接服务**

非官方桥接服务：在本地（默认 127.0.0.1:4142）暴露 /v1/responses、/v1/messages 与 OpenAI 兼容的 chat/embeddings/models 端点，将 Codex CLI、Codex App、Claude Code、Continue 等客户端的请求转发到 GitHub Copilot 上游。通过 GitHub 设备码登录获取凭证，自动改写 ~/.codex/config.toml 与 ~/.claude/settings.json；支持 MCP 工具名适配、模型代理解释、reasoning 参数钳制与桥接管理的 Web 搜索（Copilot HTTP/SearXNG/Copilot CLI 后端）。README 声明为非官方桥，上游 API 变更可能导致失效。以 npx 分发，开发需 Bun ≥ 1.2。

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

- 同时暴露 /v1/responses、/v1/messages 与 OpenAI 兼容端点，LiteLLM/Continue/Cline/Aider 可直接接入
- MCP 工具名与 tool call 载荷按各上游模型约束适配并还原客户端身份
- 桥接管理 Web 搜索：Copilot HTTP、SearXNG、Copilot CLI 三种后端，结果经最终模型处理
- GPT-5/Claude/Gemini 系列别名解析与 reasoning_effort 钳制

## 适用场景

- 让 Claude Code 或 Codex CLI 使用 Copilot 订阅的模型额度
- 把 Continue/Cline/Aider 等工具接到本地兼容端点
- 通过 Usage Viewer 查看 Copilot 配额快照

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L6: > Use GitHub Copilot as a local OpenAI/Anthropic-compatible API, so Codex CLI, Codex App, Claude Code and Continue c
> L30: copilot-bridge is more than a raw HTTP proxy:
> L58: The bridge exposes both adapter-style endpoints (`/v1/responses`,

## 星数曲线

```mermaid
xychart-beta
    title "betaHi/copilot-bridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-26 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b00985c19be0` · [字段定义](../../DATASET.md)*
