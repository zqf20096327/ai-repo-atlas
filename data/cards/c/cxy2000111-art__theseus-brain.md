# cxy2000111-art/theseus-brain

⭐ 17 · Python · GPL-3.0 · 推送 2026-08-13 · [GitHub](https://github.com/cxy2000111-art/theseus-brain) · 个人维护 · 中文 README

**供 AI 通过 MCP 游玩的中文纯文字 roguelike 游戏服务器**

《忒修斯之脑》是一座以身体改造争论为背景的纯文本轮回 roguelike：玩家一世一世地死，机化率跨世累积且不可逆。本体是一个零依赖、仅需 Python 3 的 MCP stdio 服务器，提供 new_run/choose/bequeath 等七个工具，供 Claude 等 AI 客户端代人类游玩；也可用 --cli 在终端由人直接玩，或经 http_bridge.py 以 HTTP 端点供手机接入。含 2d6 检定、按机化率衰减的技能传承、跨世回响与手写记忆词条机制，附 1273 条剧情单元的英文语言层与七道门禁自测。代码 GPL-3.0，文案 CC BY-SA 4.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP（stdio/JSON-RPC 2.0）服务器形态，七个工具供 AI 代玩，零依赖仅需 Python 3.8+
- 机化率跨世累积不可逆、技能传承按机化率掷骰衰减的轮回机制
- --cli 终端模式供人直接游玩；http_bridge.py 提供 HTTP 桥（会话隔离/访问令牌）
- 每世终结可手写 10 条记忆词条，独立掷骰决定是否传给下一世
- 断线续档：存档含 RNG 状态，客户端重启不丢进度

## 适用场景

- 让 Claude 等 AI 客户端通过 MCP 代我玩这个轮回 roguelike
- 自己坐到终端前用 CLI 模式玩
- 通过 HTTP 桥在手机 App 上接着玩同一条世系

## 场景标签

 · 领域:游戏/交互式小说

## 证据(README 行号)

> L59: 工具有七个：`new_run` / `choose` / `status` / `legacy` / `bequeath` / `debrief` / `recite`。
> L146: python3 server.py --cli       # 终端交互，人可以自己玩

## 星数曲线

```mermaid
xychart-beta
    title "cxy2000111-art/theseus-brain 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-29 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `4e86edc11b8a` · [字段定义](../../DATASET.md)*
