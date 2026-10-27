# DeepPythonist/EmotionTracker

⭐ 37 · Python · MIT · 推送 2026-07-13 · [GitHub](https://github.com/DeepPythonist/EmotionTracker) · 个人维护

**本地实时情绪检测桌面应用：摄像头识别情绪并存 CSV**

基于 Python 与 DeepFace 的桌面应用，通过摄像头实时识别用户面部情绪，以 Tkinter 三标签页界面（控制/监控/分析）展示当前情绪、置信度与会话统计，并按日自动生成带时间戳的 CSV 时序数据，可查看情绪分布饼图与汇总统计。所有数据本地存储，不联网传输；首次运行需联网下载模型。性能上每 3 帧处理一次、640x480 缩放、线程分离 UI 与处理以降低 CPU 负载。

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

- DeepFace 摄像头实时情绪识别，置信度低于 0.5 标记为 uncertain
- 按日自动写入 CSV（timestamp/emotion/confidence）
- 三标签页界面与情绪分布饼图、汇总统计
- 本地处理，不做网络传输；每 3 帧处理一次优化 CPU 占用

## 适用场景

- 记录我每天的情绪变化并导出 CSV 分析
- 在本地做实时的摄像头情绪监测
- 查看历史某天的情绪分布统计

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L5: A professional Python desktop application for real-time facial emotion detection using DeepFace. The application ana
> L15: - **Real-time Emotion Detection**: Uses DeepFace for accurate emotion recognition

## 星数曲线

```mermaid
xychart-beta
    title "DeepPythonist/EmotionTracker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-27 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `47adda1d6d80` · [字段定义](../../DATASET.md)*
