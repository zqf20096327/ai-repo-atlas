# LeoTheAIDev/Altiverse

⭐ 25 · TypeScript · MIT · 推送 2026-06-27 · [GitHub](https://github.com/LeoTheAIDev/Altiverse) · [官网](https://github.com/LeoTheAIDev/Altiverse) · 个人维护

**把一个决策分叉成 2–4 个平行现实的多智能体模拟工具**

浏览器端本地运行的决策探索工具：将一个决策（如校园手机禁令、医院排班）分叉为 2–4 个平行现实，每个现实包含最多约 1,000 个有人格、情绪与关系的人，在房间地图上逐日演化。用户查看分歧日、分歧树、指标趋势与因果链，可点击任意人物对比其在各现实中的境遇，并导出含建议的 Markdown/PDF 报告。核心为确定性引擎（同种子同世界），LLM 层为可选，用于生成场景、角色独白与报告文字；支持任意 OpenAI 兼容端点，无后端、可完全离线运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性模拟引擎：同种子产生相同世界，LLM 层可选
- 最多约 1,000 个有人格与关系的 agent 在 2–4 个平行现实中演化
- 分歧树、指标趋势、福祉直方图与因果链可视化
- 本地优先：无后端、无遥测、完全离线可用，数据存 localStorage

## 适用场景

- 比较不同政策方案在人群中的二阶影响
- 观察同一批人在不同决策下的境遇差异
- 生成含建议与角色访谈的决策报告并导出

## 场景标签

`多智能体` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L19: It is a **thinking tool, not a predictor.** Every number and quote comes from a **deterministic** engine (same seed
> L21: > 🔒 **Local-first & private.** No backend. No telemetry. Nothing is uploaded. Runs, presets, and any API key live o
> L186: - **LLM layer** — a thin, dependency-light client (plain `fetch`) against any OpenAI-compatible `/chat/completions

## 星数曲线

```mermaid
xychart-beta
    title "LeoTheAIDev/Altiverse 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-31 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3ee5aab577ee` · [字段定义](../../DATASET.md)*
