# kzw-ai/word-learning-system

⭐ 26 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/kzw-ai/word-learning-system) · 个人维护 · 中文 README

**面向中级汉语学习者的自适应词汇学习系统**

基于北京大学硕士论文构建的全栈汉语词汇学习平台：以 SM-2 改良算法做间隔重复调度，多层推荐引擎（紧急复习/计划复习/新内容）结合 AdaBoost、Gaussian NB 与 XGBoost 投票集成进行个性化推荐，提供 VKS 词汇量测量、汉字→词→搭配→句子多模块学习链、学习分析仪表盘、TTS 发音与 PWA 离线支持。语料基于 BCC 语料库频率分析与依赖句法搭配抽取。技术栈为 Next.js 14 前端与 Flask/SQLite 后端，提供在线演示、本地脚本启动与 Docker 部署三种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 改良 SM-2 间隔重复与多层推荐引擎（含置信度评分）
- VKS 词汇知识量表测定学习起点
- 汉字→词→搭配→句子递进式学习链与 TTS 发音
- PWA 离线支持与跨设备学习进度同步

## 适用场景

- 中级汉语（CFL）学习者做个性化词汇学习与复习
- 通过 VKS 测评确定词汇学习切入点
- 查看学习热力图与掌握趋势分析

## 场景标签

 · 领域:教育/语言学习

## 证据(README 行号)

> L13: An intelligent, adaptive vocabulary learning system for intermediate-level Chinese as a Foreign Language (CFL) lear
> L17: - 🧠 **Adaptive Recommendation Engine** — AI-powered personalized learning path based on user proficiency, learning 
> L68: |**ML Models**|AdaBoost (Multinomial NB), Gaussian NB, XGBoost with voting ensemble|

## 星数曲线

```mermaid
xychart-beta
    title "kzw-ai/word-learning-system 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `98a13e72db18` · [字段定义](../../DATASET.md)*
