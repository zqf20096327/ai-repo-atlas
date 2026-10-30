# aertslab/CREsted

⭐ 84 · Python · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/aertslab/CREsted) · 组织维护

**基于 scATAC-seq 数据训练增强子深度学习模型的 Python 包**

面向单细胞基因组学研究的 Python 包：在 scATAC-seq 数据上训练序列深度学习模型，研究细胞类型特异性增强子编码，并支持在核苷酸分辨率下设计合成增强子序列。集成 scverse 框架，兼容主流 scATAC-seq 处理工具输出；提供峰值高度归一化等预处理技术与多种建模架构。基于 Keras 3，可选 TensorFlow 或 PyTorch 后端；预处理与数据导入功能无需深度学习后端。训练模型需安装相应 CUDA/cuDNN 支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 scATAC-seq 数据上训练增强子序列模型
- 细胞类型特异性、核苷酸分辨率的合成增强子序列设计
- 集成 scverse 框架，兼容主流 scATAC-seq 处理工具输出
- 基于 Keras 3，TensorFlow 与 PyTorch 后端可选

## 适用场景

- 训练模型捕捉特定细胞类型的增强子编码
- 设计细胞类型特异性的合成增强子序列
- 对 scATAC-seq 数据做峰值归一化等预处理与导入

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L12: **CREsted** (Cis-Regulatory Element Sequence Training, Explanation, and Design) is an easy-to-use deep learning pac
> L27: CREsted is built on top of Keras 3 and can therefore be used with your deep learning backend of choice (TensorFlow 

## 星数曲线

```mermaid
xychart-beta
    title "aertslab/CREsted 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 82 --> 85
    line [83, 84, 84]
```

2026-10-18 83 → 2026-10-30 84（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a83f8166ab7a` · [字段定义](../../DATASET.md)*
