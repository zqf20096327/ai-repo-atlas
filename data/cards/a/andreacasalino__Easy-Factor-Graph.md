# andreacasalino/Easy-Factor-Graph

⭐ 36 · C++ · GPL-3.0 · 推送 2026-09-13 · [GitHub](https://github.com/andreacasalino/Easy-Factor-Graph) · 个人维护

**C++ 无向图模型/因子图库：构建、查询与训练概率模型**

面向 C++ 开发者的通用无向概率图模型（因子图）库：支持以 builder 模式逐个插入变量与因子动态构建随机场和条件随机场，可在环图与 polytree 上做信念传播，查询条件边缘分布与最大后验估计，从模型采样（Gibbs），并通过梯度方法（梯度下降、共轭梯度、拟牛顿等）训练可调因子模型。支持 XML/JSON 导入导出、内部线程池并行，训练依赖外部库并默认经 CMake 拉取 Eigen；另提供 pip 可装的 Python 绑定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 动态构建随机场/条件随机场，信念传播支持 loopy graph 与 polytree
- 条件边缘分布、MAP 估计、Gibbs 采样查询
- 梯度下降/共轭梯度/拟牛顿等训练方法，可获取权重与梯度
- XML/JSON 模型导入导出与 pybind 的 Python pip 绑定

## 适用场景

- 在 C++ 项目中构建并查询离散概率图模型
- 训练条件随机场完成序列/结构化预测任务
- 通过 Python 绑定在 Python 环境中使用因子图能力

## 场景标签

 · 领域:机器学习/概率图模型

## 证据(README 行号)

> L7: **Easy Factor Graph**, aka **EFG**, is a general purpose c++ library for handling **undirected graphical models**, s
> L27:  * train **random** and **conditional random fields** with gradient based approaches (**gradient descend**, **conju

## 星数曲线

```mermaid
xychart-beta
    title "andreacasalino/Easy-Factor-Graph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-30 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d3f5bb96f613` · [字段定义](../../DATASET.md)*
