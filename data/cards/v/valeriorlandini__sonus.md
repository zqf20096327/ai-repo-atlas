# valeriorlandini/sonus

⭐ 18 · C++ · MIT · 推送 2026-10-09 · [GitHub](https://github.com/valeriorlandini/sonus) · [官网](https://valeriorlandini.github.io/sonus/) · 个人维护

**面向 Max/MSP 的声音实验与算法作曲外部对象包**

用 C++ 编写的 Max/MSP 外部对象（externals）集合，覆盖四类：振荡器/生成器（含元胞自动机、Lorenz/Rössler 混沌吸引子、神经网络振荡器）、效果与采样处理（bitcrusher、滤波、声像）、神经网络与 AI（DNN、感知机、遗传算法、Lindenmayer 系统）、数学工具。另含六个 Max for Live 设备。供 Max/MSP 用户在补丁中使用；Releases 提供 Windows/macOS 编译二进制，也可用 CMake 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 60+ 个 C++ 外部对象，含混沌系统与元胞自动机生成器
- 神经网络相关对象：DNN、感知机、人工神经元、遗传算法
- 六个使用这些外部对象的 Max for Live 设备
- 提供 Windows/macOS 预编译二进制与 CMake 构建流程

## 适用场景

- 在 Max/MSP 中做实验性声音合成与算法作曲
- 用元胞自动机、混沌吸引子等数学系统生成声音素材
- 在 Max for Live 中使用打包的合成器与效果器设备

## 场景标签

 · 领域:音乐/音频工具

## 证据(README 行号)

> L5: An open source Max/MSP package for sound experimentation and algorithmic composition.
> L42: ### Neural Networks and AI

## 星数曲线

```mermaid
xychart-beta
    title "valeriorlandini/sonus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `7c42ed6bae79` · [字段定义](../../DATASET.md)*
