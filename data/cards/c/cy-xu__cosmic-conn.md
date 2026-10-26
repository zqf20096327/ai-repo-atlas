# cy-xu/cosmic-conn

⭐ 29 · Python · GPL-3.0 · 推送 2026-04-06 · [GitHub](https://github.com/cy-xu/cosmic-conn) · 个人维护

**给天文学家的宇宙线检测深度学习框架、数据集与工具集**

面向 CCD 天文图像中宇宙线（CR）检测问题的端到端方案，包含 PyTorch 深度学习框架、预训练 CR 检测模型、由 LCO 全球望远镜网络 23 台仪器超 4,500 张科学图像组成的标注数据集（LCO CR dataset），以及命令行工具、Web 交互式掩码可视化编辑应用与 Python API。支持地面/空间成像与光谱观测数据，可处理 FITS 文件批量检测，也可用 LCO CR 数据集训练新模型。以 Python 包形式通过 pip/uv 安装，PyTorch 需指定 cpu 或 cuda extra 显式安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LCO CR 数据集：23 台仪器、超 4,500 张标注科学图像
- PyTorch 训练框架，覆盖地面/空间成像与光谱观测的通用 CR 检测模型
- 命令行批量处理 FITS 文件与 Python API 集成到数据流水线
- Web 应用支持 CR 掩码实时可视化与编辑

## 适用场景

- 批量检测天文 CCD 图像中的宇宙线污染
- 在数据还原流水线中通过 Python API 集成 CR 检测
- 用 LCO CR 数据集训练适应自己观测设备的 CR 检测模型

## 场景标签

`目标检测` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L13: Cosmic-CoNN is an end-to-end solution to help tackle the cosmic ray (CR) detection problem in CCD-captured astronom
> L17: 2. A PyTorch deep-learning framework that trains generic, robust CR detection models for ground- and space-based im

## 星数曲线

```mermaid
xychart-beta
    title "cy-xu/cosmic-conn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7bcdc0de9ca1` · [字段定义](../../DATASET.md)*
