# chiennv2000/orthrus

⭐ 482 · Python · MIT · 推送 2026-08-12 · [GitHub](https://github.com/chiennv2000/orthrus) · 个人维护

**无损加速 LLM 推理的双视角扩散解码框架**

提供官方实现与模型 checkpoint：在同一模型内统一自回归视角与扩散视角，二者共享同一 KV cache，实现并行 token 生成。通过模型内精确共识机制保证输出与原基座模型的预测分布严格一致（无损），模型库基于 Qwen3（1.7B/4B/8B），报告 4.25×-5.36× 平均加速。仅微调约 16% 参数、基座 LLM 冻结。提供 uv/pip 源码安装、Colab 即试与 Apple Silicon MLX 推理支持；vLLM/SGLang 原生集成标注为 coming soon。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 自回归+扩散双视角共享同一 KV cache，O(1) 额外缓存开销
- 精确共识机制保证与基座模型分布严格一致的损失无损生成
- 基于 Qwen3 的 1.7B/4B/8B 模型库，报告平均 4.25×-5.36× 加速
- Apple Silicon 原生 MLX 推理支持

## 适用场景

- 在不改变输出分布的前提下加速 LLM 文本生成
- 长上下文场景下提升端到端推理吞吐
- 在 Apple Silicon 上本地运行加速后的 Qwen3 模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: Official implementation and model checkpoints for **Orthrus**, a dual-architecture framework that unifies the exact 
> L48: - **Strictly Lossless Generation:** Employs an exact intra-model consensus mechanism to guarantee that the output m

## 星数曲线

```mermaid
xychart-beta
    title "chiennv2000/orthrus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 481 --> 483
    line [482, 482]
```

2026-10-18 482 → 2026-10-21 482（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `e676a0de0247` · [字段定义](../../DATASET.md)*
