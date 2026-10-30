# xpepper/perplexity-agent-skill

⭐ 19 · Shell · MIT · 推送 2026-02-02 · [GitHub](https://github.com/xpepper/perplexity-agent-skill) · 个人维护

**为 AI 编码助手接入 Perplexity 联网检索的 Agent Skills 包**

一个符合 Agent Skills 标准的技能包，通过 Perplexity CLI（llm 及 llm-perplexity 插件）让 AI 编码助手具备联网检索、独立验证与深度推理委托能力，兼容 Claude Code、GitHub Copilot、Cursor、Windsurf 等 30+ agent。需 Perplexity API key，按任务选用 sonar/sonar-pro/sonar-reasoning 等模型。提供 npx skills CLI 快速安装与手动 git clone 两种方式。

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

- 基于 Perplexity CLI（llm + llm-perplexity 插件）而非 MCP 服务器
- 支持 Agent Skills 标准的 30+ AI 编码助手
- 按任务自动选择 sonar/sonar-pro/sonar-deep-research 等 5 种模型
- 提供 .skill 打包脚本 package-skill.sh

## 适用场景

- 让编码助手查询最新文档与库版本信息
- 对架构和技术选型决策做独立第二意见验证
- 将复杂多步推理任务委托给 Perplexity 深度推理模型

## 场景标签

 · 领域:AI 编码助手/agent 技能

## 证据(README 行号)

> L1: # Perplexity Web Research Skill
> L3: An Agent Skills package that leverages the Perplexity CLI for web research, deep reasoning, and independent validati
> L37: This skill uses the Perplexity CLI (`llm` with `llm-perplexity` plugin) instead of MCP servers because:

## 星数曲线

```mermaid
xychart-beta
    title "xpepper/perplexity-agent-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `f2c2de31e395` · [字段定义](../../DATASET.md)*
