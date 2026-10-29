# wydrox/ppmlx

⭐ 25 · Python · MIT · 推送 2026-09-07 · [GitHub](https://github.com/wydrox/ppmlx) · 个人维护

**在 Apple Silicon Mac 上本地运行 LLM 的 OpenAI 兼容 API 服务器**

基于 Apple MLX 框架的本地 LLM 推理运行时与 API 服务器：通过 ppmlx CLI 下载模型、终端聊天、在 :6767 端口启动 OpenAI 兼容 API，任何 OpenAI 兼容客户端（Cursor、Continue、LangChain 等）可直接接入。附带模型量化转换、可选的远程路由策略（OpenAI/Anthropic/OpenRouter）、macOS Keychain 凭据管理、Claude Code 订阅透传以及实验性本地记忆图与 Agent IR 工具运行时。要求 macOS Apple Silicon（M1+）与 Python 3.11+，多项目功能标注为实验性、接口可能在稳定版前变更。README 含与 Ollama 的吞吐/首 token 延迟对比基准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- ppmlx serve 启动 OpenAI 兼容 API（:6767），任意兼容客户端可接入
- 基于 Apple MLX 的本地推理，隐私上模型推理留在本机
- HF 模型量化转换为 MLX 格式（ppmlx quantize）
- 可选远程路由（OpenAI/Anthropic/OpenRouter）与 Claude Code 订阅透传

## 适用场景

- 在 Mac 上本地跑 LLM 并给 Cursor/Continue/LangChain 等工具提供 OpenAI 兼容接口
- 下载、管理与量化 GGUF/HF 模型到 MLX 格式
- 本地推理优先、按路由策略选择性调用远程提供商

## 场景标签

`推理引擎` `模型量化` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Run LLMs on your Mac.** OpenAI-compatible API powered by Apple Silicon.
> L26: ppmlx serve                 # start API server on :6767
> L86: That's it. Any OpenAI-compatible tool works out of the box:

## 星数曲线

```mermaid
xychart-beta
    title "wydrox/ppmlx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `89570019156f` · [字段定义](../../DATASET.md)*
