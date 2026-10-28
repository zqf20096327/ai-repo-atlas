# vansh070605/PlacementOS

⭐ 19 · JavaScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/vansh070605/PlacementOS) · [官网](https://placementosai.vercel.app/) · 个人维护

**本地优先的 AI 求职指挥中心：多 Agent 分析代码与市场助力求职**

面向求职者的本地优先职业管理平台：React 前端加 FastAPI 后端，通过 10 个专用 Agent 组成的多 Agent RAG 架构运作——解析职位描述、在 ChromaDB 中检索项目组合、生成兼容度评分与定制简历要点、起草领英私信与求职信、模拟 ATS 评分与模拟面试，并用本地 TensorFlow/Keras 回归模型预测薪资区间。LLM 推理默认使用 Gemini（gemini-1.5-flash），API 不可用时回退到本地 Qwen2.5 与 SentenceTransformer 模型；档案经 Firebase 实时同步。需自行配置 Gemini 与 Firebase 密钥后从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 个专用 Agent：JD 解析、RAG 匹配、简历要点生成、领英/邮件起草、ATS 评分、模拟面试等
- 本地 TensorFlow/Keras 神经网络预测薪资区间（P25-P75），完全离线运行
- LocalModelRegistry 支持离线回退：Qwen2.5-1.5B、BERT NER、Cross-Encoder、随机森林
- 全局候选人档案经 Firebase 实时同步，注入 Agent 提示上下文

## 适用场景

- 跟踪求职投递漏斗并按生命周期阶段管理（Kanban 看板）
- 针对具体 JD 定制简历要点、求职信与学习计划
- 用本地模型预测薪资区间并生成谈判脚本
- 扫描自己的 GitHub 仓库生成架构概述与面试防御问题

## 场景标签

`多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L20: **PlacementOS** is a comprehensive, local-first career management platform. It transcends traditional job applicati
> L38: PlacementOS is driven by a localized FastAPI backend orchestrating **10 specialized autonomous agents**. This syste
> L55: * **Agent 7 (Salary Intelligence):** Feeds parameters into a locally trained TensorFlow/Keras neural network regres

## 星数曲线

```mermaid
xychart-beta
    title "vansh070605/PlacementOS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `ccc87ca06fe9` · [字段定义](../../DATASET.md)*
