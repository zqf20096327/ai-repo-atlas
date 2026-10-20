# HKUDS/DeepTutor

⭐ 41,612 · Python · Apache-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/HKUDS/DeepTutor) · [官网](http://arxiv.org/abs/2604.26962) · 组织维护 · 中文 README

**面向学习者的多智能体个性化辅导系统**

由 HKUDS 维护的开源 AI 辅导系统，围绕知识库（RAG）、多智能体循环与三层记忆构建，提供 Chat、Guided Learning、Deep Research、Book 生成、Visualize、练习题等功能面；支持接入自建 Partners（可连接本地 Claude Code / Codex）、通过 15 个 IM 渠道通信、以 Docker Compose 或源码部署，并区分单用户与多用户（含管理员账户）部署形态。提供 CLI（deeptutor start / skill install）与在线文档站点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 86,200 位贡献者
- 涨星:近 1 天 **+83**(自 20261016 起算)
- 安装:npm 包 `to` 月下载 25,674
- 平台:— · 协议:OPENAI-API / MCP / OLLAMA

## 能力要点

- 知识中心支持 GraphRAG / LightRAG / PageIndex / 关联知识库 / Obsidian
- 三层记忆（L1/L2/L3）与单智能体循环驱动的学习功能面
- 可通过 15 个 IM 渠道接入 Partners 机器人
- 提供 CLI：deeptutor start、deeptutor skill install、deeptutor doctor

## 适用场景

- 搭建带个人知识库的 AI 辅导环境进行日常学习
- 把辅导机器人接入微信等 IM 渠道随时提问
- 对上传文档做问答、出题与深度研究报告

## 场景标签

`多智能体` `RAG` `文档问答` · 领域:Agent 开发

## 证据(README 行号)

> L3: # DeepTutor: Lifelong Personalized Tutoring
> L137: > **[2026.5.22]** v1.4.0 — GA cut of v1.4: Auto Mode, three-layer Memory, agentic Deep Research / Solve / Question
> L23: Python 3.11+

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 low · 依据 README sha `708ea46f9d4b` · [字段定义](../../DATASET.md)*
