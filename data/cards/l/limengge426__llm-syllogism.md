# limengge426/llm-syllogism

⭐ 21 · Python · MIT · 推送 2026-09-27 · [GitHub](https://github.com/limengge426/llm-syllogism) · [官网](https://openreview.net/pdf?id=fMIpSy6NVW) · 个人维护 · 中文 README

**LLM 三段论推理基准：44 形式 11,000 题揭示五模型共性偏差**

AAAI 2026 Bridge 论文配套基准与流水线：从 WordNet 上下位链采样词项，生成覆盖全部 44 个经典三段论形式（24 有效、20 无效）共 11,000 题的结论正确性判别任务；模型零样本作答。配套 Python 脚本完成题目生成、prompt 构造与 API 并发查询（断点续跑、退避重试）。论文报告 GPT-4o、Gemini、LLaMA、Qwen、DeepSeek 五个模型错误模式高度一致（两两 Pearson r=0.886），有效结论准确率 93% 而无效仅 56%。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 44 个三段论形式 × 250 题共 11,000 项，词项取自 WordNet 上下位链
- 零样本、无思维链的正确性判别任务设计
- asyncio 并发查询脚本，支持限速退避、重试与断点续跑
- 离线捆绑 WordNet，无需 NLTK 下载

## 适用场景

- 评测 LLM 是否依赖语言表层规律而非逻辑结构
- 复现论文中五模型的中项位置偏差与有效/无效不对称结果
- 构建或扩展逻辑推理基准数据集

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L100: |**Total**|**44**||**11,000**||
> L79: A **Mood** (e.g. `AAA`) sets the types of the two premises and the conclusion. A **Figure** (1–4) sets where the mi
> L21: |🔗|**Different models make the same mistakes.** GPT-4o, Gemini, LLaMA, Qwen and DeepSeek find the same syllogisms e

## 星数曲线

```mermaid
xychart-beta
    title "limengge426/llm-syllogism 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `7cd8e2633158` · [字段定义](../../DATASET.md)*
