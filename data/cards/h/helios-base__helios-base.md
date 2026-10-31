# helios-base/helios-base

⭐ 48 · C++ · MIT · 推送 2026-10-24 · [GitHub](https://github.com/helios-base/helios-base) · 组织维护 · 中文 README

**RoboCup 2D 足球仿真联赛的示例智能体球队代码包**

HELIOS Base 是面向 RoboCup Soccer 2D Simulator（兼容 rcssserver-16）的示例球队实现，包含可启动的 agent2d 球队脚本。程序依赖 Boost（1.38 或更高）与 librcsc 库，在 Ubuntu 16.04+ 上通过 bootstrap/configure/make 从源码构建，README 还说明如何指定 librcsc 安装路径。配套多篇论文（含 HELIOS Base 2014 Springer 论文及历年冠军队技术文献），供 RoboCup 参赛者与多智能体系统研究者参考使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 兼容 rcssserver-16 的 RoboCup 2D 仿真球队实现
- 提供 start.sh 一键启动 agent2d 球队
- 源码构建流程含 --with-librcsc 自定义路径配置
- 附带 HELIOS 系列论文文献列表（2013-2020）

## 适用场景

- 作为 RoboCup 2D 仿真联赛参赛球队的基础代码
- 研究多智能体系统在动态对抗环境中的协作决策
- 学习足球仿真中局面评估与行为规划方法的参考实现

## 场景标签

`多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L4: helios-base is a sample team for the RoboCup Soccer 2D Simulator.
> L49: The paper about HELIOS Base:

## 星数曲线

```mermaid
xychart-beta
    title "helios-base/helios-base 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-31 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `102a40f9dafd` · [字段定义](../../DATASET.md)*
