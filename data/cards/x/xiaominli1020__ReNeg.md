# xiaominli1020/ReNeg

⭐ 35 · Python · 推送 2025-12-22 · [GitHub](https://github.com/xiaominli1020/ReNeg) · [官网](https://arxiv.org/pdf/2412.19637) · 组织维护

**为文生图/文生视频模型学习全局负向嵌入的研究代码**

论文配套开源实现：通过奖励引导的梯度下降直接学习负向嵌入（negative embedding），替代手写负向提示词。同一文本编码器的生成模型可共享学到的嵌入，README 提供 SD1.4/1.5/2.1 与 Pixart-alpha 的预训练嵌入，并展示向 ZeroScope、VideoCrafter2、LTX-Video 等视频模型的迁移示例。含推理与训练代码，需 conda 环境与 cu118 版 PyTorch，在线 Demo 尚未提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 奖励引导梯度下降学习全局负向嵌入
- 提供 SD1.4/1.5/2.1、Pixart-alpha 四组预训练嵌入
- 负向嵌入可跨模型迁移至文生视频（ZeroScope/VideoCrafter2/LTX-Video）
- 推理代码支持仅正向提示、负向提示、负向嵌入三种对比模式

## 适用场景

- 我想用学到的负向嵌入替换手写负向提示词来改善 SD 出图
- 在同一文本编码器的不同生成模型间复用负向嵌入
- 复现论文并训练自己的负向嵌入

## 场景标签

`图像生成` `强化学习` · 领域:内容生成

## 证据(README 行号)

> L7: We present **ReNeg**, a **Re**ward-guided approach that directly learns **Neg**ative embeddings through gradient des
> L18: Any text-conditioned generative model utilizing the same text encoder can share their negative embeddings. We provi

## 星数曲线

```mermaid
xychart-beta
    title "xiaominli1020/ReNeg 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-31 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2d3d5b7db6af` · [字段定义](../../DATASET.md)*
