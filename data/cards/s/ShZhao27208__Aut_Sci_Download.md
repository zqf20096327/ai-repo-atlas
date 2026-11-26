# ShZhao27208/Aut_Sci_Download

⭐ 10 · Python · MIT · 推送 2026-06-29 · [GitHub](https://github.com/ShZhao27208/Aut_Sci_Download) · 个人维护 · 中文 README

**给 AI agent 与科研用户按 DOI/关键词下载论文 PDF 的 CLI 工具**

由 Python CLI 脚本组成的学术论文 PDF 下载工具：接受 DOI、arXiv ID、PMCID、PMID 或搜索关键词，按标识符前缀路由到 8 个数据源（Elsevier、Springer、IEEE、arXiv、Unpaywall、Semantic Scholar、PubMed、CNKI）并下载 PDF。部分数据源需免费 API Key，CNKI 需高校账号（FSSO/WebVPN cookie 导出）。可独立运行，也可作为 Claude Code skill 定义（.claude/skills/sci-download.md）被 agent 自动触发调用。MIT 许可，通过 git clone + pip 安装依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 DOI 前缀等输入自动路由到 8 个学术数据源
- Claude Code skill 定义，agent 场景下自动触发
- 支持关键词搜索并限制返回条数
- 配置集中存储于 ~/.aut-sci-download/（.env 与 config.json）

## 适用场景

- 给 Claude Code 等 agent 接入论文下载能力
- 通过 DOI 快速获取开放获取版本的论文 PDF
- 用高校账号从知网下载中文期刊与学位论文

## 场景标签

`科研工具` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L7: Download academic papers from 8 sources via simple Python CLI scripts. Works standalone or as a Claude Code skill.
> L143: ## Claude Code Integration

## 星数曲线

```mermaid
xychart-beta
    title "ShZhao27208/Aut_Sci_Download 星数(近 2 点)"
    x-axis ["2026-11-01", "2026-11-26"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-01 10 → 2026-11-26 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `96d247cc5b94` · [字段定义](../../DATASET.md)*
