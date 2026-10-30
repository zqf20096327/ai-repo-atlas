# univieCUBE/deepnog

⭐ 30 · Python · BSD-3-Clause · 推送 2025-12-16 · [GitHub](https://github.com/univieCUBE/deepnog) · 组织维护

**用深度网络将蛋白质序列分配到直系同源组的工具**

读取 FASTA 等格式的蛋白质序列文件，用深度网络（DeepNOG、DeepFam 架构）预测其所属的直系同源组，支持 eggNOG 5.0 与 COG 2020 数据库，可在 CPU 或 GPU 上运行；也提供训练自定义模型的功能。模型文件因体积原因不随包发布，首次使用时自动下载到缓存目录（可用 DEEPNOG_DATA 环境变量修改）。提供 deepnog 命令行工具，可设置置信度阈值过滤预测结果。支持 Biopython SeqIO 列出的各种文件格式，但仅测试过 FASTA。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 深度网络预测蛋白质直系同源组（eggNOG 5.0、COG 2020）
- CPU 或 GPU 运行，提供 infer 与 train 两种命令
- 模型自动下载缓存，可设置信度阈值过滤预测
- 支持 DeepNOG 与 DeepFam 网络架构

## 适用场景

- 将蛋白质序列批量分配到 eggNOG/COG 直系同源组
- 为特定分类学层级训练自定义预测模型
- 以 CSV 输出带置信度的蛋白组预测结果

## 场景标签

 · 领域:生物信息学/蛋白质组学

## 证据(README 行号)

> L20: Assign proteins to orthologous groups (eggNOG 5) on CPUs or GPUs with deep networks.
> L51: Call the `deepnog` command line tool with a

## 星数曲线

```mermaid
xychart-beta
    title "univieCUBE/deepnog 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-30 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c9306b830530` · [字段定义](../../DATASET.md)*
