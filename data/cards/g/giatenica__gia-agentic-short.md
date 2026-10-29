# giatenica/gia-agentic-short

⭐ 19 · Python · Apache-2.0 · 推送 2026-06-22 · [GitHub](https://github.com/giatenica/gia-agentic-short) · [官网](https://giatenica.com) · 个人维护

**自主学术研究流水线：从项目输入到可审计的论文草稿**

端到端多 agent 学术研究原型代码库：以项目文件夹为输入，经 intake、文献检索与综合、缺口解决、证据抽取、计算分析与论文写作等阶段，产出 Markdown/JSON 可检视工件与 LaTeX 论文。设置证据、引用、分析等门控，缺失前置条件时阻断或降级，核心原则为"无出处不陈述"。使用 Claude 系列模型（Opus/Sonnet/Haiku 按任务分工），需 ANTHROPIC_API_KEY。自我声明为开发中的原型，预期会变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- A01-A25 共 25 个专职 agent 组成的分阶段流水线
- 证据/引用/分析门控：不满足前置条件即阻断或降级输出
- LLM 生成代码在隔离子进程（-I 模式与最小环境白名单）中执行
- 本地 intake 服务器对上传 ZIP 做路径穿越防护与数量/大小上限

## 适用场景

- 让 AI 流水线自动完成文献综述到论文初稿的研究流程
- 需要每条声明可溯源到证据条目的可审计研究产出
- 对研究管线各阶段工件做确定性回归检查

## 场景标签

`多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L10: This repository is building an end-to-end, agent-driven system that goes from project intake to an auditable resear
> L124: - **Agents**: Deterministic wrappers around LLM calls and local tools; each agent returns `AgentResult` with struc
> L177: |Complex Reasoning|`claude-opus-4-5-20251101`|Research, scientific analysis, academic writing|

## 星数曲线

```mermaid
xychart-beta
    title "giatenica/gia-agentic-short 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0c62312b2fa5` · [字段定义](../../DATASET.md)*
