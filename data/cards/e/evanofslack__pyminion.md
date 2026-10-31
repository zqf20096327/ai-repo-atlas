# evanofslack/pyminion

⭐ 24 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/evanofslack/pyminion) · [官网](https://pypi.org/project/pyminion/) · 个人维护

**Dominion 卡牌游戏引擎与机器人对局模拟库**

用 Python 实现的桌游 Dominion 规则引擎：提供 API 操作游戏引擎，支持命令行人机对局、多人对局以及多个 bot 之间的自动对局。bot 通过继承 BotDecider 类并实现 action_priority / buy_priority 策略方法定义，内置 Big Money 等示例；Simulator 类可批量运行上千局对局并输出胜负统计。要求 Python 3.10 及以上，经 pypi 安装，附 /bots 与 /examples 示例目录。策略为规则式优先级列表，非机器学习模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 Dominion 完整规则与逻辑并提供 API
- BotDecider 接口可自定义出牌与购牌策略
- Simulator 批量模拟对局并输出胜负统计
- 命令行交互式人机对局

## 适用场景

- 写 bot 策略并用大量模拟对局验证胜率
- 通过 API 程序化分析 Dominion 对局
- 命令行与 bot 或多人进行对局

## 场景标签

 · 领域:游戏/模拟

## 证据(README 行号)

> L8: Pyminion is a library for executing and analyzing games of Dominion.
> L40: Defining new bots is relatively straightforward. Inherit from the


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `15d969b6df23` · [字段定义](../../DATASET.md)*
