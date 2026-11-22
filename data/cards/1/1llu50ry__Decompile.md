# 1llu50ry/Decompile

⭐ 587 · TypeScript · MIT · 推送 2026-11-21 · [GitHub](https://github.com/1llu50ry/Decompile) · [官网](https://github.com/1llu50ry/Decompile) · 个人维护

**面向逆向工程/游戏安全的 MCP 服务器：聚合 RE 工具与 6000+ 技能库**

一个面向二进制逆向与应用行为分析的 MCP 服务器：通过单一连接聚合 60+ RE/调试后端（Ghidra、IDA、Binary Ninja、radare2、x64dbg 等），内置 230+ 原生 MCP 工具（PE/ELF/Mach-O/DEX 等格式解析、签名扫描、熵分析），并策展 6,000+ 技能、170+ agent、3,000+ prompt 等知识资产，支持多 agent 协作 mesh。定位用户为安全研究、反作弊分析、恶意软件分析等从业者，声明仅用于授权分析与防御性工程。安装提供安装脚本、npx 一行命令与源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聚合 60+ RE/调试 MCP 后端，smart_decompile 自动挑选可用后端
- 230+ 原生 MCP 工具：PE/ELF/DEX/WASM/.NET/GGUF 等解析、AoB 签名扫描、熵分析
- 6,000+ 技能、170+ agent、190+ 插件、3,000+ prompt 的可检索知识库
- decompile setup 一行命令注册到 42 个 MCP 客户端

## 适用场景

- 分析游戏或应用二进制的加壳、加密常量与结构
- 反作弊工程师研究绕过手法并加固自身系统
- 恶意软件/移动安全分析中调用 Frida、JADX 等后端
- CTF pwn 题中用 pwndbg/angr/AFL++ 做漏洞研究

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: ### One MCP for reverse engineering across binaries, applications, and runtime behavior.
> L21: 1. **Aggregates 60+ RE / debug MCP backends** behind one connection — `smart_decompile` picks IDA when running, fal
> L25: 5. **Ships a one-shot CLI** (`decompile setup`, `decompile analyze <path>`, `decompile capabilities`, `decompile do


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `2e5520d4e22b` · [字段定义](../../DATASET.md)*
