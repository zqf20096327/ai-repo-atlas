# woldann/exoproc

⭐ 102 · TypeScript · MIT · 推送 2026-10-31 · [GitHub](https://github.com/woldann/exoproc) · 个人维护

**让 AI agent 经 MCP 检查与插桩 Windows x64 进程的 CLI 工具箱**

Exoproc 提供 21 个工具的 MCP 服务器与独立终端 CLI，面向 Windows x64 进程的逆向与插桩：进程发现、内存读写与模式扫描、5 字节 MinHook 函数挂钩、线程上下文重定向执行远程调用、TinyCC 将 C 编译为 x86_64 shellcode、窗口枚举与截图、JAR/JVM 检查，全程零 DLL 注入且不使用 CreateRemoteThread。setup 向导自动发现并配置已安装的 AI agent，写入门 stdio MCP 配置并安装技能文件；实时插桩命令仅能在 Windows x64 上原生运行，编译/仿真等离线操作支持跨平台。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 21 工具 MCP 服务器（stdio）+ 统一 CLI 双形态
- 零 DLL 注入、无 CreateRemoteThread 的线程上下文重定向执行
- TinyCC JIT 将 C 编译为可重定位 x86_64 shellcode，含离线仿真验证
- setup 向导自动配置 Claude Code/Cursor 等 8 类 agent 并备份配置

## 适用场景

- 让 AI 编码 agent 调试运行中的进程、读取内部状态、拦截 API 调用
- 对原生 Windows 应用做实时内存修改与函数挂钩
- 将 C 代码编译为 shellcode 并反汇编验证
- 枚举桌面窗口控件并截图供 agent 分析

## 场景标签

 · 领域:开发者工具/逆向与进程插桩

## 证据(README 行号)

> L27: **Exoproc connects your AI coding agent directly to Windows x64 process internals.** It equips agents (Claude Code,
> L219: Exoproc exposes **21 high-performance tools** over standard Model Context Protocol (stdio):
> L23: > Exoproc targets native **Windows x64** process runtime. Development and offline operations (C-to-shellcode JIT co

## 星数曲线

```mermaid
xychart-beta
    title "woldann/exoproc 星数(近 2 点)"
    x-axis ["2026-11-20", "2026-11-25"]
    y-axis "stars" 101 --> 103
    line [102, 102]
```

2026-11-20 102 → 2026-11-25 102（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `ebd4e4be12fa` · [字段定义](../../DATASET.md)*
