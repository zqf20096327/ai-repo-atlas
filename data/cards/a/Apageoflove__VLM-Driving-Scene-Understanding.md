# Apageoflove/VLM-Driving-Scene-Understanding

⭐ 14 · Python · MIT · 推送 2026-09-18 · [GitHub](https://github.com/Apageoflove/VLM-Driving-Scene-Understanding) · 个人维护 · 中文 README

**VLM 驾驶场景结构化理解：图片输入输出四类分析**

基于 Qwen2.5-VL-3B-Instruct 与 QLoRA（4-bit NF4、LoRA r=8）微调的驾驶场景理解系统：输入一张驾驶场景图片，输出车道线、车辆、交通标志、驾驶风险四项结构化分析，记录带 schema 校验，解析失败自动修复重试。训练数据来自 nuScenes CAM_FRONT（500 训练 + 50 评估），在云端 RTX 3090 24GB 完成微调。提供 Gradio Web Demo、Python API 与 vlm_drive 包（推理、断点续跑、自动评估、31 项纯 CPU 测试）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单图输入输出车道线/车辆/交通标志/风险四项结构化分析
- QLoRA 微调 Qwen2.5-VL-3B-Instruct（4-bit NF4 + LoRA r=8）
- vlm_drive 包：schema 校验、修复重试、断点续跑、自动评估报告
- 提供 Gradio Demo 与 Python API 两种推理方式

## 适用场景

- 对 nuScenes 等驾驶场景图片做结构化要素分析
- 复现 QLoRA 微调 VLM 的完整训练与评估流程
- 批量推理并自动产出维度评估报告

## 场景标签

`微调` `多模态` · 领域:感知与多模态

## 证据(README 行号)

> L3: 基于 **Qwen2.5-VL-3B-Instruct** + **QLoRA** 微调的驾驶场景结构化理解项目。输入一张驾驶场景图片，模型输出四项结构化分析：车道线、车辆、交通标志、驾驶风险。
> L18: |基座模型|Qwen2.5-VL-3B-Instruct (7.1GB)|

## 星数曲线

```mermaid
xychart-beta
    title "Apageoflove/VLM-Driving-Scene-Understanding 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `21b164d1dbd7` · [字段定义](../../DATASET.md)*
