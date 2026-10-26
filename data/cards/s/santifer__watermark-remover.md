# santifer/watermark-remover

⭐ 29 · Python · MIT · 推送 2026-01-29 · [GitHub](https://github.com/santifer/watermark-remover) · 个人维护

**用 YOLO 检测+LaMa 修补去除图片水印的 CLI 工具**

面向需要批量处理带水印图片的用户的命令行工具：YOLO 自动检测水印位置，LaMa 模型对水印区域进行图像修补重建，并提供 OpenCV 修补作为更快备选；当 YOLO 未检测到水印时回退到图像角落处理。以 git clone 源码方式安装，需 Python 3.10+ 与约 2GB 内存，LaMa 模型（约 200MB）首次使用时自动下载到 ~/.cache/torch/。提供置信度、padding、角落参数等选项，README 含英文与西班牙文双语。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLO 自动检测水印，无需手动配置
- LaMa inpainting 重建图像，另有 OpenCV 快速备选方法
- 未检测到时回退到图像角落处理（可配置角落位置与尺寸比例）
- LaMa 模型首次使用自动下载

## 适用场景

- 批量去除 LinkedIn 头像、图库素材等图片上的水印
- 对简单水印用 OpenCV 方法快速处理

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L5: > CLI tool to remove watermarks from images using artificial intelligence.
> L30: - **Automatic detection** with YOLO - detects watermarks without manual configuration
> L31: - **LaMa inpainting** - realistically reconstructs the image

## 星数曲线

```mermaid
xychart-beta
    title "santifer/watermark-remover 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `52728989c8d4` · [字段定义](../../DATASET.md)*
