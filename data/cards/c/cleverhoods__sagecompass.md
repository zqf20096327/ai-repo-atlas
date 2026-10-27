# cleverhoods/sagecompass

⭐ 30 · Python · Apache-2.0 · 推送 2026-01-26 · [GitHub](https://github.com/cleverhoods/sagecompass) · 个人维护

**多 agent 决策框架：评估商业创意是否值得引入 AI**

由 Drupal、LangGraph 与 Gradio UI 三部分组成的决策评估系统，通过 Problem Framing、Goals & KPI、Feasibility、Decision Synthesis 四个阶段的多个 agent（共 8 个），对商业创意做问题定义、目标量化、可行性与成本估算，输出数值化的“是否值得做 AI”判断。当前实现仅支持 OpenAI API key，本地运行需 DDEV 启动 Drupal 容器，uv 管理 Python 环境，版本要求 Python ≥3.13、uv ≥0.9.13、ddev ≥1.24.10。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 阶段流水线：问题定义→目标与 KPI→可行性→决策综合
- 8 个分工 agent（问题定义/目标/KPI/资格/方案设计/成本/决策等）
- Drupal + LangGraph + Gradio UI 三组件架构
- 输出数值化的 AI 采纳决策依据

## 适用场景

- 企业在立项前评估某业务创意是否真的需要 AI
- 以虚拟顾问形式对 AI 创意做一致逻辑的多维度评审
- 获得含成本与 KPI 的数值化决策摘要

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L2: SageCompass is an augmented decision system that checks whether a business idea actually needs AI
> L22:  - The current implementation was created for **_OPENAI_API_KEY_** only

## 星数曲线

```mermaid
xychart-beta
    title "cleverhoods/sagecompass 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `6b804fbd1957` · [字段定义](../../DATASET.md)*
