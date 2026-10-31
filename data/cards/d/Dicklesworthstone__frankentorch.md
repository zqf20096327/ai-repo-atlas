# Dicklesworthstone/frankentorch

⭐ 16 · Rust · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/Dicklesworthstone/frankentorch) · 个人维护

**PyTorch 的 Rust 净室重实现，含确定性自动微分与合规性测试**

面向 PyTorch 生态开发者的净室（clean-room）Rust 重实现项目：目标是与上游 PyTorch 可观察行为完全重叠的 drop-in 替代，保留张量语义、autograd 契约、优化器行为与序列化契约。核心机制包括确定性自动微分契约（DAC，可重放的梯度图执行与证据账本）、strict/hardened 兼容模式分离、差分合规测试 harness，以及基于 RaptorQ 纠删编码的长寿命工件持久化。工作区含 12 个 Rust crate，覆盖 tensor 核心、CPU 内核、nn/optim/data 层与合规验证。当前为 CPU 优先实现，README 声称包尚未发布到 registry，Metal 内核版本仅为发布准备。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 确定性自动微分契约（DAC）：可重放梯度图与出处完整的梯度证据
- 12 个 Rust crate 工作区：tensor/dispatch/CPU 内核/autograd/nn/optim/data
- 差分合规与端到端 forensics 测试 harness，针对 PyTorch 行为 oracle
- RaptorQ 纠删编码支撑的工件持久化与完整性校验流水线

## 适用场景

- 需要内存安全语言实现的 PyTorch 兼容张量/训练栈
- 要求梯度计算确定性可重放与证据审计的训练场景
- 研究 PyTorch 到 Rust 的移植与行为一致性验证方法

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L9: FrankenTorch is not a partial rewrite. The target is a true drop-in replacement with complete feature and functional
> L35: - deterministic autograd, CPU kernels, serialization, conformance harnesses, and higher-level nn/optim/data layers 

## 星数曲线

```mermaid
xychart-beta
    title "Dicklesworthstone/frankentorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2ba739d2adc7` · [字段定义](../../DATASET.md)*
