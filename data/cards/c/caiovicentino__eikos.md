# caiovicentino/eikos

⭐ 41 · Python · MIT · 推送 2026-10-01 · [GitHub](https://github.com/caiovicentino/eikos) · [官网](https://huggingface.co/caiovicentino1) · 个人维护

**面向金融与交易的校准单次类型化决策开源模型（4B/27B）**

Eikos 是 MIT 许可的开放类型化决策模型家族，含 4B 与 27B 两档，各有 bf16/FP8/INT4 GPU 构建及 Apple Silicon 的 MLX 构建。模型对给定状态的结构化问题在单次前向中作答，为每个选项返回校准概率，支持一次处理最多数百个选项与图像输入，并提供 HTTP 服务、agent 会话与增量状态。仓库包含推理与服务代码、数据管线、训练（LoRA+软交叉熵）、量化与评测全流程；基座为 Qwen3.5，服务端依赖 vLLM ≥0.30.0。局限：不预测价格、不做多步长推理、不构成法律或投资建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个选项返回校准概率，支持基于置信度阈值的行为策略
- 单次前向处理多问题/多选项（最多 588 选项），共享状态走前缀缓存
- 提供 bf16/FP8/INT4 GPU 与 MLX 构建，量化需通过与 bf16 对齐的门禁
- 全流程开源：数据管线、训练配方、量化与评测框架

## 适用场景

- 对金融/贸易合规规则做结构化裁决并按置信度分流
- 在交易系统中批量回答同一状态下的多个决策问题
- 在 Apple Silicon 或单张 80–96GB GPU 上本地部署校准决策模型
- 复现训练数据与评测流程

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5: **Eikos** (εἰκός, *"the probable"*) is a family of open typed-decision models, released under MIT. Each model:
> L7: - returns a **calibrated probability for every option**, so a caller can act on confident decisions and escalate
> L11: Silicon. The focus is global finance, trading and trade finance: applying stated rules, policies and rulebooks to

## 星数曲线

```mermaid
xychart-beta
    title "caiovicentino/eikos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-28 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `43ffe447509f` · [字段定义](../../DATASET.md)*
