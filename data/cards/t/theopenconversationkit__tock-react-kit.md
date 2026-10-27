# theopenconversationkit/tock-react-kit

⭐ 23 · TypeScript · MIT · 推送 2026-09-02 · [GitHub](https://github.com/theopenconversationkit/tock-react-kit) · [官网](https://doc.tock.ai) · 组织维护

**将 Tock 对话机器人嵌入网页的 React 组件工具包**

面向 Web 开发者的聊天界面工具包：通过 Bot API（可用 SSE）连接运行于 API 模式的 Tock Bot，提供对话用户界面、默认组件与动画、主题化样式（调色板/字号/尺寸/CSS 覆盖）、自定义渲染器（文本/图片/按钮）以及消息元数据与流式响应支持。可经 npm 作为 React 模块引入，或通过 unpkg 独立脚本在纯 HTML 页面使用（脚本自带 React 副本）。README 声明已被 SNCF、Enedis 等机构的对话助手用于生产环境。前提条件是需先运行一个 API 模式的 Tock Bot。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 Bot API（可用 SSE）与 Tock Bot 通信，支持流式响应
- 提供 renderChat 与可复用的 React 组件、useTock Hook
- 主题化样式：调色板、排版、尺寸及各类 CSS 覆盖
- 自定义渲染器支持文本/图片/按钮的重绘

## 适用场景

- 在 React 应用中嵌入 Tock 聊天机器人界面
- 不用构建工具、在纯 HTML 页面用独立脚本渲染聊天窗口
- 按品牌定制聊天界面的颜色、字体与组件样式

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L21: A toolkit to easily embed Tock chatbots into Web pages.
> L25: - connection/dialog with a Tock bot using _Bot API_ (using SSE if available)

## 星数曲线

```mermaid
xychart-beta
    title "theopenconversationkit/tock-react-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ac89da5ad0be` · [字段定义](../../DATASET.md)*
