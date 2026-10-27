# Sema4AI/actions

⭐ 140 · Python · Apache-2.0 · 推送 2026-04-10 · [GitHub](https://github.com/Sema4AI/actions) · [官网](https://sema4.ai/) · 组织维护

**用 Python 编写 MCP 工具/AI Actions，连接 AI Agent 与企业系统**

Sema4.ai Action Server：开发者用 @tool/@action 装饰器标记 Python 函数，服务器基于函数声明、类型标注与 docstring 自动生成并暴露 API，使脚本可通过 MCP、OpenAI GPTs Actions、LangChain 等协议被 AI Agent 调用。通过 package.yaml 管理完整 Python 环境（由 RCC 提供，含 conda-forge 依赖），内置运行日志与 trace。项目前身为 Robocorp Action Server，正迁移至 Sema4.ai 组织。安装方式含 pip、brew 与各平台独立二进制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- @tool/@action 装饰器自动生成 MCP/OpenAI GPTs 兼容 API
- package.yaml 声明完整 Python 环境与依赖，由 RCC 管理
- 内置每次工具/Action 运行的日志与 trace 记录
- 提供 pip、brew、独立二进制及 VS Code 扩展多种使用途径

## 适用场景

- 把内部 Python 脚本封装成 MCP 工具供 Agent 调用
- 为 OpenAI 自定义 GPT 暴露可鉴权的 Actions API
- 在隔离环境中托管会接触企业数据与应用的 Agent 动作代码

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L13: # Build MCP Tools or AI Actions that connect AI Agents with the real-world - all in 🐍 Python.
> L17: Sema4.ai Action Server makes your Python scripts compatible with Agents using protocols such as MCP, OpenAI's custo

## 星数曲线

```mermaid
xychart-beta
    title "Sema4AI/actions 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 139 --> 141
    line [140, 140]
```

2026-10-18 140 → 2026-10-27 140（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `594ae7ac2fa3` · [字段定义](../../DATASET.md)*
