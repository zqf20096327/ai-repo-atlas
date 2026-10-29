# deseven/mod-pbc

⭐ 63 · C++ · Unlicense · 推送 2026-10-04 · [GitHub](https://github.com/deseven/mod-pbc) · 个人维护

**为 AzerothCore/Playerbots 机器人加 LLM 性格层的模块**

AzerothCore 模块，基于 mod-playerbots 为游戏机器人叠加性格层：角色卡、事件触发回复（聊天/拾取/升级/Boss 击杀等，按可配置概率）、超限后提炼带重要性评分的长期记忆、角色间及与玩家的关系追踪。提示词发送到兼容的 LLM API，响应由角色在游戏内说出；战斗/移动等机器人逻辑不变。通过 git clone 或源码包放入 modules 目录后重编译服务器安装，依赖 nlohmann/json 与 cpp-httplib 已内置捆绑，另含可选 HTTP/WS 服务器与 Web 管理界面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Unlicense |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 事件驱动回复：基于角色卡、历史、关系与实时上下文构建提示词调用 LLM API
- 历史超限时提炼带重要性评分的叙述式记忆，按 token 预算选取
- 角色间及角色与玩家之间的关系追踪与更新
- 可选内置 HTTP/WS 服务器与 Web 界面，管理历史/关系/记忆

## 适用场景

- 在私服中与有性格、记忆和关系的机器人队友一起剧情化练级
- 为 mod-playerbots 机器人编写角色卡并展开长期互动
- 通过 Web 界面或 API 编辑聊天历史、关系与记忆

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: `mod-playerbots-characters` (or `mod-pbc` for short) is an AzerothCore module built around mod-playerbots, breathing
> L11: Characters react to in-game events (chat, item pickups, duels, level-ups, boss kills, quests) based on configurable

## 星数曲线

```mermaid
xychart-beta
    title "deseven/mod-pbc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-29 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `64b6605381b2` · [字段定义](../../DATASET.md)*
