# Hamna-Munir/MoodGuard-AI

⭐ 26 · Python · MIT · 推送 2026-05-24 · [GitHub](https://github.com/Hamna-Munir/MoodGuard-AI) · 个人维护

**面向心理健康监测的表情情绪识别 Web 应用**

基于 Flask 的 Web 应用：用 TensorFlow/Keras 训练的 CNN 模型（FER2013 数据集，35K+ 训练图，7 类情绪，模型精度 66.6%）对上传图片、拍摄照片或摄像头实时画面做人脸情绪检测，OpenCV 负责人脸检测与图像预处理，Flask 加载 .h5 模型本地推理，不向外部服务器发送面部数据。提供照片分析、实时检测、检测历史与仪表盘界面。需手动放置模型文件 moodguard_model.h5 后运行，摄像头检测需浏览器授权。

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

- CNN 模型检测 7 类情绪（FER2013 训练，35K+ 图，精度 66.6%）
- 上传图片与实时摄像头两种检测方式
- 全部本地处理，无云端上传、无外部 API
- Flask Web 界面含照片分析、视频检测与历史记录

## 适用场景

- 上传照片或用摄像头检测当前面部情绪
- 本地运行的情绪识别演示与学习项目
- 查看历次检测记录以追踪情绪状态

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L14: **MoodGuard** is an AI-powered emotion recognition and mental health monitoring web application that uses **Convolu
> L16: The system can analyze **uploaded images**, **captured photos**, and **live webcam feeds** to predict emotional sta
> L18: It is designed with a **privacy-first local AI approach**, meaning no facial data is sent to any external server.

## 星数曲线

```mermaid
xychart-beta
    title "Hamna-Munir/MoodGuard-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `b2f6b06bd6a8` · [字段定义](../../DATASET.md)*
