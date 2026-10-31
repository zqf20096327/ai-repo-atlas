# sumitvairagar/edge-ai-kit

⭐ 15 · Dart · MIT · 推送 2026-05-05 · [GitHub](https://github.com/sumitvairagar/edge-ai-kit) · 个人维护

**Flutter 端侧 LLM 应用的 UI 工具包：设备检测、模型管理与聊天组件**

面向 Flutter 开发者的 UI 工具包，填补 flutter_gemma 推理引擎与实际应用需求之间的空缺：提供设备能力检测（RAM/GPU/存储/芯片组分级）、含 7 个模型的目录与按设备画像打分的推荐机制、首次启动引导流程，以及多轮流式聊天、图像问答、函数调用、思维链可视化、Prompt Lab 与基准测试（tokens/sec、TTFT）等现成组件。需 Flutter 3.41+，Android 12+/iOS 16+，建议 4GB+ RAM；受 Google AI Edge Gallery 启发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 设备能力检测与设备分级（DeviceTier）
- 7 个模型目录与按设备画像的模型推荐
- 现成组件：AI Chat、Ask Image、Tool Use、Thinking Mode、Prompt Lab、Benchmark
- 通过 git 依赖引入 pubspec.yaml，附带演示应用

## 适用场景

- 快速搭建带端侧 LLM 的 Flutter 聊天/视觉问答应用
- 首次启动时扫描设备并推荐合适的本地模型
- 在真机上测量端侧模型的 tokens/sec 与首 token 延迟

## 场景标签

`聊天机器人` `模型评测` · 领域:对话与助手

## 证据(README 行号)

> L8: EdgeAI Kit fills the gap between `flutter_gemma` (inference engine) and what developers actually need: device capabi
> L3: **The missing UI toolkit for on-device LLMs in Flutter.**

## 星数曲线

```mermaid
xychart-beta
    title "sumitvairagar/edge-ai-kit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e3f83c4f4cc1` · [字段定义](../../DATASET.md)*
