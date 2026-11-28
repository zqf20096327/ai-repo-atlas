# Contextwaise/contextwaise-python

⭐ 3 · Python · MIT · 推送 2026-11-14 · [GitHub](https://github.com/Contextwaise/contextwaise-python) · [官网](https://contextwaise.com/docs/sdk) · 组织维护

**给 Agent 开发者的工具结果压缩 SDK：省 token 且可回取**

在 agent 循环中于工具返回瞬间对结果做压缩，避免长结果在后续轮次重复发送。四级机制：本地确定性 Shapers 清理噪声（错误永不移除）、尺寸门槛、按相关性在预算内裁剪、模型可调用 expand(ref, question) 取回任意部分。视图按 tool call id 逐字节复放以保持 prompt cache 命中。无 API key 时仅运行本地清理；提供 Anthropic/OpenAI/Vercel AI SDK 适配器与 asyncio 接口，Python 3.10+，唯一依赖 httpx。

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

- expand(ref, question) 可回取被省略内容，本地 Shapers 不移除错误
- 视图按 tool call id 逐字节复放，保持 provider prompt cache 命中
- 工具 schema 与动作列表被检测并完整送达模型
- Anthropic/OpenAI 适配器非强制依赖，支持 asyncio 并发

## 适用场景

- 长任务 agent 循环中压缩工具结果以降低 token 开销
- 多 agent 共用一个客户端时按 agent 分组管理结果
- 跨进程部署 agent 时以 Redis/数据库实现 ledger

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7:  Shrinks agent tool results before the model reads them: cache-safe, reversible, intent-aware.
> L18: In an agent loop, every tool result is resent on every later turn. A 20K-token test log read at turn 3 of a 20-turn

## 星数曲线

```mermaid
xychart-beta
    title "Contextwaise/contextwaise-python 星数(近 2 点)"
    x-axis ["2026-11-27", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-27 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `cea116a1825a` · [字段定义](../../DATASET.md)*
