# sibylsea-hub/heros3-agent-companion

⭐ 5 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/sibylsea-hub/heros3-agent-companion) · 个人维护 · 中文 README

**让 AI agent 陪你玩英雄无敌3（VCMI）的游戏 mod**

在开源引擎 VCMI 上打补丁的游戏 mod，把能在本机跑命令、读写文件的 agent（Claude Code、Codex、Gemini CLI 等）接入英雄无敌3：游戏内常驻聊天标签、每回合读存档生成实时陪玩汇报（含剧透保护）、agent 可作为热座玩家接管某个颜色、提供不触发作弊标记的 GM 改动命令，以及从字符画生成 .h3m 地图并写入告示牌/事件/藏信等叙事物件的地图工具。所有数据留在本地。Windows 可玩，Mac 开发中；需自行用 Visual Studio 2022 编译打补丁的 VCMI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 游戏内常驻聊天窗口，Tab 原版聊天栏消息也能收到
- 每回合读自动存档生成局面汇报，带剧透保护与本地记忆
- agent 可作为本地玩家接管颜色，超时由游戏 AI 兜底
- 字符画→.h3m 地图生成，支持藏信、事件、传记等叙事元素

## 适用场景

- 让 AI agent 加入英雄无敌3战局当盟友或对手
- 和 AI 边玩边聊天，获得回合局势提示
- 让 AI 生成带个人化彩蛋和藏信的自定义地图
- 不触发作弊标记地修改游戏内资源与状态

## 场景标签

 · 领域:游戏/娱乐

## 证据(README 行号)

> L5: 在 VCMI（开源的英雄无敌 3 引擎）上打了一层补丁，让你的 AI 坐进你的游戏里：陪你玩、跟你聊、替你改、当你的盟友，还会给你写地图、在地图里给你藏信。
> L7: 只要是能在你电脑上跑命令、读写文件的 agent 都能用：Claude Code、Codex、Gemini CLI……工具都是普通的命令行程序，说明写在 `AGENTS.md` 里，agent 读了就会用。我们本机用的是 Claud
> L61: - **换颜色显示**：不喜欢红色？任意两个颜色可以对调显示：界面、旗子、小地图、颜色名都跟着换。只改画面，不改规则和存档。

## 星数曲线

```mermaid
xychart-beta
    title "sibylsea-hub/heros3-agent-companion 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-22"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-10-20 5 → 2026-11-22 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `6d471c736000` · [字段定义](../../DATASET.md)*
