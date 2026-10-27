# guywaldman/magic-cli

⭐ 745 · Rust · MIT · 推送 2026-04-21 · [GitHub](https://github.com/guywaldman/magic-cli) · [官网](https://guywaldman.com/posts/introducing-magic-cli) · 个人维护

**用 LLM 帮你在终端生成与搜索命令的 CLI 工具**

Rust 编写的命令行工具，借助 LLM 提供三类功能：按自然语言提示生成命令建议（suggest）、给出任务让模型尝试生成并执行命令（ask，实验性）、基于嵌入对 shell 历史做语义搜索（search，实验性）。支持本地 ollama 与云端 OpenAI 两种 LLM 供应方，可配置模型与嵌入模型。命令输出方式支持剪贴板或当前 shell 会话执行（后者标注 unsafe）。项目自述处于早期开发阶段，可能存在破坏性变更与 bug。通过安装脚本、Homebrew、PowerShell 脚本或预编译二进制安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- suggest/ask/search 三类命令生成与历史语义搜索功能
- 支持 ollama 本地与 OpenAI 云端两种 LLM 供应方
- 嵌入模型可配置（默认 nomic-embed-text / text-embedding-ada-002）
- 提供安装脚本、Homebrew、PowerShell 与预编译二进制多种安装方式

## 适用场景

- 忘记 ffmpeg/kubectl 等工具参数时用自然语言获取命令
- 描述任务让模型生成执行命令（ask，实验性）
- 在 shell 历史中做语义搜索找回曾用过的命令

## 场景标签

`代码生成` `语义搜索` · 领域:编码与开发

## 证据(README 行号)

> L7: Magic CLI is a command line utility which uses LLMs to help you use the command line more efficiently, inspired by p
> L21: - Suggest a command (see section)
> L24: - Use a local or remote LLM (see section)

## 星数曲线

```mermaid
xychart-beta
    title "guywaldman/magic-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 744 --> 746
    line [745, 745]
```

2026-10-18 745 → 2026-10-27 745（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `be5e3f2827d6` · [字段定义](../../DATASET.md)*
