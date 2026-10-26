# mesutpiskin/id-card-detector

⭐ 332 · Python · MIT · 推送 2026-05-16 · [GitHub](https://github.com/mesutpiskin/id-card-detector) · 个人维护

**深度学习身份证件信息区域检测与 OCR 工具**

基于 TensorFlow 2 SavedModel（Faster R-CNN 系）的证件信息区域（ROI）检测项目：对身份证/驾照图片或摄像头画面执行目标检测与分类，裁剪 ROI 并可选调用 EasyOCR 提取姓名、出生日期等文字。提供图像与摄像头两个 CLI 脚本，支持按分数阈值过滤与快照面板按键 OCR；YOLO（ultralytics）为可选后端。按平台给出分体 requirements 安装方式，需本地放置 SavedModel 与 labelmap 文件；另有需 Python 3.7/TF 1.15 的遗留流程。

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

- TF2 SavedModel 检测 + EasyOCR 可选 OCR 的证件信息提取流水线
- 图像与摄像头两种运行脚本，摄像头模式支持 9 张快照按键 OCR
- 可选切换 YOLO（ultralytics）后端替代 TF2 检测器
- 按平台（Apple Silicon/Intel/Linux/Windows）提供安装文件

## 适用场景

- 从证件照片中定位并裁剪姓名、出生日期等信息区域
- 接入摄像头实时检测证件并按需 OCR 提取文字
- 作为证件 OCR 前端的 ROI 检测组件复用

## 场景标签

`目标检测` `OCR` · 领域:感知与多模态

## 证据(README 行号)

> L5: You can use this project to extract information DOB (name, surname, date of birth, etc.) on the identity card. To do
> L11: This project can do object detection + object classification + multiple object detection all at the same time.

## 星数曲线

```mermaid
xychart-beta
    title "mesutpiskin/id-card-detector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 331 --> 333
    line [332, 332]
```

2026-10-18 332 → 2026-10-26 332（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `78fadc7fc8f1` · [字段定义](../../DATASET.md)*
