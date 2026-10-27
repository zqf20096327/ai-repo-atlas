# appcuarium/synapptic

⭐ 23 · Python · MIT · 推送 2026-03-25 · [GitHub](https://github.com/appcuarium/synapptic) · 个人维护

**分析 AI 编程会话并生成用户画像与行为守卫的持久记忆工具**

面向使用 AI 编程助手的开发者：synapptic 读取 Claude Code 的 JSONL 会话记录，经 LLM 提取沟通风格、工作流偏好与 AI 失败模式，生成含用户画像、偏好与行为守卫的配置文件，自动写入 Claude Code、Cursor、Copilot 等 9 种助手的规则文件。支持 Anthropic/OpenAI/Ollama 等多种处理提供方，含 LLM-as-judge 行为基准测试、本地会话回看面板（SQLite 索引、WebSocket 实时流）与后台自动处理钩子。以 pip 安装的 CLI 工具提供，标注为 Beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 从会话记录提取九个维度的用户画像与行为守卫，写入 9 种 AI 助手规则文件
- LLM-as-judge 基准测试逐条验证守卫有效性，可排除反向守卫
- 本地会话仪表盘：搜索历史会话、实时 WebSocket 流、token 用量与成本统计
- 支持 100% 本地模式（Ollama/LM Studio），数据不出本机

## 适用场景

- 让 Claude Code、Cursor 等助手在会话开始时自动加载我的偏好与规则
- 回顾和搜索全部历史 AI 编程会话并查看成本
- 在第二屏幕实时围观终端里的结对编程会话

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: **synapptic** analyzes your AI coding sessions and builds a living profile that your agent loads at the start of eve
> L58: |**Claude Code**|`~/.claude/projects/*/memory/user_archetype.md`|
> L72: **synapptic** currently reads session transcripts from **Claude Code** (`~/.claude/projects/*/*.jsonl`), which stor

## 星数曲线

```mermaid
xychart-beta
    title "appcuarium/synapptic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5d50075cd085` · [字段定义](../../DATASET.md)*
