# vybraan/vyai

⭐ 15 · Go · MIT · 推送 2026-09-16 · [GitHub](https://github.com/vybraan/vyai) · 个人维护

**终端内与 Gemini 对话的轻量 CLI 工具，支持上下文保持**

用 Go 编写的终端聊天客户端，替代用 curl 调用 Gemini API 的方式，调用时保持会话上下文。用户从 ai.google.dev 获取 API key 并通过 GOOGLE_API_KEY 环境变量配置后即可在终端中对话。提供 vim 风格键盘快捷键（多标签切换、新建/编辑/搜索会话、滚动等）。安装途径包括 Arch Linux 的 AUR 包、Windows 的 scoop bucket、以及从源码 make run / go run 运行，另有 repology 收录的发行版打包状态。

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

- 终端内调用 Gemini API 并保持会话上下文
- vim 风格快捷键：多标签、新建/编辑/搜索会话、滚动
- AUR 与 scoop 两种包管理器安装方式
- Go 语言实现，可从源码 make run 直接运行

## 适用场景

- 在终端里直接与 Gemini 对话，不想开网页或写 curl
- 用编辑器撰写长提示词后发送
- 在多个会话标签间切换并搜索历史聊天

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L2: I got tired of using `curl` to make API calls to Gemini just to have an "AI" in my terminal. I wanted something that
> L6: 1. Get a Gemini API key from ai.google.dev.

## 星数曲线

```mermaid
xychart-beta
    title "vybraan/vyai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a0a3d33ba228` · [字段定义](../../DATASET.md)*
