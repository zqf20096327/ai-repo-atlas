# RubyWang0/WindRise

⭐ 107 · TypeScript · 推送 2026-07-31 · [GitHub](https://github.com/RubyWang0/WindRise) · 组织维护 · 中文 README

**自托管的 AI 智能体运行系统框架，支持沙箱文件操作**

基于 FastAPI（后端）+ React/Vite/Tailwind（前端）的前后端分离 AI Agent 运行框架，提供智能体核心、意图识别路由、链式思维展示，并自动创建 workspace/ 文件夹作为本地操作沙箱。开源版未内置多模态生成、书籍创作等高级工作流（私有业务逻辑已排除），但保留插件式工作流扩展接口，开发者可在 workflows/ 目录编写 Python 脚本并在路由中注册分发。API Key 等配置仅存于浏览器 LocalStorage。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 插件式自定义工作流扩展接口（workflows/ 目录 + 意图路由分发）
- 沙箱文件操作与链式思维展示
- 前后端分离架构，API 配置仅存本地浏览器 LocalStorage

## 适用场景

- 自建可定制工作流的 AI 助手/智能体服务
- 在私有环境中运行带沙箱文件操作的对话式 agent
- 按业务意图分发多步骤自动化任务

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: `windrise_agent_opensource` 是一个独立的 **AI Agent (智能体) 运行系统**。它基于 FastAPI + React + Vite + Tailwind CSS 构建，提供了一套基础的、支持沙
> L36: 本系统提供了插件式工作流的扩展接口，您可以按照以下步骤轻松接入自己编写的复杂任务工作流：

## 星数曲线

```mermaid
xychart-beta
    title "RubyWang0/WindRise 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 106 --> 108
    line [107, 107]
```

2026-10-18 107 → 2026-10-24 107（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `de3d337192e4` · [字段定义](../../DATASET.md)*
