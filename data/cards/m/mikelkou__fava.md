# mikelkou/fava

⭐ 43 · Jupyter Notebook · MIT · 推送 2026-10-12 · [GitHub](https://github.com/mikelkou/fava) · 组织维护

**用变分自编码器从组学数据构建蛋白质关联网络的方法**

FAVA 基于 Variational Autoencoder 从单细胞 RNA 测序（scRNA-seq）、蛋白质组学等组学数据构建蛋白质关联网络，旨在缓解既有网络偏向被充分研究蛋白的问题。以 Python 库（favapy）形式提供，支持 AnnData 对象和计数/丰度矩阵输入，另带命令行接口（favapy 命令指定输入输出路径，可选 tsv/csv 格式参数），文档含 notebook 使用示例，可引用其 BiorXiv 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 VAE 从 scRNA-seq/蛋白质组学数据构建蛋白质网络
- 支持 AnnData 对象与计数/丰度矩阵两种输入
- 提供 Python 库与命令行两种使用方式
- 减少既有网络对已被充分研究蛋白的偏向

## 适用场景

- 从自己的单细胞或蛋白质组数据构建蛋白质关联网络
- 为研究不足的蛋白寻找功能关联线索
- 在 notebook 或 CLI 中批量处理组学数据

## 场景标签

 · 领域:生物信息学/蛋白质组学

## 证据(README 行号)

> L1: # fava FAVA: Functional Associations using Variational Autoencoders
> L8: FAVA is a method used to construct protein networks based on omics data such as single-cell RNA sequencing (scRNA-se

## 星数曲线

```mermaid
xychart-beta
    title "mikelkou/fava 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-28 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `459619a9015e` · [字段定义](../../DATASET.md)*
