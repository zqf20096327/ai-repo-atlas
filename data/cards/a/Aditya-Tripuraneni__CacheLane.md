# Aditya-Tripuraneni/CacheLane

⭐ 22 · TypeScript · Apache-2.0 · 推送 2026-07-23 · [GitHub](https://github.com/Aditya-Tripuraneni/CacheLane) · [官网](https://cache-lane.vercel.app/) · 个人维护

**Claude Code 的本地缓存代理层：重组提示词以降低 token 成本**

介于 Claude Code 与 api.anthropic.com 之间的代理：按波动性将请求划分为稳定/易变区域并在边界放置 cache_control 断点，使稳定前缀命中 Anthropic 提示缓存；对连续 K 轮（默认 3）未使用的工具输出替换为存根（可经 cachelane_expand MCP 工具恢复），并有空闲期 keepalive 探测与自动升级 1 小时缓存层。状态存于本地 SQLite，默认不存储提示词或代码。以 npm CLI 提供，安装后无需改变使用方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 放置 cache_control 断点使稳定前缀按 0.1× 缓存读取计费
- K-pruning 将闲置 K 轮的工具输出替换为存根，可经 MCP 工具无损恢复
- keepalive 空闲探测保持前缀热缓存，≥50k token 前缀自动升级 1 小时层
- 本地 SQLite 存储元数据，默认不保存提示词与工具输出内容

## 适用场景

- 长会话编码时降低 Claude Code 的输入 token 成本
- 查看会话级缓存命中与节省统计
- 对闲置工具输出做提示词瘦身而保留可恢复性

## 场景标签

 · 领域:LLM 基础设施/成本优化

## 证据(README 行号)

> L9: > CacheLane sits between Claude Code and `api.anthropic.com` and reorganizes each turn's prompt so Anthropic's promp
> L177: `cachelane install` makes two edits to your Claude Code configuration:
> L179: 1. **Registers an MCP server** in `~/.claude.json` (`mcpServers.cachelane`). Claude Code launches `cachelane mcp` 

## 星数曲线

```mermaid
xychart-beta
    title "Aditya-Tripuraneni/CacheLane 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-28 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6caf0b7ac31d` · [字段定义](../../DATASET.md)*
