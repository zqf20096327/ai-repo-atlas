# mkang315/CST-YOLO

⭐ 76 · Python · GPL-3.0 · 推送 2026-09-22 · [GitHub](https://github.com/mkang315/CST-YOLO) · 个人维护

**ICIP 2024 论文 CST-YOLO 官方代码：基于改进 YOLOv7 与 CNN-Swin Transformer 的血细胞检测**

论文《CST-YOLO: A Novel Method for Blood Cell Detection Based on Improved YOLOv7 and CNN-Swin Transformer》（ICIP 2024 口头报告）的官方 PyTorch 实现，面向计算机视觉与医学图像研究者。模型基于 YOLOv7 改进，引入 CNN-Swin Transformer，网络配置文件为 cst-yolo.yaml。在 BCCD、CBC、BCD 三个血细胞检测数据集上训练与评估，检测红细胞、白细胞与血小板。通过 pip 安装依赖，支持单卡与多卡分布式训练及测试脚本，需 Python>=3.8、Torch<=1.7.1、CUDA<=11.1。GPL-3.0 许可，部分工具代码基于 YOLOv7 与 Swin Transformer 仓库。

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

- 改进 YOLOv7 融合 CNN-Swin Transformer 的血细胞检测模型
- 在 BCCD/CBC/BCD 三个数据集上训练评估，检测 RBC/WBC/血小板三类细胞
- 提供单 GPU 与多 GPU 分布式训练及测试命令
- README 提供多种引用格式（IEEE/APA/BibTeX 等）

## 适用场景

- 复现论文的血细胞检测实验结果
- 作为血细胞检测任务的模型基础进行二次研究
- 在 CBC/BCCD 等医学图像数据集上训练检测模型

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L8: This is the source code for the paper titled "CST-YOLO: A Novel Method for Blood Cell Detection Based on Improved YO
> L40: We trained and evaluated CST-YOLO on three blood cell detection datasets Blood Cell Count and Detection (BCCD), Com

## 星数曲线

```mermaid
xychart-beta
    title "mkang315/CST-YOLO 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-25 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `582d39a18a01` · [字段定义](../../DATASET.md)*
