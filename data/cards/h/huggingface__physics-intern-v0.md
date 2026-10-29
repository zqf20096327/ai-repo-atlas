# huggingface/physics-intern-v0

⭐ 50 · Python · 推送 2026-10-14 · [GitHub](https://github.com/huggingface/physics-intern-v0) · [官网](https://huggingface.co/spaces/huggingface/physics-intern) · 组织维护

**多智能体框架：自主求解数学与理论物理研究问题**

面向数学与理论物理科研的多智能体系统：以自然语言陈述问题，系统自动分解为子问题、执行推导、编写并运行验证代码、自我批判审查，直至产出经验证的完整解答（ANSWER.md）。默认多智能体管线编排九个专职角色（surveyor/planner/orchestrator/researcher/computer/reviewer/deep critic/adjudicator/formatter），另有单代理 Autophysicist 模式。所有状态存于结构化 ResearchState 并用 git 版本控制。支持 Anthropic/OpenAI/Google Gemini/HuggingFace 多提供商。需 Python 3.12+ 与 uv 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 九角色多智能体研究管线与 Autophysicist 单代理两种模式
- 研究状态存于 ResearchState 并以 git 快照记录，每步可恢复
- 通过 models.yaml 注册表接入 Anthropic/OpenAI/Gemini/HuggingFace 多提供商
- 支持 vLLM 服务本地模型（见 DOCUMENTATION.md）

## 适用场景

- 让 AI 自主推导理论物理问题（如从欧氏路径积分推导霍金温度）
- 自动化数学/物理研究问题分解、推导与验证流程
- 科研中批量运行问题 YAML 的自动化求解

## 场景标签

`多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L3: A multi-agent scaffolding system for autonomous scientific research in mathematics and theoretical physics.
> L7: PhysicsIntern takes a problem stated in plain language (e.g. "derive the Hawking temperature from the Euclidean path
> L9: The project ships two research modes: a **multi-agent pipeline** (the default) that orchestrates nine specialised ro

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/physics-intern-v0 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-29 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `10e4a5917fce` · [字段定义](../../DATASET.md)*
