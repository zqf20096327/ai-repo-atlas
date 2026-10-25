# RocketMaDev/pwndbg-mcp

⭐ 38 · Python · MIT · 推送 2026-04-07 · [GitHub](https://github.com/RocketMaDev/pwndbg-mcp) · 个人维护 · 中文 README

**让 AI agent 通过 MCP 调用 pwndbg 调试 ELF 的工具**

面向 CTF pwn 题的 MCP 服务器，把 pwndbg/GDB 的调试能力暴露给 AI agent：通过 GDB/MI 直接与 GDB 通信，提供加载可执行文件、执行 GDB 命令、进程交互（收发数据、中断）、heap/telescope 等 pwndbg 别名工具，返回格式为 TOON。默认在 localhost:8780 启动，支持 stdio/http/sse 传输。README 提示推荐改用 tmux 技能方式、每实例仅一个 GDB 会话、多个工具存在远程代码执行风险，建议用 bwrap 做隔离。未发布到 PyPI，需克隆仓库后用 uv 安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 GDB/MI 与 GDB 直接通信，提供 17 个调试与进程交互工具
- 支持 stdio/http/sse 三种传输，默认 HTTP streamable 于 localhost:8780
- eval_to_send_to_process 可访问 pwntools 并发送任意二进制数据
- 可集成 decomp2dbg 连接反编译器

## 适用场景

- CTF pwn 题中让 AI agent 辅助调试 ELF 二进制
- AI agent 读取进程内存、分析堆结构并执行 GDB 命令
- 配合 IDA Pro MCP 等其他 MCP 做联合逆向分析

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: An MCP tool endows AI agent with the capability to debug ELF. This tool is designed
> L41: By default starting pwndbg-mcp without args launch a mcp server at `localhost:8780` with `gdb`

## 星数曲线

```mermaid
xychart-beta
    title "RocketMaDev/pwndbg-mcp 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23", "2026-10-25"]
    y-axis "stars" 34 --> 39
    line [35, 36, 38, 38]
```

2026-10-18 35 → 2026-10-25 38（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `e41d59767796` · [字段定义](../../DATASET.md)*
