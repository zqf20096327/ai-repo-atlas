# OvOhao/auto-paper-collecter

⭐ 64 · Python · MIT · 推送 2026-06-28 · [GitHub](https://github.com/OvOhao/auto-paper-collecter) · 个人维护 · 中文 README

**自托管的 LLM 文献聚合工具：按关键词每日自动追踪新论文**

基于 Python/FastAPI/SQLite 的自托管学术文献聚合服务：用户订阅英文关键词后，系统跨 arXiv、Crossref、Semantic Scholar、GitHub、HuggingFace、Papers with Code 与 RSS 多源检索，用 LLM 做关键词联想扩展与相关性过滤，为每篇生成中文摘要，并产出领域热点与每周报告，支持收藏/笔记/BibTeX 及邮件、微信、Telegram、Slack 推送。提供零构建单页仪表盘；LLM 通过任意 OpenAI 兼容网关配置，可禁用退回原始摘要。另内置 Claude Code/Codex 可用的 Agent Skill 版（纯标准库零依赖）。目前单用户无鉴权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- arXiv/Crossref/Semantic Scholar/GitHub/HuggingFace/RSS 等多源聚合检索
- LLM 关键词联想扩展与计算机领域相关性过滤
- 生成中文摘要、领域热点分析与每周报告
- 内置 Claude Code / Codex 通用的 Agent Skill（零依赖、免 API key）

## 适用场景

- 每天自动追踪自己研究方向的新论文并生成中文摘要
- 定期了解领域热点与子方向论文增量
- 配合企业微信/Telegram/邮件接收当日文献推送

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L50: > 🧠 用 **LLM 做"联想式"扩展检索**，不再只匹配字面关键词
> L52: > ✍️ 为每篇生成**中文摘要**(一句话 TL;DR / 方法 / 核心贡献)

## 星数曲线

```mermaid
xychart-beta
    title "OvOhao/auto-paper-collecter 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 62 --> 65
    line [63, 64, 64]
```

2026-10-18 63 → 2026-10-31 64（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `348deb7967d2` · [字段定义](../../DATASET.md)*
