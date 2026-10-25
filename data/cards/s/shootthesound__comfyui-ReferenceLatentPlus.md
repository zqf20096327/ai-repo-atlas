# shootthesound/comfyui-ReferenceLatentPlus

⭐ 36 · Python · 推送 2026-06-07 · [GitHub](https://github.com/shootthesound/comfyui-ReferenceLatentPlus) · 个人维护

**ComfyUI 参考潜空间节点增强版：逐图强度、时间步门控与自动遮罩**

ComfyUI 内置 ReferenceLatent 节点的替代节点，面向使用参考图做图像生成的用户。提供每张参考图独立的符号强度（-5.0~50.0）、独立时间步区间、基于 MediaPipe 的 face/hair/body/clothes/background 自动遮罩（三种填充模式）、百万像素上限控制注意力开销，以及单节点 1–4 图输入与内置 VAE 编码。兼容 Flux 系列、Lumina2、Z-Image、Wan 系列、Hunyuan、Qwen-Image 等消费 reference_latents 的模型。MediaPipe 为可选依赖，未安装时自动遮罩静默失效；负强度与 latent_zero/latent_noise 填充为实验性、分布外行为。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐图符号强度与逐图时间步区间（调度分区避免重叠）
- MediaPipe 自动遮罩（face/hair/body/clothes/background），可被显式 mask 覆盖
- 百万像素上限保持宽高比下采样，控制注意力开销
- 单节点 1–4 参考图输入，槽位渐进显现，内置 VAE 编码

## 适用场景

- 在 ComfyUI 中用参考图控制生成结果的风格或身份
- 只让参考图的脸部/服装等局部参与生成，屏蔽其余区域
- 多张参考图分别设置生效强度与去噪时间区间

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3:  A drop-in replacement for ComfyUI's stock <code>ReferenceLatent</code> node, with the controls I always wished it h
> L6:  Works with Flux, Flux2/Klein, Lumina2, Z-Image, Wan, Hunyuan, Qwen-Image — anything that consumes <code>reference_l

## 星数曲线

```mermaid
xychart-beta
    title "shootthesound/comfyui-ReferenceLatentPlus 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 34 --> 37
    line [35, 36, 36]
```

2026-10-18 35 → 2026-10-25 36（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `94d15f854851` · [字段定义](../../DATASET.md)*
