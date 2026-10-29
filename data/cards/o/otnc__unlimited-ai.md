# otnc/unlimited-ai

⭐ 22 · TypeScript · ISC · 推送 2026-10-23 · [GitHub](https://github.com/otnc/unlimited-ai) · [官网](https://www.npmjs.com/package/unlimited-ai) · 个人维护

**Node.js/TypeScript 封装 Voids API 聊天补全的客户端库**

面向开发者的 npm 包，封装 Voids API（api.voids.top）的 AI 聊天补全接口：提供 AI 实例类与函数式两套 API，支持静态上下文（system 提示、few-shot 消息）、按会话 ID 的多轮历史、流式输出、会话导入导出与重启后恢复。可获取与模糊搜索可用模型列表，模型以 ID 指定（如 gpt-4o）。请求经远程 API 完成，包本身不运行模型。注意声明与 Voids API 无隶属关系，v6.x 及以下不再支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | ISC |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 类与函数式双 API：generate/ask/stream/models/searchModels
- 会话 ID 管理多轮历史，支持导入导出与跨重启恢复
- 流式输出（AsyncGenerator 逐块产出回复）
- 静态上下文链式配置与模型模糊搜索

## 适用场景

- 在 Node.js 项目中调用 Voids API 生成聊天补全
- 为多用户维护独立对话历史
- 以流式方式展示模型回复

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: Fast, minimal Node.js wrapper for the Voids API AI chat completions.
> L493: console.log(config.API_URL);    // https://api.voids.top/v1/chat/completions

## 星数曲线

```mermaid
xychart-beta
    title "otnc/unlimited-ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-29 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b905784ad0b7` · [字段定义](../../DATASET.md)*
