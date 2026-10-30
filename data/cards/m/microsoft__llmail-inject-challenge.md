# microsoft/llmail-inject-challenge

⭐ 28 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/microsoft/llmail-inject-challenge) · [官网](https://arxiv.org/abs/2506.09956) · 组织维护

**LLMail-Inject 提示注入攻防挑战赛的实现代码与数据分析**

微软与 ISTA、ETH Zurich 联合举办的 LLMail-Inject 自适应提示注入挑战赛的代码库，含比赛平台实现、参赛提交数据集的分析，以及 RAG 系统与防御实现在 src/agent/workloads 下。比赛模拟一个带 LLM 助手的邮件客户端：参赛者扮演攻击者发送邮件，目标是绕过 Spotlighting、PromptShield、LLM-as-a-judge、TaskTracker 等防御诱导 LLM 执行未授权操作或数据外泄，共 4 个场景、40 个关卡，使用 Phi-3-medium 与 GPT-4o mini。比赛已结束，仓库保留代码与数据集分析。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模拟 LLM 邮件助手场景下的自适应提示注入攻防挑战（4 场景、40 关卡）
- 包含 5 类提示注入防御实现（Spotlighting/PromptShield/LLM-as-a-judge/TaskTracker/组合）
- 开源了挑战赛提交数据集并提供数据分析
- 使用 Phi-3-medium-128k-instruct 与 GPT-4o mini，固定 top-p=0.92 与种子保证可复现

## 适用场景

- 研究提示注入攻击与防御在 RAG 场景下的表现
- 分析挑战赛提交数据集以评估防御有效性
- 复用平台代码构建类似的 LLM 安全评测环境

## 场景标签

`网络安全` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: This repo contains the implementation and codebase of the previously hosted competition LLMail-Inject. This is assoc
> L29: - This repo contains data analysis of the challenge submissions and dataset.
> L31: - This repo contains the platform implementation and may help clarify some design specifics of the LLMs, attacks, a

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/llmail-inject-challenge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 29
    line [27, 28]
```

2026-10-18 27 → 2026-10-30 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `82dbdca22a3d` · [字段定义](../../DATASET.md)*
