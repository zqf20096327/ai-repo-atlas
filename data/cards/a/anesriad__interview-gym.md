# anesriad/interview-gym

⭐ 15 · Python · 推送 2026-07-16 · [GitHub](https://github.com/anesriad/interview-gym) · 个人维护

**本地离线的数据科学/ML 面试刷题应用，配本地 LLM 导师**

LeetCode 风格的本地练习应用，覆盖 SQL、Python/DSA、应用 ML、系统设计与 AI/LLM 工程五个题域，含 85+ 道已验证题目。SQL 按隐藏参考查询判分，Python 按隐藏测试用例判分；AI 导师通过 Ollama 运行本地 LLM（默认 qwen3-coder:30b），提供渐进式提示、结构化反馈、自由聊天，并可按需生成经执行验证的新题。技术栈为 FastAPI + DuckDB + SQLite 后端与 React + Monaco 前端，除初始安装外全程离线，进度存于本地 SQLite。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五个题域、85+ 道已验证题目，含 34 道 AI/LLM 工程题
- 本地 LLM 导师：渐进式苏格拉底提示与结构化反馈
- 一键生成新题，后端执行参考解验证后入库
- SQL 判错附诊断说明（分组粒度、join 扇出等）

## 适用场景

- 数据科学/ML 岗位面试日常刷题备考
- 在无订阅、无云端环境下练习并获取 AI 提示反馈
- 本地生成新题扩展题库

## 场景标签

 · 领域:教育/面试准备工具

## 证据(README 行号)

> L3: A **local, offline, LeetCode-style practice app** for data science / ML / AI engineer interviews — SQL, Python/DSA, 
> L18: - **AI mentor, 100% local** — escalating Socratic hints (never dumps the answer), structured feedback with root-cau
> L25: FastAPI + DuckDB + SQLite backend · React (Vite) + Monaco frontend · Ollama (`qwen3-coder:30b` by default) for the 

## 星数曲线

```mermaid
xychart-beta
    title "anesriad/interview-gym 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `754bd3424a84` · [字段定义](../../DATASET.md)*
