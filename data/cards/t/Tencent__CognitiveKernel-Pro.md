# Tencent/CognitiveKernel-Pro

⭐ 533 · Python · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/Tencent/CognitiveKernel-Pro) · 组织维护 · 中文 README

**腾讯 AI Lab 的深度研究 Agent 框架与训练方案**

面向深度研究（Deep Research）任务的 agent 框架：主体 agent 配合 Web 浏览器引擎（Playwright 驱动）与多种文档解析工具执行任务，支持反思重试（no_answer/gpt_judge 评估）。同时提供可复现的 SFT 训练配方（含 rejection sampling 与轨迹采样）及微调检查点 Qwen3-8B-CK-Pro，另有 subgoal-GRPO 的 RL 训练配方。工具链以免费为主，Google Search API 可替换为 DuckDuckGo。需 Python 3.12 与多系统依赖，建议在沙箱中运行（生成的代码会被直接执行且无安全检查）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 深度研究 agent 框架，配套 Web 浏览器引擎与反思重试机制
- 提供可复现的 SFT 训练配方及 subgoal-GRPO RL 配方
- 开源微调检查点 Qwen3-8B-CK-Pro 与部分 SFT 数据
- 工具链以免费 API 为主，付费的 Google Search 可换 DuckDuckGo

## 适用场景

- 搭建并运行深度研究 agent 完成多跳问答与网页任务
- 基于开源 SFT 配方训练自己的 agent 基础模型
- 在 GAIA 数据集上复现实验结果

## 场景标签

`Agent 框架` `微调` `强化学习` · 领域:Agent 开发

## 证据(README 行号)

> L1: # Cognitive Kernel-Pro: A Framework for Deep Research Agents and Agent Foundation Models Training
> L6: - Fully reproducible open-source SFT training recipe that outperforms RL-based models like WebDancer and WebSailor—n
> L70: # Assume we have set up a vllm model server and a web-browser server (currently these are active: WEB_IP

## 星数曲线

```mermaid
xychart-beta
    title "Tencent/CognitiveKernel-Pro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 532 --> 534
    line [533, 533]
```

2026-10-18 533 → 2026-10-30 533（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `5ef607309e44` · [字段定义](../../DATASET.md)*
