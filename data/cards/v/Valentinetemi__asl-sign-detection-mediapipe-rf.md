# Valentinetemi/asl-sign-detection-mediapipe-rf

⭐ 20 · Jupyter Notebook · 推送 2026-03-27 · [GitHub](https://github.com/Valentinetemi/asl-sign-detection-mediapipe-rf) · 个人维护

**面向尼日利亚聋人群体的 ASL 字母手语实时检测系统**

检测 28 类 ASL 字母手势：用 MediaPipe 提取 21 个手部关键点（63 维 x/y/z 特征），相对腕点归一化后由 XGBoost 分类，训练不使用原始图像像素，模型体积为 KB 级。作者称该流程对肤色不敏感，并在深色皮肤上经摄像头测试。数据来自 Kaggle ASL 字母数据集（87,000 张原始图像，提取后保留 69,273 样本），提供 Streamlit 网页应用（上传图像 + TTS）与训练 notebook。README 亦列明局限：以 ASL 代理 NSL、M/N 等易混淆对、弱光下性能下降、数据来源单一。

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

- MediaPipe 21 关键点 + 归一化 + XGBoost，28 类 ASL 字母达 98.43% 准确率
- 不训练原始像素，模型为 KB 级，推理基于 63 维几何特征
- README 声明经深肤色真实摄像头验证
- 提供 Streamlit 网页应用（上传 + TTS）与完整训练 notebook

## 适用场景

- 实时识别 ASL 字母手势用于无障碍沟通
- 在低资源环境下以轻量模型做手语字母检测
- 复现训练流程或基于关键点数据集做实验

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L16: Ọwọ AI is an ASL alphabet detection system that achieves **98.43% accuracy across 28 sign classes** - without train
> L108: |Hand Detection|MediaPipe HandLandmarker 0.10.33|

## 星数曲线

```mermaid
xychart-beta
    title "Valentinetemi/asl-sign-detection-mediapipe-rf 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1b6c75c5ab07` · [字段定义](../../DATASET.md)*
