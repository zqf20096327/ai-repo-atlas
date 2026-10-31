# Inupedia/anime-character-image-preprocessing

⭐ 37 · Python · MIT · 推送 2026-02-27 · [GitHub](https://github.com/Inupedia/anime-character-image-preprocessing) · 个人维护 · 中文 README

**动漫角色图片预处理工具：制作 Stable Diffusion 训练数据集**

Python 编写的角色图片预处理工具，通过背景透明化（rembg 多模型）、边界裁剪、基于人脸检测的智能裁剪（YOLO/OpenCV Cascade）、WD Tagger 生成 Booru 风格标签、Real-ESRGAN 4× 超分放大等功能，将角色图片转换为适合模型训练的数据集；另含按画师 ID 或关键词的 Pixiv 下载器（需配置 Cookie 与代理）。提供 Gradio Web UI 与 CLI 两种使用方式，支持混合命令串行执行多项任务。发布页提供 Windows/macOS/Linux 预构建可执行文件，也可用 uv 从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 种背景去除模型可选（推荐 isnet-anime 处理动漫角色）
- WD Tagger 生成可直接用于 Stable Diffusion 训练的 Booru 标签，置信度可调
- 基于人脸检测的智能裁剪，支持多人图自动分张
- Real-ESRGAN 动漫优化模型 4× 超分（约 2.4MB 自动下载）

## 适用场景

- 为训练角色 LoRA/模型批量准备打标与裁剪好的数据集
- 按画师 ID 或关键词从 Pixiv 下载作品素材
- 低分辨率图片裁剪后放大修复到 512×512 以上

## 场景标签

`图像视频处理` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L11: A Python-based character image preprocessing tool that transforms character images into a dataset suitable for trai

## 星数曲线

```mermaid
xychart-beta
    title "Inupedia/anime-character-image-preprocessing 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-31 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `ea0ca96c87d8` · [字段定义](../../DATASET.md)*
