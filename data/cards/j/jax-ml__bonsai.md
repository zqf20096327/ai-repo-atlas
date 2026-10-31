# jax-ml/bonsai

⭐ 246 · Python · Apache-2.0 · 推送 2026-05-29 · [GitHub](https://github.com/jax-ml/bonsai) · 组织维护

**流行模型的极简 JAX 实现，降低 JAX 上手门槛**

Google JAX 团队维护的模型实现库，以简洁、可改写的代码在 JAX 中复现流行模型，目标读者是 JAX 学习者与学术研究者。收录约 17 个模型：图像分类（ResNet50/VGG/EfficientNet/ConvNeXT/DenseNet/ViT）、LLM（Qwen3/umT5）、VLM（Gemma3）、Mamba2、Whisper、CLIP 等，按就绪程度标注状态，部分模型仍需数值测试。README 提示大规模/工业用途应转向 MaxText 与 MaxDiffusion。通过 git clone 后 pip install -e 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Qwen3 模型仅约 400 行 JAX 代码实现
- 覆盖图像分类、LLM、VLM、SSM、语音识别等多类模型（约 17 个）
- 按状态（就绪/开发中/进行中/计划中）标注各模型成熟度

## 适用场景

- 学习流行模型在 JAX 中的简洁实现
- 在 JAX 上做模型实验与学术创新
- 查找可改写的模型参考代码

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: Bonsai is a minimal, lightweight JAX implementation of popular models.
> L64: Jump right into our Qwen3 model, implemented in 400 lines of code in JAX.

## 星数曲线

```mermaid
xychart-beta
    title "jax-ml/bonsai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 245 --> 247
    line [246, 246]
```

2026-10-18 246 → 2026-10-31 246（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `764392615fe8` · [字段定义](../../DATASET.md)*
