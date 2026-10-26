# Mocas-12/gh-pain-intel

⭐ 30 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/Mocas-12/gh-pain-intel) · [官网](https://gh-pain-intel-8egvafff3urokytzxa63x2.streamlit.app/) · 个人维护 · 中文 README

**用 LLM 分析 GitHub issues 痛点并生成市场调研报告的工具**

面向产品与市场研究场景的 Python 工具：通过 GitHub REST API 拉取目标仓库近期 issues，经并发批量 LLM 语义分析完成痛点分类（bug/feature/question 等）、1-5 级严重度评分、情感标注，再做两阶段主题聚类与趋势分析，最终导出三段式 Markdown 市场调研报告。支持 13 个 LLM 预设（OpenRouter/OpenAI/Gemini/Claude/DeepSeek 等）及任意 OpenAI 兼容端点，本地 Ollama 可免 key 运行。提供 Streamlit 交互面板与无头 CLI 双入口，另含 GitHub Trending 日增星榜单；只读公开数据，匿名 GitHub 配额为 60 次/小时，配置 token 可提至 5,000。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- issue 痛点分类 + 1-5 级严重度评分 + 情感标注 + 两阶段主题聚类
- 13 个 LLM 预设可一键切换，任意 OpenAI 兼容端点可接入
- 本地 Ollama 可完全免 key 运行
- Streamlit 面板 + 无头 CLI 双入口，CLI 支持定时任务

## 适用场景

- 调研竞品或自家仓库的高频用户痛点与功能请求
- 跟踪开发者在 issues 中的情感趋势与热门话题
- 结合 GitHub Trending 日增星榜发现起量仓库并纳入分析

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: **Monitor GitHub issue pain points → deep LLM semantic analysis → export market research reports in one click**
> L28: - 🔎 **Pain-Point Classification**: per-issue semantic classification (bug / feature / question / doc / other) + pai
> L47: 2. **Classify**: issue text is batched concurrently to the selected LLM, forced to return structured JSON (category

## 星数曲线

```mermaid
xychart-beta
    title "Mocas-12/gh-pain-intel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-26 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `1d06c0abc8cd` · [字段定义](../../DATASET.md)*
