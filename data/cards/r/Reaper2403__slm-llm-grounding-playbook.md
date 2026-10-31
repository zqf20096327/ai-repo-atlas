# Reaper2403/slm-llm-grounding-playbook

⭐ 15 · Python · MIT · 推送 2026-04-27 · [GitHub](https://github.com/Reaper2403/slm-llm-grounding-playbook) · 个人维护

**LLM+SLM 双通道事实接地架构模式与参考实现**

面向构建实时对话系统的开发团队，提供将快速对话 LLM 与后台小型接地模型（SLM）结合的架构模式：LLM 负责对话交付，SLM 在后台从对话中抽取硬事实并维护共享账本，运行时管理权限、确认循环与工具门控。仓库内容为文档（方法论、架构、反模式、微调指南）、可复制的 JSON schema、提示词模板与调度规则，以及 starter_sdk/python 下的一个小型 Python 参考实现，模式提炼自应急调度原型。

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

- 快慢双通道分工：LLM 管对话，SLM 管证据式事实抽取与状态延续
- 共享账本作为事实真相源，工具按账本门控而非 LLM 置信度
- 包含微调指南（优先微调后台 SLM）与评测/数据集策略
- 提供 schemas、prompts、orchestration 与 Python 参考实现

## 适用场景

- 构建需要长程事实一致性的实时语音/对话 agent
- 在应急调度、医疗问诊、支持分诊等场景落地接地架构
- 了解 LLM 对话循环之外如何做事实追踪与工具门控

## 场景标签

`语音 Agent` `提示工程` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: Patterns for combining a fast conversational LLM with a smaller grounding model (SLM) that tracks hard facts in the 
> L22: - **Fast voice/chat lane**: the LLM speaks immediately from the last committed state.
> L28: - the **SLM** owns evidence-only fact extraction and state carry-forward

## 星数曲线

```mermaid
xychart-beta
    title "Reaper2403/slm-llm-grounding-playbook 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `420a3b41144a` · [字段定义](../../DATASET.md)*
