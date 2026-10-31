# sbelharbi/bah-dataset

⭐ 13 · Python · BSD-3-Clause · 推送 2026-09-17 · [GitHub](https://github.com/sbelharbi/bah-dataset) · [官网](https://sbelharbi.github.io/bah-dataset) · 组织维护

**视频中的矛盾/犹豫情绪识别数据集及 PyTorch 基准代码**

面向数字行为干预场景的多模态情感计算数据集：BAH 含 1,427 段视频（10.60 小时）、300 名加拿大参与者通过网页平台用摄像头与麦克风回答 7 个诱发矛盾/犹豫（A/H）情绪的问题；由三位专家标注时间戳及帧级/视频级 A/H 线索，并提供转写文本、裁剪对齐人脸与参与者元数据。附 PyTorch 2.2.2 代码，支持视觉（vision）、音频（vggish）、文本（bert）三种模态，覆盖帧级/视频级监督分类、零样本预测与基于域适应的个性化基准实验；需自行下载数据集与预训练权重，预处理流程分块进行。代码基于 ABAW3 仓库修改。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1,427 段视频、300 名参与者、10.60 小时，含 1.79 小时 A/H 标注
- 三位专家提供时间戳级与帧/视频级标注，附转写与人脸数据
- 支持 vision/vggish/bert 三模态的帧级与视频级基准实验
- 提供监督学习数据划分、零样本与域适应个性化实验代码

## 适用场景

- 训练多模态模型识别视频中的矛盾/犹豫情绪
- 为情感计算与数字健康干预研究提供基准数据集
- 复现或改进 A/H 识别的多模态融合与时序建模方法

## 场景标签

 · 领域:情感计算/数字健康

## 证据(README 行号)

> L47: This paper introduces the Behavioural Ambivalence/Hesitancy (*BAH*) dataset
> L58: Additionally, this paper includes benchmarking results using baseline models on

## 星数曲线

```mermaid
xychart-beta
    title "sbelharbi/bah-dataset 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a616f9bcbda3` · [字段定义](../../DATASET.md)*
