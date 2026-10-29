# Grolea-HQ/paperclip-blueprints

⭐ 18 · Python · MIT · 推送 2026-09-14 · [GitHub](https://github.com/Grolea-HQ/paperclip-blueprints) · [官网](https://www.grolea.com/paperclip-blueprints) · 组织维护

**从 Markdown 简报生成可导入 Paperclip 的 agent 公司包**

面向 Paperclip 平台用户的 CLI 工具：读取描述公司身份、目标、约束的结构化 Markdown 简报，调用 Anthropic API（Claude Opus 4.8 / Sonnet 4.6）生成符合 paperclip/v1 与 agentcompanies/v1 schema 的完整目录树（.paperclip.yaml、COMPANY.md、agents/projects/tasks/skills 等），可直接导入 Paperclip 实例。关键机制包括按角色派生的 run-policy 上限、确定性派生的 routine 调度时间、canon 条目编码与 reach 检查（advisory 不阻塞）。限制：需 Python 3.11+、uv、Anthropic API key（每次生成约 $1–3，3–8 分钟），以及一个 Paperclip 实例。v0.1 完成态，兼容性声明标注了日期并声明会过期。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 结构化 Markdown 简报 → schema 校验通过的 Paperclip 公司包
- per-agent run-policy 上限（turn cap、并发限制、heartbeat 开关）
- routine 调度由任务 slug 确定性派生，同一简报产出相同计划
- canon 条目逐项 reach 检查（carried/thin/missing/coverage unknown）

## 适用场景

- 我不想手写身份文档与组织结构，用简报一键生成 Paperclip 公司包
- 为多 agent 公司设定调度例程与 run-policy 上限
- 核对规则条目是否真的落到生成的 agent 程序文件中

## 场景标签

`代码生成` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7: A CLI tool that takes a structured Markdown brief and generates a complete, deployable **Paperclip company bundle** 
> L111: - Anthropic SDK (LLM access — Claude Opus 4.8 and Sonnet 4.6)

## 星数曲线

```mermaid
xychart-beta
    title "Grolea-HQ/paperclip-blueprints 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-29 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `2e8974bbd493` · [字段定义](../../DATASET.md)*
