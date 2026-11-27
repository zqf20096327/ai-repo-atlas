# HyperGAN/HyperGAN

⭐ 1,181 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/HyperGAN/HyperGAN) · [官网](https://hypergan.github.io/HyperGAN/) · 组织维护

**面向开发者的 GAN 训练框架：TOML 配方训练、跟踪、导出生成模型**

HyperGAN 以 PyPI 包分发，从声明式 hypergan-model/1 TOML 配方训练生成对抗模型，内置 HNDL 神经图与 ParticleGAN 训练机制。提供 Docker 风格 CLI（train/ps/validate/sample/gc 等）与惰性加载的类型化 Python API，训练运行记录于全局注册表并以 Web Observatory 实时查看；训练好的 EMA 生成器可导出为 .pt、pt2、onnx、safetensors 四种独立部署格式。支持 NCCL 多 GPU 训练，多主机训练标注为实验性。需 Python 3.11+，训练需安装 torch>=2.6。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TOML 声明式配方定义与结构校验（hypergan new/validate）
- Docker 风格运行管理：Run ID、slug、标签、全局注册表与运行对比
- 导出 EMA 生成器为 bundle/pt2/onnx/safetensors 四种格式
- 本地 Web Observatory 实时学习曲线与 REST/SSE API

## 适用场景

- 从图片文件夹自动生成适配分辨率的 GAN 项目并训练
- 多 GPU 环境下训练并跟踪 CIFAR 等基准实验
- 将训练好的生成器导出为独立格式部署到服务端
- 通过浏览器实时查看训练进度与指标曲线

## 场景标签

`模型训练` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L8: **Train generative models. Follow their progress. Export the result.**
> L18: HyperGAN 2.2.0 trains generative models from declarative `hypergan-model/1` TOML recipes using HNDL neural graphs a

## 星数曲线

```mermaid
xychart-beta
    title "HyperGAN/HyperGAN 星数(近 3 点)"
    x-axis ["2026-10-25", "2026-11-20", "2026-11-27"]
    y-axis "stars" 1180 --> 1184
    line [1183, 1181, 1181]
```

2026-10-25 1,183 → 2026-11-27 1,181（-2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `9beb1889f7a2` · [字段定义](../../DATASET.md)*
