# teamchong/vectorjson

⭐ 18 · JavaScript · Apache-2.0 · 推送 2026-03-10 · [GitHub](https://github.com/teamchong/vectorjson) · [官网](https://www.npmjs.com/package/vectorjson) · 个人维护

**面向 LLM 工具调用的 O(n) 流式 JSON 解析库**

基于 WASM SIMD（simdjson 经 Zig 编译）的流式 JSON 解析库，面向构建 LLM agent 的开发者：以 O(n) 增量解析取代逐 chunk 全量重解析，提供字段级流式（事件订阅）、Zod/Valibot 等 schema 驱动解析（schema 外字段字节级跳过）、早期中止错误输出、Worker tape 转移与 WASM 级深度比较。README 声明其基准测试相对多个 AI SDK 解析路径有加速；同时说明一次性完整解析场景 JSON.parse 更快。npm 安装，零配置导入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- O(n) 增量流式解析，每个字节只扫描一次
- 事件解析器支持按路径订阅字段级流式回调
- schema 驱动解析，schema 外字段字节级跳过不分配对象
- 支持早期检测错误输出并中止剩余流，及 WASM tape 级深度比较

## 适用场景

- Agent UI 在工具调用流式输出时立即展示工具名并逐字符流式代码
- 检测到 LLM 输出错误结构时提前中止以节省 token
- 大 payload 只读取少数字段而无需完整物化对象

## 场景标签

 · 领域:LLM 基础设施/解析库

## 证据(README 行号)

> L8: O(n) streaming JSON parser for LLM tool calls, built on WASM SIMD. Agents act faster with field-level streaming, det
> L23: Current AI SDKs — Vercel, Anthropic, TanStack, OpenClaw — re-parse the *entire accumulated buffer* on every token:

## 星数曲线

```mermaid
xychart-beta
    title "teamchong/vectorjson 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `51e2cb3d1f3e` · [字段定义](../../DATASET.md)*
