# yiksiu-chan/SpeakEasy

⭐ 16 · Python · MIT · 推送 2026-03-07 · [GitHub](https://github.com/yiksiu-chan/SpeakEasy) · [官网](https://arxiv.org/abs/2502.04322) · 组织维护

**LLM 越狱攻击研究框架：多轮/多语言诱导攻击与危害评分**

ICML 2025 论文 Speak Easy 的官方代码库。提供基于多步、多语言查询的越狱攻击方法（可叠加 Direct Request、GCG、TAP 三种框架），以及 HarmScore 评分指标（衡量回答的可操作性与信息量）。支持 OpenAI API 与 vLLM 本地推理后端，附带用于训练评分模型的 DPO 偏好数据集与 CLI 工具。面向 LLM 安全研究人员，用于红队评估与攻击对比实验。限制：需 Python 3.9+，翻译等组件依赖 Azure/Google 等可选服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多步/多语言查询诱导越狱，可叠加 baseline_dr/gcg/tap 三种攻击框架
- HarmScore 指标：结合可操作性与信息量评分，另提供 GPT-4 judge 二分类
- 附带 5 个 DPO 偏好数据集（Parquet 格式）用于训练评分模型
- 支持 OpenAI API 与 vLLM 本地推理两种后端

## 适用场景

- 对 LLM 做红队攻击测试，度量越狱成功率（ASR）
- 在 HarmBench/AdvBench 等基准上复现论文攻击结果
- 用 HarmScore 对已有问答数据批量评分

## 场景标签

`网络安全` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L14: We show that simple interactions such as multi-step, multilingual querying can elicit sufficiently harmful jailbrea
> L118: |`gpt4judge`|GPT-4-based judge for binary jailbreak detection|
> L162: │   ├── backends/          # Model inference backends (OpenAI, vLLM)

## 星数曲线

```mermaid
xychart-beta
    title "yiksiu-chan/SpeakEasy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `056b46e9fc41` · [字段定义](../../DATASET.md)*
