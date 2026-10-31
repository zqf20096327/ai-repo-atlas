# johndpope/OmniTransfer-hack

⭐ 16 · Python · NOASSERTION · 推送 2026-07-19 · [GitHub](https://github.com/johndpope/OmniTransfer-hack) · [官网](https://pangzecheung.github.io/OmniTransfer/) · 个人维护

**单张肖像生成身份保持视频的 LTX-2.3 训练与推理工具集**

从零复现 OmniTransfer（arXiv:2601.14250）的项目，后转向以官方 LTX-2.3-22B IC-LoRA-Ingredients 适配器为核心：输入一张（至多四张）参考肖像与文本提示，生成保持人物外观的新场景视频，无需训练。仓库保留 OmniTransfer 三阶段实现及修复（RCL 修复、非有限梯度守卫等），提供仓内 IC-LoRA 训练器、MetaQuery/Qwen-VL 语义控制连接器训练路径、肖像库抽取与 mashup 数据构建工具。面向视频扩散模型研究/开发用户，需本地准备 LTX-2.3 权重与 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单图肖像+提示词生成身份保持视频（零训练推理）
- 仓内 IC-LoRA 训练器，可从 Ingredients LoRA 热启动微调
- MetaQuery：Qwen-VL 读参考图、可学习查询注入交叉注意力实现语义控制
- OmniTransfer 研究线保留多处训练修复（RCL keep-mask、非有限梯度守卫等）

## 适用场景

- 用一张肖像照片生成人物出现在新场景的视频
- 在自己的角色数据上微调身份保持 IC-LoRA
- 复现或改进 OmniTransfer 训练流程

## 场景标签

`视频生成` `微调` · 领域:内容生成

## 证据(README 行号)

> L4: (arXiv:2601.14250) on LTX‑2.3. After building and
> L18: |**Character identity → new scene from 1 image**|Ingredients IC‑LoRA (inference)|❌ none|
> L37: Ingredients LoRA; the model generates a video that keeps the reference's

## 星数曲线

```mermaid
xychart-beta
    title "johndpope/OmniTransfer-hack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a021f7a4149d` · [字段定义](../../DATASET.md)*
