# KaiFelixBennett/hermes-claude-code-local

⭐ 32 · Shell · 推送 2026-10-05 · [GitHub](https://github.com/KaiFelixBennett/hermes-claude-code-local) · [官网](https://hermes-agent.nousresearch.com/) · 个人维护

**在本地 llama.cpp 上运行 Hermes Agent 与 Claude Code 的接线和脚本套件**

提供将 Hermes Agent 直连 llama.cpp、并可选通过 LiteLLM 代理桥接 Claude Code 到本地模型的配置脚本与启动脚本：Windows 用 PowerShell 脚本、Linux/macOS 用 setup.sh 安装 Hermes Agent 与 llama.cpp 并下载 GGUF 模型（默认 Qwen3.6-27B Q4_K_M，约 17 GB）。Hermes 走直连路径，Claude Code 走 LiteLLM 网关（127.0.0.1:4000）；附 Telegram 远程控制、自愈重启包装脚本与按 GGUF 的调参文档。README 给出硬件要求：16 GB RAM 起步、GPU 强烈建议、27B Q4 模型需 24+ GB VRAM。仓库不含模型权重与 llama.cpp 二进制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Hermes→llama.cpp 直连路径 + Claude Code→LiteLLM→llama.cpp 可选桥接
- 一键安装脚本（Windows PowerShell / Linux/macOS setup.sh），自动写回 hermes_config.yaml
- 支持 MTP/投机解码的 Qwen3.6-27B-MTP GGUF 默认配置
- Telegram 远程控制与 LiteLLM 崩溃自愈包装脚本

## 适用场景

- 在自有硬件上跑自主 agentic 编码任务，不产生 API 费用
- 让 Claude Code 调用本地模型而非 Anthropic API
- 通过 Telegram 在后台指挥 Hermes 执行多步任务

## 场景标签

`编码 Agent` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L12: This repo wires Hermes Agent directly to `llama.cpp` and optionally bridges Claude Code through a local LiteLLM pro
> L50: - **Hermes Agent** running locally with llama.cpp as the inference engine
> L51: - **Claude Code bridge** via LiteLLM (optional) — Claude Code talks to your local model instead of Anthropic's API

## 星数曲线

```mermaid
xychart-beta
    title "KaiFelixBennett/hermes-claude-code-local 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-26 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c7b8763cfaa0` · [字段定义](../../DATASET.md)*
