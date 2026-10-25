# mehmetbulutaktas458-dev/Aozora-Forge

⭐ 57 · HTML · 推送 2026-10-24 · [GitHub](https://github.com/mehmetbulutaktas458-dev/Aozora-Forge) · 个人维护

**低显存扩散模型微调工具包：12GB 显卡上微调 SDXL/ANIMA**

面向 SDXL 与 ANIMA 系扩散模型的显存节约型微调工具包，定位为已有底模基础上的适配训练而非从零训练。核心机制包括自适应梯度检查点、分层参数冻结、量化 latent 缓存、混合精度编排、优化器状态卸载至主机内存/NVMe、动态微批次与长宽比分桶数据管线；附带响应式 Web 仪表盘与多语言界面。提供三个自研低内存优化器（Tenrai/Kaze/Sora）。README 称 1024px 微调 SDXL 可在约 12GB 显存内完成；当前聚焦单卡训练，多卡在 2026 路线图中。未展示具体安装命令或代码入口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自适应梯度检查点、分层参数冻结与量化 latent 缓存等显存节约机制
- 优化器状态可卸载至主机内存或 NVMe，动态微批次自动拆分合并
- 三个自研优化器 Tenrai/Kaze/Sora，支持梯度裁剪与参数组超参
- 响应式 Web 仪表盘：实时损失/显存/温度读数、样例预览、配置编辑

## 适用场景

- 在 12GB 级消费级显卡上微调 SDXL 或 ANIMA 模型
- 用自定义数据集把底模适配到特定画风或题材
- 训练过程中通过 Web 仪表盘监控显存与进度

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L18: This is a fine-tuning companion, not a from-scratch trainer. It assumes you already have a base checkpoint — Stable
> L59: This is where the magic happens. The training loop coordinates forward passes, backward passes, optimizer updates, 

## 星数曲线

```mermaid
xychart-beta
    title "mehmetbulutaktas458-dev/Aozora-Forge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-25 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `80fd75faa27b` · [字段定义](../../DATASET.md)*
