# ankurCES/WOPR_TUI_2026

⭐ 17 · Rust · MIT · 推送 2026-07-07 · [GitHub](https://github.com/ankurCES/WOPR_TUI_2026) · 个人维护

**复刻1983年 WarGames WOPR 的冷战模拟终端游戏**

用 Rust 编写的终端 UI 冷战模拟游戏：玩家扮演军事顾问，在 ASCII 世界地图上应对升级的地缘政治危机，包含 DEFCON 5→1 分级系统、多语言情报拦截、导弹轨迹动画与 CRT 风格开机序列。危机场景由 LLM 生成（每回合4个选项，含后果启发式与终局检测），支持 Anthropic Claude、MiniMax 或内置 Stub 提供方（6个预置场景，无需 API key）。通过一键安装脚本或 cargo 从源码构建，读取 ~/.blumi/settings.json 配置 LLM。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 生成危机场景，每回合提供 4 个决策选项与终局检测
- DEFCON 5→1 分级系统与颜色编码升级展示
- 内置 Stub 提供方含 6 个预置场景，无需 API key 即可游玩
- 多语言情报拦截（英文/俄文西里尔/简体中文）与 ASCII 世界地图动画

## 适用场景

- 在终端里体验 WarGames 风格的核危机决策模拟
- 接入 LLM 获得每次不同的生成式危机剧情
- 作为 ratatui 终端游戏实现的学习样例

## 场景标签

 · 领域:游戏/终端娱乐

## 证据(README 行号)

> L22: **WOPR TUI 2026** brings that experience to your terminal. You step into the role of a military advisor at a Cold W
> L39: - **AI Scenario Engine** — LLM-generated crises with 4 player options per turn, consequence heuristics, and endgame
> L89: No config needed to play — falls back to the stub provider with 6 built-in scenarios.

## 星数曲线

```mermaid
xychart-beta
    title "ankurCES/WOPR_TUI_2026 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `db607c55a0d2` · [字段定义](../../DATASET.md)*
