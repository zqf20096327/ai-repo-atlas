# zerob13/dsh-better-markdown

⭐ 22 · TypeScript · MIT · 推送 2026-08-17 · [GitHub](https://github.com/zerob13/dsh-better-markdown) · [官网](https://github.com/zerob13/dsh-better-markdown#readme) · 个人维护 · 中文 README

**DeepSeek Harness Web 的流式 Markdown 渲染插件**

面向 DeepSeek Harness Web 客户端的插件：通过 slot shadowing 将对话中 assistant 的流式与完成态 Markdown 全部替换为 markstream-react 渲染，支持未闭合语法持续解析、KaTeX 数学、Mermaid 图表、Shiki 流式代码高亮；原始 HTML 转义、链接图片仅允许安全外部协议，插件 renderer 抛错时 Harness 原 renderer 自动接管。不修改 Harness 源码，通过 dsh plugin 命令从 npm 或 Git 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 流式与 settled 消息共用同一 Markstream renderer，避免完成态切换
- 支持 Mermaid 图表、KaTeX 数学、Shiki 代码高亮（均打包离线可用）
- raw HTML 转义、安全协议白名单、Mermaid strict mode 的安全边界
- 利用 slot shadowing，插件失败时 Harness 原 renderer 自动接管

## 适用场景

- 让 DeepSeek Harness Web 对话中的流式 Markdown 渲染更稳定
- 在聊天界面中直接查看 Mermaid 图表与数学公式
- 避免消息完成瞬间 Markdown 显示切换或闪烁

## 场景标签

 · 领域:LLM 客户端/前端插件

## 证据(README 行号)

> L18: `dsh-better-markdown` 是一个 DeepSeek Harness Web 客户端插件。安装后，Web 对话中所有带流式状态的 assistant Markdown 都由 `markstream-react` 解
> L60: 插件使用 Harness 公开的 client module 与 slot shadowing，不修改 Harness 源码，也不替换全局 React。

## 星数曲线

```mermaid
xychart-beta
    title "zerob13/dsh-better-markdown 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25", "2026-10-30"]
    y-axis "stars" 19 --> 23
    line [20, 21, 22, 22]
```

2026-10-18 20 → 2026-10-30 22（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0010cdb34727` · [字段定义](../../DATASET.md)*
