# joseph-nagel/diffusion-demo

⭐ 20 · Jupyter Notebook · MIT · 推送 2026-08-31 · [GitHub](https://github.com/joseph-nagel/diffusion-demo) · 个人维护

**DDPM/DDIM 去噪扩散模型的 PyTorch 教学演示**

基于 PyTorch 与 Lightning 实现的去噪扩散模型演示仓库，含 DDPM 理论介绍与 DDIM 加速采样的配套 notebook。提供两个实验应用：2D Swiss roll 分布上的生成式 DDPM 训练，以及 MNIST 上无条件/按类别条件生成手写数字的模型。训练通过 config 文件调用脚本完成，可用 TensorBoard 或 MLflow 监控实验，示例代码设计为便于修改和扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DDPM 理论介绍与 DDIM 加速采样的配套 notebook
- Swiss roll 2D 分布与 MNIST 无条件/条件生成两组示例
- 通过 YAML config 配置训练问题与模型定义
- 支持 TensorBoard 与 MLflow 实验监控

## 适用场景

- 学习去噪扩散模型的前向/反向过程原理
- 修改和扩展示例做扩散模型的小型实验
- 对比无条件与条件生成的效果

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository contains a simple implementation of denoising diffusion models. It is PyTorch-based and employs Ligh
> L31: The second application is based on the MNIST dataset. Here, one can construct a DDPM that is either unconditioned (

## 星数曲线

```mermaid
xychart-beta
    title "joseph-nagel/diffusion-demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `38bb483b2f42` · [字段定义](../../DATASET.md)*
