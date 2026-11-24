# rayanrejeb/ai-chess-coach

⭐ 6 · Python · GPL-3.0 · 推送 2026-11-09 · [GitHub](https://github.com/rayanrejeb/ai-chess-coach) · 个人维护

**桌面国际象棋教练：拉取棋局、Stockfish 评分并用 Gemini 讲解**

桌面应用：从 Chess.com 与 Lichess 增量同步棋局，用两个并行 Stockfish 进程为每步评分（按损失胜率分级），标记战术动机，再由 Gemini 按每段最多 24 plies 写逐着评论；聊天中可就任意局面提问，Gemini 可调用 evaluate_position 工具查询引擎。应用对每条回答做落点核验（grounding check），未通过的一次退回修正。仅在 Windows 11 + Python 3.13 上测试，Gemini 免费层有每日请求限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Stockfish 双进程并行分析，结果按局面/深度/线路缓存
- Gemini 以 Stockfish 为工具回答 what-if 提问
- 聊天与评论的走法落点核验，未验证回答标注提示
- Chess.com 按月、Lichess 流式的增量同步

## 适用场景

- 复盘自己在 Chess.com/Lichess 的对局并追问失误原因
- 在单一窗口快速批量浏览两平台的棋局
- 让引擎核验 AI 给出的着法建议

## 场景标签

 · 领域:游戏/棋类分析工具

## 证据(README 行号)

> L7: AI Chess Coach downloads your games, rates every move with Stockfish and has Gemini write a comment for each one. Yo
> L77: The moves go to Gemini in parts of at most 24 plies and 40,000 characters of data, with their rating, engine lines 

## 星数曲线

```mermaid
xychart-beta
    title "rayanrejeb/ai-chess-coach 星数(近 3 点)"
    x-axis ["2026-11-10", "2026-11-22", "2026-11-24"]
    y-axis "stars" 4 --> 7
    line [5, 6, 6]
```

2026-11-10 5 → 2026-11-24 6（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `97aa113264df` · [字段定义](../../DATASET.md)*
