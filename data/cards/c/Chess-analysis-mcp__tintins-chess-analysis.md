# Chess-analysis-mcp/tintins-chess-analysis

⭐ 52 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/Chess-analysis-mcp/tintins-chess-analysis) · [官网](https://chess-analysis-mcp.github.io/tintins-chess-analysis/) · 个人维护

**Stockfish 引擎复盘加 LLM 讲解的国际象棋教练应用**

单进程 Python 应用：内置 Stockfish 引擎池对整局棋复盘，输出失误清单、胜率图、评估条与着法箭头，可从 Lichess/Chess.com 按用户名拉取或粘贴 PGN 导入棋局。AI 讲解部分通过 headless claude -p（使用 Claude 订阅）或本地模型/OpenAI 兼容提供者运行，把引擎结论转成自然语言；引擎复盘本身无需 AI 即可工作。同时提供 Claude Code 的 MCP 服务器与共享同一引擎会话的 FastAPI 网页棋盘，另有带 Glicko-2 评分的战术题训练模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Stockfish 全局复盘：失误清单、逐侧准确率、胜率图、多 PV 箭头
- AI 教练（Snowie）基于引擎事实生成文字讲解与对话
- MCP 服务器与网页棋盘共享同一引擎与复盘会话
- 战术题训练（Glicko-2 评分、Storm 计时、自身失误转化为题目）

## 适用场景

- 复盘 Lichess/Chess.com 或粘贴 PGN 的对局并看文字解释
- 在 Claude Code 终端里做棋局分析
- 针对自己反复出现的失误模式做战术训练

## 场景标签

 · 领域:游戏/棋类分析工具

## 证据(README 行号)

> L9: real **Stockfish** lines instead of guessed. Under the hood it reviews your game with the engine and
> L34: > engine review itself (mistake list, eval bar, win graph, arrows) works without any of it.

## 星数曲线

```mermaid
xychart-beta
    title "Chess-analysis-mcp/tintins-chess-analysis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 50 --> 53
    line [51, 52]
```

2026-10-18 51 → 2026-10-25 52（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2d7fa458509b` · [字段定义](../../DATASET.md)*
