# agentty-org/agentty

⭐ 561 · C++ · MIT · 推送 2026-11-26 · [GitHub](https://github.com/agentty-org/agentty) · [官网](https://agentty.org) · 组织维护

**终端里的 AI 编程代理：单二进制、毫秒启动、可接任意模型**

用 C++26 编写的终端 agent harness，以单个静态二进制分发（约 23 MB，无 Node/Python/Electron）。围绕模型提供工具调用、OS 级沙箱（seccomp/Landlock/AppContainer 等）、上下文检索、多模型路由与 TUI 界面；支持订阅登录（Claude/ChatGPT/Copilot/Kimi）、十余家 API 提供商、本地 Ollama 及任意 OpenAI 兼容端点，可在 Zed/JetBrains(ACP)、MCP、CI 与离线 SSH 机器上运行。从源码构建需 C++26 工具链（GCC 14+ 等）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单静态二进制，约 47 ms 启动、21 MB 空闲内存，无 npm install
- 接入订阅账号或十余家 API 提供商，支持本地 Ollama 与任意 OpenAI 兼容端点，线程内热切换模型
- 默认沙箱：seccomp/Landlock/cgroups/seatbelt/AppContainer，凭据文件掩码与网络代理限制
- 本地检索引擎（search_code/search_docs），支持 Claude Code 格式的 Agent Skills 与 MCP 双向集成

## 适用场景

- 在终端里让 AI 代理读代码、改代码、跑测试修 bug
- 用已订阅的 Claude/ChatGPT/Copilot/Kimi 账号驱动编程代理，无需额外 API key
- 在无外网的隔离机器上通过 SSH 中继运行 AI 编程会话
- 在脚本与 CI 中以 agentty run 单条命令执行带工具的提示词

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: **An agent harness for your terminal.** Ready to type in 47 ms, 21 MB of memory while idle.
> L29: The model decides what to do; the **harness** is everything around it: the tools it can call, the
> L31: you steer it from. agentty is that harness, written in C++26 and shipped as a single static binary.

## 星数曲线

```mermaid
xychart-beta
    title "agentty-org/agentty 星数(近 19 点)"
    x-axis ["2026-10-25", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-15", "2026-11-16", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-25", "2026-11-27"]
    y-axis "stars" 553 --> 631
    line [617, 618, 619, 618, 619, 617, 614, 618, 620, 621, 623, 624, 623, 625, 567, 559, 560, 561, 561]
```

2026-10-25 617 → 2026-11-27 561（-56）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `5c89039d9545` · [字段定义](../../DATASET.md)*
