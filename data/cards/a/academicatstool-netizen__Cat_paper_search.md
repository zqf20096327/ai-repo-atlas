# academicatstool-netizen/Cat_paper_search

⭐ 15 · Python · MIT · 推送 2026-06-17 · [GitHub](https://github.com/academicatstool-netizen/Cat_paper_search) · [官网](https://academicats.com) · 组织维护 · 中文 README

**给研究者的 agent 技能：跨 5 大学术库检索真实论文并精读 PDF**

可运行在 Claude Code、Claude 网页/桌面及 Codex 等 agent 上的学术检索技能：一次提问并行查询 OpenAlex、Crossref、arXiv、Semantic Scholar、Europe PMC 五个学术数据库，去重后按研究相关度排序，结果均为可验证的真实记录；对开放获取论文解析 PDF、抽取文本并生成带页码引用的结构化精读。付费墙论文会如实标注，不虚构内容。提供 git clone、.skill 上传与 PORTABLE_PROMPT.md 三种接入方式，为 AcademiCats 付费产品的开源精简版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一次查询并行检索 5 个学术数据库（免 key），去重并按研究相关度排序
- 对开放获取 PDF 解析文本并输出带页码引用的结构化精读
- 所有结果来自公开 API 真实记录，付费墙论文如实标注不虚构
- 支持 Claude Code / Claude 网页桌面 / Codex / 任意模型（便携提示词）多种运行路径

## 适用场景

- 让 Claude 或 Codex 帮我按主题批量查找真实可验证的论文
- 对某篇开放获取论文做带页码引用的深度阅读和要点提取
- 避免通用聊天模型编造不存在的论文和结论

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L7: **Find real academic papers across the world's scholarly databases — then read any open-access one in depth. Grounde
> L18: 📄 **Read, not skim** — pick any open-access paper and it resolves the PDF, extracts the text, and gives you a struc
> L55: **🖥️ Claude Code** — runs locally, triggers itself (full-power version)

## 星数曲线

```mermaid
xychart-beta
    title "academicatstool-netizen/Cat_paper_search 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `a83b29a58b89` · [字段定义](../../DATASET.md)*
