# metacore-stack/neural-realtime-face-snapshot

⭐ 15 · Python · 推送 2025-11-13 · [GitHub](https://github.com/metacore-stack/neural-realtime-face-snapshot) · 个人维护

**实时人脸检测与识别桌面程序：MTCNN 检测 + FaceNet 嵌入 + KNN 比对**

基于 MTCNN 与 FaceNet 的实时人脸检测与识别系统：用 OpenCV 从摄像头采集图像，MTCNN 完成人脸检测与对齐，FaceNet 将人脸映射为 128 维特征向量，再用 KNN 比对欧氏距离判断是否同一人，实现识别。提供简单 UI：打开摄像头、为检测到的人脸命名并存入数据集（.npy 格式保存/加载）、多脸同框识别。另在 LFW 数据集上提供测试脚本 ctrUi.py，README 给出了不同 n 值下的准确率与耗时实验记录。运行方式为直接运行 main.py，由个人贡献者维护。

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

- MTCNN 三级级联网络完成人脸检测与对齐
- FaceNet 生成 128 维特征向量，KNN 比对欧氏距离实现识别
- UI 支持摄像头采集、人脸命名入库与 .npy 数据集保存/加载
- 提供 LFW 数据集测试脚本与准确率/耗时实验记录

## 适用场景

- 从摄像头实时检测并识别人脸
- 录入人脸特征建立识别数据集
- 在 LFW 数据集上复现人脸识别准确率测试

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L66: ## Real-time face detection and recognition system based on **MTCNN** and **FaceNet**
> L70: 1. Image acquisition from camera using opencv.

## 星数曲线

```mermaid
xychart-beta
    title "metacore-stack/neural-realtime-face-snapshot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `dbdc63389352` · [字段定义](../../DATASET.md)*
