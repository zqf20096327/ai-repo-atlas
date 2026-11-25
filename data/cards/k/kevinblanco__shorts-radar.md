# kevinblanco/shorts-radar

⭐ 6 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/kevinblanco/shorts-radar) · 个人维护

**找出跑赢自身频道的 YouTube Shorts，AI agent 生成拍摄提案**

由两部分组成：一条 Python 管道，通过 SerpApi 的五个引擎（Trends、YouTube 搜索、视频、频道、字幕）抓取某细分领域的 Shorts，用三个相对自身频道的指标（×频道、每日浏览、每订阅者浏览）计算 0-100 雷达分并输出 JSON；一个 shorts-strategist agent 技能，供 Claude Code 或其他 MCP 客户端读取该 JSON，经 SerpApi MCP server 复核后产出三条 Short 提案、一页 brief 与领域快照。每次运行最多 42 次 SerpApi 搜索，结果缓存于本地。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五引擎 SerpApi 管道：搜索→Shorts→视频详情→频道基线→逐字开场白
- 以自身频道中位数为基准的三指标百分位评分（0-100）
- 本地缓存使同一搜索的第二次运行零消耗
- 随附 .mcp.json 与 shorts-strategist 技能，接入 Claude Code 等 MCP 客户端

## 适用场景

- 为自己的频道找可模仿模式的 Shorts 选题
- 让 agent 基于当日 YouTube 数据生成拍摄提案
- 在预算内评估某细分领域的 Shorts 表现格局

## 场景标签

`网页抓取` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L8: 2. **An agent** (`shorts-strategist`) for Claude Code or any MCP client. It reads that JSON, re-checks the top Short
> L62: Approve the `serpapi` server when asked, then ask: *"What Shorts should I make next in ai agents?"* The agent reads

## 星数曲线

```mermaid
xychart-beta
    title "kevinblanco/shorts-radar 星数(近 3 点)"
    x-axis ["2026-11-12", "2026-11-21", "2026-11-25"]
    y-axis "stars" 4 --> 7
    line [5, 6, 6]
```

2026-11-12 5 → 2026-11-25 6（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `73a627e5d671` · [字段定义](../../DATASET.md)*
