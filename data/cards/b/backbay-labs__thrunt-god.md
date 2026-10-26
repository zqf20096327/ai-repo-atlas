# backbay-labs/thrunt-god

⭐ 41 · JavaScript · MIT · 推送 2026-07-13 · [GitHub](https://github.com/backbay-labs/thrunt-god) · 组织维护

**面向 agentic IDE 的威胁狩猎命令系统**

以斜杠命令与工作流形式嵌入 Claude Code、OpenCode、Gemini、Codex、Copilot、Cursor、Windsurf 等 agentic IDE 的威胁狩猎系统。每场狩猎按 Signal→Hunt→Swarm→Receipt→Publish 五阶段推进：从检测信号立案、形成可检验假设、并行 agent 执行调查，到证据链绑定查询与时间戳，最终仅打包经校验的发现。状态以文件形式存放于 .planning/ 目录，支持 git 提交与 workstream 隔离。通过 npx 安装，另有 VS Code 扩展 alpha 版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 五阶段狩猎流程：Signal→Hunt→Swarm→Receipt→Publish
- 并行 agent（Swarm）执行结构化调查，证据绑定查询与时间戳
- /thrunt:autonomous 一条命令端到端跑完剩余阶段
- 所有查询、回执与发现以文件形式存放于 .planning/ 目录

## 适用场景

- 安全分析师在 IDE 中从检测信号立案并推进威胁狩猎
- 建立长期威胁狩猎项目并按信号反复开案
- 需要每条结论绑定证据链的合规化狩猎流程

## 场景标签

`网络安全` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L11:  Threat hunting command system for agentic IDEs.
> L65: |**Swarm**|Parallel agents execute structured investigations across available sources|

## 星数曲线

```mermaid
xychart-beta
    title "backbay-labs/thrunt-god 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-26 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `63c42a3bb110` · [字段定义](../../DATASET.md)*
