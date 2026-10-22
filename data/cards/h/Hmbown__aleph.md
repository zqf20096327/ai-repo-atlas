# Hmbown/aleph

⭐ 218 · Python · MIT · 推送 2026-04-11 · [GitHub](https://github.com/Hmbown/aleph) · [官网](https://aleph-web.pages.dev/) · 个人维护

**把 agent 变成递归语言模型的 MCP 服务器与技能**

面向 LLM 客户端的 MCP server + skill：将搜索索引、代码执行、证据与递归状态保存在提示窗外的 Python 进程中，暴露 30+ 工具（加载上下文、rg/语义搜索、Python 与 JS/TS REPL 执行、think/sub_query 递归、会话保存恢复），让模型对大型代码库、日志、长文档迭代推理而不占用上下文。通过 pip 安装，aleph-rlm CLI 一键配置 Claude Code/Codex/Cursor 等 MCP 客户端，子查询后端可选 Claude CLI、Codex MCP、OpenAI 兼容 API 或本地 llama.cpp（GGUF）。附 action 策略与上下文隔离等安全机制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 30+ MCP 工具：上下文加载、搜索、服务端代码执行、递归子查询
- 工作状态存于提示窗外进程，支持会话保存与恢复
- JS/TS 沙箱运行时含 Recipe DSL 与本地辅助函数集
- 本地模型路径：llama.cpp + GGUF 全流程本机运行

## 适用场景

- 对大型代码库构建工作区地图并迭代检索分析
- 加载大日志文件做模式追踪与事件关联
- 把复杂调查拆成多轮子查询并保存会话跨次续查

## 场景标签

`Agent 框架` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L7: Aleph is an MCP server and skill for
> L69: |`aleph`|`aleph.mcp.local_server:main`|**MCP server.** This is what MCP clients launch. Exposes 30+ tools for conte

## 星数曲线

```mermaid
xychart-beta
    title "Hmbown/aleph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 217 --> 219
    line [218, 218]
```

2026-10-18 218 → 2026-10-21 218（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3772823a4001` · [字段定义](../../DATASET.md)*
