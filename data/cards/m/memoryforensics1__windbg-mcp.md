# memoryforensics1/windbg-mcp

⭐ 43 · C# · MIT · 推送 2026-10-10 · [GitHub](https://github.com/memoryforensics1/windbg-mcp) · 个人维护

**给 LLM agent 的 Windows 调试 MCP 服务器（29 个工具）**

用 C#（.NET 8）编写的 MCP 服务器，将 Windows 调试引擎（DbgEng COM）、KDNET 内核调试、Frida 用户态注入、dbgsrv 远程调试、TTD 时间旅行调试与 VMware 虚拟机生命周期控制封装为 29 个 MCP 工具，供任意 MCP 兼容的 LLM 客户端调用。面向逆向工程、恶意软件分析与漏洞研究方向。关键机制：调试命令在专用 MTA COM 线程执行、所有工具带硬超时、kd_execute 阻断 g/t/p 执行控制命令、快照恢复前自动拆除调试会话。运行需 .NET 8 SDK、VMware Workstation 与 Windows 客户机；Frida/dbgsrv/WinDbg Preview 为可选依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 直接 DbgEng COM 调用而非子进程包装，命令在专用 MTA 线程执行
- KDNET 内核调试为主用例：断点、单步、BSOD 检测、事件等待带超时
- 集成 Frida、dbgsrv、TTD 三种用户态调试途径
- VM 快照恢复前自动拆除 KD/Frida/dbgsrv 会话

## 适用场景

- 让 AI agent 自主操作虚拟机做内核调试与崩溃分析
- 恶意软件分析中由 LLM 执行 WinDbg 命令与 Frida hook
- 漏洞研究时用 agent 部署驱动并设断点跟踪

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server that gives AI agents complete control over a Windows VM for kernel debugging, 
> L5: Built in C# (.NET 8), it wraps the Windows Debugger Engine (DbgEng COM), VMware Workstation, Frida, and dbgsrv into 

## 星数曲线

```mermaid
xychart-beta
    title "memoryforensics1/windbg-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 41 --> 44
    line [42, 43, 43]
```

2026-10-18 42 → 2026-10-30 43（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `ec59ef7eaae1` · [字段定义](../../DATASET.md)*
