# Kame696/kame-api-rotation-for-agent-zero

⭐ 22 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/Kame696/kame-api-rotation-for-agent-zero) · [官网](https://github.com/Kame696/kame-api-rotation-for-agent-zero) · 个人维护

**Agent Zero 插件：多 API key 轮换与模型自动降级，聚合配额池**

面向 Agent Zero 框架的插件（KAME，Key-Aware Management Engine），将多个免费层 API key 聚合为一个池：按负载选择最空闲的健康 key，遇 429/RESOURCE_EXHAUSTED/503 等错误按响应体中的重试时长让 key 精确休息，慢响应由备份 key 和后备模型竞速，首个应答胜出。声明从 82 个 provider 文档学习 774 种错误形态，不依赖 allowlist。通过 Agent Zero Plugin Hub 安装或手动放入插件目录，需 Agent Zero v1.14+，无需额外依赖。面板与聊天命令展示轮换状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 key 聚合为单池，429 时按 provider 自带的 retryDelay/Retry-After 精确休息
- 慢响应竞速机制：备份 key 与后备模型并行，首个应答胜出
- 声明学习 82 个 provider、774 种错误形态，按错误体而非 provider 名判定
- 面板、rotation chip 与 /kame 系列聊天命令展示与配置

## 适用场景

- 用多个免费层 key 拼出更大的可用配额跑 Agent Zero
- 主模型限流或过载时自动切到下一健康 key 或后备模型
- 通过面板和聊天命令监控各 key 的休息与切换状态

## 场景标签

 · 领域:LLM 基础设施/API 管理

## 证据(README 行号)

> L40: Round-robin tools cycle your keys blindly and keep hitting the one that just failed. **KAME decides from the error 
> L128: |**Needs**|Agent Zero v1.14+ or the V2 line — nothing else, no extra package|

## 星数曲线

```mermaid
xychart-beta
    title "Kame696/kame-api-rotation-for-agent-zero 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2e396bf16be0` · [字段定义](../../DATASET.md)*
