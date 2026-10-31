# Predictable-Dialogs/agent-embed

⭐ 16 · TypeScript · AGPL-3.0 · 推送 2026-10-05 · [GitHub](https://github.com/Predictable-Dialogs/agent-embed) · [官网](https://predictabledialogs.com/docs/category/widgets) · 组织维护

**网站嵌入 AI 聊天组件库：接入 Predictable Dialogs 后端**

提供可嵌入网页的 AI 聊天前端组件（Bubbles、Standard、Popup 及 Topic Buttons），通过 script/JS 引入 CDN 包后初始化，与 Predictable Dialogs 后端通信，后端再调用 OpenAI LLM。前提是先在其官网创建 agent；apiHost 可指向自有后端。支持 initialPrompts 起始提示卡片、filterResponse 响应处理函数、气泡按钮主题与放置位置配置，并提供 open/close/toggle 等 JS 命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Bubbles / Standard / Popup / Topic Buttons 四类嵌入组件
- apiHost 与 agentName 可配置为自有后端
- initialPrompts 起始提示卡片与 filterResponse 响应自定义处理
- 气泡按钮的主题样式、左右放置与预览消息配置

## 适用场景

- 在我的网站上加一个 AI 聊天助手
- 通过 Topic Buttons 在页面预置话题入口
- 把聊天气泡按钮样式与品牌风格统一

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L6: The agent-embed repository provides components which can be embedded on a website and communicates with the predicta
> L21:   import Agent from 'https://cdn.jsdelivr.net/npm/@agent-embed/js@latest/dist/web.js'

## 星数曲线

```mermaid
xychart-beta
    title "Predictable-Dialogs/agent-embed 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6ec8ca07ea54` · [字段定义](../../DATASET.md)*
