# lna-lab/distill-kura

⭐ 54 · Python · MIT · 推送 2026-09-30 · [GitHub](https://github.com/lna-lab/distill-kura) · 组织维护

**给 agent 开发者：带证据门控的蒸馏式长期记忆系统**

面向 agent 宿主的长期记忆服务：召回按语义进行（快路径由五头确定性识别器拦截直问问题，未过门则把整个索引放进一次提示让小模型点名），写入由确定性 Python 门控——候选记忆必须携带原材料中逐字存在的引文，按 [USER]/[TOOL]/[ACT]/[SELF] 分级授权，无证据引文的候选被丢弃。索引以三层结构（pinned/fresh/trigger）织入系统提示作为常驻地图。以 DeepSeek Harness 插件、MCP 服务器、HTTP 服务和 Python 库形式提供，仅依赖标准库，无向量库、无嵌入、无框架。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 写入路径由逐字引文证据门控，数字必须有 [TOOL] 来源
- 五头确定性快路径识别器：直问召回约 2ms，不确定即回退到 thinker
- 三层常驻地图（pinned/fresh/trigger）注入系统提示，块内不含时钟以保前缀缓存
- 仅标准库依赖，无向量数据库、无嵌入、无框架

## 适用场景

- 为自建 agent 宿主提供按语义召回的长期记忆服务
- 防止 agent 把无证据断言写入记忆并被后续会话当事实复读
- 通过 MCP 让 Claude Code/VS Code/Goose 等宿主读取记忆地图

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L8: Ships as a DeepSeek Harness plugin,
> L9: an MCP server for any other host, an HTTP service, and a Python library. Standard
> L224: |Claude Code, VS Code, Goose|MCP `instructions` carries a short pointer (**2KB cap**); the map itself comes from t

## 星数曲线

```mermaid
xychart-beta
    title "lna-lab/distill-kura 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 52 --> 55
    line [53, 54, 54]
```

2026-10-18 53 → 2026-10-27 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cf83595976bb` · [字段定义](../../DATASET.md)*
