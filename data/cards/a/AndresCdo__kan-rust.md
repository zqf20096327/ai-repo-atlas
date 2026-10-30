# AndresCdo/kan-rust

⭐ 21 · Rust · MIT · 推送 2026-08-11 · [GitHub](https://github.com/AndresCdo/kan-rust) · 个人维护

**Rust 实现的固定网格 Kolmogorov-Arnold 网络（KAN）库**

以正确性优先为原则的 Rust crate，实现固定网格 KAN：三次 B 样条边激活、全量反向模式梯度、SGD 更新、显式种子的确定性初始化，以及带版本的 JSON 持久化与推理往返。所有公开操作校验输入并返回 Result，设有限制（至多 25 万可训练参数、8 MiB JSON 状态）。正则化、自适应网格、剪枝、符号拟合在 0.2.0 中明确未实现。面向使用 Rust 构建/训练 KAN 模型的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三次 B 样条边激活与全量反向模式梯度
- 版本化 JSON 持久化与推理往返
- 显式种子的确定性初始化
- 输入校验返回 Result，参数量与序列化体积设上限

## 适用场景

- 在 Rust 项目中构建与训练固定网格 KAN 模型
- 以确定性 JSON 格式保存并复载 KAN 模型
- 通过 CLI 训练演示模型并检查已有模型文件

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: `kan` is a correctness-first Rust implementation of a fixed-grid
> L9: - Degree-three B-spline edge activations on exterior-extended uniform knots.
> L10: - Full reverse-mode gradients through every KAN layer.

## 星数曲线

```mermaid
xychart-beta
    title "AndresCdo/kan-rust 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `56ecd99942ee` · [字段定义](../../DATASET.md)*
