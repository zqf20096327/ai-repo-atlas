# helios-base/librcsc

⭐ 31 · C++ · LGPL-3.0 · 推送 2026-07-13 · [GitHub](https://github.com/helios-base/librcsc) · 组织维护

**开发 RoboCup 足球仿真球队及工具的 C++ 基础库**

面向 RoboCup Soccer Simulation 的 C++ 基础库，用于开发仿真足球队及相关工具，程序兼容 rcssserver-18。构建依赖 C++17 与 Boost 1.41+，通过 bootstrap/configure/make 源码编译安装，支持 --prefix 自定义安装目录并配置 LD_LIBRARY_PATH 与 PATH；可选生成 Doxygen 文档，提供 make uninstall 卸载方式。许可证为 LGPL v3，由 HELIOS 团队维护，README 引用 RoboCup 2013 与 2007 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供与 rcssserver-18 配合工作的球队开发基础库
- 依赖 C++17 与 Boost 1.41 及以上版本
- 支持 configure --prefix 自定义安装目录与源码编译
- 可选用 Doxygen/Graphviz 生成文档

## 适用场景

- 开发 RoboCup 2D 仿真足球参赛队伍
- 编写与 rcssserver 配合的足球仿真相关工具
- 作为 HELIOS Base 等上层球队代码的依赖库

## 场景标签

 · 领域:机器人/多智能体仿真

## 证据(README 行号)

> L5: librcsc is a basic library to develop a simulated soccer team and related tools for the RoboCup Soccer Simulation.
> L6: All programs can work with rcssserver-18.

## 星数曲线

```mermaid
xychart-beta
    title "helios-base/librcsc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-26 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `93efc4e772e1` · [字段定义](../../DATASET.md)*
