# Otosaku/NeMoConformerASR-iOS

⭐ 19 · Swift · 推送 2026-06-04 · [GitHub](https://github.com/Otosaku/NeMoConformerASR-iOS) · 个人维护

**iOS/macOS 端侧语音转文字 Swift 库（NeMo Conformer CTC）**

基于 NVIDIA NeMo Conformer CTC Small（13M 参数）的 Swift 库，通过 CoreML 在 iOS/macOS 设备本地执行英文语音识别，返回全文与带时间戳的分段结果。支持 5–20 秒输入自动补齐，长音频经 VAD 智能分段（NeMoVAD-iOS）处理，可输出 encoder 嵌入供下游任务。模型（约 30MB）需从 Google Drive 单独下载，依赖 NeMoFeatureExtractor-iOS 提取 Mel 频谱。README 顶部声明本项目已演进为 VoxRT，建议使用者转向 VoxRT。

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

- 端侧 CoreML 运行 NeMo Conformer CTC Small（13M 参数）
- VAD 智能分段处理长音频，返回带时间戳分段
- 支持 5/10/15/20 秒输入自动补齐
- 可获取 encoder 嵌入（MLMultiArray）供下游任务

## 适用场景

- 在 iOS/macOS 应用中做本地英文语音转文字
- 处理长录音并获取分段与时间戳
- 提取语音 encoder 嵌入用于其他任务

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: Swift library for speech recognition using NVIDIA NeMo Conformer CTC model on iOS/macOS with CoreML.
> L20: - NVIDIA NeMo Conformer CTC Small model (13M parameters)

## 星数曲线

```mermaid
xychart-beta
    title "Otosaku/NeMoConformerASR-iOS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a16c0e1cd9a6` · [字段定义](../../DATASET.md)*
