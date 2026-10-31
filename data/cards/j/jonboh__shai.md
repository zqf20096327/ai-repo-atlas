# jonboh/shai

⭐ 27 · Rust · MIT · 推送 2026-03-30 · [GitHub](https://github.com/jonboh/shai) · [官网](https://jonboh.dev/posts/shai/) · 个人维护

**终端内的 LLM Shell 助手：按描述生成命令并解释命令**

用 Rust 编写的命令行 AI 助手，通过 OpenAI 模型（GPT-3.5-turbo/GPT-4 系列）按自然语言描述生成 shell 命令，或解释已有命令的作用与副作用，并会指出潜在危险命令。通过 shell 集成脚本（Bash/Zsh/Fish/Nushell/PowerShell）绑定快捷键，把生成的命令直接写回命令行缓冲区。无对话记忆，每次请求独立发送；--operating-system/--shell 选项提供环境上下文，另有 pwd/depth/environment 等默认关闭的实验性上下文选项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言描述生成 shell 命令，Ctrl+a 接受后写回缓冲区
- 解释命令用途、副作用并标注危险操作
- 支持 Bash/Zsh/Fish/Nushell/PowerShell 集成脚本与快捷键
- 实验性上下文选项：工作目录、目录树、环境变量、可用程序列表

## 适用场景

- 不记得命令语法时快速生成正确的 shell 命令
- 解释教程或论坛中拿来的陌生命令，确认副作用
- 在终端内通过快捷键即时生成与核验命令

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L4: - Command Generation: Shai allows you to quickly ask a LLM model to generate a command based on what it should do.
> L20: The model explanations will briefly explain the command and enumerate a list of common side-effects.

## 星数曲线

```mermaid
xychart-beta
    title "jonboh/shai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2d6b2c000594` · [字段定义](../../DATASET.md)*
