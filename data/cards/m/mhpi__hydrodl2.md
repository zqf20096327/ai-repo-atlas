# mhpi/hydrodl2

⭐ 24 · Python · NOASSERTION · 推送 2026-10-03 · [GitHub](https://github.com/mhpi/hydrodl2) · [官网](https://mhpi.github.io/benchmarks/) · 组织维护

**给水文研究者：基于 PyTorch 的可微分水文模型库**

MHPI 维护的可微分水文模型库，基于 PyTorch 实现多个 HBV 水文模型变体（含伴随梯度隐式方案、多尺度分布式、逐时与多时间尺度版本），模型为标准 torch.nn.Module 子类，可与神经网络经 𝛿MG 组合实现端到端可微分训练，支持参数学习、偏差修正与缺失过程表示。提供 pip 安装，配 Quick Start 示例与多篇论文引用条目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个 HBV 系列可微分水文模型（含伴随梯度与多尺度变体）
- 模型为标准 torch.nn.Module，可与神经网络端到端联合训练
- 支持参数学习、偏差修正、缺失过程表示

## 适用场景

- 用可微分建模做水文参数学习与径流预测
- 在 𝛿MG 框架中组合物理模型与神经网络
- 复现已发表的 dPL 水文建模研究

## 场景标签

`科研工具` `模型训练` · 领域:学习与行业

## 证据(README 行号)

> L13: A library of hydrological models developed on PyTorch and designed alongside 𝛿MG for the creation of end-to-end dif
> L34: Models are standard `torch.nn.Module` subclasses and can be composed with neural networks via &delta;MG for end-to-

## 星数曲线

```mermaid
xychart-beta
    title "mhpi/hydrodl2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `95ab23924ce1` · [字段定义](../../DATASET.md)*
