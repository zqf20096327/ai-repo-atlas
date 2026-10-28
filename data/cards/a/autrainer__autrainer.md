# autrainer/autrainer

⭐ 24 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/autrainer/autrainer) · [官网](https://autrainer.github.io/autrainer/) · 组织维护

**面向计算机听觉任务的模块化深度学习训练工具包**

基于 PyTorch 与 Hydra 构建的计算机听觉深度学习工具包，通过 YAML 配置文件与命令行执行可复现的深度学习实验，支持模块化扩展自定义组件。提供 pip 安装与七类可选依赖（LaTeX 绘图、MLflow/TensorBoard 日志、openSMILE 特征提取、多种音频/图像增强库）。Windows 用户需先安装 PyTorch 2.0 及以上版本。附带快速入门、教程与 CLI 参考文档，并有 arXiv 预印本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 PyTorch + Hydra 的 YAML 配置化训练
- pip 安装并支持七类可选依赖扩展
- 提供快速入门、教程与完整 CLI 命令参考
- 在 Hugging Face 发布模型并有 arXiv 预印本

## 适用场景

- 用 YAML 配置与命令行复现计算机听觉实验
- 实现并注册自定义训练模块
- 接入 MLflow/TensorBoard 记录训练日志

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L11: `autrainer` is built on top of `PyTorch <https://pytorch.org/>`_ and `Hydra <https://hydra.cc/>`_,
> L12: offering a modular and extensible way to perform reproducible deep learning experiments

## 星数曲线

```mermaid
xychart-beta
    title "autrainer/autrainer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `884e9848447e` · [字段定义](../../DATASET.md)*
