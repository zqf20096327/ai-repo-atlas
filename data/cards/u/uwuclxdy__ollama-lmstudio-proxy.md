# uwuclxdy/ollama-lmstudio-proxy

⭐ 33 · Rust · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/uwuclxdy/ollama-lmstudio-proxy) · 个人维护

**将 LM Studio 模型通过 Ollama API 暴露的 Rust 代理**

Rust 编写的代理服务器：对外提供全套 Ollama API 端点（chat/generate/embeddings 等），将请求转发给 LM Studio 本地服务器，使 Claude Code、VSCode Copilot、Open WebUI 等 Ollama 客户端可直接使用 LM Studio 加载的模型。支持 SSE 流式、reasoning 参数透传、`/v1/*` 直通（含 Anthropic Messages 与 OpenAI Responses）、web 工具端点与可选 Bearer 认证。要求 LM Studio 0.4.0+，与 Ollama 端口冲突需先停 Ollama。通过 cargo install 或预编译二进制分发，MIT/Apache-2.0 双许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖全部 Ollama 端点并映射 LM Studio 模型 id 为 Ollama 风格命名
- `/v1/*` 直通含 Anthropic Messages 与 OpenAI Responses，Claude Code 可经 ANTHROPIC_BASE_URL 接入
- 支持 SSE 流式取消、reasoning（think/reasoning_effort）、按请求 num_ctx
- 提供 /api/web_fetch 与 /api/web_search 工具端点，无需 ollama.com 账号

## 适用场景

- 让 Claude Code 或 VSCode Copilot 直接调用 LM Studio 里的模型
- 把 LM Studio 接入仅支持 Ollama API 的客户端（如 Open WebUI）
- 本地统一 11434 端口入口，后端由 LM Studio 提供推理

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Use LM Studio models with anything that speaks the Ollama API.**
> L18: - **Every Ollama endpoint:** chat, generate, embeddings, tags, ps, show, pull, create, copy, delete, blobs.
> L60: |**ollama-lmstudio-proxy** (this)|Speaks the Ollama API, forwards to LM Studio|One Ollama endpoint, LM Studio behin

## 星数曲线

```mermaid
xychart-beta
    title "uwuclxdy/ollama-lmstudio-proxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-30 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `46f35af1ea1f` · [字段定义](../../DATASET.md)*
