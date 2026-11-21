# anupbagale/how-vit-works

⭐ 5 · Python · MIT · 推送 2026-10-10 · [GitHub](https://github.com/anupbagale/how-vit-works) · 个人维护

**用 NumPy 手写逐步讲解 Vision Transformer 工作原理的教程**

教学型仓库：以一张脑部 MRI 风格切片为例，逐步展示 ViT 的完整前向过程——切 patch、patch embedding、位置编码、自注意力、[CLS] 分类，全部用 NumPy 手写实现，并在 tests/ 中验证与 PyTorch 输出 logits 一致（误差 1e-4 内）。训练用 6,000 张合成切片，单 block、4 heads、47,234 参数，测试准确率 99.5%。附 CNN 对照仓库与 CNN vs ViT 对比表。作者明确说明局限：仅一个 block、数据为合成、attention 不必然等于解释。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全部 ViT 运算（patchify、attention、layer norm）用 NumPy 手写实现
- NumPy 与 PyTorch 输出 logits 一致性在 tests/ 中校验
- 展示每个注意力头的关注位置与 [CLS] 对各 patch 的 softmax 权重
- 附 CNN 对照仓库及 CNN vs ViT 逐项对比表

## 适用场景

- 想逐步理解 Vision Transformer 前向传播的每一步
- 通过对比同一输入在 CNN 与 ViT 中的处理方式学习两类架构差异
- 查看 attention map 在医学影像任务中的可解释性示例

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L1: How a Vision Transformer (ViT) works
> L13: Transformers took over language, then vision, and now medical imaging. Most explanations stop at the
> L150: ```bash

## 星数曲线

```mermaid
xychart-beta
    title "anupbagale/how-vit-works 星数(近 3 点)"
    x-axis ["2026-10-28", "2026-10-31", "2026-11-21"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-10-28 4 → 2026-11-21 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `f99e222ab4bf` · [字段定义](../../DATASET.md)*
