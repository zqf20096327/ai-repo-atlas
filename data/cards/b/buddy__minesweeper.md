# buddy/minesweeper

⭐ 18 · JavaScript · 推送 2026-10-17 · [GitHub](https://github.com/buddy/minesweeper) · 组织维护

**LLM agent 扫雷基准：同一棋盘让至多九个模型并行对局**

在完全相同的规则、工具层与种子下，让最多九个 AI 模型并行玩扫雷：同一颗种子生成所有赛道的地雷与开局格子，各模型同一时刻开始，按同一时钟计时。计分维度为揭开安全格比例、耗时与 token 成本，区分 turn（交还棋盘次数）与 move（改变棋盘的调用）。前端为无依赖、无构建步骤的原生 HTML/CSS/JS，结束后生成揭示速度图表与排名表。要求 Node 22+，无安装步骤，通过 .env 填入各 provider API key 后运行 node server.mjs，密钥仅存于监听 127.0.0.1 的本地服务端。

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

- 同一种子构建所有赛道，保证各模型面对相同棋盘
- 至多九个模型并行对局，同一时钟计时
- 按揭开比例、耗时与 token 成本计分并生成排名
- 无依赖无构建的前端，密钥仅存于本地代理服务端

## 适用场景

- 横向比较多个 LLM 在同一推理任务上的表现与成本
- 录制模型对局过程用于展示或分析
- 快速本地搭建多模型扫雷评测环境

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L1: # Minesweeper · AI agent benchmark
> L7: Up to nine AI models play Minesweeper side by side, under the same rules and the same tool layer, so
> L10: clock, which is what makes the times worth comparing. Each is scored on how much of the board it

## 星数曲线

```mermaid
xychart-beta
    title "buddy/minesweeper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `575f380bbea7` · [字段定义](../../DATASET.md)*
