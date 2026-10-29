# erfnzdeh/Divar-AI-Contest

⭐ 146 · Python · 推送 2026-08-08 · [GitHub](https://github.com/erfnzdeh/Divar-AI-Contest) · [官网](https://quera.org/events/divar-0404) · 个人维护 · 中文 README

**Divar AI 竞赛冠军 LLM Agent 解题方案合集（CTF 形式）**

收录 Divar 在 Quera 平台举办的 AI 竞赛前两名（第 1、2 名）及仓库主人参赛过程的完整解题代码：11 道题中 7 道含整理后的解法，基于 GPT-4.1-mini（经 Metis AI 的 OpenAI 兼容网关）与 LangGraph ReAct agent 构建，覆盖视觉 OCR、工具路由、多模态、代码修复等场景。仓库保留比赛期间的分支提交历史与 war_room 工作区快照，运行需自备 Metis API key。第 1 名方案位于 first_place/，第 2 名位于 P* 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 道题中 7 道含解法，含 grand finale「Divar Agent」
- 基于 GPT-4.1-mini + Metis AI OpenAI 兼容网关，第 1 名用 LangGraph ReAct agent
- 保留比赛 8 小时内的实时提交历史与 war_room 快照
- 提供按题运行的说明：pip 安装依赖 + Metis API key 即可调用 DivarContest 类

## 适用场景

- 学习 LLM agent 解 CTF 式任务的实现方法
- 研究工具路由、多模态处理、编码 agent 等具体题解
- 了解竞赛形式的 agent 评测设计与参赛过程记录

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: **CTF for AI agents — the 🥇 1st & 🥈 2nd place solutions, plus a live war-room history**
> L22: The twist: you don't submit *answers* — you submit an **agent**. Each problem requires a `solution.py` exposing a `
> L108: - **Ali Salesi** — finished 🥇 **1st overall** — his submissions live in `first_place/`, built on LangGraph ReAct a

## 星数曲线

```mermaid
xychart-beta
    title "erfnzdeh/Divar-AI-Contest 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 142 --> 147
    line [143, 146, 146]
```

2026-10-18 143 → 2026-10-29 146（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `72554df0f9d1` · [字段定义](../../DATASET.md)*
