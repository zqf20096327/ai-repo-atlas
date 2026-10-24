# csy-csy123/pr-review-agent-council

⭐ 87 · Python · 推送 2026-05-24 · [GitHub](https://github.com/csy-csy123/pr-review-agent-council) · [官网](https://github.com/csy-csy123/pr-review-agent-council#readme) · 个人维护 · 中文 README

**多 Agent 辩论式 PR 代码审查工具，含 AI Judge 质量评估**

基于 learn-claude-code 工程思路、用 Python + Aliyun DashScope/Qwen 实现的只读 PR Review Agent：读取 Git diff 与 PR 描述，Security/Correctness/Test/Maintainability 等多 reviewer 生成候选 finding，Lead Debate Controller 动态执行质疑、补证、反驳、合并与裁决，ReportWriterAgent 输出固定 JSON schema 的标准化报告。可显式触发 AI Judge（默认 qwen-plus）按证据质量等维度评分。另含公司知识 RAG 对齐、Skill Loading 注入审查规范、JSONL transcript 可观测，支持 --llm-provider none 本地兜底模式。面向中文用户的学习与简历展示项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Debate Loop 多轮质疑/补证/合并/裁决的 finding 质量控制
- 只读 Tool Calling（git_diff、search_code、secret_scan 等受控工具）
- ReportWriterAgent 固定 JSON schema + 程序模板渲染标准化报告
- AI Judge 按 critical coverage、evidence quality 等维度评分
- 公司知识 RAG（DashScope embeddings，无 key 时 keyword_fallback）

## 适用场景

- 用多 Agent 辩论流程自动审查 PR diff 并产出结构化报告
- 学习 Multi-Agent 协作、Tool Calling 与 Skill Loading 的工程实现
- 对比不同 agent 策略的审查质量（debate vs council baseline）
- 把通用审查能力对齐到公司编码规范与安全基线

## 场景标签

`代码审查` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: 面向中文用户的 **Debate Council PR Review Agent**。项目基于 `learn-claude-code` 的 Agent 工程思路改造，用 Python + Aliyun DashScope/Qwen 
> L27: - **AI Judge 质量评估**：独立命令触发，默认使用 `qwen-plus`，按 critical issue coverage、evidence quality、severity accuracy、duplicate/
> L244: > 基于 Python、Aliyun DashScope/Qwen 实现 Debate Council PR Review Agent，构建 Security/Correctness/Test/Maintainability R

## 星数曲线

```mermaid
xychart-beta
    title "csy-csy123/pr-review-agent-council 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 86 --> 88
    line [87, 87]
```

2026-10-18 87 → 2026-10-24 87（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `1199699a3fc9` · [字段定义](../../DATASET.md)*
