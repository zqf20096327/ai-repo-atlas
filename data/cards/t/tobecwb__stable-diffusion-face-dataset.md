# tobecwb/stable-diffusion-face-dataset

⭐ 44 · CC-BY-4.0 · 推送 2026-10-09 · [GitHub](https://github.com/tobecwb/stable-diffusion-face-dataset) · 个人维护

**Stable Diffusion 生成的男女面部正则化图像数据集**

预渲染的男女面部图像数据集，共约 1500 张，由 Stable Diffusion 1.5（512px）、2.1（768px）和 SDXL 1.0（1024px）基础模型生成，未使用 LORA，目标是无特定风格、尽可能写实的人脸照片。生成后经人工筛选与后处理：Photoshop Neural Filter 编辑、GFPGAN 1.3/1.4 与 ESRGAN 增强，并训练 YOLOv8 分割模型自动生成面部区域掩码；有缺陷手部的图像被剔除。图像以 CC-BY-4.0 许可发布。作者说明因租用服务器成本与个人硬件限制，后续大规模更新可能性低。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC-BY-4.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 约 1500 张经人工筛选与后处理的写实人脸图像
- 由 SD 1.5 / 2.1 / SDXL 1.0 基础模型生成，含三种分辨率
- 后处理流程含 GFPGAN、ESRGAN 增强与自训 YOLOv8 面部分割掩码
- 图像以 CC-BY-4.0 许可发布

## 适用场景

- DreamBooth 或 Textual Inversion 训练时用作正则化图像
- 为写实风格人脸生成任务提供参照数据

## 场景标签

 · 领域:图像生成/数据集

## 证据(README 行号)

> L1: # Stable Diffusion Face Dataset
> L2: Images of men and women, mainly faces, seeking to generate more realistic images (without wax skin), generated with 

## 星数曲线

```mermaid
xychart-beta
    title "tobecwb/stable-diffusion-face-dataset 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-30 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3d5afcf10974` · [字段定义](../../DATASET.md)*
