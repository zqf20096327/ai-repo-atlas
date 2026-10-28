# skhalidmahmud/Gesture-to-Speech

⭐ 19 · Python · MIT · 推送 2026-05-08 · [GitHub](https://github.com/skhalidmahmud/Gesture-to-Speech) · 个人维护

**实时手语转语音翻译器：摄像头识别手势并转为文字与语音**

面向听障沟通场景的原型项目：通过摄像头采集画面，MediaPipe 检测每只手 21 个关键点，OpenCV 处理与绘制视频流；将 30 帧手部关键点序列输入自训练的 LSTM 模型，置信度超过 80% 时输出识别词汇，翻译为文字与音频。前端为 React.js 面板。README 以开发日志形式记录进展，项目自述处于活跃开发中，目前训练数据仅覆盖 HELLO 与 THANKS 两个手势，未提供安装命令或部署说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- MediaPipe 实时手部关键点检测（每手 21 点）
- LSTM 网络基于 30 帧关键点序列识别手势，置信度阈值 80%
- OpenCV 处理摄像头画面并绘制骨架
- React.js 前端面板

## 适用场景

- 听障人士与不熟悉手语者的实时沟通辅助
- 摄像头手语识别的学习原型与二次开发参考

## 场景标签

 · 领域:计算机视觉/人机交互

## 证据(README 行号)

> L6: The app uses a webcam to track hand gestures in real-time. Using a custom TensorFlow model, it recognizes specific s
> L49: The app maintains a 30-frame buffer of hand landmarks. Every time a new frame comes in, the 30-frame sequence is pa

## 星数曲线

```mermaid
xychart-beta
    title "skhalidmahmud/Gesture-to-Speech 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `236de194a44a` · [字段定义](../../DATASET.md)*
