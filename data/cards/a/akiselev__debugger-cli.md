# akiselev/debugger-cli

⭐ 23 · Rust · GPL-3.0 · 推送 2026-08-16 · [GitHub](https://github.com/akiselev/debugger-cli) · 个人维护

**面向 LLM 编程代理的命令行调试器（基于 DAP）**

跨平台 CLI 调试工具，通过 Debug Adapter Protocol 调试 C/C++/Rust/Python/Go/JS 等语言的程序。采用 CLI 前端 + 后台守护进程双模式架构：守护进程维持持久调试会话并在无客户端连接时缓冲事件，使各次命令调用间会话不中断。输出结构化、面向 LLM 代理解析设计。支持 lldb-dap、debugpy、Delve、GDB、CUDA-GDB、js-debug、CodeLLDB 等适配器，`debugger setup` 可安装所需适配器。以 Rust 编写，通过 cargo 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CLI + 守护进程架构，跨命令调用维持持久调试会话并缓冲事件
- 支持任意 DAP 适配器（lldb-dap/debugpy/Delve/GDB/CUDA-GDB/js-debug/CodeLLDB）
- 结构化、面向 LLM 代理解析的输出
- `debugger setup` 一键安装调试适配器

## 适用场景

- 让 LLM 编程代理以脚本方式交互式调试程序
- 在断点处检查变量、表达式、栈帧与线程状态
- 跨 Linux/macOS/Windows 调试多语言程序

## 场景标签

 · 领域:开发工具/调试

## 证据(README 行号)

> L3: **A command-line debugger built for LLM coding agents**
> L9: `debugger-cli` is a cross-platform debugging tool that enables LLM coding agents (and humans!) to debug executables 

## 星数曲线

```mermaid
xychart-beta
    title "akiselev/debugger-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6a3ab9de5812` · [字段定义](../../DATASET.md)*
