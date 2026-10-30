# Dicklesworthstone/bio_inspired_nanochat

⭐ 62 · Python · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/Dicklesworthstone/bio_inspired_nanochat) · 个人维护

**Nanochat 研究分叉：用生物启发机制替代静态权重的语言模型**

Karpathy Nanochat 的研究分支，将静态权重替换为突触蛋白的计算模拟：实现突触前释放（RRP 资源池疲劳）、BDNF 元可塑性、快/慢双权重、CaMKII/PP1 双稳态锁存、带能量代谢与生命周期的结构化 MoE 等 11+ 机制，权重可在推理期间变化。含 CMA-ES 超参优化与统计评估层，提供 Triton GPU 与 Rust CPU 实验内核（默认关闭）。当前所有机制仅在 CPU 玩具规模验证，尚未在 GPU 上训练模型；在线 Hebbian 可塑性因预注册实验未达标改为 opt-in。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 突触前释放/Hebbian 快权重/结构化 MoE 生命周期等 11+ 生物机制，运行于 live path
- 权重在推理期间生长、疲劳、恢复的实时演化机制
- CMA-ES 超参优化（Phase 1 接入 10 参数）与配对检验/Bootstrap 统计评估层
- Triton CUDA 与 Rust CPU 内核（默认关闭，与规范 PyTorch 路径做奇偶校验）

## 适用场景

- 研究生物启发机制对语言建模损失的影响（消融矩阵实验）
- 试验推理期间权重可变的 Transformer 架构
- 在玩具规模复现并扩展突触可塑性与 MoE 生命周期实验

## 场景标签

`模型训练` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: This is a research fork of Nanochat that replaces standard static weights with **computational analogs of synaptic p
> L11: Standard LLMs are "frozen crystals"—static matrices of `float16` numbers that never change once training is done. *
> L25: **Evidence status (2026-10-13):** everything marked ✅ below is implemented on the live path and unit-tested at toy 

## 星数曲线

```mermaid
xychart-beta
    title "Dicklesworthstone/bio_inspired_nanochat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-30 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `df4cee3f904f` · [字段定义](../../DATASET.md)*
