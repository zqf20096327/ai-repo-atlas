# artemxdata/Car-Damage-Assessment-AI

⭐ 23 · Jupyter Notebook · MIT · 推送 2026-05-19 · [GitHub](https://github.com/artemxdata/Car-Damage-Assessment-AI) · 个人维护

**面向保险/车队的车辆损伤视觉检测与决策系统**

基于 YOLOv8n（在 CarDD 数据集 4,000+ 图像上训练，10 类损伤，mAP@50 0.581）的车辆损伤检测与评估系统：图像上传后由 CV 模型检测损伤，规则化决策代理按 YAML 策略输出 AUTO_APPROVE/HUMAN_REVIEW/ESCALATE 三类决策，附决策追溯与人工覆写审计日志。提供 Streamlit UI 与 FastAPI REST API，LLM 仅为可选指导层、可完全禁用。作者声明这不是生产级保险系统，需领域微调。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- YOLOv8n 在 CarDD 上训练，10 类损伤，CPU 推理即可运行
- 确定性策略驱动决策（AUTO_APPROVE/HUMAN_REVIEW/ESCALATE）+ 决策追溯
- 人工覆写作为治理事件记录，LLM 可完全禁用不影响正确性
- FastAPI REST API（/assess 等 4 端点）+ 22 项测试与 CI

## 适用场景

- 保险理赔/车队管理中自动初筛车辆损伤案件
- 将损伤评估接入现有理赔流水线（REST API）
- 演示 AI 辅助决策如何保留人工控制与可审计性

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L9: > High-trust vehicle damage assessment system combining **trained YOLOv8 Computer Vision**, deterministic policy-dri
> L22: The CV model is trained on the CarDD dataset — the first public large-scale dataset for car damage detection (4,000
> L144: 2. YOLOv8 detects visible damages (10 classes)

## 星数曲线

```mermaid
xychart-beta
    title "artemxdata/Car-Damage-Assessment-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a6f8180a1a40` · [字段定义](../../DATASET.md)*
