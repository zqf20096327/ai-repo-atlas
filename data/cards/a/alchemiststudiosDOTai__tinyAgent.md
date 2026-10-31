# alchemiststudiosDOTai/tinyAgent

⭐ 89 · Python · MIT · 推送 2026-07-12 · [GitHub](https://github.com/alchemiststudiosDOTai/tinyAgent) · [官网](http://tinyagent.xyz/) · 组织维护

**Python 轻量 LLM agent 框架：函数即工具、流式对话**

面向 Python 开发者的小型模块化 agent 框架，提供 Agent 类管理对话状态、流式 LLM 交互、工具执行与事件订阅；工具以普通函数定义并支持结构化输出、终止结果与 before/after_tool_call 宿主钩子。提供商无关，支持任何 OpenAI 兼容 /chat/completions 端点（OpenRouter、OpenAI、Chutes、本地服务器），并支持 Anthropic 风格提示缓存。可选 tinyagent._alchemy 扩展由仓库内 Rust crate 编译并随部分 PyPI wheel 分发，当前仅支持 openai-completions 与 minimax-completions，图片块暂不支持。项目自述为 Beta，API 可能随小版本变化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 流式优先架构，所有 LLM 交互支持流式响应
- 函数定义工具，支持结构化输出与工具循环终止控制
- 适配任意 OpenAI 兼容 /chat/completions 端点
- Anthropic 风格提示缓存降低多轮对话成本

## 适用场景

- 在 Python 应用中构建带工具调用的对话式 agent
- 通过事件订阅实现实时 UI 更新
- 使用宿主钩子拦截或替换不安全的工具调用

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: A small, modular agent framework for building LLM-powered applications in Python.
> L23: TinyAgent provides a lightweight foundation for creating conversational AI agents with tool use capabilities. It fe

## 星数曲线

```mermaid
xychart-beta
    title "alchemiststudiosDOTai/tinyAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 88 --> 90
    line [89, 89]
```

2026-10-18 89 → 2026-10-31 89（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `c9e6b06580e0` · [字段定义](../../DATASET.md)*
