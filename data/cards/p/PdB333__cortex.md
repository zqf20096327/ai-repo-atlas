# PdB333/cortex

⭐ 31 · C++ · MIT · 推送 2026-10-22 · [GitHub](https://github.com/PdB333/cortex) · 个人维护

**Windows 运行时分析与逆向工具，内置供 AI agent 调用的 MCP 服务**

面向 Windows 软件的原生桌面应用，集成内存扫描（兼容 Cheat Engine .CT 表）、Zydis 反汇编、调试器、可逆补丁、Lua 自动化、崩溃诊断与逆向工程工作区。内置 MCP 服务器（cortex.exe mcp），AI agent 可动态附加进程、并发操作多个目标；默认只读，写入需人工以 --allow-writes 启动并在调用中声明 mutation_permission，拒绝操作记录到 JSONL。以便携 zip 与源码构建（CMake+Ninja，C++17）两种方式提供。限制：仅限自有或授权软件，MCP 管道令牌可被同用户读取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Cheat Engine 级内存扫描并读写 .CT 兼容表
- 内置原生 MCP 服务器，支持动态附加与多目标并发
- 默认只读 + 双重写权限门控（--allow-writes 与 mutation_permission）
- x86/x64 双架构运行时，桌面端 Dear ImGui + D3D11 便携运行

## 适用场景

- 调试与逆向分析我自己拥有的 Windows 软件
- 让 AI agent 在我监督下读取和修改目标进程内存
- 游戏模组调试、崩溃诊断与内存数值追踪

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: **Runtime inspection, debugging and reverse engineering for Windows software, in one native app — with a first-class
> L23: - **One app, not a toolbox.** Scanner, memory viewer, disassembler, debugger, patcher, tracer, RE workspace, script
> L25: - **Built for agents too.** `cortex.exe mcp` is a native MCP server: attach processes on the fly, drive several tar

## 星数曲线

```mermaid
xychart-beta
    title "PdB333/cortex 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-27 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `de6f95d6cfd6` · [字段定义](../../DATASET.md)*
