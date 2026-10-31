# MatN23/AdaptiveTrainingSystem

⭐ 20 · Python · Apache-2.0 · 推送 2026-10-13 · [GitHub](https://github.com/MatN23/AdaptiveTrainingSystem) · 个人维护

**面向 ML 工程师的 MoE/MoD Transformer 训练框架，含自定义 CUDA/Metal 内核**

从零训练 Transformer 的完整框架：实现 MoE（8-64 专家）与 MoD（动态深度）稀疏架构，提供自定义 CUDA 内核（RMSNorm/RoPE/SwiGLU/路由）与 Apple Silicon Metal shader，不可用时自动回退 PyTorch；含自适应编排器（18 种自主干预）、ZeRO CPU/NVMe 卸载、DeepSpeed/FSDP/ColossalAI 多卡训练、多源合法数据下载器与 C++/Metal 推理后端。面向需要全栈控制权的 ML 工程师与研究团队；不含预训练权重与教程，仅支持从零训练，假定用户具备 ML 工程背景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MoE/MoD/混合稀疏架构，支持 500M-300B+ 参数规模
- 自定义 CUDA 内核（宣称 2-7x 加速）与 Metal shader，均带 PyTorch 自动回退
- 自适应编排器监控 20+ 指标并触发 18 种干预
- 权重级所有权标识：向模型权重嵌入可检测 canary 签名

## 适用场景

- 从零训练 MoE/MoD 稀疏 Transformer 模型
- 在 GPU VRAM 不足时用 CPU/NVMe 卸载训练大参数模型
- 在自有数据与合规要求下搭建企业内部训练基础设施

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L17: Adaptive Training System is a production-grade transformer training framework implementing Mixture of Experts (MoE)
> L40: This is a complete training system with custom CUDA kernels, not a model zoo or API wrapper. Every component from t
> L46: **Intended for:**

## 星数曲线

```mermaid
xychart-beta
    title "MatN23/AdaptiveTrainingSystem 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 low · 依据 README sha `ab99ab41372e` · [字段定义](../../DATASET.md)*
