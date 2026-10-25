# Miosa-osa/OSA

⭐ 79 · Elixir · Apache-2.0 · 推送 2026-10-09 · [GitHub](https://github.com/Miosa-osa/OSA) · 组织维护

**终端 AI 代理：分类任务、过滤噪声并路由到多模型执行**

面向终端用户的命令行 AI 代理，用 Elixir/OTP 引擎与 Rust TUI 两部分组成，通过本机 127.0.0.1 HTTP+SSE 通信。首次运行向导选择提供商（默认本地 Ollama），支持 27 个提供商及回退链。内置 82 个延迟加载工具、子代理并发、跨会话记忆、持久化目标与队列，提供 ask/auto-edit/plan/overdrive 等权限模式、目录信任机制、约 70 个斜杠命令及 headless 运行（osa run）。一条命令安装，提供预构建二进制与 Docker 两种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Elixir/OTP 引擎 + Rust TUI 双进程架构，本地 127.0.0.1 通信
- 27 个 LLM 提供商及回退链，支持本地 Ollama
- 82 个内置工具、子代理多步执行、跨会话记忆
- ask/auto-edit/plan/overdrive 等分级权限模式与工作区信任机制

## 适用场景

- 在终端里用自然语言让代理完成编码与运维任务
- 用本地 Ollama 或订阅类模型在本地跑多步代理工作
- headless 模式嵌入脚本流水线执行代理任务

## 场景标签

`编码 Agent` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L94: - **The engine**: an Elixir/OTP application. This is the brain: the agent
> L52: ✓ 27 providers + fallback       ✓ Nothing leaves your machine unless you say so

## 星数曲线

```mermaid
xychart-beta
    title "Miosa-osa/OSA 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 77 --> 80
    line [78, 79, 79]
```

2026-10-18 78 → 2026-10-25 79（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ada9eb4ce7e3` · [字段定义](../../DATASET.md)*
