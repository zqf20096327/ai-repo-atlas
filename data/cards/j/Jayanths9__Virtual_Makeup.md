# Jayanths9/Virtual_Makeup

⭐ 65 · Python · 推送 2026-09-14 · [GitHub](https://github.com/Jayanths9/Virtual_Makeup) · 个人维护

**给人脸图像/摄像头实时添加虚拟彩妆的桌面应用与脚本**

基于 MediaPipe 面部关键点检测（478 点）与 OpenCV 的虚拟彩妆工具：在嘴唇、眼影、眼线、眉毛区域生成彩色掩膜并在 LAB 色彩空间混合。提供 PySide6 桌面应用（选色、预设、肤色/光照自适应、磨皮、背景虚化、前后对比）与 image.py、camera.py 两个命令行脚本。需 Python 3.11，支持 conda 或 pip 安装依赖，运行于 Windows/macOS/Linux。作者为不莱梅大学个人开发者。

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

- MediaPipe 478 点面部关键点定位，LAB 色彩空间混合妆容
- 按测得的肤色（冷暖底调）与亮度自适应调整妆色
- PySide6 桌面应用与两个命令行脚本（图像/摄像头）
- presets.json 可编辑预设，含磨皮与背景虚化

## 适用场景

- 在照片或摄像头画面上试不同妆容配色
- 实时直播/视频中虚拟上妆
- 通过编辑 presets.json 定制妆容预设

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: Adds virtual makeup (lips, eyeshadow, eyeliner and eyebrows) to a face in an image or a live webcam feed, using Medi
> L94: In this project Mediapipe [1] facial landmarks and opencv is used to add makeup on facial features.

## 星数曲线

```mermaid
xychart-beta
    title "Jayanths9/Virtual_Makeup 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-27 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `dcac9becd86e` · [字段定义](../../DATASET.md)*
