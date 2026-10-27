# erweixin/rego

⭐ 22 · Go · MIT · 推送 2025-12-30 · [GitHub](https://github.com/erweixin/rego) · 个人维护 · 中文 README

**Go 语言的组件式声明 TUI 框架，支持 Hooks 风格开发**

面向 Go 开发者的终端 UI 框架，提供 React Hooks 风格 API（Use/UseEffect/UseKey）、基于泛型的编译期类型检查、声明式布局组件（VStack/HStack/Box）、焦点管理、鼠标事件与 Button/TextInput/Markdown 等内置组件；显式 Key 机制解除了 React Hooks 调用顺序限制。内置 Bridge 机制支持 AI Agent 场景的流式输出与智能滚动。通过 go get 安装，附带 showcase/todo/agent 等 12 个示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Hooks 风格状态管理与显式 Key（可在 if/for 块中使用）
- 基于 Go 泛型的编译期类型检查
- 内置焦点管理（Tab 导航）与鼠标事件支持
- Bridge 机制处理 AI Agent 流式输出与智能滚动

## 适用场景

- 用 React 经验快速构建 Go 终端界面
- 搭建带流式输出的 AI Agent CLI 工具
- 构建日志/聊天类的自动滚动终端面板

## 场景标签

 · 领域:开发框架/终端 UI

## 证据(README 行号)

> L7: > Bringing React Hooks-style development experience to Go CLI/TUI
> L143: ## AI Agent Scenarios

## 星数曲线

```mermaid
xychart-beta
    title "erweixin/rego 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3e19820746be` · [字段定义](../../DATASET.md)*
