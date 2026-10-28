# Alexandre-Delplanque/HerdNet

⭐ 58 · Python · MIT · 推送 2026-10-12 · [GitHub](https://github.com/Alexandre-Delplanque/HerdNet) · 个人维护

**面向非洲哺乳动物的航拍图像检测与计数深度学习模型**

ISPRS 论文 "From Crowd to Herd Counting" 的官方代码：实现 HerdNet 模型，在航拍影像中检测并计数非洲哺乳动物（骆驼、大象、水牛等多个物种）。提供基于 animaloc 库的训练与评估流程，支持点标注与边界框两种 CSV 数据集格式，附带两个预训练权重（18M 参数，代码 MIT 许可、权重 CC BY-NC-SA-4.0 仅限学术用途）。工具链含补丁切分、Hydra 配置驱动的训练/测试、FiftyOne 可视化与推理导出 CSV 检测结果。通过 conda 环境安装，训练与推理依赖 CUDA。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 航拍影像多物种哺乳动物检测与计数（两个预训练模型）
- 支持点标注与边界框两种 CSV 数据集格式
- Hydra 配置驱动的训练/测试工具与 FiftyOne 可视化
- 推理工具输出检测 CSV、标注图与动物缩略图

## 适用场景

- 在非洲航拍调查影像中检测并计数野生哺乳动物
- 用自己的航拍数据训练动物检测计数模型
- 生态调查中批量生成物种检测结果与可视化

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L4: Code for paper "From Crowd to Herd Counting: How to Precisely Detect and Count African Mammals using Aerial Imagery 
> L26: |HerdNet|18M|Ennedi 2019|Desert, xeric shrubland and grassland|Camel, donkey, sheep and goat|73.6%|6.1|9.8|15.8%|PT

## 星数曲线

```mermaid
xychart-beta
    title "Alexandre-Delplanque/HerdNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-18 58 → 2026-10-28 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3d948aecf85b` · [字段定义](../../DATASET.md)*
