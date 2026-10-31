# alwayswdc/sci-papers-downloder

⭐ 31 · Python · MIT · 推送 2026-02-09 · [GitHub](https://github.com/alwayswdc/sci-papers-downloder) · 个人维护 · 中文 README

**为 AI agent 提供的学术论文检索下载技能：Scopus 搜索+Unpaywall 优先下载**

面向对话式 AI 与自动化 agent 工作流的论文下载技能：通过 Elsevier/Scopus API 检索并获取结构化元数据（DOI/标题/年份/来源/被引数），按 DOI 下载全文，优先走 Unpaywall 开放获取通道，可选启用 Sci-Hub CLI 作为回退。脚本将自然语言意图（few/batch/max/latest）映射为具体 CLI 行为，支持 JSON 输出供流水线解析。需配置 Elsevier API key 与 Unpaywall 邮箱；以 git clone 安装到 Codex 技能目录使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Scopus 关键词/标题/原始查询检索与结构化元数据输出
- Unpaywall 优先、可选 Sci-Hub CLI 回退的 DOI 下载策略
- 自然语言数量意图映射（few/batch/max + latest 过滤）
- JSON 输出供自动化 agent 流水线解析

## 适用场景

- 让 AI agent 按主题批量下载最新论文
- 自动化文献调研流水线中按 DOI 获取开放获取全文
- 构建需要论文元数据（DOI/被引数）的研究工作流

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L11: > Designed for conversational AI use ("download a batch", "download latest papers") and automated agent workflows.
> L112: ## 🔌 Use as a Codex Skill
> L117: git clone https://github.com/wdc63/sci-papers-downloder.git ~/.codex/skills/sci-papers-downloder

## 星数曲线

```mermaid
xychart-beta
    title "alwayswdc/sci-papers-downloder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c4ad80a7b2a0` · [字段定义](../../DATASET.md)*
