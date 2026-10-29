# MeiFagundes/PolarisAI

⭐ 19 · C# · GPL-3.0 · 推送 2026-10-13 · [GitHub](https://github.com/MeiFagundes/PolarisAI) · [官网](https://meifagundes.com/polaris-ai/) · 个人维护

**.NET Core 个人助理原型：意图分类并生成回复**

基于 .NET Core 构建的个人助理原型，提供 REST Web API。核心机制：用 Starlight（ML.NET）对用户查询做意图分类，再根据预测意图选取回复文本；内置闹钟、提醒、天气、新闻、音乐、通话与闲聊等意图和响应代码。API 暴露 query 与 debug 路由，并将请求详情记录到配置的数据库。README 仅含介绍与一个 2019 年的闹钟示例，未提供安装运行说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 使用 Starlight 进行意图分类，按预测意图选取回复
- 内置闹钟、提醒、天气、新闻、音乐、通话、闲聊等意图与响应
- 暴露 query 与 debug 两个 REST 路由
- 请求详情记录到配置的数据库

## 适用场景

- 发送自然语言查询获得助理式回复（如设置闹钟）
- 通过 debug 路由查看意图分类过程
- 作为 ML.NET 意图分类应用的参考实现

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: PolarisAI is a personal-assistant prototype built with .NET Core. Its web API uses Starlight for intent classificati
> L7: The included intent and response code covers requests such as alarms, reminders, weather, news, music, calls, and sm

## 星数曲线

```mermaid
xychart-beta
    title "MeiFagundes/PolarisAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `3787c148ceb4` · [字段定义](../../DATASET.md)*
