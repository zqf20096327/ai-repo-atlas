# miloudbelarebia/sprint-agent

⭐ 24 · Python · MIT · 推送 2026-05-09 · [GitHub](https://github.com/miloudbelarebia/sprint-agent) · [官网](https://miloudbelarebia.github.io/sprint-agent/) · 个人维护

**给 AI 编程代理提供持久化敏捷冲刺上下文的 CLI 工具**

纯 Python、零依赖的命令行工具，为 AI 编程代理（Claude Code、Cursor、Copilot、Codex、Gemini、Aider、Windsurf）生成并维护 .sprint/ 目录，以 Markdown 文件承载 backlog、冲刺计划、每日状态与回顾，代理通过自动读取的配置文件在会话开始时获得项目上下文。提供 pip 安装与单文件两种分发方式，后者面向受限环境。README 中的 83% token 减少数字来自作者个人项目的基准测试，并声明结果会因项目而异。

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

- 生成 .sprint/ 目录：AGENT.md、冲刺文件、backlog 与回顾模板
- 兼容 7 种 AI 编程代理，通过各代理的自动读取配置文件接入
- 纯 Python 标准库实现，零依赖，支持单 .py 文件分发
- sprint-agent sync 命令将冲刺变更 git 提交推送

## 适用场景

- 独立开发者让 AI 代理在跨会话时保留项目进度记忆
- 以周冲刺和 backlog 结构组织 AI 辅助开发工作流
- 受限环境（企业防火墙、CI、离线机器）中单文件部署使用

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L15: Sprint Agent gives AI coding agents persistent memory and structured workflow — so they stop wasting tokens re-read
> L120: Works with any AI coding agent that reads project files:
> L122: |Agent|Auto-config file|How it works|

## 星数曲线

```mermaid
xychart-beta
    title "miloudbelarebia/sprint-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `229dca2d1f23` · [字段定义](../../DATASET.md)*
