# XpressAI/xaibo

⭐ 15 · Python · MIT · 推送 2026-10-03 · [GitHub](https://github.com/XpressAI/xaibo) · [官网](https://xaibo.ai) · 组织维护

**协议驱动的模块化 AI agent 开发框架**

面向开发者的 Python agent 框架，通过协议接口定义组件交互，支持替换 LLM、向量存储与工具而不改核心逻辑。组件经透明代理自动观测输入输出，内置序列图式调试 UI。提供依赖注入以使用 mock 组件做确定性测试。开发服务器附带 OpenAI 兼容 chat completions API，模块系统覆盖 OpenAI/Anthropic/Google 等提供商及向量记忆，支持 MCP。需 Python 3.11+，用 uv 初始化项目。

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

- 协议驱动架构，可替换 LLM/向量存储/工具
- 透明代理观测组件输入输出，内置序列图调试 UI
- 开发服务器提供 OpenAI 兼容 API（localhost:9001/openai）
- 依赖注入与 mock 组件测试，支持 MCP 工具与服务

## 适用场景

- 构建可测试、可观测的模块化 agent
- 通过 OpenAI 兼容客户端接入自建 agent
- 在真实 LLM API 前用 mock 组件验证 agent 逻辑

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: Xaibo is a modular framework designed to help you build sophisticated AI systems that are easy to test, debug, and e
> L92:  * **Extensible Module System:** Ships with modules for major LLM providers (OpenAI, Anthropic, Google), local embe

## 星数曲线

```mermaid
xychart-beta
    title "XpressAI/xaibo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c0b3fe5e2ba1` · [字段定义](../../DATASET.md)*
