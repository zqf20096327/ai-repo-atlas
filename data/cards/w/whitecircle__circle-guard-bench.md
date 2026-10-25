# whitecircle/circle-guard-bench

⭐ 82 · Python · Apache-2.0 · 推送 2026-03-07 · [GitHub](https://github.com/whitecircle/circle-guard-bench) · [官网](https://whitecircle.ai) · 组织维护

**评估 LLM 护栏模型防护能力的基准测试框架**

由 White Circle 公司开发的 LLM 护栏（guardrail）评测基准：在 17 类有害内容分类体系上测量护栏模型的有害内容检测、越狱抵抗、误报率与运行时性能，并给出综合准确率与速度的积分。支持 openai_api、vLLM、SGLang、transformers 四种推理引擎，通过 guardbench CLI 运行评测与生成排行榜；数据集托管于 HuggingFace，公开部分需接受许可条款后访问。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 17 类有害内容、含越狱对抗变体的数据集格式
- 同时评测准确率、攻击鲁棒性与延迟的综合积分制
- 支持 openai_api / vllm / sglang / transformers 四种推理引擎
- guardbench CLI 支持评测、排行榜排序、按类别分组

## 适用场景

- 安全团队为生产环境选型护栏模型
- 对自研 guard 模型做多类别有害内容与越狱评测
- 生成含逐类别与宏平均分数的评测排行榜

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L5: **CircleGuardBench** is the first-of-its-kind benchmark for **evaluating the protection capabilities** of large lang
> L20: - Standardized evaluation of multiple LLMs and guard models
> L27: Most benchmarks focus on accuracy alone, ignoring critical production requirements like speed and jailbreak resista

## 星数曲线

```mermaid
xychart-beta
    title "whitecircle/circle-guard-bench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 81 --> 83
    line [82, 82]
```

2026-10-18 82 → 2026-10-25 82（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3fdc9e0f19b8` · [字段定义](../../DATASET.md)*
