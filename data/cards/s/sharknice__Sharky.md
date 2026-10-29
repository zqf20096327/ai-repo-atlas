# sharknice/Sharky

⭐ 45 · C# · 推送 2026-10-16 · [GitHub](https://github.com/sharknice/Sharky) · 个人维护

**C# 编写的星际争霸2 AI 机器人开发框架**

面向星际争霸2 AI bot 开发者的 C# 框架：封装游戏接口设置与每帧更新流程，提供 Manager（建造/微操/单位/地图/目标）分层架构，支持三族与 Random、多建造序列动态切换、敌方策略识别、基于每帧微操的采矿与战斗控制、A* 寻路与地图网格数据、聊天回复配置及对局结果保存。开发者可克隆源码或通过 NuGet 包引入，需自行安装星际争霸2及天梯地图。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Manager 分层架构：BuildManager/MicroManager/UnitManager/MapManager/TargetingManager 每帧更新
- 支持三族与 Random，可按对局与敌方策略动态切换建造序列
- MicroTask 按优先级执行采矿、防守、骚扰、虫卵注射等任务，每类单位可配独立微操控制器
- 按帧更新地图网格数据（敌方对空/对地 DPS、视野、可通行区域）并支持 A* 寻路

## 适用场景

- 开发参加 AI Arena 天梯的星际争霸2 bot
- 在框架上实现自己的建造策略、微操逻辑或机器学习决策
- 通过聊天 JSON 配置让 bot 回应玩家聊天与宣告进攻

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L2: A C# framework for developing StarCraft 2 AI bots
> L4: The goal of Sharky is to provide a framework that handles all the complex setup and mundane details of creating a bo

## 星数曲线

```mermaid
xychart-beta
    title "sharknice/Sharky 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-29 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `659c87a7cc97` · [字段定义](../../DATASET.md)*
