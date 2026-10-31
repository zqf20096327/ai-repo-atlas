# toratako/ghidra-cli

⭐ 14 · Rust · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/toratako/ghidra-cli) · 个人维护

**面向 AI agent 的 Ghidra 无头逆向 CLI，输出结构化 JSON**

用 Rust 编写的命令行工具，供 AI agent 自动化原生二进制逆向工程：反编译、查询、类型、脚本与补丁，每项目维持一个持久 Java 桥接，在 Ghidra 的 JVM 中保留分析状态。需另行安装 Ghidra 与 JDK 21，通过 cargo 从源码构建或下载预编译二进制（Windows/Linux/macOS）。附带可安装到 Claude Code、Codex、Cursor 等 agent 的技能包，并给出在 ChatGPT Web Chat Linux 沙箱中运行的流程。项目声明处于活跃开发期，不保证向后兼容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 反编译、查询、类型、脚本与补丁命令，输出结构化 JSON
- 每项目持久 Java 桥接，跨命令保留 Ghidra JVM 分析状态
- 提供适配 Claude Code/Codex/Cursor/Gemini CLI/OpenCode 的技能包
- 提供 ghidra-cli doctor 运行环境诊断命令

## 适用场景

- 让 AI agent 无头执行 Ghidra 二进制分析与反编译
- 在 CTF 或逆向工作流中以 CLI 形式驱动 Ghidra
- 把 Ghidra 能力以技能包形式接入编码 agent

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: A Rust CLI for AI agents automating native-binary reverse engineering with
> L8: Ghidra: decompilation, queries, types, scripts, and patches. One persistent Java

## 星数曲线

```mermaid
xychart-beta
    title "toratako/ghidra-cli 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `19b8671e07d2` · [字段定义](../../DATASET.md)*
