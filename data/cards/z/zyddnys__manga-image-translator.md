# zyddnys/manga-image-translator

⭐ 10,636 · Python · GPL-3.0 · 推送 2026-11-18 · [GitHub](https://github.com/zyddnys/manga-image-translator) · [官网](https://cotrans.touhou.ai/) · 个人维护 · 中文 README

**一键翻译漫画等各类图片内文字的工具**

面向难以获得专业翻译的图片（群聊、图板上的漫画/图像）的文字翻译工具： pipeline 包含文字检测、OCR、翻译、图像修复（去字）与排版渲染。主要支持日语，也支持简繁中文、英语等 20 余种小语种。提供本地批处理、Web 服务、API、WebSocket 多种运行模式，模型在运行时自动下载到 ./models 目录。安装方式为 pip/venv 或 Docker 镜像（约 15GB）；部分依赖需编译，Windows 需先装 C++ Build Tools；GPU 加速需安装对应 PyTorch/CUDA 版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 检测+OCR+翻译+修复+排版的一体化图像翻译管线
- 支持本地批处理、Web、API、WebSocket 多种运行模式
- 提供在线演示站点与浏览器油猴脚本
- 模型运行时自动下载，Docker 镜像内置全部依赖与模型

## 适用场景

- 批量翻译无官方翻译的漫画图片
- 自建 Web/API 服务为图片提供翻译
- 翻译群聊或图板上的单张图像文字

## 场景标签

`图像视频处理` `OCR` · 领域:感知与多模态

## 证据(README 行号)

> L9: > One-click translation of text in various images\
> L13: This project aims to translate images that are unlikely to be professionally translated, such as comics/images on v
> L15: Supports image repair (text removal) and typesetting.

## 星数曲线

```mermaid
xychart-beta
    title "zyddnys/manga-image-translator 星数(近 28 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 10508 --> 10644
    line [10519, 10522, 10526, 10532, 10537, 10544, 10545, 10548, 10550, 10552, 10557, 10562, 10532, 10579, 10584, 10588, 10593, 10599, 10604, 10608, 10613, 10615, 10619, 10624, 10625, 10627, 10633, 10633]
```

2026-10-22 10,519 → 2026-11-24 10,633（+114）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `2d986bfd6834` · [字段定义](../../DATASET.md)*
