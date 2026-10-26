# julienkay/com.doji.diffusers

⭐ 66 · C# · MIT · 推送 2026-02-20 · [GitHub](https://github.com/julienkay/com.doji.diffusers) · 组织维护

**在 Unity 中运行预训练扩散模型的 Sentis 包**

Doji 维护的 Unity 包，将 Hugging Face diffusers 库移植到 Unity Sentis 运行时，供 Unity 开发者在引擎内直接运行预训练扩散模型生成图像。目前支持有限数量的管线与调度器：模型方面支持 SD 1.5/2.1、SDXL、SD-Turbo、SDXL-Turbo；调度器支持 PNDM、DDIM、EulerDiscrete、EulerAncestralDiscrete；管线支持 txt2img 与 img2img，并提供切片推理的异步方法。通过 OpenUPM scoped registry 安装，当前需搭配自定义 fork 的 Sentis；README 自声明处于早期实验阶段，非生产就绪。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- diffusers 库向 Unity Sentis 的移植
- 支持 SD 1.5/2.1、SDXL、SD-Turbo、SDXL-Turbo 模型
- 提供 txt2img 与 img2img 管线及异步切片推理
- 实现 4 种调度器（PNDM/DDIM/EulerDiscrete/EulerAncestralDiscrete）

## 适用场景

- 在 Unity 游戏或应用内直接生成图像
- 用 txt2img/img2img 管线做运行时图像生成
- 在 Unity 工作流中实验 Stable Diffusion 系列模型

## 场景标签

`图像生成` `推理引擎` · 领域:内容生成

## 证据(README 行号)

> L8: A Unity package to run pretrained diffusion models with Unity Sentis
> L14: This is essentially a port of Hugging Face’s [diffusers] library.

## 星数曲线

```mermaid
xychart-beta
    title "julienkay/com.doji.diffusers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-10-18 66 → 2026-10-26 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0b7ceff4c90c` · [字段定义](../../DATASET.md)*
