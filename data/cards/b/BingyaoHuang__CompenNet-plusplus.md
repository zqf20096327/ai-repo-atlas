# BingyaoHuang/CompenNet-plusplus

⭐ 28 · Python · NOASSERTION · 推送 2025-12-15 · [GitHub](https://github.com/BingyaoHuang/CompenNet-plusplus) · 个人维护

**投影仪光度补偿的端到端深度学习系统（ICCV'19）**

CompenNet++ 的 PyTorch 官方实现：一个端到端的全投影仪补偿系统，从相机捕获图像学习几何校正与光度补偿，生成补偿后的投影仪输入图像，无需两步法所需的约 42 张额外采样图像。提出两种任务特定的权重初始化方法保证收敛稳定，并提供简化技术提升运行效率。面向计算成像/计算机视觉研究者，提供基准数据集（约 11G）下载，通过 conda 环境安装依赖后运行 main.py 训练与测试，训练过程用 visdom 可视化。许可证限非营利非商业使用。

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

- 端到端学习几何校正，无需约 42 张额外采样图像
- 两种任务特定的权重初始化方法保证收敛与稳定
- 提供约 11G 的基准数据集
- 训练过程通过 visdom 实时可视化

## 适用场景

- 在非平面纹理投影表面上做投影仪光度补偿研究
- 复现 ICCV'19 CompenNet++ 论文实验
- 将自己的投影-相机采集数据接入训练流程

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L6: PyTorch implementation of [CompenNet++][1]. Also see [journal version][7].
> L9: * The proposed **CompenNet++** is the **first end-to-end full** projector compensation system.

## 星数曲线

```mermaid
xychart-beta
    title "BingyaoHuang/CompenNet-plusplus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-26 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f6f37b1504a3` · [字段定义](../../DATASET.md)*
