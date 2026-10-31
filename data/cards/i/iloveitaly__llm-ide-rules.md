# iloveitaly/llm-ide-rules

⭐ 13 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/iloveitaly/llm-ide-rules) · [官网](https://github.com/iloveitaly/llm_ide_rules) · 个人维护

**跨 IDE 的 LLM 指令规则下载与格式转换 CLI 工具**

面向使用 AI 编码助手的开发者：将集中维护的 LLM 提示指令下载到本地，并在 Cursor、Claude Code、GitHub Copilot、OpenCode、Codex 等不同 IDE 的指令/命令格式之间进行 explode（拆分为多个规则文件）与 implode（合并）转换。支持从 GitHub 下载更新并保留本地自定义内容（通过标记追加），也提供将项目内改进的提示提取回上游仓库的流程。通过 uvx 以 CLI 形式安装运行；本地开发依赖 uv、just、zsh、jq。README 声明部分 glob 假设与作者个人的 Python/TypeScript 模板和工具选择（如 fastapi）绑定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一指令源在 5 种 AI 编码工具间格式转换（explode/implode）
- download 命令拉取上游更新并保留标记以下的本地自定义指令
- 支持 GITHUB_TOKEN 认证访问私有仓库与规避 API 限流
- 提供 git diff + patch 流程将项目内提示改动提取回上游

## 适用场景

- 我在多个 IDE（Cursor/Copilot/Claude Code）间复用同一套编码指令
- 我维护跨项目的 LLM 编码规则并集中同步更新
- 我想把项目里改进的提示贡献回统一仓库

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L8: This project makes it easy to download prompts and implode/explode them so they can be used by various providers. It
> L18: Different AI coding assistants use different formats for instructions and commands:
> L50: The `llm-ide-rules` CLI provides commands to manage LLM IDE prompts and rules:

## 星数曲线

```mermaid
xychart-beta
    title "iloveitaly/llm-ide-rules 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0984ee43c068` · [字段定义](../../DATASET.md)*
