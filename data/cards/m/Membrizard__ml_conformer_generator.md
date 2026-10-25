# Membrizard/ml_conformer_generator

⭐ 61 · JavaScript · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/Membrizard/ml_conformer_generator) · 组织维护

**给药物/化学研究者：按目标形状生成3D分子构象的扩散模型工具**

基于等变扩散模型（EDM）与图卷积网络（GCN）的空间感知分子生成工具：在形状约束（如蛋白结合口袋）下生成原子坐标与类型，GCN 预测邻接矩阵，再经标准化管线（片段选取、价键检查、RDKit 清洗、MMFF94 几何优化）输出化学有效分子。支持目标引导的 RL 微调（兼容 REINVENT4 评分函数）、片段内绘与惯性片段匹配。提供 Python 包（pip，含 PyTorch 与免 torch 的 ONNX 后端）、npm 包、浏览器 Demo、Streamlit 应用；权重自动从 Hugging Face 下载。训练数据为 ChEMBL 中 15–39 重原子的 160 万化合物，限定 H/C/N/O/F/P/S/Cl/Br 元素。

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

- 形状约束下的 3D 分子生成（EDM 生成坐标与原子类型，GCN 预测邻接矩阵）
- RL 微调引导生成，评分函数可自定义且兼容 REINVENT4
- 提供 PyTorch 与免 torch 的 ONNX 双后端及 npm/浏览器端推理
- 权重自动从 Hugging Face 解析下载，含蒸馏小模型（更低显存）

## 适用场景

- 按蛋白结合口袋形状生成新分子做配体设计或骨架跃迁
- 固定子结构后补全/生长分子的其余部分
- 用自定义性质评分函数做 RL 微调筛选候选分子

## 场景标签

 · 领域:计算化学/药物设计

## 证据(README 行号)

> L7: is a tool for spatially-aware molecule generation with an Equivariant Diffusion Model (EDM)
> L121: - **Equivariant Diffusion Model (EDM) [[1]](https://doi.org/10.48550/arXiv.2203.17003)**: For generating atom coor

## 星数曲线

```mermaid
xychart-beta
    title "Membrizard/ml_conformer_generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-25 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d0d436dd0e86` · [字段定义](../../DATASET.md)*
