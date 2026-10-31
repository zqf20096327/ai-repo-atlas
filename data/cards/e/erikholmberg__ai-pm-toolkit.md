# erikholmberg/ai-pm-toolkit

⭐ 34 · Python · MIT · 推送 2026-10-01 · [GitHub](https://github.com/erikholmberg/ai-pm-toolkit) · 个人维护

**面向 AI 产品经理的提示词、模板、脚本与框架工具集**

个人维护的 AI 产品经理工具箱：收录 PM 核心任务与 AI/ML 工作的提示词库、PRD/OKR/RICE 等模板、118 个按类组织的 Python 脚本（实验、成本/ROI、交付、评测、AI 安全等），以及 Jira/LiteLLM/OpenRouter 数据连接器、多个 MCP 服务器（Jira、Confluence、GitHub、Slack 等）与治理/学习资料。脚本内置样本数据与冒烟测试，114 个中 113 个无需 pip install 即可运行；作者声明为个人工具箱，不主动接受外部贡献。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 118 个分类 Python 脚本，配样本数据与全量冒烟测试
- connectors 将 Jira 与 LiteLLM/OpenRouter 数据拉取为脚本可读的 CSV 契约
- 面向 Jira、Confluence、GitHub、Slack、Notion、LangSmith 等的 MCP 服务器集合
- 模型定价表带 last_verified 日期，未验证条目显式标注

## 适用场景

- 生成 PRD、OKR、事后复盘等产品文档
- 运行 A/B 实验、成本/ROI 与交付周期等分析脚本
- 为 AI 产品搭建评测与 ship/no-ship 决策流程

## 场景标签

`提示工程` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L3: A comprehensive collection of prompts, templates, tools, and frameworks for Product Managers working with AI/ML prod
> L18: |**prompts/**|AI-assisted prompts for core PM tasks, AI/ML work, and developer communities|
> L20: |**scripts/**|118 Python utilities by category: experiments, cost/ROI, delivery & velocity, adoption & health, inci

## 星数曲线

```mermaid
xychart-beta
    title "erikholmberg/ai-pm-toolkit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 33 --> 36
    line [35, 34, 34]
```

2026-10-18 35 → 2026-10-31 34（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `deb1c65b20e0` · [字段定义](../../DATASET.md)*
