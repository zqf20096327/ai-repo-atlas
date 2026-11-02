# terryso/ccshell

⭐ 12 · JavaScript · MIT · 推送 2026-02-21 · [GitHub](https://github.com/terryso/ccshell) · [官网](https://gptkit.eth.limo/14E1AB0A-C74D-4B92-A290-915EA41440C9/) · 个人维护 · 中文 README

**macOS 自然语言驱动 shell 命令的 CLI 工具**

面向 macOS 用户的命令行工具：将自然语言任务描述转换为 shell 命令并执行，支持 Claude Code CLI（默认）与 Gemini CLI 两种 AI 提供方。采用四层策略：优先用内置本地工具、经包管理器搜索安装现有工具、复用脚本库、最后生成新脚本。AI 生成的脚本自动保存到 ~/.ccshell/scripts/ 并按关键词相似度复用。README 明确警告其使用 --dangerously-skip-permissions 与 YOLO 模式绕过权限检查，建议仅在沙箱或可信开发环境使用。需 Node.js>=14 与 Claude Code CLI，通过 npm 全局安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言任务描述转换为 shell 命令并执行
- 四层策略：本地工具→在线搜索安装→脚本库复用→生成新脚本
- 脚本库自动保存 AI 生成脚本并按相似度复用
- 支持 Claude Code CLI 与 Gemini CLI 双提供方

## 适用场景

- 用自然语言完成批量文件重命名、媒体格式转换等命令行任务
- 不记忆命令语法也能完成系统管理与网络任务
- 复用历史 AI 生成脚本避免重复生成

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L14: ccshell allows you to describe tasks in natural language and automatically converts them to shell commands for exec
> L36: - **🤖 Multiple AI Providers**: Choose between Claude Code CLI (default, detailed output) and Gemini CLI (YOLO mode)
> L150: ### Supported AI Providers

## 星数曲线

```mermaid
xychart-beta
    title "terryso/ccshell 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-02"]
    y-axis "stars" 11 --> 13
    line [12, 12]
```

2026-10-18 12 → 2026-11-02 12（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0c03fe9c26ed` · [字段定义](../../DATASET.md)*
