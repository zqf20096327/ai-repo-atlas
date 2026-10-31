# cskonopka/broadcast-research

⭐ 13 · Python · 推送 2026-03-02 · [GitHub](https://github.com/cskonopka/broadcast-research) · [官网](https://cskonopka.gitbook.io/broadcast-research) · 个人维护

**模拟视频素材的数据挖掘研究项目：生成分析数据池**

个人研究项目：作者自 2015 年起录制模拟视频合成器创作内容，按年份/日期目录框架（edits/raw）归档，用 Go 程序调用 FFmpeg/FFprobe 与 ImageMagick 对素材做两类处理——生成 png/jpg/gif/直方图等派生内容，以及输出每月 CSV 分析文件（视频元数据与图像统计量），合并为主数据文件。项目目标是以此构建开源数据池，并计划应用机器学习与 NLP 研究创作过程的心理趋势。需自行编译 Go 程序，依赖 FFmpeg、ImageMagick 等系统工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以年度/日期目录框架归档模拟视频源素材
- Go 程序调用 FFmpeg 生成 png/jpg/gif 派生内容
- FFprobe 与 ImageMagick identify 输出每月 CSV 分析文件（视频元数据、图像统计量）
- 各 CSV 文件无表头，字段定义记录于各数据集 README

## 适用场景

- 对个人视频素材库做系统化的元数据提取与归档
- 为艺术创作过程研究构建可分析的数据池
- 批量生成视频的缩略图、帧图与直方图

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L4: *broadcast-research* is a data project that explores the potential of analog video synthesis as a new content source
> L54: Design data-mining programs intended to generate content and analysis files using source content from the edits fol

## 星数曲线

```mermaid
xychart-beta
    title "cskonopka/broadcast-research 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `295fc1c06ff3` · [字段定义](../../DATASET.md)*
