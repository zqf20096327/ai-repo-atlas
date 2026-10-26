# ttxttx1111/sts2-llm

⭐ 41 · Python · MIT · 推送 2026-07-28 · [GitHub](https://github.com/ttxttx1111/sts2-llm) · 个人维护 · 中文 README

**让 GitHub Copilot 代理接管并复盘《杀戮尖塔 2》对局的定制包**

面向《Slay the Spire 2》的 GitHub Copilot customization pack：通过 STS2MCP 的 MCP 工具读取游戏状态并执行打牌、选奖励、走地图、商店、火堆等操作，由 `player.agent.md` 作为入口在 piloting/review/research 之间切换。提供四层记忆（run playbook、timeline、复盘 archive、跨局 lesson ledger），核心循环为 play->timeline->review->archive->compress->recall->revise。需 Windows、Steam 版游戏、STS2MCP mod 与本地 15526 服务；`deprecated/` 目录保留三组历史版本快照。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 经 STS2MCP MCP 工具读取状态并执行打牌/奖励/路线/商店等游戏动作
- 四层记忆系统：playbook、timeline、复盘 archive、跨局 lesson ledger
- 战斗安全协议：读状态->验证牌->执行->重读，避免手牌索引漂移
- 提供 VS Code 与 Copilot CLI 两种 MCP 配置参考

## 适用场景

- 让 Copilot CLI 或 VS Code 代理接管当前 run 对局
- 对死亡/胜利/关键节点做复盘并沉淀跨局经验
- 对不确定策略问题做外部研究再结合牌局落地

## 场景标签

`AI 助手` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: 一个面向《Slay the Spire 2》的 GitHub Copilot 玩家代理定制包：让 Copilot CLI / VS Code 通过 STS2MCP 读取游戏状态、做当前 run 决策、复盘失败与胜利，并把经验沉淀成可
> L9: - **真实接管游戏**：通过 STS2MCP 的 MCP 工具读取状态、打牌、选奖励、走地图、进商店、火堆与事件。
> L38: - GitHub Copilot CLI：推荐的本地命令行玩家入口。

## 星数曲线

```mermaid
xychart-beta
    title "ttxttx1111/sts2-llm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-26 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `04b92abb788b` · [字段定义](../../DATASET.md)*
