# diagram-of-thought/diagram-of-thought

⭐ 201 · 推送 2026-05-14 · [GitHub](https://github.com/diagram-of-thought/diagram-of-thought) · [官网](https://huggingface.co/papers/2409.10038) · 组织维护

**单模型构建推理 DAG 的推理框架论文官方实现**

论文《On the Diagram of Thought》的官方实现：让单个 LLM 通过角色标记（proposer/critic/summarizer）内化提出→批判→修正→总结循环，将推理过程构建为有向无环图（DAG）；用类型化序列化协议（@node/@edge/@status）记录推理路径，支持确定性提取与事后验证，并以范畴论/topos 理论给出形式化保证。README 以提示词模板方式提供使用方法，适用于任何具备能力的 LLM，面向研究结构化推理、可验证性与可解释性的研究者和开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单模型内化 propose→critique→refine→summarize 循环，无需外部控制器
- @node/@edge/@status 类型化协议记录推理 DAG，支持确定性提取与在线校验
- 以 topos 理论形式化，最终总结对应信息序上的 colimit
- 提供最小提示词模板，可引导任意 LLM 执行 DoT 推理

## 适用场景

- 研究 LLM 结构化推理与自我修正，获取可审计的推理轨迹
- 金融/医疗等高可靠场景构建可解释推理应用
- AI 安全与评测工具中对推理路径做确定性提取与事后分析

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L13: **Diagram of Thought (DoT)** is a framework that enables a **single LLM** to construct and refine a mental map of i
> L52: You can guide any capable LLM to perform DoT reasoning with the following prompt structure. The model learns to alt
> L94:  * **AI Researchers** studying structured reasoning, self-correction, or verifiability in LLMs who need **auditable

## 星数曲线

```mermaid
xychart-beta
    title "diagram-of-thought/diagram-of-thought 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 200 --> 202
    line [201, 201]
```

2026-10-18 201 → 2026-10-27 201（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2f29a28e3001` · [字段定义](../../DATASET.md)*
