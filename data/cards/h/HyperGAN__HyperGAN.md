# HyperGAN/HyperGAN

⭐ 1,183 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/HyperGAN/HyperGAN) · 组织维护

**可组合的 GAN 框架：用 PyTorch 构建、训练与共享生成对抗网络**

面向开发者、研究者和艺术家的可组合 GAN 框架，基于 PyTorch 构建。提供 Python API 与 CLI：通过 JSON 配置定义或替换网络组件，支持训练自定义模型（如 preset:celeba）、采样生成图像，并可将训练好的模型以 hypergan 格式或 ONNX 格式共享到其他项目。支持 Windows/OSX/Linux，训练推荐 Nvidia GTX 1080+ GPU，可切换 CPU 后端但文档标注训练过慢。当前为 1.0 pre-release 开放测试阶段。数据集仅需图片文件夹，默认对不洁数据做缩放与裁剪。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- JSON 配置定义可组合架构，组件可替换为自定义 PyTorch 实现
- 提供 CLI 与 Python API（训练/采样/加载已训练模型）
- 模型可导出为 ONNX 供任意项目使用
- 支持迁移学习、在线学习与无监督分布对齐

## 适用场景

- 用图片文件夹训练自定义 GAN 生成图像
- 在 Python 项目中集成已训练的生成模型
- 研究可组合 GAN 架构与无监督对齐

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L21: HyperGAN builds generative adversarial networks in pytorch and makes them easy to train and share.
> L7: A composable GAN built for developers, researchers, and artists.

## 星数曲线

```mermaid
xychart-beta
    title "HyperGAN/HyperGAN 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 1182 --> 1184
    line [1183, 1183]
```

2026-10-18 1,183 → 2026-10-28 1,183（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `fcae9a163b49` · [字段定义](../../DATASET.md)*
