# CarloWood/machine-learning

⭐ 27 · C++ · 推送 2026-01-13 · [GitHub](https://github.com/CarloWood/machine-learning) · 个人维护

**个人机器学习沙盒：纯 C++ 实现神经网络并借 Tensorflow 跑 GPU**

作者自述的首个机器学习实验项目（sandbox）：用纯 C++ 编写机器学习代码，通过 TensorflowCC 接入 Tensorflow 以利用 GPU 运行。面向 Linux 环境，依赖 TensorflowCC 编译较繁琐，README 建议 Arch Linux 或使用预构建 docker 容器（也支持在 Windows 的 WSL 中启动容器）。本机构建需 autogen.sh + cmake，并用 gitache 自动拉取编译不在发行版仓库中的依赖，另需设置多个环境变量与 ~/.libcwdrc 配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 C++ 实现机器学习，借助 Tensorflow 在 GPU 上运行
- 提供 docker 容器工作方式（含 Windows 经 WSL 的路径）
- gitache 自动克隆、配置、编译并安装发行版未提供的依赖

## 适用场景

- 以 C++ 从零实践神经网络与机器学习算法
- 在标准化 docker 容器中搭建 Linux 机器学习实验环境

## 场景标签

 · 领域:机器学习/实验代码

## 证据(README 行号)

> L1: This is an ongoing effort to do Machine Learning in pure C++,
> L2: leveraging Tensorflow to make it run on the GPU.

## 星数曲线

```mermaid
xychart-beta
    title "CarloWood/machine-learning 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `4f4a06a6660f` · [字段定义](../../DATASET.md)*
