# drkostas/3D-Semantic-Segmentation

⭐ 66 · Jupyter Notebook · Apache-2.0 · 推送 2026-10-13 · [GitHub](https://github.com/drkostas/3D-Semantic-Segmentation) · 个人维护

**课程项目：基于 Transformer 的 3D 医学图像语义分割**

深度学习课程（COSC 525）的期末项目，开发并运行基于 Transformer 的语义分割模型处理 3D 医学图像。主入口为 main.py，其余代码位于 src 文件夹。安装通过 Makefile 完成，支持 conda 或 venv 环境创建（env=conda|venv 标志），运行时以命令行参数指定数据集、网络与配置文件。要求 Python > 3.6 与 Bash shell，许可证为 Apache License。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Transformer 用于 3D 医学图像语义分割
- Makefile 一键创建 conda/venv 环境并安装依赖与运行测试
- main.py 命令行接口：指定数据集、网络、配置文件

## 适用场景

- 在 3D 医学图像数据集上训练/运行 Transformer 分割模型
- 作为课程项目或分割实验代码参考

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L12: Final Project for the Deep Learning course (COSC 525). Involves the development of a semantic
> L13: segmentation model with transformers on 3D medical images

## 星数曲线

```mermaid
xychart-beta
    title "drkostas/3D-Semantic-Segmentation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-10-18 66 → 2026-10-26 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `86be93401fd7` · [字段定义](../../DATASET.md)*
