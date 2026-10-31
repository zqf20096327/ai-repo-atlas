# Koratahiu/Advanced_Optimizers

⭐ 38 · Python · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/Koratahiu/Advanced_Optimizers) · 个人维护

**PyTorch 高级优化器集合：AdamW/Muon 等变体与内存优化训练**

以 pip 包 adv_optm 形式提供的深度学习优化器集合，收录 AdamW、Muon、AdaMuon、Signum、Prodigy 等变体的增强实现，面向使用 PyTorch 训练模型的开发者。机制上支持 torch.compile 编译路径（需 PyTorch 2.3+）、1-bit 分解模式（nnmf_factor）、BF16 随机舍入、融合与原地操作、cautious weight decay 等，以降低内存占用并加速优化器步进；对 PEFT/LoRA 参数需先行标记。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AdamW/Muon/AdaMuon/Signum/Prodigy 等多个优化器增强变体
- 全部优化器支持 torch.compile 编译路径
- 1-bit 分解模式与 BF16 随机舍入等内存优化技术
- cautious/centered/Fisher/geometric 等权重衰减变体

## 适用场景

- 微调大模型时换用低内存占用的优化器变体
- 在 LoRA/PEFT 训练中使用带谱缩放的优化器
- 通过 torch.compile 加速优化器步进

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L12: pip install adv_optm
> L42: from adv_optm import AdamW_adv
> L49: * For PEFT/LoRA models, tag parameters before passing them to the optimizer so spectral scaling and other features 

## 星数曲线

```mermaid
xychart-beta
    title "Koratahiu/Advanced_Optimizers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-31 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cad79b7c4c59` · [字段定义](../../DATASET.md)*
