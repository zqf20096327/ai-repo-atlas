# Aashritha-2005/MotionIQ-Squat-analysis

⭐ 16 · Python · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/Aashritha-2005/MotionIQ-Squat-analysis) · 个人维护

**给健身者实时计深蹲次数并提示动作问题的姿态分析工具**

从摄像头或视频逐帧提取人体关键点（YOLO11s-pose，17 点），基于 32 帧窗口的因果 LSTM 识别深蹲阶段（站立/下蹲/触底/起身）并计数，再以几何阈值规则标记过浅、前倾等动作问题，导出 ONNX 在 Apple Silicon Mac 上实时运行。准确率数据来自录播视频与 5 名留出受试者；实测仅限一人侧视，非深蹲动作会被误计，前倾与膝外翻判定不可靠或未验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- YOLO11s-pose 姿态关键点 + 32 帧 2 层 LSTM 阶段识别（ONNX 导出）
- 逐帧端到端延迟中位数 20.55 ms（Apple Silicon，66.7 ms 预算内）
- 留出集相位宏 F1 0.891，计数 381/387 次
- 基于逐次几何统计的阈值式动作规则（过浅/前倾/膝外翻）

## 适用场景

- 对着摄像头做深蹲时实时计数与深度提示
- 回放已有深蹲视频跑完整流水线分析
- 复现姿态+时序模型的动作识别实验流程

## 场景标签

 · 领域:计算机视觉/健身

## 证据(README 行号)

> L3: MotionIQ watches a person doing squats, detects body keypoints, recognises the movement phase on every frame
> L23: - **Pose:** pretrained YOLO11s-pose (CNN), 17 keypoints per frame.
> L25: - **Phase model:** a unidirectional (causal) 2-layer LSTM over the last 32 frames (2.1 s), exported to ONNX.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `c011e9c58b50` · [字段定义](../../DATASET.md)*
