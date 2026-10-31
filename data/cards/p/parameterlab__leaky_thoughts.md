# parameterlab/leaky_thoughts

⭐ 18 · Python · MIT · 推送 2026-01-12 · [GitHub](https://github.com/parameterlab/leaky_thoughts) · 组织维护

**论文代码：研究大型推理模型思维链中的隐私泄露**

EMNLP 2025 论文 Leaky Thoughts 的官方代码库，研究大型推理模型（LRM）作为个人代理时其推理轨迹中的隐私泄露问题。提供两类实验：eval_cp.py 直接探测模型，基于 AirGapAgent-R 数据集计算效用、隐私与 PII 泄露分数；agentic 实验在 WebArena 模拟网页环境中交互评估，需 EC2 实例与 Docker 部署环境。支持 vllm/openrouter/openai 提供方，含 LLM-as-a-judge 评估与 RAnA/RSwA 推理匿名化流程。使用 uv 管理依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- eval_cp.py 探测模型推理中的敏感数据泄露并计算效用/隐私/PII 分数
- 发布 AirGapAgent-R 数据集（Hugging Face）
- WebArena agentic 环境下的交互式隐私评估
- RAnA（推理后匿名化再作答）与 RSwA 流程实验

## 适用场景

- 复现论文中的 LRM 隐私泄露探测实验
- 评估推理模型在代理任务中的隐私风险
- 在 WebArena 模拟环境中测试模型交互时的数据暴露

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: This is the repository for the paper Leaky Thoughts: Large Reasoning Models Are Not Private Thinkers.
> L7: This project investigates privacy leakage within the reasoning traces of Large Reasoning Models (LRMs) when they fun

## 星数曲线

```mermaid
xychart-beta
    title "parameterlab/leaky_thoughts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `17bb10ec59f2` · [字段定义](../../DATASET.md)*
