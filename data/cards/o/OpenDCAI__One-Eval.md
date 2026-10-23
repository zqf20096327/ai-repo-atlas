# OpenDCAI/One-Eval

⭐ 164 · Python · Apache-2.0 · 推送 2026-08-31 · [GitHub](https://github.com/OpenDCAI/One-Eval) · [官网](https://wcny4qa9krto.feishu.cn/wiki/AJX6w5SbGiJxctkQQdfckVqKnYf) · 组织维护 · 中文 README

**基于 Agent 的 LLM 自动评测框架：自然语言到评测报告**

基于 DataFlow 与 LangGraph 构建的 LLM 自动化评测框架，主打 NL2Eval：输入自然语言评测目标后自动完成 benchmark 推荐、数据准备、推理执行、指标匹配、打分与多维报告生成，并将评测重构为图结构（Graph/Node/State）的可追溯、可中断流程，支持人在关键节点介入。内置 Bench Gallery 统一管理 MATH、GSM8K、MMLU、CEval 等纯文本基准元信息。提供两种使用方式：在 Claude Code 等编码 agent 中以 Skill 直接调用，或部署 FastAPI 后端加 React 前端的 Web UI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- NL2Eval：自然语言目标自动编排完整评测流程并生成报告
- 图结构执行（Graph/Node/State），支持中断与人工干预
- 内置 Bench Gallery 覆盖推理/通识/指令跟随等主流基准
- 可作为便携 Skill 在 Claude Code / Codex 内直接使用

## 适用场景

- 用一句自然语言启动 LLM 评测并获得报告
- 在 benchmark 选择、结果审查等节点人工介入调整策略
- 集成私有数据集与自定义评测指标

## 场景标签

`模型评测` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L14: One-Eval is an automated Agent-based evaluation framework for Large Language Models, designed to achieve **NL2Eval*
> L38: - 🧩 **End-to-End Automation**: Automatically completes benchmark recommendation, data preparation, inference execut

## 星数曲线

```mermaid
xychart-beta
    title "OpenDCAI/One-Eval 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 163 --> 165
    line [164, 164]
```

2026-10-18 164 → 2026-10-23 164（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7dbeff497628` · [字段定义](../../DATASET.md)*
