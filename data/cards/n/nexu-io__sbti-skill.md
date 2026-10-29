# nexu-io/sbti-skill

⭐ 31 · JavaScript · MIT · 推送 2026-04-10 · [GitHub](https://github.com/nexu-io/sbti-skill) · [官网](https://github.com/nexu-io/nexu) · 组织维护 · 中文 README

**给 AI agent 的 SBTI 赛博人格测试技能，30 题出 27 种人格**

以 SKILL.md 形式提供的纯 prompt 技能，安装到 OpenClaw 类 agent（nexu 桌面客户端）后可运行：30 道题、5 大模型×15 维度计分，生成 15 位等级码并与 25 种标准人格模式做曼哈顿距离匹配，输出人格代码、雷达图、深度解读、TOP 3 匹配等。支持测用户本人（逐题作答）或让 AI agent 以自身视角自测；结果可一键部署为 nexu.space 分享落地页。无依赖，git clone 即用，含 2 种特殊人格（兜底与隐藏彩蛋）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 30 题 × 15 维度（自我/情感/态度/行动/社交 5 模型）计分体系
- 曼哈顿距离匹配 25 种标准人格模式，<60% 兜底为 HHHH
- 支持让 AI agent 以自身视角自测人格
- 结果可部署为 nexu.space 可分享落地页

## 适用场景

- 在 nexu/OpenClaw agent 里玩 SBTI 人格测试
- 让 AI agent 自测，看它的'赛博人格'
- 生成可分享的人格测试结果页面

## 场景标签

 · 领域:娱乐/agent 技能

## 证据(README 行号)

> L8: 互联网最火的沙雕人格测试，现在可以在你的 AI agent 里玩了。
> L14: > 🧠 **SBTI 赛博人格测试** 是 nexu 生态的一部分 — 可一键安装的开源 OpenClaw 桌面客户端。
> L126: 30 道题 → 维度计分 → 等级转换 → 人格匹配 → 结果展示

## 星数曲线

```mermaid
xychart-beta
    title "nexu-io/sbti-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-29 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `733157ea2d65` · [字段定义](../../DATASET.md)*
