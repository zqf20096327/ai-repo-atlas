# huggingface/transformers-to-mlx

⭐ 51 · Python · 推送 2026-06-16 · [GitHub](https://github.com/huggingface/transformers-to-mlx) · 组织维护

**将 transformers LLM 架构转换为 MLX 的 Agent Skill**

Hugging Face 维护的 Agent Skill，用于把 transformers 语言模型移植到 mlx-lm：在虚拟环境中安装 mlx-lm 与 transformers，进行模型发现、分析配置与建模代码、完成移植并运行测试，最后可向 mlx-lm 代码库开 PR 并生成独立测试清单。支持 MoE、MLA（DeepSeek 式）、混合 SSM+注意力、GatedDeltaNet、分布式推理等架构处理。限制：不支持 VLM（仅转换其 LLM 部分），量化模型不上传 Hub，无 thinking 专项测试。面向使用 Claude 类 agent 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 虚拟环境内自动完成依赖安装、模型发现、移植与测试流程
- 支持 MoE、MLA、混合 SSM+注意力、GatedDeltaNet 等架构
- 可向 mlx-lm 开 PR 并为独立测试仓库生成测试清单
- 附带 compare_predictions.py 等独立比对工具脚本

## 适用场景

- 把 transformers 上的 LLM 架构移植到 MLX 并提交 PR
- 借助独立测试仓库核验移植结果的正确性
- 通过比对脚本对比 transformers 与 MLX 的前向输出

## 场景标签

 · 领域:LLM 基础设施/模型移植

## 证据(README 行号)

> L3:  Agent Skill to aid in the conversion of transformers models to MLX
> L7: Use this Skill to support conversion of language models from transformers to MLX. It currently works for **LLM model

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/transformers-to-mlx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-30 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b76354e82004` · [字段定义](../../DATASET.md)*
