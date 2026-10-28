# neflibata-feng/MyArxiv-Agent

⭐ 125 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/neflibata-feng/MyArxiv-Agent) · [官网](https://myarxiv.2006.site) · 个人维护 · 中文 README

**个人 arXiv 论文自动化知识空间模板：抓取、筛选、归档与笔记**

由个人维护的 arXiv 论文知识空间：通过 GitHub Actions 每日定时抓取指定领域（默认 AI Agent）的 arXiv 论文元数据写入 SQLite，经 Inbox.md 人工筛选后自动归档至 Papers/ 并生成 Notes/ 笔记模板与目录索引；配置集中在 config.yaml，支持环境变量覆盖。可作为 fork 模板建立独立仓库，并提供 GitHub Pages 网页版（依赖 PAT 鉴权）。agent/ 目录沉淀文献综述、文档转换、引用管理等 skill 模块，标注为开发中且未与主流程强绑定。仓库声明一般不接受贡献。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 每日定时抓取 arXiv 论文元数据并按 ID 去重写入 SQLite
- Inbox.md 筛选后自动归档至 Papers/ 并生成笔记模板与目录索引
- config.yaml 集中配置，支持 ARXIV_AGENT__ 前缀环境变量覆盖
- agent/ 目录含文献综述、MarkItDown 转换、OpenAlex 检索、引用管理等 skills（开发中）

## 适用场景

- 我每天想自动追踪某个领域的最新 arXiv 论文并筛选阅读
- fork 一个模板搭建自己的论文归档与研究笔记仓库
- 通过网页版在浏览器中筛选与管理论文 Inbox

## 场景标签

`科研工具` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L11: - 这是一个由 **neflibata-feng** 个人维护和自用的 arXiv 论文知识空间，用于自动整理 AI Agent 相关论文、筛选阅读内容并持续撰写研究笔记。
> L62: 1. **每日抓取**：每日固定时间（默认为北京时间9：25）自动抓取特定领域（默认为AI Agent）的最新论文并写入 SQLite。默认最大抓取量为每日最新的150篇论文，且按 arXiv ID 去重。

## 星数曲线

```mermaid
xychart-beta
    title "neflibata-feng/MyArxiv-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 124 --> 126
    line [125, 125]
```

2026-10-18 125 → 2026-10-28 125（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `8eea2fa553eb` · [字段定义](../../DATASET.md)*
