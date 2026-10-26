# allanbunch/node-red-openai-api

⭐ 54 · JavaScript · MIT · 推送 2026-06-18 · [GitHub](https://github.com/allanbunch/node-red-openai-api) · [官网](https://www.npmjs.com/package/@inductiv/node-red-openai-api) · 个人维护

**Node-RED 节点包：在低代码流中调用 OpenAI 及兼容 API**

将 OpenAI API 及 OpenAI 兼容 API 接入 Node-RED 的 contrib 节点包，面向在可视化流程中构建事件驱动 AI 应用的开发者。核心模型为一个负责方法调用的 OpenAI API 节点加一个管理 API Base、认证与组织设置的 Service Host 配置节点，方法选择器覆盖 Admin、Responses、Realtime、ChatKit、Vector Stores、Sora 视频等约 30 个 API 家族；支持流式输出、websocket 连接、webhook 验签，可通过自定义 base URL 与认证头对接兼容提供商。基于 openai Node SDK 6.40.0，要求 Node.js ≥18、Node-RED ≥3，提供 30 余个可导入示例流程。

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

- 单一节点覆盖约 30 个 OpenAI API 家族（Responses/Realtime/ChatKit/Admin/Sora 等）
- Service Host 配置支持自定义 base URL、认证头与查询串认证，可对接 OpenAI 兼容提供商
- 流式输出、Responses websocket、webhook 签名验证等事件驱动能力
- examples/ 下提供 30 余个可直接导入的示例流程

## 适用场景

- 在 Node-RED 流程中调用 OpenAI 的生成、嵌入、审核等 API
- 用低代码方式编排多步骤、带工具调用的 AI 工作流
- 通过自定义 API Base 接入其他 OpenAI 兼容服务商

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: This project brings the OpenAI API, and OpenAI-compatible APIs, into Node-RED as workflow-native building blocks.
> L35: - one `OpenAI API` node handles the runtime method call
> L69: Use the `Service Host` config to target compatible API providers with custom base URLs, custom auth header names, q

## 星数曲线

```mermaid
xychart-beta
    title "allanbunch/node-red-openai-api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-26 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cae722a778bd` · [字段定义](../../DATASET.md)*
