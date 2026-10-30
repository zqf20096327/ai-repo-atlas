# keegan0521/AnyFlow

⭐ 15 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/keegan0521/AnyFlow) · 组织维护

**任意步数视频扩散框架：文生视频/图生视频训练与推理**

基于 flow maps 的任意步数（any-step）视频扩散框架，单个模型可适配任意推理步数预算，在少步数下生成视频且随步数增加质量稳定提升。支持因果与双向视频扩散模型的蒸馏、文生视频/图生视频/视频到视频任务，并在 1.3B 至 14B 参数规模上验证。基于 Diffusers 构建，提供 conda 环境搭建、预训练权重下载（HuggingFace）、Gradio 演示、torchrun 多卡训练与 VBench 评测流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单模型适配任意推理步数预算的 flow map 蒸馏框架
- 支持因果与双向架构、T2V/I2V/V2V 三类任务
- 1.3B 至 14B 参数规模验证
- 提供 VBench 评测配置与预训练模型下载

## 适用场景

- 研究任意步数视频扩散蒸馏方法
- 用预训练权重做文生视频/图生视频推理
- 在自己的数据集上训练并跑 VBench 评测

## 场景标签

`视频生成` `模型训练` · 领域:内容生成

## 证据(README 行号)

> L12: We introduce **AnyFlow**, the first any-step video diffusion framework built on flow maps. **AnyFlow** offers these
> L16: - 🎬 **Multiple Tasks**: **AnyFlow** supports Text-to-Video, Image-to-Video, and Video-to-Video generation within on

## 星数曲线

```mermaid
xychart-beta
    title "keegan0521/AnyFlow 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-23 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `05efd7ea0b05` · [字段定义](../../DATASET.md)*
