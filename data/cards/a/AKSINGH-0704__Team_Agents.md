# AKSINGH-0704/Team_Agents

⭐ 17 · Python · MIT · 推送 2026-03-28 · [GitHub](https://github.com/AKSINGH-0704/Team_Agents) · [官网](https://policyai-app.vercel.app) · 组织维护

**健康保险保单智能问答平台：读保单 PDF、检测隐藏陷阱**

面向投保人的全栈 AI 平台（Next.js 14 + FastAPI + GPT-4o-mini + Supabase pgvector），覆盖健康保险全周期：自然语言保单发现与排名、19 维保单对比、上传保单 PDF 的三层混合 RAG 问答（语义+关键词 RRF 融合），输出覆盖判定（COVERED/NOT_COVERED 等）、赔付可行性评分、8 类隐藏陷阱检测与条款级引用，另有医疗报告→保单匹配、理赔资格咨询与覆盖缺口分析。目录含印度 10 家保险公司、30+ 份真实保单 PDF。定位为教学与演示用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三层混合 RAG（pgvector 语义 + tsvector 关键词 + RRF 融合）检索保单条款
- 检测 8 类隐藏陷阱（房间费上限、等待期、子限额等）并给出条款引用
- 覆盖判定/赔付红绿灯/置信度评分的可解释输出
- 结构化目录含 10 家印度保险公司与 30+ 份已解析嵌入的保单 PDF

## 适用场景

- 上传保单 PDF 询问某治疗是否覆盖并获得带引用的判定
- 按预算和既往病症对比筛选健康保险
- 理赔前评估可行性并获取所需文件清单

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L22: **PolicyAI** is an end-to-end AI-powered platform covering the **full health insurance lifecycle** — from finding t
> L41: Upload any policy PDF and ask any coverage question. The **3-layer hybrid RAG pipeline** retrieves the most relevan
> L111: |**LLM**|OpenAI GPT-4o-mini|Structured JSON reasoning at temperature 0.1|

## 星数曲线

```mermaid
xychart-beta
    title "AKSINGH-0704/Team_Agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `575cd02851ac` · [字段定义](../../DATASET.md)*
