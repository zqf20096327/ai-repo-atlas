# ammawla/encode-toolkit

⭐ 22 · Python · AGPL-3.0 · 推送 2026-09-27 · [GitHub](https://github.com/ammawla/encode-toolkit) · [官网](https://pypi.org/project/encode-toolkit/) · 个人维护

**面向 Claude 的 ENCODE 基因组数据 MCP 服务器与插件**

为 Claude Code 及其他 MCP 客户端提供 ENCODE 项目数据接入：20 个 MCP 工具覆盖 ChIP-seq、ATAC-seq、RNA-seq、WGBS、Hi-C、CUT&RUN 等实验的搜索、文件下载（含 MD5 校验）、批量下载与本地追踪；另含 47 个技能与 7 条 Nextflow 流水线，可交叉检索 GTEx、ClinVar、GWAS Catalog、JASPAR 等 14 个数据库，并生成带溯源的论文方法段落。支持 Claude Code 插件市场、uvx、npx、pip 等多种安装方式，需 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20 个 MCP 工具覆盖 ENCODE 检索、下载、追踪与溯源
- 交叉接入 GTEx/ClinVar/GWAS/JASPAR 等 14 个数据库
- 47 个工作流技能与 7 条 Nextflow 分析流水线
- 生成含引文的论文方法段落与文件溯源链记录

## 适用场景

- 用自然语言在 Claude 中搜索和批量下载 ENCODE 数据
- 交叉查询多个基因组数据库验证变异与表达数据
- 记录衍生文件来源并生成可引用的方法学段落

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L28: Search ENCODE, cross-reference 14 databases, run 7 analysis pipelines, and generate publication-ready methods — all
> L149: |**ENCODE**|20 MCP tools (live API)|ChIP-seq, ATAC-seq, RNA-seq, Hi-C, WGBS, CUT&RUN data|
> L66: claude mcp add encode -- uvx encode-toolkit

## 星数曲线

```mermaid
xychart-beta
    title "ammawla/encode-toolkit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-28 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `da65b71602c3` · [字段定义](../../DATASET.md)*
