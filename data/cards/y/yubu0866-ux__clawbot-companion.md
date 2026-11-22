# yubu0866-ux/clawbot-companion

⭐ 5 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/yubu0866-ux/clawbot-companion) · 个人维护 · 中文 README

**微信一对一 AI 陪伴聊天机器人桥接程序**

通过微信官方 ClawBot/iLink 机器人通道接入个人微信私聊的陪伴型机器人桥：以本地 JSON/Markdown 配置定义角色人设与生活事实，内置主动消息决策引擎（时段/概率/静默判断）与按日采样的有机模式，支持风格微调、情景记忆、内容包管理，以及可选的图/视频生成接口与音频交付检查。默认走 OpenAI 兼容格式 API，也可用文件队列的 agent 模式；会话与状态仅存本地。单机 Python 运行，支持 Linux 与 Windows。

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

- 走微信官方 ClawBot/iLink 通道，以官方机器人身份一对一私聊
- 人设/生活事实/内容包全配置驱动，仓库自带 3 份示例人设
- 主动消息只做决策不直接生成文案，含情绪模型与有机模式
- 入站媒体理解（图片/视频抽帧/语音转写）与出站媒体质检

## 适用场景

- 在微信里维持一个设定一致的角色日常陪伴聊天
- 换配置文件快速切换不同角色人设
- 本地化保存聊天状态、不依赖第三方云端存储

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: > An open-source WeChat companion bridge: a long-running bot that chats with one user in WeChat, keeps a consistent 
> L5: 一个开源的微信陪伴型机器人桥接程序：它以一个设定一致的虚构角色与单个使用者日常聊天，支持主动问候、风格微调、内容包（衣橱/场景/表情/妆容）与可选的媒体生成接口。默认通过兼容 OpenAI 格式的 API 生成回复，也支持文件队列驱
> L15: - **通道**：走微信官方 ClawBot / iLink 机器人通道，以官方机器人身份接入个人微信一对一私聊；不走个人号协议逆向（那类接法有封号风险，也不建议用主力号），不需要企业微信或公众号资质。

## 星数曲线

```mermaid
xychart-beta
    title "yubu0866-ux/clawbot-companion 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-11-22"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-10-28 5 → 2026-11-22 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `f05fba930fb6` · [字段定义](../../DATASET.md)*
