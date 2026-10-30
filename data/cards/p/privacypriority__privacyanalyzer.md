# privacypriority/privacyanalyzer

⭐ 18 · TypeScript · Apache-2.0 · 推送 2026-08-10 · [GitHub](https://github.com/privacypriority/privacyanalyzer) · [官网](https://privacyanalyzer.in) · 组织维护

**面向印度 DPDP 法案的 AI 隐私政策分析 Web 应用**

基于 Next.js/TypeScript 的 Web 应用：用户提交网站 URL，系统通过三级抓取（Firecrawl、Crawlee Playwright、原生 fetch）获取隐私政策，再用 OpenRouter 模型（默认 DeepSeek Chat）按 6 个加权类别、120+ 条标准对照 DPDP Act 2023 与 DPDP Rules 2025 全部 23 条规则进行分析，输出用户视角的隐私评分与合规评分（1-10）、风险分级与改进建议。面向普通用户、企业主与合规/法务团队。自部署需 Node.js 18+ 与 OpenRouter API key，Firecrawl 为可选，托管在 Vercel。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双评分体系：Overall Privacy Score 与 DPDP Compliance Score（1-10）
- 覆盖 DPDP Rules 2025 全部 23 条规则与 7 个附表，120+ 评估标准
- 三级抓取降级：Firecrawl → Crawlee Playwright → 原生 fetch
- 5 级风险分类与 A+ 至 F 字母等级

## 适用场景

- 分析某网站的隐私政策对个人数据的处理方式与风险
- 企业自查隐私政策是否符合印度 DPDP 法案要求
- 法务/合规团队获取带法条引用的合规差距报告

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L9: **India's first AI-powered privacy policy analyzer helping users understand how websites handle their personal data 
> L28: - 🤖 **AI-Powered**: OpenRouter models (default `openrouter/free`, with NVIDIA Nemotron and GPT-OSS fallbacks) for s
> L214: - **AI Model**: DeepSeek Chat via OpenRouter

## 星数曲线

```mermaid
xychart-beta
    title "privacypriority/privacyanalyzer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `d6a369fa2ceb` · [字段定义](../../DATASET.md)*
