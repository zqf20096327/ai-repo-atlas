# linxule/openinterviewer

⭐ 30 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/linxule/openinterviewer) · [官网](https://openinterviewer.vercel.app) · 个人维护 · 中文 README

**给研究者的开源 AI 定性访谈平台：AI 主持访谈并生成分析**

面向定性研究人员（UX/用户研究）的访谈平台：研究者配置研究、发放不含配置信息的不透明参与者链接，AI 访谈员（可编辑风格、3 种结构模式）执行访谈，先保存转录再运行分析，仪表盘中查看逐次综合、汇总分析与 Explore 问答（带定位引文）。支持 4 个 AI 提供商（Gemini/Claude/OpenAI/OpenRouter）直连或经网关调用。部署方式包括 Cloudflare 自托管（SQLite Durable Object）、Node/Vercel 自托管（需 Upstash）与托管研究者账号模式，另提供无需密钥的确定性演示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 访谈员执行访谈，转录先保存后分析，AI 失败不产出虚构回答
- 4 个 AI 提供商，可直连或经 Vercel/Cloudflare AI Gateway 调用
- Explore 对已存转录回答问题并附定位引文；导出 JSONL/CSV/Markdown
- 支持英/简中/法/日/韩/西 6 种访谈语言与设备端语音输入

## 适用场景

- 我需要让 AI 替我主持一批定性访谈并汇总分析
- 我在 Cloudflare 或 Vercel 上自托管访谈研究实例
- 先体验参与者到研究者的完整流程再做决策

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: OpenInterviewer is an open-source platform for adaptive, AI-assisted qualitative interviews. Researchers configure a
> L14: - 4 AI providers (Google Gemini, Anthropic Claude, OpenAI and OpenRouter), called directly or through Vercel AI Gat

## 星数曲线

```mermaid
xychart-beta
    title "linxule/openinterviewer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-26 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3c752a9aa946` · [字段定义](../../DATASET.md)*
