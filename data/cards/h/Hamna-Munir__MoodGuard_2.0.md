# Hamna-Munir/MoodGuard_2.0

⭐ 24 · Python · 推送 2026-06-24 · [GitHub](https://github.com/Hamna-Munir/MoodGuard_2.0) · [官网](https://moodguard-v-2.streamlit.app/) · 个人维护

**实时情绪检测与专注度追踪的 AI 心理状态分析平台**

基于 Python 和 Streamlit 构建的 7 模块 AI 心理状态分析系统：用 CNN（FER2013 训练、ONNX Runtime 推理）实时识别 7 类情绪，用 MediaPipe 面部关键点计算眼部特征并由 RandomForest 分类专注状态，规则引擎将情绪与专注组合映射为行为状态并触发建议，Google Gemini 1.5 Flash 生成个性化生产力建议（配额耗尽时回退到规则生成）。支持网页摄像头实时分析、照片上传分析、会话历史 CSV 导出。需要 Python 3.11+、摄像头与 Gemini API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CNN+ONNX Runtime 实时识别 7 类情绪
- MediaPipe 468 关键点计算 EAR 特征，RandomForest 分类专注状态
- 规则引擎映射情绪×专注组合为行为状态并触发建议
- Gemini 生成个性化建议，配额耗尽回退规则生成

## 适用场景

- 学习或工作时追踪自己的情绪与专注状态
- 上传照片检测情绪概率分布
- 回顾会话历史图表并导出 CSV 数据

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L20: **MoodGuard 2.0** is a 7-module AI Mental State Intelligence System built with Python and Streamlit. It detects hum
> L39: |😊 **Emotion Detection**|Detects 7 emotions (Happy, Sad, Angry, Neutral, Fear, Surprise, Disgust) in real-time usin
> L42: |✦ **AI Insights**|Google Gemini 1.5 Flash analyzes your session and generates personalized productivity advice|

## 星数曲线

```mermaid
xychart-beta
    title "Hamna-Munir/MoodGuard_2.0 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d166224a1b90` · [字段定义](../../DATASET.md)*
