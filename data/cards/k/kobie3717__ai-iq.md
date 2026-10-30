# kobie3717/ai-iq

⭐ 18 · Python · MIT · 推送 2026-07-09 · [GitHub](https://github.com/kobie3717/ai-iq) · 个人维护

**自托管的 AI Agent 长期记忆库（SQLite，单文件）**

Python 库，为 AI agent 与编码助手提供长期记忆：基于单个 SQLite 文件存储，支持 FTS5 关键词+语义向量+图遍历的混合检索、知识图谱（实体/关系/扩散激活）、冲突检测、FSRS-6 记忆衰减、Reflexion 反思加载与 Dream 去重整合等。零服务器、离线可用、无 API key，声明兼容 Claude/GPT-4/Gemini 等任意 LLM；提供 pip 安装、CLI（memory-tool）与 Claude Code 插件。属于 Claw Stack（记忆+凭证层），可独立运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 SQLite 文件存储，FTS5+语义+图遍历混合检索
- 冲突检测、FSRS-6 记忆衰减与 Dream 去重整合
- Passport 系统：记忆的完整档案（图连接/溯源/访问/置信评分）
- 提供 memory-tool CLI 与 Claude Code 插件自动捕获

## 适用场景

- 为我的 AI 编码助手或 Python agent 加持久长期记忆
- 离线、无云端环境下自托管管理 agent 记忆
- 跨项目复用 agent 学到的经验与反思

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L6: > Python library for AI agent long-term memory. SQLite-based. Works with Claude, GPT-4, Gemini, or any LLM. Mem0 alt
> L60: - **Single SQLite file = your AI's brain** — No servers, no vector DB, no setup

## 星数曲线

```mermaid
xychart-beta
    title "kobie3717/ai-iq 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `58d8e638ed6d` · [字段定义](../../DATASET.md)*
