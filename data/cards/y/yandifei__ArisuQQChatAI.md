# yandifei/ArisuQQChatAI

⭐ 18 · Python · LGPL-2.1 · 推送 2026-01-01 · [GitHub](https://github.com/yandifei/ArisuQQChatAI) · [官网](https://github.com/yandifei/ArisuQQChatAI) · 个人维护 · 中文 README

**接入 DeepSeek API 的 QQ 群自动回复 AI 机器人**

基于 uiautomation 与 PyQt6 的 Windows 桌面程序，通过 DeepSeek API 在多个 QQ 群中自动回复消息。支持自定义人设与上下文对话，提供关键词回复策略、发送者过滤、权限分级、指令系统与插件机制（联网搜索、发图、时间查询等）。需自备 DeepSeek API 密钥，且需将 QQ 主题设为“极简白”以配合界面自动化；开发者声明权限系统存在设计缺陷（权限可被复制），且不处理 issues。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | LGPL-2.1 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 DeepSeek API 自动回复 QQ 群消息，支持自定义人设与上下文
- 插件系统实现多模态与 LLM 外部操作执行（联网搜索、发图等）
- 关键词/发送者级别的自定义回复策略与权限分级
- 全局异常捕获、线程自动重启与日志轮替

## 适用场景

- 让自己的 QQ 群有 AI 自动聊天回复
- 通过人设与上下文配置打造特定性格的群聊 AI
- 用插件扩展机器人的搜索、发图等能力

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L12:  - 使用deepseek的api自动回复
> L31:  - 插件工具实现了LLM的外部感知和操作执行，一个真正能干活的Agent
> L81: - 💡此软件的根本目的是打造接入DeepSeek的API接口实现“满分”🧠的问题解答和为用户提供《情绪价值💖》！

## 星数曲线

```mermaid
xychart-beta
    title "yandifei/ArisuQQChatAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `44b7e8b9db95` · [字段定义](../../DATASET.md)*
