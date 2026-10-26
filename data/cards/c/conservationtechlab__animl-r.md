# conservationtechlab/animl-r

⭐ 26 · R · NOASSERTION · 推送 2026-09-21 · [GitHub](https://github.com/conservationtechlab/animl-r) · 组织维护

**相机陷阱图像/视频动物自动识别的 R 机器学习包**

面向生态学研究者的 R 包，通过 reticulate 依赖 Python 版 animl-py 完成机器学习部分：构建文件清单、用 MegaDetector 目标检测器识别潜在动物、再用物种分类模型对裁剪图分类，支持图像与视频帧、序列分类算法，并可将结果导出为按预测分类的文件夹、camtrapR、COCO JSON 或 Timelapse CSV 格式。要求 R≥4.0、Python≥3.12 与 animl-py，经 CRAN 安装后需调用 animl_install() 配置环境，建议在配备专用 GPU 的计算机上运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MegaDetector 目标检测 + 物种分类器的两步识别流程
- 支持图像与视频帧，含序列分类算法
- 导出格式覆盖文件夹分类/camtrapR/COCO JSON/Timelapse CSV
- CRAN 提供 R 包安装，自动配置 Python 依赖

## 适用场景

- 批量自动识别相机陷阱影像中的动物物种
- 将识别结果整理为 camtrapR 或 Timelapse 可用的数据格式
- 处理含视频的野外监测数据的序列级分类

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: Animl comprises a variety of machine learning tools for analyzing ecological data. The package includes a set of fun
> L9: Below are the steps required for automatic identification of animals within camera trap images or videos.

## 星数曲线

```mermaid
xychart-beta
    title "conservationtechlab/animl-r 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-26 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b7802a44e177` · [字段定义](../../DATASET.md)*
