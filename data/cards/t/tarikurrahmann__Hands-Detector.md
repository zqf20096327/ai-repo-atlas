# tarikurrahmann/Hands-Detector

⭐ 17 · Python · MIT · 推送 2026-07-24 · [GitHub](https://github.com/tarikurrahmann/Hands-Detector) · 个人维护

**实时手部 21 关键点检测与左右手分类的视觉管线**

基于 MediaPipe HandDetector 与 OpenCV/cvzone 的手部追踪项目：在图像或视频流中检测 21 个手部关键点，估计左右手归属并在实时窗口叠加可视化标签。视频源解析器按顺序查找 hands.mp4、video/hands.mp4 或 CLI 提供的路径，找不到时回退到 Webcam 0。面向手势识别、手语检测、交互系统等视觉应用的开发者，以 Python 脚本形式运行。

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

- 实时检测并渲染 21 个手部关键点
- 按检测手型或中心位置分类 Left/Right 手
- 视频源自动解析：本地文件→CLI 路径→摄像头回退
- MIT 许可，接受贡献（手势识别、虚拟鼠标等列为待办方向）

## 适用场景

- 在视频或摄像头画面中追踪手部关键点
- 为手势识别或手语检测项目做基础检测
- 构建基于视觉的人机交互原型

## 场景标签

`图像视频处理` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L22: `Hands_detector` tracks 21 hand landmarks in real time using a MediaPipe-based `HandDetector`. It estimates Left vs
> L30:  - Detects and renders hand joints with cvzone/MediaPipe-style precision


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `c244cb7edb90` · [字段定义](../../DATASET.md)*
