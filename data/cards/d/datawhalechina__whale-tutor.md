# datawhalechina/whale-tutor

⭐ 21 · TypeScript · AGPL-3.0 · 推送 2026-05-20 · [GitHub](https://github.com/datawhalechina/whale-tutor) · 组织维护 · 中文 README

**AI 驱动的交互式课程学习引擎：markdown 讲稿一键生成可学课程**

面向课程作者、学习者与开发者的开源教学引擎。课程作者写 YAML 学习路径与 markdown 讲稿，CLI 通过 AI 拆分学习目标（LO）、出题并生成完整可交互课程；学习者按 mastery 状态机（untouched→exposed→practicing→mastered）系统推进，答错触发 AI 换说法题，连续错 3 次回讲解兜底，配梯度提示与侧支 QA。提供 4 种交互模式（含浏览器内 Pyodide 跑 Python），事件流全打点。架构为 Vue 3 + NestJS + MySQL + DeepSeek（AI Gateway 可换 OpenAI 兼容服务），通过 npm 安装 CLI 使用，需 Node.js ≥ 22 与 MySQL ≥ 8.0，DeepSeek API Key 可选（缺失时 build 不可用）。AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- markdown 讲稿 → AI 4 阶段生成完整 yaml/md 课程（whale-tutor build / generate）
- LO 级 mastery 状态机 + 答错 AI 换说法题 + 连错兜底回讲解
- 4 种交互模式：概念辨析 / 浏览器 Pyodide 代码沙盒 / 找 bug / 开放回忆（AI rubric 评估）
- 梯度提示 StuckProtocol 与侧支 QA 多轮追问，学习者行为全事件流打点

## 适用场景

- 老师/教研把 markdown 讲稿转成带出题与 mastery 跟踪的交互课程
- 学习者跟着预设学习路径系统学习，卡住时求提示或换说法题
- 开发者扩展新交互 pattern 或基于事件流做学习分析

## 场景标签

 · 领域:教育/课程创作与学习平台

## 证据(README 行号)

> L38: - 🎯 **每个学习目标(LO, Learning Objective)有 mastery 状态机**(untouched → exposed → practicing → mastered)
> L138: - **`whale-tutor build`** — 写 markdown 讲稿(每章一份 md)→ AI 4 阶段生成完整 yaml/md 课程骨架

## 星数曲线

```mermaid
xychart-beta
    title "datawhalechina/whale-tutor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a614ef7a9081` · [字段定义](../../DATASET.md)*
