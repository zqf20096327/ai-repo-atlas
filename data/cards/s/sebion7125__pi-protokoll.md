# sebion7125/pi-protokoll

⭐ 5 · TypeScript · MIT · 推送 2026-11-17 · [GitHub](https://github.com/sebion7125/pi-protokoll) · [官网](https://pi.dev/packages/pi-protokoll) · 个人维护 · 中文 README

**Pi 编码 agent 扩展：用本地 LLM 做长会话上下文压缩**

一个 Pi 编码 agent 的扩展，目标是让本地模型跑超长会话：模型在每轮回答末尾写一段固定格式的 protocol，压缩时由代码从这些 protocol 组装分级摘要（verbatim/detail/status 三层），只在最后一小步调用模型更新工作状态，从而替代 Pi 内置的整段重读重总结流程。提供 protocol_read/search/turn 查询工具、开关与 repair 等命令、统计与 recall 评测命令。要求 Pi ≥ 1.1，构建与测试均基于 OpenAI 兼容服务器上的本地 Qwen3.x 模型，其他 provider 标注为未测试。

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

- 每轮末尾写入 <protocol> 块，压缩时由代码组装分层摘要
- 压缩结果三级限长：verbatim/detail/status 各有 token 上限
- protocol_read/search/turn 工具让历史轮次仍可检索
- /protokoll stats/recall/export 提供压缩耗时与摘要保留度统计

## 适用场景

- 本地模型跑几十万 token 上下文的编码会话
- 让 Pi 会话压缩不阻塞且压缩后前缀缓存继续命中
- 回查早期轮次的原始记录与已制定规则

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: A Pi extension that makes very long sessions possible with local models:
> L13: Pi's built-in compaction sends the old history to the model and waits while it writes a
> L145: - Built and tested with **local models behind an OpenAI-compatible server** (Qwen3.x).

## 星数曲线

```mermaid
xychart-beta
    title "sebion7125/pi-protokoll 星数(近 3 点)"
    x-axis ["2026-11-15", "2026-11-16", "2026-11-23"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-11-15 4 → 2026-11-23 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `8662cf79c6fe` · [字段定义](../../DATASET.md)*
