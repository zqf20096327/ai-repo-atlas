# Mehedi-hasan-Dev/Visual-Model-Forge

⭐ 53 · HTML · 推送 2026-10-24 · [GitHub](https://github.com/Mehedi-hasan-Dev/Visual-Model-Forge) · 个人维护

**无代码图像分类训练工作台：可视化调参、实时训练**

PerceptaForge 是浏览器端的图像分类训练工具：在可视化画布上选择卷积/transformer 骨干网络、优化器、增广与学习率调度，实时查看损失、准确率、梯度范数等遥测面板；支持配置并排对比、数据集摄入适配（文件夹/CSV/归档）、以 manifest 记录配置与随机种子以复现实验。以容器运行时镜像加启动器形式分发，通过挂载数据集目录并打开本地地址使用。硬件加速可选，无 GPU 时回退到较慢运行。仓库描述提及 Streamlit 与 Keras。

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

- 可视化画布上选择骨干网络与优化器并实时查看训练遥测
- 优化器全参数面暴露，支持两种配置并排对比
- session manifest 记录配置、种子与数据集指纹以复现训练轨迹
- 整体运行于隔离容器，无外部遥测，可离线（air-gapped）运行

## 适用场景

- 不写样板代码搭建和调参图像分类模型
- 对比不同骨干网络与优化器配置的训练曲线
- 以可复现 manifest 归档并交接训练实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L17: **PerceptaForge** is a browser-driven training atelier for anyone who wants to sculpt image classification pipeline
> L105: - Obtain the runtime image through your organization's preferred artifact channel.
> L107: - Start the canvas service and open the provided local address in your browser.

## 星数曲线

```mermaid
xychart-beta
    title "Mehedi-hasan-Dev/Visual-Model-Forge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-24 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `4f60197331e8` · [字段定义](../../DATASET.md)*
