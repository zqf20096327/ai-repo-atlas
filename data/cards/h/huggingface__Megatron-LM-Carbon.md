# huggingface/Megatron-LM-Carbon

⭐ 10 · Python · 推送 2026-05-19 · [GitHub](https://github.com/huggingface/Megatron-LM-Carbon) · 组织维护

**Carbon DNA 语言模型的两阶段训练代码，基于 Megatron-LM**

提供 Carbon DNA 语言模型的训练流程：Phase 1 用上游 Megatron-LM 的 pretrain_gpt.py 做交叉熵预训练（100B token，WSD 调度），Phase 2 通过自带的 pretrain_gpt_hybrid.py 加入 FNS/BP marginal 损失，把 6-mer token logits 边缘化为碱基级概率继续训练。上游 Megatron-LM 以锁定 commit 的 git submodule 引入，避免长期分叉。训练经 sbatch 启动脚本提交，路径与数据位置可通过环境变量覆盖；日志默认写入 wandb，可选 trackio。已发布 3B/8B 检查点到 Hugging Face。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两阶段训练：CE 预训练后叠加 Factorized Nucleotide Supervision 损失
- 上游 NVIDIA/Megatron-LM 以 pinned git submodule 引入以保持可复现
- sbatch 启动脚本支持环境变量覆盖集群路径与数据位置
- 提供 trackio 运行时 shim 修复上游 wandb writer 的 Tensor 序列化问题

## 适用场景

- 复现或继续训练 Carbon 3B/8B DNA 语言模型
- 在自有集群上用 sbatch 提交两阶段 DNA 模型训练
- 开发基于 Megatron-LM 的自定义训练损失时参考 hybrid loss 配置
- 用 trackio 或 wandb 记录训练日志

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: Training code for the Carbon DNA language model: a thin Python package
> L15: |**Phase 1 — pretrain**|Cross-entropy|upstream `pretrain_gpt.py` (no carbon-side modifications)|WSD, peak LR 3e-4|1
> L16: |**Phase 2 — refine**|CE + Factorized Nucleotide Supervision|`src/carbon/pretrain_gpt_hybrid.py`|WSD (3B) / cosine 

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/Megatron-LM-Carbon 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-21"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-23 10 → 2026-11-21 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `506203ac64b2` · [字段定义](../../DATASET.md)*
