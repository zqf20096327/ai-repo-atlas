# Lethe044/hermes-legal

⭐ 26 · Python · MIT · 推送 2026-10-10 · [GitHub](https://github.com/Lethe044/hermes-legal) · 个人维护

**免费多供应商 AI 合同审查工具：风险评分、红线建议与签/谈/拒结论**

面向开发者、自由职业者与小团队的命令行合同审查工具（同时提供 Python 包、Web 仪表盘与 GitHub Action）。读取 .txt/.pdf/.docx 合同，逐条评分风险（1-10），检测缺失标准条款，给出具体替换语言（可导出 DOCX/带 Word 修订标记的内联红线），并输出 SIGN/NEGOTIATE/REJECT 结论。默认内置离线规则引擎无需 API key；可接入 Groq、Gemini 免费额度或付费模型增强分析。支持按客户/交易方视角评分、批量扫描、版本对比、截止日期提取、合同组合仪表盘与 OCR。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐条风险评分与 SIGN/NEGOTIATE/REJECT 结论
- 内置离线规则引擎，无 API key 可用；可选 Groq/Gemini 免费额度
- 生成 Word 修订标记（OOXML Track Changes）的内联红线与 DOCX/PDF 报告
- 记忆历史合同，追踪交易方条款恶化趋势与续约/通知期限

## 适用场景

- 审阅 NDA、自由职业、雇佣等合同并给出可谈判的红线建议
- 批量扫描合同文件夹并生成 CSV/Excel/HTML 风险汇总
- 在 CI 中对 PR 里的合同文件自动审查并评论
- 跟踪多份合同的截止日期与交易方风险趋势

## 场景标签

 · 领域:法律科技/文档分析

## 证据(README 行号)

> L9: **Free, multi-provider AI contract analysis for developers, freelancers, and small teams.**
> L18: It works with zero budget: a built-in offline rule engine needs no API key at
> L19: all, and free tiers on Groq and Google Gemini give you full LLM-grade analysis

## 星数曲线

```mermaid
xychart-beta
    title "Lethe044/hermes-legal 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-29 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d9a9d9ef3264` · [字段定义](../../DATASET.md)*
