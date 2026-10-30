# rybakov-ks/ParticleAnalyzer

⭐ 38 · Python · GPL-3.0 · 推送 2026-01-25 · [GitHub](https://github.com/rybakov-ks/ParticleAnalyzer) · [官网](https://particleanalyzer.ru) · 个人维护 · 中文 README

**电镜图像中纳米颗粒的自动分割与尺寸分析工具**

面向 SEM/TEM 图像的计算机视觉工具：使用 YOLOv11/12/26、RF-DETR Seg、Detectron2 等模型自动分割纳米颗粒，SAHI 滑窗模式处理高分辨率小颗粒，输出面积、周长、等效直径、Feret 直径等统计表与尺寸分布图，支持像素/微米双单位与比例尺标定。以 PyPI 包安装，通过浏览器界面运行，可选 LLM（OpenRouter/Hugging Face）解读 SEM 数据。无 CUDA GPU 时可用 CPU 运行但速度较慢。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模型支持：YOLOv11/12/26、RF-DETR Seg (Preview)、Detectron2
- SAHI 滑窗模式检测高分辨率图像中的小颗粒
- 面积/周长/Feret 直径等统计输出与分布可视化，像素与微米双单位
- 比例尺两点标定自动计算像素-微米换算
- 可选 LLM（OpenRouter/Hugging Face API key）解读 SEM 数据

## 适用场景

- 电镜图像中纳米颗粒的自动分割与粒径统计
- 高分辨率图像中小颗粒的滑窗检测
- 发表材料表征结果前生成颗粒尺寸分布数据

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L23:  A Computer Vision-Based Tool for Automatic Segmentation and Size Analysis of Nanoparticles in Scanning Electron Mi
> L48: - Automated particle segmentation in SEM images
> L53: - Supports multiple AI models: YOLOv11, YOLOv12, YOLOv26, RF-DETR Seg (Preview) and Detectron2

## 星数曲线

```mermaid
xychart-beta
    title "rybakov-ks/ParticleAnalyzer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-30 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1d536e2fd6d0` · [字段定义](../../DATASET.md)*
