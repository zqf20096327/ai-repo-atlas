# muhiris/wgpt

⭐ 25 · JavaScript · 推送 2026-03-09 · [GitHub](https://github.com/muhiris/wgpt) · 个人维护

**终端里免 API key 与 Google Bard 对话的 CLI 工具**

基于 Node.js/npm 的命令行工具，通过读取用户在 bard.google.com 登录后的 __Secure-1PSID cookie 建立会话，无需官方 API key 即可在终端向 BardAI 发送消息、获取回复，并支持改写消息或附加代码片段。面向想在终端环境中实验 AI 对话与生成回复的开发者。全局安装后以 wgpt 命令直接调用，首次运行需粘贴 cookie 完成配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无需 API key，通过 __Secure-1PSID cookie 接入 Bard
- 终端内发送消息、获取回复
- 支持消息改写与附加代码片段

## 适用场景

- 在终端快速与 Bard 对话实验
- 无需申请 API key 体验 AI 聊天
- 命令行里生成或改写文本与代码片段

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: `wgpt` is an npm package that allows you to interact with BardAI right from your terminal. With `wgpt`, you can easi
> L18: To get started with the CLI tool, you'll be asked to provide a cookie from `https://bard.google.com/`. First, log i

## 星数曲线

```mermaid
xychart-beta
    title "muhiris/wgpt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6c9efd1be382` · [字段定义](../../DATASET.md)*
