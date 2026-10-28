# mrzaizai2k/VIETNAMESE_LICENSE_PLATE

⭐ 38 · Python · MIT · 推送 2025-11-14 · [GitHub](https://github.com/mrzaizai2k/VIETNAMESE_LICENSE_PLATE) · 个人维护

**越南停车场车牌识别程序（KNN+OpenCV，1/2 行车牌）**

用于停车场场景的越南车牌识别程序，支持单行与双行车牌。流程分三步：车牌检测（灰度化、Top Hat/Black Hat 对比度增强、高斯滤波、自适应阈值、Canny 边缘检测、轮廓筛选）、字符分割（透视校正旋转、按高宽比与面积过滤轮廓）、字符识别（KNN，字符归一化为 20x30 像素，人工标注生成 classifications.txt 与 flattened_images.txt 数据文件）。提供图像与视频测试脚本，需按 requirements.txt 安装依赖。README 附实测指标：车牌检出率单行 49.2%、双行 39.3%，字符完全识别率约 31-33%，并列出反光、多角度等失败原因。refactor 分支含车牌管理网站。作者为 YouTube 教程频道。

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

- 车牌检测→字符分割→KNN 字符识别三段式流程
- 支持越南单行与双行车牌
- GenData.py 生成 KNN 训练数据（人工按键标注）
- README 附检出率与字符识别错误率实测表格

## 适用场景

- 我需要在停车场场景识别越南车牌
- 我想学习 OpenCV 传统图像处理做车牌识别的完整流程
- 我想参考 KNN 做字符识别的教学实现

## 场景标签

`OCR` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L13: This project using the machine learning method called KNN and OpenCV, which is a powerful library for image process
> L34: 1. License Plate Detection

## 星数曲线

```mermaid
xychart-beta
    title "mrzaizai2k/VIETNAMESE_LICENSE_PLATE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-28 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `423949cc9453` · [字段定义](../../DATASET.md)*
