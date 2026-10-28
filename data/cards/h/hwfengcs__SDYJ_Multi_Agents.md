# hwfengcs/SDYJ_Multi_Agents

⭐ 50 · Python · MIT · 推送 2026-07-25 · [GitHub](https://github.com/hwfengcs/SDYJ_Multi_Agents) · 个人维护 · 中文 README

**LangGraph 多智能体深度研究框架：计划-审核-检索-出报告**

基于 LangGraph 的多智能体研究框架，由 Coordinator、Planner、Researcher、Rapporteur 分工，将开放式研究任务拆成意图识别、计划生成、人工审核、多源检索、综合报告的工作流。支持 DeepSeek、OpenAI、Claude、Gemini 统一 LLM 抽象层，集成 Tavily、arXiv 检索；证据以 E# 编号进入 prompt 并做引用校验，剔除编造引用。提供 Trace v2 时间线、deterministic replay、SQLite checkpoint 断点续跑，以及可作为 CI gate 的离线/在线 benchmark。通过 git clone + pip 安装，含 CLI 与交互式菜单，输出 Markdown/HTML/JSON 报告。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Human-in-the-loop：研究计划先经用户批准或反馈修改
- 证据项 E# 规范化、引用校验与编造引用剔除
- Trace v2 可观测性 + deterministic replay + checkpoint 断点续跑
- 离线 benchmark 含 LLM 故障注入场景，可作 CI gate

## 适用场景

- 我要让多智能体自动完成开放式主题的深度研究并生成带引用的报告
- 我需要在研究中途审核并修改研究计划
- 我要在 CI 中用 benchmark 和阈值 gate 回归测试 agent 表现

## 场景标签

`多智能体` `Agent 框架` `RAG` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L9: SDYJ Multi Agents 是一个基于 LangGraph 的多智能体研究框架。它把开放式研究任务拆成“意图识别 -> 计划生成 -> 人工审核 -> 多源检索 -> 综合报告”的可控工作流，并重点提供 Trace v2、d
> L17: - **证据驱动报告**：检索结果规范化为 `E1/E2/...` 证据项；进入 prompt 的证据按相关性预算裁剪；LLM 被要求主动引用 `[E#]`，启发式补引仅作兜底；交付前校验并剔除编造引用。
> L87: sdyj research "对比 LangGraph、AutoGen 和 CrewAI 的设计取舍"

## 星数曲线

```mermaid
xychart-beta
    title "hwfengcs/SDYJ_Multi_Agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-28 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `65e9fbcb3130` · [字段定义](../../DATASET.md)*
