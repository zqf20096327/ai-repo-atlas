# aimclub/Edulytica

⭐ 52 · Jupyter Notebook · BSD-3-Clause · 推送 2026-07-06 · [GitHub](https://github.com/aimclub/Edulytica) · [官网](https://aimclub.github.io/Edulytica/) · 组织维护 · 中文 README

**基于 LLM 的教育与科研文本分析框架，辅助评审论文**

ITMO 大学 aimclub 团队维护的开源框架，基于 LLM 对毕业论文和青年学者文章的文本成果进行评估，开箱即用提供集成 Web 应用。功能包括从引言中提取目标与任务、生成初步评审意见、大文本摘要及目标达成度评估；内置针对摘要与目标评估的专门训练模型与配套数据集。系统采用 RAG 技术，提交文档时须选择会议/事件类型（5 种，涉及俄语/英语、不同级别刊物），该选择影响生成质量。部署方式为 Docker Compose 或源码方式（venv + pip + Celery + npm）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从毕业论文引言提取目标与任务
- 为科学文章生成初步评审意见
- 大文本摘要与目标达成度评估的专训模型及数据集
- RAG 场景下按 5 种会议/事件类型适配生成

## 适用场景

- 评审专家辅助审查毕业论文与青年学者文章
- 生成文章的初步评审意见以缩短深入分析时间
- 对长文进行摘要并评估目标达成情况

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L20: Edulytica is an open-source framework for evaluating text results of educational and scientific activities based on
> L28: - As part of the work with scientific articles, the functionality of forming a primary review has been implemented;

## 星数曲线

```mermaid
xychart-beta
    title "aimclub/Edulytica 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-26 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `1d8a5975d869` · [字段定义](../../DATASET.md)*
