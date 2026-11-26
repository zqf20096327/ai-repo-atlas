# procoder-net/notisift

⭐ 3 · Kotlin · MIT · 推送 2026-11-09 · [GitHub](https://github.com/procoder-net/notisift) · [官网](https://github.com/procoder-net/notisift/releases/latest) · 个人维护

**按单条通知分拣的 Android 离线通知整理器，AI 可选**

面向 Android 用户的通知整理应用：以单条通知（而非应用或渠道）为粒度，将通知分为 Important、Later、Junk 三层并归入分组。决策顺序为内置离线规则优先，用户规则覆盖一切，AI 决策模型为可选项（自带 key，支持多家云模型、本地 Ollama/LM Studio 或手机端 Gemini Nano）。无账号、无服务器，被归入 Later/Junk 的通知保留 14 天且可恢复；新安装默认 Preview 模式不移动任何通知。提供 APK 下载或源码自行构建（JDK 17+、Android SDK 36）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按单条通知而非应用分拣到 Important/Later/Junk 三层并自动分组
- 内置离线规则可独立工作，AI 为可选层，支持本地模型（Ollama/LM Studio）与手机端 Gemini Nano
- 自然语言输入生成规则卡片，附撤销机制
- 无账号无服务器；Later/Junk 保留 14 天且可从 Cleared 恢复

## 适用场景

- 同一应用的重要消息置顶而促销通知静音隐藏
- 将可延后的通知定时（如早晚各一次）集中送达
- 全程离线使用本地模型整理通知，数据不出手机
- 对群聊设置仅被提及时提醒

## 场景标签

 · 领域:移动工具/通知管理

## 证据(README 行号)

> L9: **Show Amazon deliveries, hide Amazon deals.** Android only lets you control notifications per app or channel.
> L25: > - **No AI? Still works.** Built-in on-phone rules make the same decisions offline. The model makes them sharper.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `2417990bab0c` · [字段定义](../../DATASET.md)*
