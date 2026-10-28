# edwarddn/dinosaur-edward-game

⭐ 19 · Java · 推送 2026-06-23 · [GitHub](https://github.com/edwarddn/dinosaur-edward-game) · 个人维护

**Java 复刻 Chrome 恐龙游戏，内置遗传算法训练的神经网络 AI**

以 Java 25 从零实现物理与渲染逻辑的 Chrome 恐龙跑酷游戏改编版，未使用外部游戏引擎，构建过程借助 Spring Boot 与 Lombok。内置基于神经网络的 AI，通过遗传算法的自然选择进行训练，训练完成后保存网络权重供后续使用。提供两种 AI 相关模式：与 AI 对战，以及训练 AI。为 macOS(AArch64)、Linux(x64)、Windows(x64) 提供安装包下载，开发者也可用 Maven 命令从源码编译运行并打包多平台安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 物理与渲染引擎用 Java 25 从零构建，无外部游戏引擎
- 神经网络 AI 通过遗传算法训练，训练后保存权重
- 提供与 AI 对战和训练 AI 两种模式
- 可用 Maven 打包生成 dmg/deb/exe 多平台安装包

## 适用场景

- 玩 Java 版 Chrome 恐龙跑酷游戏
- 与遗传算法训练出的神经网络 AI 对战
- 观察和运行神经网络的遗传算法训练过程

## 场景标签

 · 领域:游戏/游戏 AI

## 证据(README 行号)

> L25: - Features an artificial intelligence based on a neural network trained by a genetic algorithm.
> L36: 1. After starting the game, select the "Play versus Artificial Intelligence" option in the main menu.

## 星数曲线

```mermaid
xychart-beta
    title "edwarddn/dinosaur-edward-game 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f9dbf0694b8d` · [字段定义](../../DATASET.md)*
