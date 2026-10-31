# purohit10saurabh/toyFLUX

⭐ 15 · Python · Apache-2.0 · 推送 2026-08-03 · [GitHub](https://github.com/purohit10saurabh/toyFLUX) · 个人维护

**学习用 FLUX 扩散 Transformer 的极简 PyTorch 实现**

用于学习 FLUX.1 与 FLUX.2 扩散 Transformer（DiT）架构的玩具项目：实现双流/单流 Transformer 块与联合注意力、rectified flow matching 训练（速度预测、logit-normal 时间步采样）、Euler ODE 采样推理及 VAE 编解码器。架构从 diffusers 与 BFL 官方仓库推断，每个 .py 附带 .md 的逐行源码映射。README 声明由 AI 辅助编写（vibe-coded），并因剥离 ControlNet、KV 缓存等组件而与预训练权重不兼容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- FLUX.1 与 FLUX.2 的 DiT 架构实现（双流/单流块、联合注意力）
- rectified flow matching 训练与 Euler ODE 采样推理
- VAE 编码器/解码器实现
- 每个 .py 文件附带到官方仓库固定 commit 的逐行源码映射

## 适用场景

- 通过可读实现学习 FLUX 扩散 Transformer 的设计
- 理解 rectified flow matching 的训练与采样机制
- 对比 FLUX.1 与 FLUX.2 架构差异（文本编码器、调制、RoPE 等）

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L12: A toy project to learn about the FLUX.1 and FLUX.2 diffusion transformers (DiT) by Black Forest Labs. Built for und
> L18: - **FLUX.1 and FLUX.2 DiT architectures**- Double-stream and single-stream transformer blocks with joint attention

## 星数曲线

```mermaid
xychart-beta
    title "purohit10saurabh/toyFLUX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e62051d11f7e` · [字段定义](../../DATASET.md)*
