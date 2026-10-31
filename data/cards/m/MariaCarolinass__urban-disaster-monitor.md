# MariaCarolinass/urban-disaster-monitor

⭐ 14 · Jupyter Notebook · MIT · 推送 2026-10-29 · [GitHub](https://github.com/MariaCarolinass/urban-disaster-monitor) · [官网](https://huggingface.co/spaces/carolinasoares/urban-disaster-monitor-v2) · 组织维护

**城市灾害场景目标检测系统与数据集：识别平民、救援者与动物**

面向洪水、结构坍塌、山体滑坡等城市灾害场景的计算机视觉项目：提供 3,240 张多标签标注图像的六类数据集（平民、救援者、牛、马、狗、猫，含 832 张 AI 生成的合成图像），并训练 YOLOv26 与 RF-DETR 两个检测器家族共六个变体，权重托管在 Hugging Face，通过 Gradio 界面上传图像/视频并选择模型变体进行检测。项目源于 UFRN 计算机视觉课程，为 Smart Metropolis 的 SPICI 项目志愿开发，救援者类别用于减少仅救援队区域的误报。

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

- 3,240 张图像、6 类多标签灾害场景数据集（CC BY 4.0）
- 832 张 Gemini 2.5 Flash Image 生成的合成图像经人工审核
- YOLOv26 n/s/m/l 与 RF-DETR Nano/Medium 六个训练变体
- Gradio 交互界面，权重从 Hugging Face 自动下载

## 适用场景

- 救援团队在灾害现场图像/视频中检测平民、救援者与动物
- 灾害管理平台按类别减少救援队区域的误报
- 研究者基于该数据集训练或对比灾害场景检测模型

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L30: **Urban Disaster Monitor** is a computer vision system for detecting and classifying **individuals** (Civilians and
> L36: - Interactive **Gradio** interface for uploading and testing images and videos
> L151: The interface lets users select the model family and variant before processing an image or video; weights are down

## 星数曲线

```mermaid
xychart-beta
    title "MariaCarolinass/urban-disaster-monitor 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `ffff5d1749ad` · [字段定义](../../DATASET.md)*
