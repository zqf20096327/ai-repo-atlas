# franco-ruggeri/codecompanion-lualine.nvim

⭐ 23 · Lua · MIT · 推送 2026-01-24 · [GitHub](https://github.com/franco-ruggeri/codecompanion-lualine.nvim) · 个人维护

**Neovim 状态栏组件：显示 CodeCompanion 活跃请求数**

为 lualine.nvim 提供的 CodeCompanion 状态组件：在状态栏显示当前活跃的 CodeCompanion 请求数量，请求进行中显示 spinner，空闲时显示对勾；组件带图标且可自定义选项。组件仅在 CodeCompanion 加载后启用，遵循其懒加载配置，README 建议不要将 CodeCompanion 添加为 lualine 的依赖。基于 CodeCompanion 官方文档中的示例实现，通过 lazy.nvim 安装。

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

- 显示活跃 CodeCompanion 请求数量
- 请求中显示 spinner，空闲显示对勾
- 带图标且支持选项自定义
- 遵循 CodeCompanion 懒加载配置

## 适用场景

- 在 Neovim 状态栏查看 AI 编程助手的请求状态
- 了解当前 CodeCompanion 是否正在生成响应

## 场景标签

 · 领域:开发者工具/Neovim 插件

## 证据(README 行号)

> L5: A simple lualine component for
> L7: status indicator with the number of active CodeCompanion requests.

## 星数曲线

```mermaid
xychart-beta
    title "franco-ruggeri/codecompanion-lualine.nvim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `7346f350fa12` · [字段定义](../../DATASET.md)*
