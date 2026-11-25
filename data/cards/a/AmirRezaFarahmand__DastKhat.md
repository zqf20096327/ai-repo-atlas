# AmirRezaFarahmand/DastKhat

⭐ 10 · Python · MIT · 推送 2026-09-15 · [GitHub](https://github.com/AmirRezaFarahmand/DastKhat) · 个人维护

**给波斯语手写识别研究者提供的开源句子级手写数据集**

面向 OCR 与手写文本识别（HTR）研究构建的波斯语手写数据集：收集多位书写者的句子级手写图像，附带文本标注与元数据，以 CSV 存储句子表与样本表（含 sample_id、participant_id、ground truth、split）。数据发布于 Hugging Face；仓库含图像预处理、元数据生成、校验等脚本，通过网页表单征集书写样本。当前版本 v0.1 含 8 名书写者、560 个样本、700 条预设句子，MIT 许可。

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

- 句子级标注的波斯语手写数据集，公开托管于 Hugging Face
- v0.1 版本含 8 名书写者、560 个手写样本、700 条预设句子
- 提供图像预处理、元数据生成、数据校验等处理脚本
- 推荐 CER/WER/序列准确率作为评估指标

## 适用场景

- 训练和评估波斯语手写文本识别模型
- 开展书写者识别与笔迹风格分析实验
- 作为计算机视觉与文档理解研究的训练数据

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L9: DastKhat is an open-source Persian handwritten text dataset created for **Optical Character Recognition (OCR)** and 
> L13: The project focuses on collecting, processing, and publishing sentence-level handwritten Persian data to help resea

## 星数曲线

```mermaid
xychart-beta
    title "AmirRezaFarahmand/DastKhat 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-25"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-23 10 → 2026-11-25 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `437b7943bafd` · [字段定义](../../DATASET.md)*
