# OnlyTerp/nemotron-opus-elicitation

⭐ 10 · Python · 推送 2026-06-11 · [GitHub](https://github.com/OnlyTerp/nemotron-opus-elicitation) · 个人维护

**面向 prompt 工程者的 Nemotron 3 Ultra 提示词实验记录与模板集**

对 NVIDIA Nemotron 3 Ultra 进行的 29 项受控提示词实验合集：不微调模型，仅通过系统提示词与任务内注入改变其语气与代码审查行为，并以盲评双评委（MiMo + MiniMax）打分。仓库提供 v16–v23 提示词模板阶梯、可挂接到 Devin CLI / Claude Code 的 hook 脚本、逐实验记录与冻结测试集，MIT 许可。使用者复制模板到自己的 agent 系统提示即可，README 同时列出方法不适用的情形（如推理上限、无该缺陷的模型）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 29 项受控实验，盲评双评委打分且评分标准预注册
- v16–v23 提示词模板阶梯，每条附实验验证状态
- 提供可运行的 code-trace-check.py hook 脚本
- 包含测试集、评分脚本与逐实验证据链

## 适用场景

- 为基于 Nemotron 的 agent 挑选经过验证的系统提示模板
- 复现或审查提示词对模型行为影响的实验设计
- 给自己 agent 的代码审查流程加入强制 MATCH/MISMATCH 校验环节

## 场景标签

`提示工程` `模型评测` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L11: **We spent 29 controlled experiments making NVIDIA's Nemotron 3 Ultra warmer, more honest, and harder to fool — wit
> L94: ## Repo map

## 星数曲线

```mermaid
xychart-beta
    title "OnlyTerp/nemotron-opus-elicitation 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-23"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-20 10 → 2026-11-23 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `96369090298b` · [字段定义](../../DATASET.md)*
