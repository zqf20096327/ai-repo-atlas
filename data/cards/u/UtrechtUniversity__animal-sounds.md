# UtrechtUniversity/animal-sounds

⭐ 14 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/UtrechtUniversity/animal-sounds) · [官网](https://utrechtuniversity.github.io/animal-sounds) · 组织维护

**检测野生动物录音中黑猩猩叫声的音频分类流水线**

乌得勒支大学开发的端到端音频分类 Python 包：包含音频预处理、特征提取、可选合成数据生成、分类器训练（SVM 与 CNN10/CNN12）、评估与预测，面向黑猩猩叫声检测设计，可适配其他有标注音频的物种。预训练 CNN10/CNN12 模型发布在 Hugging Face Hub，附独立 modeling.py 与 preprocess.py，可不装本包直接使用。要求 Python >=3.12，依赖 sklearn、torch、torchaudio 等；流水线以跨环境泛化为目标。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖预处理到预测的完整音频分类流水线，支持 SVM 与 CNN 两类分类器
- 预训练 CNN10/CNN12 黑猩猩叫声分类器发布于 Hugging Face Hub
- 提供可选合成数据生成以提升目标域鲁棒性
- 各模型仓库附独立 modeling.py 与 preprocess.py，无需安装本包即可推理

## 适用场景

- 在野生动物录音中自动检测黑猩猩叫声
- 基于自己标注的音频为其他物种适配训练分类器
- 直接下载预训练模型做跨环境叫声识别预测

## 场景标签

 · 领域:生物声学/生态监测

## 证据(README 行号)

> L5: This repository provides an end-to-end audio classification pipeline for detecting animal vocalizations in wildlife 
> L46: Trained CNN10 and CNN12 chimpanzee vocalization classifiers are published on Hugging Face Hub, ready to use without

## 星数曲线

```mermaid
xychart-beta
    title "UtrechtUniversity/animal-sounds 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2e97a5f1a062` · [字段定义](../../DATASET.md)*
