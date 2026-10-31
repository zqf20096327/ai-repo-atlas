# FudanCVL/AVI-Bench

⭐ 18 · Python · NOASSERTION · 推送 2026-10-04 · [GitHub](https://github.com/FudanCVL/AVI-Bench) · [官网](https://fudancvl.github.io/AVI-Bench/) · 组织维护

**评测 Omni-MLLM 视听联合推理的基准（14 任务 5,864 样本）**

ICML 2026 论文配套的音视频多模态大模型评测基准：按感知→理解→推理三阶段组织 14 个任务、5,864 个样本，并加入 Primitive Sensation（PriSe）扩展，用合成低语义刺激测试分布外泛化；提供四级音视频智能分类体系（任务/模态/阶段/领域自适应）输出可解释诊断。仓库含统一推理入口 run.py、LLM 答案格式化与评测管线，适配任意 OpenAI 兼容 API（含自托管），支持按模板接入新模型，可断点续跑。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 14 任务 / 5,864 样本，覆盖感知、理解、推理与 PriSe 四阶段
- PriSe 用合成低语义刺激配合 double-confirm 机制探测分布外感知
- 四级分类体系（任务/模态/阶段/领域）输出聚合诊断分数
- 统一推理 + 答案格式化 + 评测管线，适配任意 OpenAI 兼容 API

## 适用场景

- 评测自家的 Omni-MLLM 在视听联合推理上的表现
- 诊断模型在音频主导任务或低语义刺激上的短板
- 向社区榜单提交模型评测结果

## 场景标签

`模型评测` `多模态` · 领域:评测与运维

## 证据(README 行号)

> L22: - a **unified inference + answer-formatting + evaluation pipeline**,
> L23: - a reference adapter for any **OpenAI-compatible API** (Gemini / GPT-4o / Claude / self-hosted),

## 星数曲线

```mermaid
xychart-beta
    title "FudanCVL/AVI-Bench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `bcae628ffa1e` · [字段定义](../../DATASET.md)*
