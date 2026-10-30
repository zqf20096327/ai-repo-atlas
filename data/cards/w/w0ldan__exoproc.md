# w0ldan/exoproc

⭐ 74 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/w0ldan/exoproc) · [官网](exoproc.woldan.me) · 个人维护

**面向 AI agent 的 Windows x64 进程逆向与插桩 MCP 工具集**

TypeScript 编写的统一 CLI 与 MCP 服务器（stdio），把 Claude Code、Cursor 等 AI 编码代理接入 Windows x64 进程内部：进程发现、内存读写与模式扫描、5 字节 MinHook 函数 detour、nthread 线程劫持、TinyCC C-to-shellcode JIT 编译、确定性 x86_64 模拟、窗口枚举与截图、JAR/JNI 分析，共 22 个 MCP 工具。实现零 DLL 注入、不使用 CreateRemoteThread。实机插桩命令仅限 Windows x64；编译与模拟等离线操作可跨平台。安装途径含 npx、bun x、PowerShell 脚本与 AOT 独立 exe。

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

- 22 个 MCP 工具覆盖进程发现、内存操作、函数 detour、线程劫击与 C JIT
- 零 DLL 注入、不使用 CreateRemoteThread 的插桩机制
- 嵌入式 TinyCC 将 C 代码编译为 x86_64 shellcode，附 Capstone 反汇编
- exoproc setup 自动检测并配置 8 种 AI agent/IDE

## 适用场景

- 让 Claude Code 等 AI 代理检查并逆向运行中的 Windows 应用
- 实时拦截 Win32 API、读取目标进程内部状态
- 把 C 代码即时编译为 shellcode 并在目标进程内执行

## 场景标签

 · 领域:系统编程/逆向工程工具

## 证据(README 行号)

> L3: ### One unified CLI and Model Context Protocol (MCP) server for Windows x64 reverse engineering, thread hijacking, f
> L27: **Exoproc connects your AI coding agent directly to Windows x64 process internals.** It equips agents (Claude Code,
> L219: Exoproc exposes **22 high-performance tools** over standard Model Context Protocol (stdio):


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5d22a2892ab7` · [字段定义](../../DATASET.md)*
