# northumber/person-autocrop

⭐ 16 · Python · 推送 2026-03-07 · [GitHub](https://github.com/northumber/person-autocrop) · 个人维护

**自动检测并裁剪照片中人物的 Python 脚本**

命令行 Python 脚本，使用 Tensorflow 与 SSD Mobilenet V2 (COCO) 模型识别照片中的人物并裁剪为单人照片。支持 .jpg/.jpeg/.png/.webp/.bmp 格式，多人物时生成多张照片，可批量处理输入文件夹，支持 GPU 计算与指定输出格式。提供 Windows/Linux 自动安装脚本（自动建虚拟环境、装依赖、下载模型），也可手动 pip 安装依赖运行。需 Python 3.10。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 SSD Mobilenet V2 (COCO) 的人物检测与裁剪
- 多人物照片自动拆分为多张单人照片
- 输入文件夹批量处理，支持 5 种图片格式
- Windows/Linux 自动安装脚本（自动建环境、下载模型）

## 适用场景

- 批量把含人物的照片裁剪为单人照
- 整理照片集中的人物肖像
- 在 GPU 上加速处理大量图片

## 场景标签

`目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L2: This is a Python script to auto-detect and auto-crop a person in a image.
> L4: This script uses **Tensorflow** and **SSD Mobilenet V2 (COCO)** to recognize people in a photo, then crop the photo 

## 星数曲线

```mermaid
xychart-beta
    title "northumber/person-autocrop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `26e39b8d4855` · [字段定义](../../DATASET.md)*
