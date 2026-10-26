# yejingyang8963-byte/Swift-gemma4-core

⭐ 27 · Swift · MIT · 推送 2026-05-01 · [GitHub](https://github.com/yejingyang8963-byte/Swift-gemma4-core) · 个人维护 · 中文 README

**纯 Swift 实现的 Gemma 4 解码器，在 iPhone/iPad/Mac 上端侧运行**

Google Gemma 4 文本解码器的纯 Swift 移植，以 sidecar 模型注册接入 Apple 的 mlx-swift-lm，可直接加载 HuggingFace 上的 Gemma 4 4-bit 仓库（如 mlx-community/gemma-4-e2b-it-4bit）。运行时无 Python、无 CoreML 转换，全部计算跑在 MLX Metal 内核上。实现 Gemma 4 的逐层嵌入（PLE）、后 20 层 KV 共享、比例 RoPE 与聊天模板旁路（token 序列与 Python mlx-lm 一致）。面向 Apple Silicon 开发者，以 SwiftPM 包提供；限制：仅支持 Gemma 4 一类模型，需 6GB 以上内存的 Apple Silicon 设备，模型权重约 1.5GB 需首次运行时下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 纯 Swift 移植 Gemma 4 解码器，运行时无 Python、无 CoreML 转换
- 实现 PLE、后 20 层 KV 共享、比例 RoPE 与聊天模板旁路
- token 输出与 Python mlx-lm 数值一致性可复现验证（提供 baseline 脚本）
- 实测 iPhone 上加载后内存 341–392 MB，生成 12–14 tok/s

## 适用场景

- 在 iOS/macOS 应用中端侧运行 Gemma 4 文本生成
- 为 mlx-swift-lm 项目补充缺失的 Gemma 4 模型支持
- 在无 Python 依赖的 Apple Silicon 环境做本地推理

## 场景标签

 · 领域:LLM 端侧推理/Apple 生态

## 证据(README 行号)

> L23: `Gemma4SwiftCore` is a **pure-Swift port** of Google's
> L30: There is no Python at runtime. There is no CoreML conversion step.
> L31: Everything from token IDs to logits runs on Apple's MLX Metal kernels,

## 星数曲线

```mermaid
xychart-beta
    title "yejingyang8963-byte/Swift-gemma4-core 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `b207a0f3d8d7` · [字段定义](../../DATASET.md)*
