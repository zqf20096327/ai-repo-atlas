# GaneshShivalingappa/Parametric-NN-Models

⭐ 20 · Python · GPL-3.0 · 推送 2026-05-08 · [GitHub](https://github.com/GaneshShivalingappa/Parametric-NN-Models) · [官网](https://doi.org/10.58286/29583) · 个人维护

**对比 PINN 与 FEM 增强神经网络在材料参数反演中的研究项目**

科研代码项目：在一维杆受拉场景下，对物理信息神经网络（PINN）、有限元增强神经网络（FEM-NN）与基于 FEM 数据的神经网络（FEM-Data-NN）进行性能与训练时间对比，用于材料参数辨识的逆向问题求解，可作为代理模型。结果与解析解基准对比并计算相对误差。通过 Singularity 容器分发，含容器构建命令与多个 singularity run --app 入口用于复现图表，未提供 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 安装:github 包 `release-assets` 月下载无数据

## 能力要点

- PINN / FEM-NN / FEM-Data-NN 三种模型的对比分析
- 以解析解为基准计算相对误差
- 训练时间分析（固定节点变样本 / 固定样本变节点）
- Singularity 容器化复现流程

## 适用场景

- 复现论文中的材料参数辨识对比实验
- 研究 PINN 与 FEM 增强方法的计算效率差异
- 作为逆向问题代理模型的参考实现

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: In this project, we conducted a comparative analysis between the Physics Informed Neural Network (PINN) and the Fini
> L14: The container can be built by running the follwing command in the terminal.

## 星数曲线

```mermaid
xychart-beta
    title "GaneshShivalingappa/Parametric-NN-Models 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-25 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `00d34cec202d` · [字段定义](../../DATASET.md)*
