# aapupu/MIST

⭐ 19 · Jupyter Notebook · GPL-3.0 · 推送 2026-06-09 · [GitHub](https://github.com/aapupu/MIST) · 组织维护

**单T细胞转录组与受体联合分析的深度学习框架**

基于 PyTorch 的变分自编码类框架 MIST，用于单 T 细胞 scRNA-seq 与 scTCR-seq 数据的联合建模，也支持 RNA-only、TCR-only 及蛋白（ADT）数据输入。提供 Python API 与命令行两种使用方式，输出训练模型（model.pt）与可被 scanpy/scirpy 继续分析的 AnnData 对象。含质控过滤、批处理、潜空间维度等训练参数，CUDA 可用时自动启用 GPU。推荐 Python 3.8 与 scirpy 0.12.0，方法发表于 Science Advances 2025。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- scRNA-seq 与 scTCR-seq 联合建模（joint/rna/tcr 三种模式）
- 支持 h5ad、10X、tracer、BD 等多种数据格式输入
- 输出 AnnData 对象，可用 scanpy/scirpy 后续分析
- 提供 Python API 与命令行两种使用方式

## 适用场景

- 对单 T 细胞转录组与 TCR 受体做联合表征学习
- 将训练结果接入 scanpy/scirpy 生态做下游分析
- 批量处理多样本、多批次的 T 细胞测序数据

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L2: MIST: an interpretable and flexible deep learning framework for single-T cell transcriptome and receptor analysis
> L28: adata, model = MIST(rna_path, tcr_path, batch, rna_data_type, tcr_data_type, type)

## 星数曲线

```mermaid
xychart-beta
    title "aapupu/MIST 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d61d45ab33d4` · [字段定义](../../DATASET.md)*
