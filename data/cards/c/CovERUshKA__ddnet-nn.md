# CovERUshKA/ddnet-nn

⭐ 16 · C++ · MIT · 推送 2026-02-18 · [GitHub](https://github.com/CovERUshKA/ddnet-nn) · 个人维护

**为 DDNet 游戏服务器接入训练神经网络的示例项目**

基于 libtorch 的神经网络项目，将训练好的模型（主题标签显示为 PPO）编译进 DDNet-Server，并提供一个已训练网络的演示视频。README 主要内容为 Windows 下的构建说明：需安装指定版本的 CUDA、Nsight NVTX、带 CUDA 支持的 libtorch，通过 cmake 生成构建文件并在 Visual Studio 中链接 libtorch 依赖库、复制 DLL 后运行。面向熟悉 C++/CMake 与 DDNet 代码库的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 使用 libtorch（CUDA 版）实现神经网络
- 提供已训练网络的 YouTube 演示视频
- 给出 Windows 下 cmake + Visual Studio 的完整链接步骤

## 适用场景

- 在 DDNet 服务器中运行神经网络控制的演示
- 作为 libtorch 集成到 DDNet 代码库的构建参考

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L1: # ddnet-nn
> L3: Example of trained neural network - https://www.youtube.com/watch?v=g63a2TTIJu8
> L6: To compile you would need to install libtorch with cuda support.

## 星数曲线

```mermaid
xychart-beta
    title "CovERUshKA/ddnet-nn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `fb1294e8f1a8` · [字段定义](../../DATASET.md)*
