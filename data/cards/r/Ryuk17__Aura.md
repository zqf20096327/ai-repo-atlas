# Ryuk17/Aura

⭐ 15 · C · Apache-2.0 · 推送 2026-10-05 · [GitHub](https://github.com/Ryuk17/Aura) · 个人维护 · 中文 README

**树莓派等 Linux SBC 上的全离线语音交互框架（骨架阶段）**

面向树莓派等 Linux 单板机的端侧全离线语音交互框架，链路为 mic → AFE → VAD → KWS → 声纹 → ASR → LLM/Agent → TTS → playback，推理统一走 MNN，云端仅作增强与兜底，不支持 RTOS。以 C++/CMake 工程提供，第三方依赖 MNN/TrickRoom 由 FetchContent 拉取，支持按模块裁剪编译，附 PC 端 host_sim 仿真。当前为 Phase 1 框架骨架：算法节点为 mock，真实模型实现在 Phase 3/4；模型权重不入库，需经 download.sh 获取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 全离线语音链路：AFE/VAD/KWS/声纹/ASR/LLM/TTS
- 推理统一走 MNN，支持模块级 CMake 裁剪开关
- PC 端 host_sim 全链路仿真（对话闭环、打断、错误注入）
- CTest 8/8 通过，覆盖构建/OSAL/pipeline/事件总线/状态机

## 适用场景

- 在树莓派等 Linux SBC 上搭建离线语音助手骨架
- 验证语音 pipeline 状态机与 barge-in 打断机制
- 按需裁剪编入 KWS/声纹/ASR/LLM/TTS 模块

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L7: 端侧全离线语音交互框架：`mic → AFE(3A/BSS) → VAD → KWS → 声纹 → ASR → LLM/Agent → TTS → playback`。
> L10: **当前状态：Phase 1（框架骨架）完成** —— 构建/OSAL/pipeline/事件总线/状态机/推理封装已落地，

## 星数曲线

```mermaid
xychart-beta
    title "Ryuk17/Aura 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4a8a04a11211` · [字段定义](../../DATASET.md)*
