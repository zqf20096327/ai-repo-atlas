# AtomiJD/jdBasic

⭐ 19 · C++ · MIT · 推送 2026-10-29 · [GitHub](https://github.com/AtomiJD/jdBasic) · [官网](https://www.jdbasic.org) · 个人维护

**BASIC 解释器/编译器：内置数组、图形、本地 LLM 与 MCP 服务**

BASIC 语言的现代实现：字节码 VM 与 APL 风格数组向量化（IOTA/SCAN/SVD/FFT），内置 SDL3 图形、ImGui、Win32 窗体、音序器、HTTP/SQLite 等模块；可经 LLVM 编译为独立 .exe，并有裸机 x86-64 内核目标与 RP2350/ESP32-S3 微控制器移植。AI 相关部分：通过 llama.cpp 运行本地 LLM、ONNX Runtime 跑 ML 模型，并内置 MCP 服务器，使 Claude Code、Cursor 等 agent 可在程序运行中检查、修改并热替换 SUB。Windows 提供下载包，Linux/macOS 从源码构建。

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

- 字节码 VM + APL 风格数组运算，LLVM 编译为原生 .exe
- 内置 MCP 服务器，AI agent 可暂停运行中的程序、改写单个 SUB 后恢复执行
- llama.cpp 本地 LLM 与 ONNX Runtime ML 模型接入
- 微控制器移植（RP2350/ESP32-S3）与裸机 x86-64 内核编译目标

## 适用场景

- 用 BASIC 语法写图形游戏、桌面工具或小型 OS
- 让 Claude Code/Cursor 等 agent 通过 MCP 结对编程、运行时改代码
- 在程序内调用本地 LLM 或 ML 模型（如 Godot RPG 的 LLM NPC）
- 把脚本编译成独立 .exe 分发

## 场景标签

 · 领域:编程语言/开发工具

## 证据(README 行号)

> L15: jdBasic is a BASIC interpreter with a bytecode VM and APL-style arrays.
> L147: - llama.cpp for local LLMs, ONNX Runtime for ML models
> L151: - MCP server (`jdbasic --mcp`) for Claude Code, Cursor, Cline and other MCP clients

## 星数曲线

```mermaid
xychart-beta
    title "AtomiJD/jdBasic 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-30 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `6deae07f1cbe` · [字段定义](../../DATASET.md)*
