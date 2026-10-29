# YanpengQi7/ai-reliability-copilot

⭐ 83 · TypeScript · 推送 2026-10-18 · [GitHub](https://github.com/YanpengQi7/ai-reliability-copilot) · [官网](https://ai-reliability-copilot.vercel.app) · 个人维护 · 中文 README

**面向 SRE 的事件调查 AI 副驾：产出结构化诊断与响应**

输入事故、告警、日志、指标或值班笔记，生成 9 段结构化响应（摘要与严重度分级、排序的根因假设及引用证据、调查清单、带回滚的缓解措施、客户影响、事后复盘草稿、后续跟进）。以 Next.js Web 应用提供，另有 CLI 与 MCP 服务器可接入现有 AI 客户端。用 AI SDK + Zod 保证结构化输出，DeepSeek 同时充当分析器与评审（可换单文件换供应商）。证据工作区保留支持与矛盾引用，浏览器端做凭证脱敏，证据上限 5 万字符。需 Node.js 22+，持久化依赖 Supabase 可选配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 段结构化事故响应输出（Zod schema 强制）
- 证据优先：引用审计、缺失/冲突记录标记、支持与矛盾证据并存
- 5 场景回归套件 × 双语 × LLM-as-judge 评审管线，含 3 次重复与误差条报告
- Web / CLI / MCP 三种使用方式，报告可导出 Markdown/JSON

## 适用场景

- 值班时把 Datadog/PagerDuty 告警贴进来快速拿到严重度与排查步骤
- 通过 MCP 客户端检索 runbook 与历史事件并保存分析
- 用回归套件与 LLM 评审管线迭代提示词并复现对比

## 场景标签

`RAG` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: Give it an incident, alert, logs, metrics, or on-call notes. It produces a structured response with severity, ranke
> L66: - **DeepSeek** for both analyzer and judge (provider-swappable in one file)

## 星数曲线

```mermaid
xychart-beta
    title "YanpengQi7/ai-reliability-copilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 82 --> 84
    line [83, 83]
```

2026-10-18 83 → 2026-10-29 83（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4c037e08ac88` · [字段定义](../../DATASET.md)*
