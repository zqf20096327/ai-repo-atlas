# fainir/most-capable-agent-system-prompt

⭐ 889 · MIT · 推送 2026-11-22 · [GitHub](https://github.com/fainir/most-capable-agent-system-prompt) · [官网](https://aiyourwork.chat/guides/lead-follow-up-for-service-companies?utm_source=github&utm_medium=about&utm_campaign=lead-follow-up-demo-en#sample-enquiry) · 个人维护

**给编码代理用的系统提示词：驱动其搭建自改进代理系统**

一个可复制的系统提示词（约 2,950 行/23,000 tokens），供 Claude Code、Codex、Cursor 等编码代理使用者粘贴到会话首条消息或系统提示中。粘贴后代理按提示中的 BUILD ORDER 指令搭建包含任务图、验证、文件记忆、评测与自改进循环的代理系统，支持两种实现姿态：以现有代理为执行引擎的 harness 包装模式，或基于 Agent SDK 的原生运行时模式。仅提供提示词文本与使用说明，本体不含代码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以文件为载体的项目操作系统（AGENTS.md/plan.md/tasks.md/knowledge.md 等）
- 两种实现模式：harness 包装现有代理或基于 Agent SDK 从零构建
- 提示词约 23,000 tokens，与 OpenAI/Claude 分词器兼容性均有说明
- 提供 macOS/Linux 终端复制命令与三种使用方式（首条消息/系统提示/指令文件）

## 适用场景

- 让编码代理为我搭建跨会话可持续工作的自动化任务系统
- 把多月份的多阶段项目交给代理持续执行并保持记忆
- 在代理执行中加入验证、审批与预算控制机制

## 场景标签

`提示工程` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5: A copy-paste system prompt for people who use coding agents like Claude Code, Codex, or Cursor: paste it in, and you
> L7: Left alone, most agent sessions forget everything between runs, call work done without checking it, and stall once a
> L52: 2. Start your agent in an empty folder (or in the repo you want it to extend) and paste the prompt as your first me

## 星数曲线

```mermaid
xychart-beta
    title "fainir/most-capable-agent-system-prompt 星数(近 11 点)"
    x-axis ["2026-10-28", "2026-10-30", "2026-11-01", "2026-11-02", "2026-11-08", "2026-11-11", "2026-11-12", "2026-11-14", "2026-11-16", "2026-11-21", "2026-11-25"]
    y-axis "stars" 877 --> 891
    line [878, 879, 880, 881, 885, 887, 888, 889, 890, 889, 889]
```

2026-10-28 878 → 2026-11-25 889（+11）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `17324fd7d6f2` · [字段定义](../../DATASET.md)*
