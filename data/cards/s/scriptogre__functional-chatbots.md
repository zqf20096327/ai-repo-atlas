# scriptogre/functional-chatbots

⭐ 15 · Jinja · 推送 2026-06-10 · [GitHub](https://github.com/scriptogre/functional-chatbots) · [官网](https://djangocon2024.christiantanul.com) · 个人维护

**DjangoCon 2024 演示：LLM 函数调用驱动 UI 状态的 Django 聊天机器人**

Django + htmx 技术栈的演示应用：聊天接口一次往返返回聊天消息、客户端 UI 事件（暗色模式/全屏/披萨模式）与服务端函数（披萨订单 CRUD）；通过 litellm 调用 Groq 托管的 Llama-3.3-70B，JSON 模式输出经 Pydantic 校验后分派事件与函数。面向参加 DjangoCon Europe 2024 workshop 的开发者，原 workshop 分支（0-start-here 至 6-server-functions-solution）作为演讲档案保留，main 分支为 2026 依赖更新版。运行依赖 Groq API key，使用 SQLite 与多阶段 Dockerfile。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一次往返返回聊天消息 + UI 事件 + 服务端函数三类结果
- litellm + Groq JSON 模式输出，Pydantic schema 校验
- htmx/hyperscript/Tailwind v4 驱动客户端 UI 状态切换
- 保留原 workshop 六个分支作为演讲档案

## 适用场景

- 学习 LLM 函数调用与 Django/htmx 集成的实现方式
- 作为函数调用驱动前端 UI 状态的参考实现
- 复现 DjangoCon Europe 2024 workshop 流程

## 场景标签

`聊天机器人` `教程课程` · 领域:对话与助手

## 证据(README 行号)

> L7: A demo of a Django chatbot that, in one round-trip, returns:
> L22: - litellm + Groq (`groq/llama-3.3-70b-versatile`)

## 星数曲线

```mermaid
xychart-beta
    title "scriptogre/functional-chatbots 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b34399e25371` · [字段定义](../../DATASET.md)*
