# zae-bayern/elpv-dataset

⭐ 312 · Python · NOASSERTION · 推送 2026-07-21 · [GitHub](https://github.com/zae-bayern/elpv-dataset) · 组织维护

**太阳能电池 EL 图像缺陷基准数据集（2,624 张带标注）**

提供从 44 块光伏组件的高分辨率电致发光（EL）图像中提取的太阳能电池片数据集：2,624 张 300x300 像素 8 位灰度图，覆盖正常与缺陷电池。每张图像标注缺陷概率（0-1 浮点值）及电池片来源组件类型（单晶/多晶），图像已做尺寸、视角归一化并消除镜头畸变。以 Python 包形式分发，pip 安装后可通过 load_dataset() 一次性载入图像与标注。用于视觉缺陷识别研究的基准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 2,624 张 300x300 灰度 EL 电池片图像，来自 44 块组件
- 每张标注缺陷概率与组件类型（单晶/多晶）
- 图像已归一化并消除镜头畸变
- pip 安装 Python 包，load_dataset() 一行载入

## 适用场景

- 训练和评估太阳能电池缺陷视觉分类模型
- 光伏组件 EL 图像缺陷检测研究的基准数据
- 学术发表中引用的标准化数据集

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L6: This repository provides a dataset of solar cell images extracted from
> L14: The dataset contains 2,624 samples of 300x300 pixels 8-bit grayscale images of

## 星数曲线

```mermaid
xychart-beta
    title "zae-bayern/elpv-dataset 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 310 --> 313
    line [311, 312, 312]
```

2026-10-18 311 → 2026-10-24 312（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `525006c4eefc` · [字段定义](../../DATASET.md)*
