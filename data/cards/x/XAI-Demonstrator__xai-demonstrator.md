# XAI-Demonstrator/xai-demonstrator

⭐ 20 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/XAI-Demonstrator/xai-demonstrator) · [官网](https://www.erklaerbare-ki.de/xai-demonstrator/) · 组织维护

**模块化可解释 AI（XAI）演示平台，供用户交互体验 XAI 系统**

模块化平台，以用例形式提供可交互的生产级可解释 AI 系统：多语言 BERT 评论情感分析（梯度特征重要度解释）、图像分类的模型无关局部解释（视觉质检）等。前后端分离，后端基于 FastAPI、前端使用 VueJS，各用例可独立 docker-compose 启动，也可整体部署。附带实验追踪组件（experiment-proxy），可记录用户请求与响应，供学术研究或用户测试分析；提供在线公开部署实例与文档站。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 按用例组织的 XAI 交互演示（情感分析、图像分类解释等）
- 整体与单用例均可 docker-compose 启动，仅需 Docker
- experiment-proxy 记录请求响应用于学术研究与用户测试
- FastAPI 后端 + VueJS 前端 + 公开在线部署

## 适用场景

- 交互体验情感分析、图像分类等 XAI 用例
- 学术研究或用户测试中记录用户与 XAI 系统的交互
- 作为模块化模板搭建自己的 XAI 演示用例

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L6: The XAI Demonstrator is a modular platform that lets users interact with production-grade Explainable AI (XAI) syste
> L36: |review-sentiment|Explain the sentiment analysis of customer reviews by a multi-lingual BERT model using gradient-b
> L45: It is possible to record user requests and additional data when the _XAI Demonstrator_ is used in academic research

## 星数曲线

```mermaid
xychart-beta
    title "XAI-Demonstrator/xai-demonstrator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `15f08664f5cd` · [字段定义](../../DATASET.md)*
