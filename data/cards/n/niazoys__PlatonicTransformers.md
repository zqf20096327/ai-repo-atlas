# niazoys/PlatonicTransformers

⭐ 65 · Python · MIT · 推送 2026-09-25 · [GitHub](https://github.com/niazoys/PlatonicTransformers) · 组织维护

**ICML 2026 论文代码：给 Transformer 加入柏拉图立体群等变注意力**

Platonic Transformers 的研究代码：以柏拉图固体旋转群为参考帧，把逐点特征提升到有限旋转-反射群上并行做注意力（共享权重），通过 RoPE 实现平移等变、群上权重共享实现离散旋转等变，近似 SE(2)/E(2)/SE(3)/E(3) 等变；去掉 softmax 可得线性时间的动态群卷积。支持 CIFAR-10、ImageNet、QM9、OMol25、ScanObjectNN 基准，面向几何深度学习研究者。需要 Python 3.12+、PyTorch 2.3+，GPU 支持需 CUDA 12.1+，FlashAttention-2/3 为可选后端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于柏拉图固体对称群的等变注意力，不改注意力机制、不增额外计算开销
- 选择平凡群即退化为标准 Transformer
- 去掉 softmax 得到线性时间内容感知群卷积
- 覆盖 CIFAR-10/QM9/OMol25/ScanObjectNN 基准与力场训练（能量/力回归）

## 适用场景

- 复现论文中图像分类、3D 识别与分子性质预测实验
- 以 pip 包形式将等变注意力模块嵌入自己的 Transformer 代码
- 做群等变架构对比研究（四面体/八面体/二十面体等群选择）

## 场景标签

 · 领域:几何深度学习/分子建模

## 证据(README 行号)

> L16: **Platonic Transformers** provide a drop-in method to build geometric inductive biases into the standard Transforme
> L21: - **Cross-domain applicability.** Competitive results across CIFAR-10 (images), ScanObjectNN (3D), QM9 & OMol25 (mo
> L30: - 🧪 **OMol25 Force-Field Training** — Energy/force regression with element references, charge/spin conditioning, EM

## 星数曲线

```mermaid
xychart-beta
    title "niazoys/PlatonicTransformers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-26 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4423d9f6ffee` · [字段定义](../../DATASET.md)*
