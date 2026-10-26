# franco-ruggeri/codecompanion-spinner.nvim

⭐ 57 · Lua · MIT · 推送 2026-08-08 · [GitHub](https://github.com/franco-ruggeri/codecompanion-spinner.nvim) · 个人维护

**Neovim 插件：CodeCompanion AI 处理时显示内联动画加载指示器**

作为 CodeCompanion 的扩展插件，在 Neovim 聊天缓冲区中于 AI 处理请求期间显示动画 spinner（"Processing..." 虚拟文本），向用户提供反馈。支持多个聊天窗口并发活跃请求（各配独立 spinner），处理文案可通过配置项自定义。安装方式为在 codecompanion.setup 的 extensions 中注册，或通过 lazy.nvim 以依赖形式引入。面向使用 CodeCompanion 的 Neovim 用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 处理期间在聊天缓冲区显示动画 spinner 虚拟文本
- 支持多聊天窗口并发请求，各自独立 spinner
- 处理文案（processing text）可配置

## 适用场景

- CodeCompanion 生成回答时获得可视化进度反馈
- 同时处理多个聊天请求时区分各窗口状态

## 场景标签

 · 领域:编辑器插件/开发工具

## 证据(README 行号)

> L5: Inline spinner for
> L8: This plugin adds an animated spinner in the CodeCompanion chat while AI is

## 星数曲线

```mermaid
xychart-beta
    title "franco-ruggeri/codecompanion-spinner.nvim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-26 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `456a010259f1` · [字段定义](../../DATASET.md)*
