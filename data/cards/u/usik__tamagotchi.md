# usik/tamagotchi

⭐ 15 · Python · MIT · 推送 2026-05-14 · [GitHub](https://github.com/usik/tamagotchi) · 个人维护

**终端里的电子宠物鸡：完整养成玩法，并对 AI 编码代理会话做出反应**

在终端中运行的 Tamagotchi 虚拟宠物游戏，复刻原版机制：饥饿、快乐、体重、纪律、健康、生病、睡眠与 6 个生命阶段，照顾质量决定 3 条进化路线，宠物在游戏关闭后仍实时成长。面向不离 CLI 的开发者：宠物通过钩子对 Claude Code、Aider、Goose 等 AI 编码代理的会话状态实时反应（如测试通过 Happy +2）。提供 tmux/Starship 集成、tama share ASCII 分享卡、JSON 输出与 Python 插件系统，支持 curl/pip/npm 安装。

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

- 完整 Tamagotchi 机制：6 个生命阶段与 3 条照顾驱动的进化路线
- 宠物对 Claude Code / Aider / Goose 会话状态实时反应（如测试通过 Happy +2）
- tama share 生成 ASCII 分享卡并可上传 Gist 嵌入 GitHub README
- tmux 状态栏 / Starship 提示符 / JSON 输出集成与 Python 插件系统

## 适用场景

- 在终端养一只虚拟宠物陪伴日常编码
- 让宠物根据我的 AI 编码代理工作状态做出反应
- 在 GitHub README 或 Discord 分享宠物 ASCII 卡片

## 场景标签

 · 领域:游戏/终端娱乐

## 证据(README 行号)

> L3: > Raise a virtual pet that lives in your terminal. A faithful recreation of the original Tamagotchi — hunger, happin
> L27: - **AI agent plugins** — pet reacts to Claude Code, Aider, and Goose sessions in real time

## 星数曲线

```mermaid
xychart-beta
    title "usik/tamagotchi 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b691ad993443` · [字段定义](../../DATASET.md)*
