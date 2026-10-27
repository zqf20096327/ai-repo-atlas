# GiggleLiu/BackwardsLinalg.jl

⭐ 35 · Julia · NOASSERTION · 推送 2025-11-24 · [GitHub](https://github.com/GiggleLiu/BackwardsLinalg.jl) · 个人维护

**线性代数函数反向传播的 Julia 自动微分扩展库**

Zygote.jl 的扩展库，为线性代数函数（SVD、随机 SVD、QR、特征分解对称情形、LQ）提供反向传播实现，支持 GPU。动机是 PyTorch 等主流机器学习包缺乏数值稳定的线性代数求导实现，而这在张量网络算法的自动微分应用中不可或缺。cholesky、powermethod、pfaffian 尚未实现；logdet/det/tr 指向 ChainRules.jl 和 Nabla.jl。项目自述仍在开发中，部分端口代码未来可能并入 Zygote.jl。

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

- 为 svd/rsvd/qr/eigen(对称)/lq 提供反向函数
- 支持 GPU
- 作为 Zygote.jl 扩展使用
- 附 TRG 反向传播测试示例

## 适用场景

- 在 Julia 中对含 SVD/QR 等分解的函数做自动微分
- 张量网络算法（如 TRG）的梯度计算

## 场景标签

 · 领域:机器学习/科学计算

## 证据(README 行号)

> L8: Backward functions for linear algebras, with GPU support.
> L31: It currently ports into `Zygote.jl`

## 星数曲线

```mermaid
xychart-beta
    title "GiggleLiu/BackwardsLinalg.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-27 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d91a952038e9` · [字段定义](../../DATASET.md)*
