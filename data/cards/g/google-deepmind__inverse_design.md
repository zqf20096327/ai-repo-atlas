# google-deepmind/inverse_design

⭐ 29 · Python · Apache-2.0 · 推送 2026-03-04 · [GitHub](https://github.com/google-deepmind/inverse_design) · 组织维护

**流体结构逆向设计代码：图网络模拟器重定向水流**

NeurIPS 2022 论文的官方代码与参数：提供 JAX 实现的 Encode-Process-Decode 图网络架构、在 3D WaterCourse 环境训练的模型权重，以及通过梯度优化地形来重定向水流的逆向设计示例。可在 Google Colab 中直接运行，或本地克隆仓库、安装 requirements 并从 Google Cloud 下载模型权重后用 Jupyter notebook 运行 demo_design_optimization.ipynb。面向研究人员复现论文或进行流体结构交互的逆向设计实验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Encode-Process-Decode 图网络架构的 JAX 实现
- 提供在 3D WaterCourse 环境训练的模型权重
- 基于梯度的地形优化示例，用于重定向水流

## 适用场景

- 复现 NeurIPS 2022 逆向设计论文
- 研究生成式模型在流体结构交互设计中的应用
- 基于预训练图网络模拟器做地形优化实验

## 场景标签

 · 领域:科学计算/物理模拟

## 证据(README 行号)

> L9: The code here provides an implementation of the Encode-Process-Decode
> L11: on the 3D WaterCourse environment, and an example of performing gradient-based

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/inverse_design 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `a77d062c3cc6` · [字段定义](../../DATASET.md)*
