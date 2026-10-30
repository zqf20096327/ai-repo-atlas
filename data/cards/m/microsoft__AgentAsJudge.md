# microsoft/AgentAsJudge

⭐ 23 · Python · MIT · 推送 2026-02-11 · [GitHub](https://github.com/microsoft/AgentAsJudge) · 组织维护

**微软的多智能体文本质量评测框架，输出评分与反馈**

由微软维护的评测框架：用多智能体推理流水线（讨论、批评、排序 agent）对 .jsonl 文本样本进行质量评估，每个样本输出 1-10 分与详细反馈。推理依赖 Azure OpenAI 服务，需配置 AZURE_DEPLOYMENT、AZURE_ENDPOINT 等环境变量；系统提示词可通过 metrics 目录下的 markdown 文件自定义。以 Python 脚本形式运行（python main.py 输入文件），README 描述与摘要存在 1-5 与 1-10 两种分制表述。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 讨论/批评/排序三类 agent 组成的多智能体评测流水线
- 每个样本输出数值评分与详细反馈
- 系统提示词可通过 markdown 文件自定义
- 校验 .jsonl 输入并报告无效行

## 适用场景

- 批量评估文本样本质量并获得可读反馈
- 按自定义标准调整提示词以适配特定评测需求
- 作为 agent 生成内容的质量把关环节

## 场景标签

`多智能体` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L4: This project evaluates the agentic quality of text samples using a multi-agent reasoning pipeline. It leverages Azur
> L7: - **Multi-Agent Evaluation**: Includes discussion, criticism, and ranking agents to evaluate text samples.

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/AgentAsJudge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `6fbebabae1a0` · [字段定义](../../DATASET.md)*
