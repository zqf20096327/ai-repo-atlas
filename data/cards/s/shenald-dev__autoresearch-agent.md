# shenald-dev/autoresearch-agent

⭐ 10 · TypeScript · GPL-3.0 · 推送 2026-11-08 · [GitHub](https://github.com/shenald-dev/autoresearch-agent) · [官网](https://shenald-portfolio.vercel.app) · 个人维护

**面向研究者与工程师的自主深度研究 CLI：多向量检索生成报告**

TypeScript 编写的 CLI 工具：将研究主题分解为多跳查询向量，经 Serper 或免配置 DuckDuckGo 搜索抓取来源（含 SSRF/DNS 重绑定防护、500KB 载荷上限），用 LangChain LCEL 链连接 OpenAI、DeepSeek、Ollama 等端点合成内容，导出 Markdown、HTML、JSON 三种报告并维护本地研究库。需 Node.js v18+ 与 LLM API Key；搜索 Key 可选。通过 npx 直接运行、npm 全局安装或源码克隆。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多向量查询分解，深度 1–5 可调，LLM 推理加确定性启发式回退
- 零配置搜索：无 Serper Key 时自动走 DuckDuckGo 抓取
- SSRF 与 DNS 重绑定加固：IP 预校验、阻断内网/回环/云元数据地址
- 导出带来源脚注的 Markdown、可打印 PDF 的独立 HTML 与 JSON 元数据

## 适用场景

- 快速调研技术选型并生成带来源引用的报告
- 为工程团队整理基准测试与生产事故复盘资料
- 搭建个人可检索的本地研究报告库

## 场景标签

`科研工具` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L21: **AutoResearch Agent** is an autonomous deep-research intelligence tool designed for engineers, researchers, and te
> L27: 4. **Synthesizes Insights** using modern LangChain Expression Language (LCEL) chains connected to OpenAI, DeepSeek,
> L39: - **🔌 Multi-Provider LLM Integration**: Full support for custom `OPENAI_BASE_URL` and custom `OPENAI_MODEL`, enabli

## 星数曲线

```mermaid
xychart-beta
    title "shenald-dev/autoresearch-agent 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-24"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-08 10 → 2026-11-24 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `93c977133f6e` · [字段定义](../../DATASET.md)*
