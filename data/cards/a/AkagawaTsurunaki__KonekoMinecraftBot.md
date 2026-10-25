# AkagawaTsurunaki/KonekoMinecraftBot

⭐ 44 · TypeScript · Apache-2.0 · 推送 2025-12-22 · [GitHub](https://github.com/AkagawaTsurunaki/KonekoMinecraftBot) · [官网](https://github.com/AkagawaTsurunaki/KonekoMinecraftBot) · 个人维护 · 中文 README

**基于有限状态机与机器学习算法的 Minecraft 游戏机器人**

用 TypeScript 与 mineflayer 编写的 Minecraft 机器人：以有限状态机为核心行为框架，每秒更新各状态转移值并按值比较切换状态；内置攻击敌怪、跟随玩家、协助收割/伐木、自动进食、睡觉、钓鱼等 12 种状态与聊天指令，配合 DB-Scan 聚类识别树木、单层感知机加权计算行为参数。提供浏览器实时查看状态图。支持 Minecraft 1.20.1/1.20.2/1.20.6，需 Node.js 20.17.0，通过 npm 安装依赖后以 npx tsx 启动。作者自述仍存在意外行为，状态机实现当前按值比较而非概率分布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 有限状态机驱动，转移值每秒（20 游戏刻）更新并按值比较切换
- DB-Scan 聚类识别周围树木，单层感知机加权计算行为参数（多数可手动调节）
- 浏览器实时查看动态更新的状态图（默认 http://127.0.0.1:5689）
- 支持聊天指令与自定义状态、算法、FSM 扩展（./src/fsm/impl）

## 适用场景

- 在单人或多人服务器中让机器人陪伴玩家作战、耕种与伐木
- 通过 Minecraft 聊天指令让机器人执行播种、收割、停止等操作
- 在其 FSM 框架上实现自定义机器人技能与状态

## 场景标签

 · 领域:游戏/AI 机器人

## 证据(README 行号)

> L9: `KonekoMinecraftBot` is an intelligent Minecraft bot based on **Finite State Machine** and some **Machine Learning
> L189: ## Machine Learning Algorithm
> L193: To search around log blocks and classify them as many clusters to identify the tree.

## 星数曲线

```mermaid
xychart-beta
    title "AkagawaTsurunaki/KonekoMinecraftBot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-25 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `09f23ebe88c3` · [字段定义](../../DATASET.md)*
