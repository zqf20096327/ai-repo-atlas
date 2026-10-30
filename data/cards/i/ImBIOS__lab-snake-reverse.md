# ImBIOS/lab-snake-reverse

⭐ 36 · HTML · 推送 2025-11-24 · [GitHub](https://github.com/ImBIOS/lab-snake-reverse) · [官网](https://imbios.github.io/lab-snake-reverse/) · 个人维护

**反向贪吃蛇浏览器游戏：玩家当苹果，被 A* 蛇追捕**

用 Vanilla JavaScript 与 HTML5 Canvas 编写的开源浏览器游戏，反转经典贪吃蛇：玩家操控苹果，蛇由 A* 寻路算法追踪，随时间自动变长。共 10 关，第 10 关为 10 条蛇的 Swarm 模式。无需安装，浏览器直接游玩，支持桌面键盘与移动端虚拟摇杆，最高分本地保存。代码零依赖、无构建步骤，git clone 即可本地修改。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- A* 寻路（PriorityQueue + Manhattan 启发式）驱动蛇追踪玩家
- Collision Grid Cache 实现 O(1) 查询，10 条蛇维持 60FPS
- 10 关递进难度，第 10 关 10 蛇 Swarm 模式
- 零依赖、无构建步骤，本地 clone 即可开发

## 适用场景

- 在浏览器中直接游玩生存向贪吃蛇变体
- 学习纯 JavaScript 游戏开发与 A* 寻路实现
- 在手机或桌面跨平台游玩并本地保存最高分

## 场景标签

 · 领域:游戏/娱乐

## 证据(README 行号)

> L11: **Reversed Snake** is a free, open-source **browser game** built with **Vanilla JavaScript** and **HTML5 Canvas**. 
> L13: The Snake is controlled by a sophisticated pathfinding algorithm (**A\* Search**) that ruthlessly hunts you down. A

## 星数曲线

```mermaid
xychart-beta
    title "ImBIOS/lab-snake-reverse 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-30 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `188888d48148` · [字段定义](../../DATASET.md)*
