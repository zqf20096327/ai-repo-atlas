# Shubham2376G/NanoI2V

⭐ 30 · Python · MIT · 推送 2026-07-18 · [GitHub](https://github.com/Shubham2376G/NanoI2V) · 个人维护

**从零实现图生视频（I2V）模型的教学代码库**

从零实现图生视频生成管线的 PyTorch 项目：覆盖因果 3D 卷积 VAE、潜空间 DiT、Flow Matching、文本/图像条件与 Classifier-Free Guidance，最终以输入图像为条件生成视频。配套结构化课程网站（shubham2376g.github.io/NanoI2V），README 展示 VAE 重建与 DiT 视频生成结果，并提供 examples/ 目录下 8 个冒烟测试脚本，可在免费 Google Colab GPU 上用微型配置与合成数据在数分钟内验证完整管线。通过 git clone 后 pip install -e . 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从零实现 VAE（CausalConv3D）、DiT（3D RoPE/adaLN-Zero）、Flow Matching 全管线
- 8 个冒烟测试脚本，可用合成数据在免费 Colab GPU 上验证端到端流程
- 配套结构化课程网站，逐模块讲解代码
- README 展示 VAE 重建与条件视频生成的实测结果

## 适用场景

- 学习现代图生视频模型的内部构建块与训练流程
- 在 Colab 上快速验证扩散视频生成环境是否可用
- 作为 DiT/Flow Matching 教学实现的研究起点

## 场景标签

`视频生成` `教程课程` · 领域:内容生成

## 证据(README 行号)

> L5: NanoI2V is a **from-scratch implementation** of an **Image-to-Video (I2V)** generation pipeline.
> L72: The Diffusion Transformer (DiT) is trained in latent space and generates video sequences conditioned on an input im

## 星数曲线

```mermaid
xychart-beta
    title "Shubham2376G/NanoI2V 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-31 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d9482ae3e72b` · [字段定义](../../DATASET.md)*
