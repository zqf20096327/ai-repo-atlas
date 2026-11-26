# julienkay/tools.doji.diffusers

⭐ 66 · C# · MIT · 推送 2026-11-25 · [GitHub](https://github.com/julienkay/tools.doji.diffusers) · 个人维护

**在 Unity 中用 Sentis 运行扩散模型的包**

将 Hugging Face diffusers 库移植到 Unity，通过 Unity Sentis 运行预训练扩散模型，为游戏/应用生成图像。目前支持的 pipeline 与 scheduler 数量有限，官方标注为实验性、非生产就绪，可能存在破坏性变更。模型经 AI Model Hub 交付，需在项目设置中声明模型条目，优先加载 .sentis 文件，.onnx 文件需转换。通过 OpenUPM 安装，FromPretrained 异步加载可在全部平台运行，非异步加载仅限 Editor 及 Windows/macOS/Linux/iOS。

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

- 移植 Hugging Face diffusers 到 Unity Sentis
- 支持 SD 1.5/2.1/SDXL/SD-Turbo/SDXL-Turbo/FLUX.2 klein 等 txt2img 与 img2img pipeline
- 内置 PNDM/DDIM/Euler 等多种 scheduler 实现
- 通过 AI Model Hub 声明并下载模型，支持打包或运行时下载

## 适用场景

- 在 Unity 游戏中运行文本生成图像的扩散模型
- 为 Unity 项目添加 img2img 图像生成能力
- 在 iOS 等移动平台本地运行预训练扩散模型

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L8: A Unity package to run pretrained diffusion models with Unity Sentis
> L14: This is essentially a port of Hugging Face’s [diffusers] library.
> L42: - List `files` only when the repository holds more than the pipeline reads, for example PyTorch weights, both `.onn


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `5f8c0a8a1add` · [字段定义](../../DATASET.md)*
