# Lethe044/agentskill-kit

⭐ 48 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/Lethe044/agentskill-kit) · [官网](https://lethe044.github.io/agentskill-kit/) · 个人维护

**给开发者：编码代理 SKILL.md 技能的检查、生成与跨代理导出 CLI 工具包**

面向使用 Claude Code、Cursor、Codex 等编码代理的开发者的命令行工具包：对 SKILL.md 技能做 lint、安全扫描（提示注入/隐藏 unicode/密钥/危险命令）、隔离运行自带测试并打分；支持用本地或免费模型（Ollama、LM Studio、Groq、Gemini 免费层、OpenRouter 免费模型）从任务描述生成技能并自动验证迭代，还可挖掘 shell 历史生成技能草稿、导出到 7 种代理格式、通过校验和验证的注册表安装技能。无运行时依赖，Python 3.9+，提供 GitHub Action 与 pre-commit 集成。限制：扫描器为启发式过滤器，askit test 非沙箱，不可信技能需容器运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- lint/scan/test/score 组成技能质量门禁，离线可用
- forge 用免费或本地模型生成技能，由 lint/scan/test 决定是否通过
- 一键导出到 Claude Code、Cursor、Windsurf、Copilot、Codex、Gemini CLI、Hermes
- 注册表下载带校验和验证，安装前先 lint 和扫描

## 适用场景

- 在信任或安装技能前做安全扫描和测试
- 为多个编码代理维护同一份技能并分别导出
- 在 CI 中对技能目录执行质量门禁
- 从 shell 历史中发现可沉淀为技能的重复工作流

## 场景标签

`提示工程` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L8: **agentskill-kit** is a command line toolkit for agent skills, the `SKILL.md` folders that coding agents such as
> L17: - **Export** one skill to Claude Code, Cursor, Windsurf, Copilot, Codex and Gemini CLI.

## 星数曲线

```mermaid
xychart-beta
    title "Lethe044/agentskill-kit 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-31"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-26 48 → 2026-10-31 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `b4c7ab3519c0` · [字段定义](../../DATASET.md)*
