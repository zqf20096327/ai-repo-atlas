# hherb/primer

⭐ 11 · Rust · AGPL-3.0 · 推送 2026-11-25 · [GitHub](https://github.com/hherb/primer) · [官网](https://primer-ai.org/) · 个人维护

**为儿童提供的苏格拉底式 AI 学习伴侣**

面向儿童的语音优先 AI 学习伴侣，以提问引导而非直接告知的方式教学，受《钻石年代》启发。核心机制包括：意图路由（声明性主张触发推理探查）、参与度/概念/理解深度三级分类器、长期记忆（滚动摘要+FTS5 检索）、间隔重复词汇复习（Leitner 盒调度）、BM25+稠密向量混合检索（RRF 融合）。数据全部本地存储，可离线运行本地模型；文本 REPL 与桌面应用可用，Rust 编写，处于 Phase 0.3 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 苏格拉底式引导：能用提问就不直接回答，并检验理解深度
- 本地优先：支持离线/airgapped 运行，学习者模型不出设备
- 混合检索（BM25+稠密向量 RRF 融合）与三套预置儿童语料
- 间隔重复词汇复习、会话休息建议与参与度分类器

## 适用场景

- 为孩子搭建可离线使用的语音学习陪伴设备
- 以苏格拉底问答方式引导孩子自主发现答案
- 跟踪孩子的概念理解深度与词汇遗忘曲线
- 德/英多语言儿童知识库检索与问答

## 场景标签

`语音 Agent` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: A Socratic AI learning companion for children — inspired by the Young Lady's Illustrated Primer in Neal Stephenson's
> L7: The Primer doesn't teach by telling. It teaches by asking. When a child says "Why is the sky blue?", the Primer does
> L31: **Phase 0.1 done; Phase 0.2 done; Phase 0.3 done.** The trait architecture and module boundaries are in place, the 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `039ac04cf38d` · [字段定义](../../DATASET.md)*
