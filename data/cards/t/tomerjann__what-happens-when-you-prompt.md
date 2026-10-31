# tomerjann/what-happens-when-you-prompt

⭐ 17 · 推送 2026-04-11 · [GitHub](https://github.com/tomerjann/what-happens-when-you-prompt) · 个人维护

**LLM 提示词全链路技术解析文档：从按键到流式 token**

一份深度参考文档（灵感来自经典的 what-happens-when），逐层追踪向 LLM 聊天应用发送一条提示词后在完整技术栈中发生的事情：浏览器端 token 计数与乐观 UI、SSE/WebSocket 流式协议、API 网关路由与鉴权、多维限流、安全分类器预筛、提示注入防御、上下文组装与窗口管理等。面向已理解 transformer 与 RAG 的工程师，提供生产直觉而非入门讲解；基于公开研究与开源推理框架的一般性模式，非任一厂商内部实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖从按键到流式 token 的浏览器→网关→推理全链路
- 解析多维限流（RPM/ITPM/OTPM）与鉴权关键路径
- 梳理安全分类器预筛与提示注入的现有缓解手段
- 对比四种上下文窗口管理策略的代价

## 适用场景

- LLM 应用工程师补齐生产链路的系统性认知
- 排查限流、流式与上下文截断相关问题时对照参考
- 作为 LLM 系统设计面谈或内训的学习材料

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: This repository answers a deceptively deep question:
> L11: The target reader is an engineer who already understands transformers, attention, and RAG - and wants **production 

## 星数曲线

```mermaid
xychart-beta
    title "tomerjann/what-happens-when-you-prompt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f5b5e0f407fd` · [字段定义](../../DATASET.md)*
