# acupof-ai/arle

⭐ 20 · Rust · MIT · 推送 2026-10-01 · [GitHub](https://github.com/acupof-ai/arle) · [官网](https://acupof-ai.github.io/arle/) · 组织维护 · 中文 README

**面向编码 agent 的本地推理服务器：Rust 单二进制，Anthropic/OpenAI API**

用纯 Rust 编写的本地 LLM 推理服务器，以单二进制发布，支持 Apple Silicon (Metal) 与 NVIDIA (CUDA) 后端。对外同时提供 Anthropic /v1/messages 与 OpenAI /v1/chat/completions 两种 HTTP API（均支持流式），可将 Claude Code、opencode、aider 等客户端指向本地。核心机制是跨轮次存活且驻留在加速器上的 KV cache 与 radix 前缀共享，使多轮 agent 对话的后续轮次首 token 延迟接近第二轮；另有内置 REPL agent、一次性执行模式与投机解码。支持 Qwen3.5/3.6/3.8、DeepSeek-V4-Flash、GLM-5.2 等模型，Metal 后端为 Beta 状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- KV cache 跨轮次驻留加速器，radix 前缀共享，仅对新增 token 做 prefill
- 单二进制同时提供 Anthropic 与 OpenAI 兼容 HTTP API（流式、工具调用）
- Metal 与 CUDA 双后端，CUDA 下 KV 分页可降级到主机内存，支持 INT8/FP8 KV
- 四种模式：serve / 交互 REPL agent / 一次性执行 / 硬件自检

## 适用场景

- 把 Claude Code 等 coding agent 指向本地模型运行，避免远程 API
- 长多轮 agent 对话中保持每轮快速响应
- 在 Mac 或 NVIDIA GPU 上本地服务 Qwen/DeepSeek 系列模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3:  The local inference server for coding agents.
> L70: |`arle serve --backend …`|HTTP server: Anthropic `/v1/messages` and OpenAI `/v1/chat/completions`, both streaming.|
> L128:  Serve["arle serve<br/><sub>Anthropic + OpenAI APIs</sub>"]

## 星数曲线

```mermaid
xychart-beta
    title "acupof-ai/arle 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a00a39385047` · [字段定义](../../DATASET.md)*
