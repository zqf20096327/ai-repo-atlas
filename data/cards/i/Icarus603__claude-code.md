# Icarus603/claude-code

⭐ 27 · TypeScript · 推送 2026-10-14 · [GitHub](https://github.com/Icarus603/claude-code) · 个人维护 · 中文 README

**Claude Code 的个人维护衍生版：单二进制终端编码 agent**

以 Claude Code v2.1.88 sourcemap 为基线重构的公开衍生 CLI（命令 ccb），单人维护，与 Anthropic 无关联。单一 agent 循环接入 Claude 订阅（OAuth）、Anthropic API、Anthropic 兼容端点、ChatGPT Codex（OAuth）、OpenAI 兼容端点（Ollama/DeepSeek/vLLM 等）及 Gemini；支持 macOS/Linux/Windows（ARM64 Windows 不支持）。功能含文件级持久记忆与 /dream 记忆整理、/loop 定时任务、后台会话 TUI 仪表盘、Agent Teams 多会话协作与确定性 Workflow 编排脚本。一行脚本安装，无需 Node/Bun。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一二进制，curl/iex 一行脚本安装并自动更新
- 多提供商接入：Claude 订阅/Anthropic API/ChatGPT Codex/OpenAI 兼容端点/Gemini
- Agent Teams 多会话协作与可恢复的 Workflow 编排脚本
- 基于文件的持久记忆及 /dream 四阶段记忆整理

## 适用场景

- 在终端用自然语言驱动代码重构、解释与测试编写
- 并行派出多个 agent 会话做 PR 审查或竞争性假设调试
- 跨提供商切换模型运行同一编码 agent

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L21: Terminal coding agent. Single binary `ccb`. Talks to Anthropic (OAuth or API key), Anthropic-compatible endpoints, 
> L23: Solo-maintained public derivative of Claude Code; baseline reconstructed from the v2.1.88 sourcemap (2026-03-31), w

## 星数曲线

```mermaid
xychart-beta
    title "Icarus603/claude-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9070d4ba08e8` · [字段定义](../../DATASET.md)*
