# brunoamaral/gregory-ai

⭐ 58 · Python · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/brunoamaral/gregory-ai) · [官网](https://gregory-ai.com/) · 个人维护

**用机器学习追踪临床研究并筛选相关论文的系统**

基于 Django 的临床研究追踪系统：通过 RSS 或手工配置来源（含 PubMed 与临床试验），抓取文献后用机器学习模型（pubmed_bert/lgbm_tfidf/lstm）预测相关性，经 Postmark 发送管理员摘要、每周摘要与临床试验通知；提供公共/私有 API、静态站点输出、Metabase 仪表盘容器、按主题与分类组织文献、ORCID 作者识别。模型可用管理命令基于人工标注数据重训练。以 Docker Compose 部署为主，当前使用案例为多发性硬化、阿尔茨海默与帕金森领域。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 机器学习预测论文相关性，支持 pubmed_bert/lgbm_tfidf/lstm 三种算法训练
- RSS/任意网站抓取 + 临床试验监测 + 邮件订阅管理（Postmark）
- Django Rest Framework 提供公共与私有 API，另含 Metabase 仪表盘容器
- 按 Subject/Category 组织文献并生成多种 RSS 输出

## 适用场景

- 研究团队持续追踪某疾病领域的最新文献与临床试验
- 管理员通过邮件摘要人工标注并迭代训练相关性模型
- 通过 API 或 RSS 将筛选后的文献整合到其他系统

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L7: Gregory is an AI system that uses Machine Learning and Natural Language Processing to track
> L20: 1. Machine Learning to identify relevant research
> L303: |`--algo ALGORITHMS`|Comma-separated list of algorithms to train (pubmed_bert,lgbm_tfidf,lstm)|

## 星数曲线

```mermaid
xychart-beta
    title "brunoamaral/gregory-ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 56 --> 59
    line [57, 58, 58]
```

2026-10-18 57 → 2026-10-31 58（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `773fd7719fd8` · [字段定义](../../DATASET.md)*
