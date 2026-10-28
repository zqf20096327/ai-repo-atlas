# DavidZhang73/pytorch-lightning-template

⭐ 36 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/DavidZhang73/pytorch-lightning-template) · 个人维护 · 中文 README

**给科研者的 PyTorch Lightning 深度学习项目模板**

基于 Lightning 全家桶的深度学习项目脚手架：将研究代码（LightningModule）、工程代码（Trainer）与非必要代码（Callbacks）分层组织，通过 LightningCLI 以配置文件切换实验，集成 Torchmetrics 指标计算与可选 WandB 实验跟踪。内置 MNIST 手写数字识别示例，提供 fit/validate/test/predict/resume 命令与配置自动保存、训练前自动 git commit 等定制功能。需要 Python 3.12，Linux x86-64 上经 uv 安装 CUDA 13.0 版 PyTorch 2.11 及 FlashAttention 2、PyTorch3D；macOS 使用 CPU/MPS 构建。FlashAttention wheel 为社区构建而非官方发布产物。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LightningCLI 配置文件驱动，快速切换多组实验
- 自定义 CustomLightningCLI：配置自动保存、训练前自动 git commit、test 后打印 checkpoint 路径
- 内置 MNIST 示例任务与 fit/validate/test/predict/resume 完整命令
- 集成 Torchmetrics，兼容并行训练策略

## 适用场景

- 科研人员快速搭建可复现的深度学习实验工程
- 通过配置文件管理多组模型与数据集实验
- 配合 WandB 跟踪实验并自动记录配置

## 场景标签

`科研工具` `MLOps` · 领域:学习与行业

## 证据(README 行号)

> L8: A template for simple deep learning projects using Lightning
> L14: PyTorch Lightning is to deep learning project development as MVC frameworks (such as Spring, Django, etc.) are to w

## 星数曲线

```mermaid
xychart-beta
    title "DavidZhang73/pytorch-lightning-template 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 34 --> 37
    line [35, 36, 36]
```

2026-10-18 35 → 2026-10-28 36（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `fd5abdfb0bf6` · [字段定义](../../DATASET.md)*
