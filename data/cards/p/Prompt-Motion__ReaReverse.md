# Prompt-Motion/ReaReverse

⭐ 4 · TypeScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/Prompt-Motion/ReaReverse) · [官网](https://reareverse.com) · 组织维护 · 中文 README

**面向逆向工程 agent 的 MCP 工具集：检查二进制与应用行为**

REA 是一个 MCP 服务器与 CLI，将用户的 agent 连接到检查原生二进制、JavaScript/Electron 应用、.NET 程序集、网站、APK、固件、抓包等目标的工具；分析在本地运行，结果附带证据与局限说明。Setup 命令向支持 MCP 的 agent（Claude Code、Codex、Cursor、Gemini CLI 等）注册服务器并安装工作流说明；深度原生分析需已有的 Hopper/Ghidra/IDA。需 Node.js 22.x/24.x/26+ 与 npm，通过 npm 包分发（MIT）。

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

- 以 MCP 服务器接入任意支持本地 MCP 的 agent，附带 CLI 独立使用
- 覆盖原生二进制、Electron、.NET、APK、固件、抓包、逻辑信号等 20 类分析目标
- 静态 JavaScript/.NET 分析无需原生分析引擎；原生分析可复用已有 Hopper/Ghidra/IDA
- 分析在本地进行，结果包含证据与局限

## 适用场景

- 让 agent 逆向分析无源码应用的功能实现并给出证据
- 检查原生二进制的伪代码、汇编与符号引用
- 分析 Electron 应用模块、IPC 与原生插件关系
- 解析 APK、固件与抓包文件的结构与内容

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L6: ### One MCP for reverse engineering across binaries, applications, and runtime behavior.
> L41: REA connects your agent to tools for inspecting native binaries, JavaScript and Electron apps, .NET assemblies, and
> L66: Setup supports Claude Code, Codex, Cursor, Gemini CLI, Grok Build and

## 星数曲线

```mermaid
xychart-beta
    title "Prompt-Motion/ReaReverse 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-11-08", "2026-11-23"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-26 3 → 2026-11-23 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `0b5f57156e7a` · [字段定义](../../DATASET.md)*
