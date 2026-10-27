# benmaster82/retro-agent

⭐ 22 · Zig · MIT · 推送 2026-03-11 · [GitHub](https://github.com/benmaster82/retro-agent) · 个人维护

**运行在 Windows XP 等老旧硬件上的终端 AI 代理**

用 Zig 编写的终端 TUI AI 代理，可在 Windows XP SP3 x86（64–512 MB RAM，无 UCRT/MSVC 运行时）上运行，也可交叉编译到 Linux x86/x64/ARM。通过 HTTP 连接局域网内另一台机器上的 Ollama 或任意 OpenAI 兼容端点，以 function calling 执行内置工具（系统诊断、进程、网络、磁盘、服务、文件操作等约 14 个）。限制：Ollama 需运行在现代机器上，模型必须支持 tool use；Linux 平台目前仅有 system_info 工具。单二进制约 750 KB，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Windows XP SP3 x86、64 MB RAM 即可运行的单一二进制（~750 KB）
- 通过 OpenAI 兼容协议连接 Ollama 并支持 function calling
- 内置系统诊断、进程、网络、磁盘、服务等约 14 个工具（Windows）
- 命令/路径白名单、审批模式、子进程超时等安全机制

## 适用场景

- 在不升级硬件的老旧 Windows XP 机器上用 AI 做系统诊断与管理
- 为复古计算设备接入局域网 LLM 获得终端 AI 助手
- 通过 function calling 让模型代查进程、网络、磁盘状态

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L10: A terminal-based AI agent written in Zig, designed to run on legacy hardware — including Windows XP SP3 x86 with as
> L12: Communicates with Ollama or any OpenAI-compatible API over local HTTP. Supports function calling (tool use) and pro
> L35: - Tool calling / function calling via OpenAI-compatible protocol

## 星数曲线

```mermaid
xychart-beta
    title "benmaster82/retro-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-27 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3738877f0b12` · [字段定义](../../DATASET.md)*
