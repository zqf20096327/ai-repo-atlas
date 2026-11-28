# Contextwaise/contextwaise-typescript

⭐ 4 · TypeScript · MIT · 推送 2026-11-14 · [GitHub](https://github.com/Contextwaise/contextwaise-typescript) · [官网](https://contextwaise.com/docs/sdk) · 组织维护

**面向 agent 开发者的工具结果上下文裁剪 SDK**

Contextwaise 的 TypeScript SDK：在工具结果返回时立即裁剪，保留原始内容并提供 expand 工具供模型取回，裁剪决策可复放以保持 prompt 缓存安全。相关性评分由托管 Contextwaise API 完成；无 API key 时仅执行本地清理，数据不出本机。提供 Vercel AI SDK、Anthropic SDK、OpenAI SDK 适配器，配套纯规则库 @contextwaise/core 与同决策的 Python SDK。开发需 Node 22.18+。

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

- 工具结果返回时裁剪、保留原始并可经 expand 工具取回
- 决策一次生成后复放，模型可见历史不变，兼容 prompt caching
- Vercel AI SDK / Anthropic SDK / OpenAI SDK 适配器
- 无 API key 时仅本地清理，无数据外发

## 适用场景

- 降低 agent 多轮对话中重复发送工具结果的 token 开销
- 发送长文档前仅保留与当前步骤相关的段落
- 在保持 prompt 缓存有效的前提下压缩上下文

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L26: |`contextwaise`|The agent SDK. Shrinks each tool result the moment it returns, keeps the original, and gives the mo
> L30: Everything that decides what is removed from your context, and everything that runs
> L32: Contextwaise API; without an API key the SDK only runs the local cleanup and nothing

## 星数曲线

```mermaid
xychart-beta
    title "Contextwaise/contextwaise-typescript 星数(近 2 点)"
    x-axis ["2026-11-27", "2026-11-28"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-27 4 → 2026-11-28 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `15bec3da975b` · [字段定义](../../DATASET.md)*
