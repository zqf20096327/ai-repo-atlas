# KietzmannLab/pyavs

⭐ 14 · Python · MIT · 推送 2026-10-12 · [GitHub](https://github.com/KietzmannLab/pyavs) · [官网](https://www.kietzmannlab.uni-osnabrueck.de/avs/) · 组织维护

**Active Visual Semantics 脑科学数据集的配套 Python 工具包**

为 AVS 数据集（5 名被试、MEG+眼动+结构 MRI，自由浏览 4,080 张自然场景）提供配套的加载与分析工具：AVSComposer 高层入口完成 MEG 读取、ICA、滤波、分段及眼动事件对齐；另含源重建、注视物体提取、BIDS 术语转换与命令行工具。数据子集可经 open_remote() 从 AWS S3 免凭证按需下载，完整版仍在增量上传。依赖 MNE-Python，FreeSurfer 仅源重建时可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AVSComposer 一站式 MEG+眼动融合预处理与分段
- 200,000+ 注释 fixation/saccade 锁定 epoch 及逐注视 COCO 类别标签
- pyavs.open_remote() 免账号从 AWS S3 按需下载数据子集
- 涵盖源重建、RSA/encoding 分析脚本与 pytest 测试套件

## 适用场景

- 加载并预处理 AVS 数据集的 MEG 与眼动数据
- 做自由视觉条件下的脑编码或表征相似性分析
- 直接下载现成 FreeSurfer SUBJECTS_DIR 做源重建

## 场景标签

 · 领域:神经科学/脑成像数据

## 证据(README 行号)

> L8: **pyAVS** is the companion Python package for the **Active Visual Semantics (AVS) dataset**:
> L9: MEG, eye tracking, and structural MRI recorded while participants freely explored natural
> L23: |Stimuli|4,080 natural scenes from the Natural Scenes Dataset (NSD)|

## 星数曲线

```mermaid
xychart-beta
    title "KietzmannLab/pyavs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b0a258e67dc7` · [字段定义](../../DATASET.md)*
