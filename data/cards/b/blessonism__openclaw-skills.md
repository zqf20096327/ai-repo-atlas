# blessonism/openclaw-skills

⭐ 55 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/blessonism/openclaw-skills) · [官网](https://github.com/openclaw/openclaw) · 个人维护 · 中文 README

**给 OpenClaw agent 用户的技能合集：搜索、内容提取、GitHub 分析等**

一组面向 OpenClaw agent 运行时的技能集合，包含 6 个独立 skill：search-layer（Brave/Exa/Tavily/Grok 四源并行搜索，意图感知评分与链式引用追踪）、content-extract（URL 转 Markdown）、mineru-extract（MinerU API 封装，PDF/Office/HTML 转 Markdown）、github-explorer（GitHub 项目结构化研判报告）、dependency-tracker（依赖健康检查）、gitclaw-backup（同步到 GitHub）。安装方式为 git clone 或对话内让 OpenClaw 自动 clone，各 skill 按需配置 API Keys 与 Python 依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- search-layer 四源并行搜索，意图感知评分与引用图 BFS 遍历
- github-explorer 输出结构化研判报告，抓 README/Issues/社区评价/arXiv 论文
- 各 skill 独立运行、按需安装
- 支持对话内由 OpenClaw 自动 clone 并链接全部 skill

## 适用场景

- 给 OpenClaw agent 增加多源搜索与引用追踪能力
- 将 URL 或反爬站点内容提取为 Markdown
- 生成 GitHub 项目的结构化分析报告
- 备份 OpenClaw 工作区到 GitHub 仓库

## 场景标签

`语义搜索` `网页抓取` `文档解析` · 领域:效率与自动化

## 证据(README 行号)

> L3: 一组 OpenClaw Agent 技能（Skills），覆盖搜索、分析、内容提取、备份等场景。
> L125: - OpenClaw（agent 运行时）

## 星数曲线

```mermaid
xychart-beta
    title "blessonism/openclaw-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-26 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `bdd59582584e` · [字段定义](../../DATASET.md)*
