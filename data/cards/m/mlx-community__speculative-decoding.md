# mlx-community/speculative-decoding

⭐ 10 · Swift · MIT · 推送 2025-12-08 · [GitHub](https://github.com/mlx-community/speculative-decoding) · 个人维护

**Apple Silicon 上 LLM 投机解码加速的 Swift 库**

基于 MLX-Swift 的投机解码（speculative decoding）实现：由小 draft 模型提出候选 token、大 target 模型并行验证，README 称在保持输出分布等价的同时获得 2-3 倍加速。提供 Swift Package 集成、高层生成 API 与流式输出、async/await 并发支持、贪心与温度采样，附带 CLI 工具用于生成与基准测试，并实验性支持以 Mamba 状态空间模型作为 drafter。面向在 Apple Silicon 上做本地 LLM 推理的 Swift 开发者，要求 macOS 14+/iOS 16+ 与 M1-M4 芯片。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- draft-target 双模型投机解码，README 称 2-3x 加速且输出分布等价
- Swift Package 集成、流式生成与 async/await 并发支持
- 内置 CLI 工具：生成、统计与基准测试命令
- 实验性支持 Mamba（状态空间模型）作为 draft 模型

## 适用场景

- 在 M 系列 Mac 上加速本地 LLM 文本生成
- 为 Swift/iOS 应用集成流式 LLM 输出
- 对比不同 draft/target 模型对的推理速度与接受率

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Native speculative decoding implementation for fast LLM inference on Apple Silicon using MLX-Swift.
> L7: Speculative decoding accelerates LLM inference by using a smaller "draft" model to propose multiple tokens, which ar
> L11: - Native Swift implementation optimized for Apple Silicon


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `1b3f1b8c4ed4` · [字段定义](../../DATASET.md)*
