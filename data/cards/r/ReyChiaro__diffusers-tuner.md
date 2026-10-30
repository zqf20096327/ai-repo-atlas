# ReyChiaro/diffusers-tuner

⭐ 16 · Python · MIT · 推送 2026-04-15 · [GitHub](https://github.com/ReyChiaro/diffusers-tuner) · 个人维护

**面向 🤗 Diffusers 的配置驱动扩散模型微调框架**

基于 Hydra 配置系统与 Accelerate 的扩散模型微调框架：覆盖数据准备、LoRA 适配器、训练循环与检查点保存，原生支持 DDP。提供轻量自实现 LoRA 适配器系统（注册/激活/多适配器按权重混合）、ForwardHandler 抽象分离各 pipeline 的训练逻辑、数据集 schema 与 bucket 分桶训练（不同分辨率/长宽比混批）。已适配 Qwen-Image 与 FLUX.1 系列 pipeline。项目自述仍在开发中（in progress）。通过 git clone 源码安装，需 Python 3.12、PyTorch 2.10+、Diffusers 0.37.0+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Hydra 分层配置驱动的微调流程，CLI 可覆盖任意字段
- 轻量 LoRA 适配器实现，支持多适配器按权重混合激活
- ForwardHandler 抽象统一各 pipeline 的训练期逻辑
- Bucket 分桶数据集支持不同分辨率混合批训练

## 适用场景

- 微调 Qwen-Image / FLUX.1 等图像编辑 diffusion pipeline
- 用配置文件复现历史实验（hydra-configs 快照）
- 通过 offload 文本编码器与预计算 prompt 嵌入降低显存占用

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L9: Our framework provides a streamlined, "plug-and-play" experience for the diffusers ecosystem, implementing a complet
> L131: `diffusers_tuner/tuner.py` wraps **Accelerate** and exposes:

## 星数曲线

```mermaid
xychart-beta
    title "ReyChiaro/diffusers-tuner 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ddb573f2c88d` · [字段定义](../../DATASET.md)*
