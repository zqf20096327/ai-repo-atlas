# ctxinf/mitmproxy-llm-better-view

⭐ 14 · TypeScript · GPL-3.0 · 推送 2026-03-22 · [GitHub](https://github.com/ctxinf/mitmproxy-llm-better-view) · 个人维护 · 中文 README

**在 mitmweb 中可视化 LLM API 请求/响应的油猴脚本**

一个 Tampermonkey 用户脚本，运行于 mitmproxy 的 Web 界面 mitmweb 中，用于格式化展示 LLM API 的请求与响应：包括 messages、tools 与元数据的可视化、流式 SSE 响应处理、消息与工具调用的折叠展开。面向希望观察 Claude Code、OpenCode 等 AI 编码工具实际聚合输入与模型输出上下文的开发者。使用时需先安装 mitmproxy，通过反向代理或正向代理截获流量，再从 GreasyFork 或 release 页安装脚本。支持 OpenAI Chat Completion、Claude、Gemini 三类 API 格式；Ollama API 与 OpenAI Response API 列为 TODO 未支持。作者声明基于个人使用模式开发测试，可能不覆盖所有 API 用法。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 格式化展示 LLM 请求/响应中的 messages、tools 与元数据
- 支持 OpenAI Chat Completion、Claude、Gemini 三种 API 格式
- 处理流式 SSE 响应，消息与工具调用可折叠展开
- 提供反向代理与正向代理两种流量接入方式

## 适用场景

- 观察 Claude Code/OpenCode 等 AI 编码工具实际发送给模型的上下文
- 调试 LLM 应用时查看请求与流式响应的详细内容
- 理解需要提供什么输入才能从 LLM 获得期望结果

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L4: **A Tampermonkey script for LLM API Request/Response Visualization in mitmweb.**
> L19: When using AI applications like `Claude Code` or `OpenCode`, if you can see what context these tools aggregate and 
> L118: - **Request/Response Visualization**: Formatted display of messages, tools, and metadata

## 星数曲线

```mermaid
xychart-beta
    title "ctxinf/mitmproxy-llm-better-view 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c2f11a093007` · [字段定义](../../DATASET.md)*
