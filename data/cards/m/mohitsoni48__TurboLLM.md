# mohitsoni48/TurboLLM

⭐ 285 · TypeScript · 推送 2026-10-21 · [GitHub](https://github.com/mohitsoni48/TurboLLM) · [官网](https://turbollm.dev) · 个人维护

**本地 LLM 引擎运行器：任意 llama.cpp 分支加自动调参与 Web UI**

面向本地推理用户的 Node 守护进程（约 7 MB npm 包，无 Electron/Python）：可指向任意 llama-server 兼容二进制（含自编译分支），加载时自动基准测试推导启动参数，提供 VRAM 装载前适配判定、实测 tokens/sec、GGUF 元数据解析、Hugging Face 浏览下载（SHA-256 校验、断点续传）。内建 Web 聊天界面与 OpenAI/Anthropic 兼容 API，可让 Claude Code 等工具指向本机；按需加载模型的网关。仅推理，需 Node ≥22 与终端命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 运行任意 llama-server 兼容引擎（含社区分支），自动探测能力并适配 UI
- 加载时基准测试自动调参，装载前给出 VRAM 适配判定
- OpenAI 与 Anthropic 兼容 API，按请求名称按需加载模型
- Hugging Face 应用内浏览下载，含 SHA-256 校验与断点续传

## 适用场景

- 让 Claude Code 等现有工具通过一条命令使用本地模型
- 使用社区 fork（低比特 KV cache、投机解码）而无需自行编译
- 管理已有 GGUF 目录并按 GPU 挑选量化方案

## 场景标签

 · 领域:LLM 基础设施/本地推理

## 证据(README 行号)

> L27: That one command starts a local daemon, opens a browser UI, and serves your models over an
> L61: - **🔌 Drop-in APIs.** OpenAI **and** Anthropic-compatible — so Claude Code and every existing
> L63: - **🔀 A gateway that loads models for you.** Name any model in your API request and TurboLLM

## 星数曲线

```mermaid
xychart-beta
    title "mohitsoni48/TurboLLM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 284 --> 286
    line [285, 285]
```

2026-10-18 285 → 2026-10-22 285（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `6933d9a0753d` · [字段定义](../../DATASET.md)*
