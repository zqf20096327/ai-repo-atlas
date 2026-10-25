# baler-collaboration/baler

⭐ 43 · Python · Apache-2.0 · 推送 2026-01-15 · [GitHub](https://github.com/baler-collaboration/baler) · [官网](https://github.com/baler-collaboration/baler.github.io) · 组织维护

**基于机器学习自编码器的科学数据压缩工具**

Baler 用于测试以机器学习自编码器压缩不同类型科学数据的可行性：提供在用户数据上训练模型、用模型压缩数据并保存压缩文件与模型、之后用模型解压文件、绘制压缩/解压性能四个步骤的工作流。面向 CFD、粒子物理等科学数据场景。提供 Python 与 Docker/Singularity/Apptainer 两种运行方式。README 注明当前暂停审查 PR，且主分支存在性能问题，论文对应版本为 v1.0.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 机器学习自编码器训练—压缩—解压—性能绘图工作流
- 支持 Python 与 Docker/Singularity/Apptainer 运行
- 论文对应版本 v1.0.0 含可用的 docker 实现

## 适用场景

- 科学数据（如粒子物理/CFD）的有损压缩实验
- 训练自编码器后长期保存与解压压缩数据
- 对比压缩/解压性能指标

## 场景标签

 · 领域:科学计算/数据压缩

## 证据(README 行号)

> L11: Baler is a tool used to test the feasibility of compressing different types of scientific data using machine learni
> L12: 1. Train a machine learning model on your data

## 星数曲线

```mermaid
xychart-beta
    title "baler-collaboration/baler 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-25 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `733e96f7f677` · [字段定义](../../DATASET.md)*
