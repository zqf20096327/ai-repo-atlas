# chand1012/claude-code-mlx-proxy

⭐ 51 · Python · MIT · 推送 2026-04-14 · [GitHub](https://github.com/chand1012/claude-code-mlx-proxy) · 个人维护

**本地 MLX 模型代理服务器：让 Claude Code 使用本地开源模型**

在 Apple Silicon Mac 上运行的本地服务器，实现 Claude Messages API 格式，将 Claude Code 的请求重定向到本地 MLX 框架加载的开源模型（默认 mlx-community/GLM-4.5-Air-3bit）。通过设置 ANTHROPIC_BASE_URL 环境变量即可接入 Claude Code；提供 /v1/messages（含 SSE 流式）、/v1/messages/count_tokens 等端点，模型、端口、生成参数均通过 .env 配置。要求 Apple Silicon Mac，代码与对话不出本机、无需 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 Claude Messages API 格式，含 SSE 流式响应
- 通过 MLX 框架加载 Hugging Face 上的开源模型
- 提供 count_tokens 与 health 端点
- 通过 .env 配置模型、端口与生成参数

## 适用场景

- 在本地 Mac 上离线运行 Claude Code 而不连接 Anthropic 服务器
- 用开源模型（GLM-4.5-Air、Llama 3、DeepSeek 等）替代云端模型写代码
- 不管理 API key、不产生调用费用地本地编码辅助

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: This project provides a local server that acts as a backend for the **Claude Code** command line coding assistant. I
> L5: This server implements the Claude Messages API format that Claude Code communicates with, redirecting all requests t

## 星数曲线

```mermaid
xychart-beta
    title "chand1012/claude-code-mlx-proxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-30 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `620a1d154978` · [字段定义](../../DATASET.md)*
