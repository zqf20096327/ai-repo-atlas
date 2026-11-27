# World-Snapshot/WSMs

⭐ 25 · Jupyter Notebook · NOASSERTION · 推送 2026-11-25 · [GitHub](https://github.com/World-Snapshot/WSMs) · [官网](https://world-snapshot.github.io/WSMs/) · 组织维护

**统一上千视觉任务的生成式世界模型 WSM v1 代码库**

WSMs 是 World Snapshot Models（WSM v1，代号 Augustus）的官方实现：以 .wsg 格式将 RGB、几何、运动、物理、材质、语义、音频等编码为 256 通道图像，在 FLUX.2 Klein 4B 骨干上用 TunnelingNet 训练每任务约 12.51M 参数的 Channel Head，单一生成模型验证 1,148 个视觉任务。提供 pip 包、推理 Pipeline、Quickstart Notebook、数据与训练日志全量开源；18B 级统一模型单文件约 43 GB，自定义任务需自备对齐数据集与 VAE latents。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一生成模型覆盖 1,148 个视觉任务，接口兼容 1,477 个任务
- TunnelingNet：每任务一个 12.51M 参数隧道，可独立训练并注册到共享骨干
- .wsg 格式将多模态信息编码为 256 通道图像
- 开源数据、训练状态、优化器与训练日志，支持自定义 Channel Head 训练

## 适用场景

- 用一个模型批量运行多种视觉生成与估计任务
- 基于自有数据训练新的条件-目标任务隧道
- 下载训练日志与检查点复现训练过程

## 场景标签

`图像生成` `多模态` `微调` · 领域:内容生成

## 证据(README 行号)

> L17: World Snapshot Models (WSMs) are an ideal world model designed to **unify, expand, and ultimately transcend Compute
> L42: WSM v1 is the first large-scale implementation of the Unified Law for Visual Tasks. The method can unify thousands 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `707b917fbeac` · [字段定义](../../DATASET.md)*
