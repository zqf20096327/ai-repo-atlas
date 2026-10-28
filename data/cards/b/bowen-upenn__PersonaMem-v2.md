# bowen-upenn/PersonaMem-v2

⭐ 51 · Python · 推送 2026-09-06 · [GitHub](https://github.com/bowen-upenn/PersonaMem-v2) · [官网](https://huggingface.co/datasets/bowen-upenn/PersonaMem-v2) · 组织维护

**LLM 个性化基准：1000 用户画像、2 万+偏好、300+场景**

面向 LLM 个性化评测的基准数据集与配套训练代码：覆盖 1000 个用户画像、20000+ 偏好、300+ 场景，重点考察模型与 agentic memory 系统从长上下文对话中推断隐式用户偏好的能力。提供 Docker 环境配置、OpenAI/Azure API 接入的前沿模型推理脚本、基于 verl 的 GRPO/SFT 训练（含 Qwen3-4B）、改造自 MemAgent 的 agentic memory 训练管线，以及从零重新生成基准的完整数据生成流程。数据从 HuggingFace 下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1000 用户画像、20000+ 偏好、300+ 场景的个性化基准
- 隐式偏好通过长上下文对话揭示（32k/128k）
- 基于 verl 的 GRPO 训练与改造的 MemAgent agentic memory 管线
- 提供从零重新生成基准的五步数据生成流水线

## 适用场景

- 评测 LLM 或记忆系统在长对话中推断用户偏好的能力
- 用 GRPO 训练个性化模型（如 Qwen3-4B）
- 研究生成式个性化场景下的用户记忆机制

## 场景标签

`模型评测` `强化学习` · 领域:评测与运维

## 证据(README 行号)

> L11: PersonaMem-v2 is the state-of-the-art LLM personalization benchmark, covering 1000 comprehensive user personas and 
> L105: ### Train a model using Agentic Memory with the verl framework:

## 星数曲线

```mermaid
xychart-beta
    title "bowen-upenn/PersonaMem-v2 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25", "2026-10-28"]
    y-axis "stars" 47 --> 51
    line [48, 49, 50, 50]
```

2026-10-18 48 → 2026-10-28 50（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f583ded4e496` · [字段定义](../../DATASET.md)*
