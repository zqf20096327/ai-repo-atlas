# bamboosir1109/dsh-lanya

⭐ 4 · Python · MIT · 推送 2026-11-20 · [GitHub](https://github.com/bamboosir1109/dsh-lanya) · [官网](https://bamboosir1109.github.io/dsh-lanya/) · 个人维护 · 中文 README

**QQ 角色集成包：接入聊天、B站互动、语音与记忆**

面向 DeepSeek Harness 的可扩展 QQ 角色集成包，将 QQ 接入（NapCatQQ / SnowLuma 双后端，经 OneBot v11）、B 站内容互动、本地 GPT-SoVITS 语音、可塑记忆与日记、自主活动与本地控制台组合到同一角色，由一个主 LLM 统一决策回复、调用工具或保持安静。当前为开发预览，插件、QQ 后端、语音引擎等组件需分别安装配置，仅支持 Windows 10/11，数据保存在本机。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- NapCatQQ / SnowLuma 双 QQ 后端，共用一套人设与记忆
- 主 LLM 统一决策对话、B站评论回复与自主活动
- 可塑记忆与日记：短期上下文、长期事实、压缩与来源记录
- 本地控制台查看连接、活动、记忆与每日费用估值

## 适用场景

- 给自己的 QQ 账号接入一个有记忆和日常的角色
- 让角色浏览 B 站视频并决定是否评论或回复
- 接入本地 GPT-SoVITS 实现可播放的语音回复

## 场景标签

`聊天机器人` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: **面向 DeepSeek Harness 的可扩展 QQ 角色集成包。**
> L44: 可以使用岚娅的风格，也可以换成你自己的角色。同一个主 LLM 带着人设、近期对话和记忆，选择回应、调用工具或安排下一件事。
> L75: **DSH 插件**提供角色提示词、调度和控制台入口；**Windows 配套服务**连接 QQ、记忆、表情、B 站等能力。外部插件与服务按需配置。

## 星数曲线

```mermaid
xychart-beta
    title "bamboosir1109/dsh-lanya 星数(近 3 点)"
    x-axis ["2026-11-12", "2026-11-19", "2026-11-24"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-12 3 → 2026-11-24 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `38c0717f7955` · [字段定义](../../DATASET.md)*
