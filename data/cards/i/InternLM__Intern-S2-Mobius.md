# InternLM/Intern-S2-Mobius

⭐ 59 · Python · 推送 2026-08-14 · [GitHub](https://github.com/InternLM/Intern-S2-Mobius) · 组织维护 · 中文 README

**35B 基础模型：知识-推理分离架构的高效推理模型**

InternLM 团队发布的 35B 参数基础模型，基于 Mobius-v0 架构，由 Xtuner 和 LMDeploy 实现。架构上将知识存入全局共享 Memory，多个 Reasoner 迭代查询与精炼隐状态，提供跨层残差连接与动态隐式推理两项机制。模型从 Qwen3.5-35B 持续预训练并经 SFT 与 RL 后训练，权重为 bfloat16 格式，可通过 LMDeploy、Transformers、vLLM、SGLang 部署，支持 MTP 投机解码，报告中称端到端推理加速近 4 倍。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 知识存入全局共享 Memory、Reasoner 迭代查询的知识-推理分离架构
- 从 Qwen3.5-35B 持续预训练并经 SFT 与 RL 后训练
- 支持 LMDeploy / Transformers / vLLM / SGLang 部署
- 支持 MTP 投机解码与最大 64K–128K 推理长度评测

## 适用场景

- 用 LMDeploy 或 vLLM 部署 API 服务进行文本推理
- 在科学类任务（生物、分子相关基准）上使用该模型
- 对比测试知识-推理分离架构的推理效率

## 场景标签

 · 领域:大模型/基础模型

## 证据(README 行号)

> L13: We introduce **Intern-S2-Mobius**, a 35B foundation model built on the Mobius-v0 architecture realized by Xtuner an
> L57: The Intern-S2-Mobius release is a 35B model stored in bfloat16 weight format. This guide provides deployment exampl

## 星数曲线

```mermaid
xychart-beta
    title "InternLM/Intern-S2-Mobius 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-29 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a11ee8c893c6` · [字段定义](../../DATASET.md)*
