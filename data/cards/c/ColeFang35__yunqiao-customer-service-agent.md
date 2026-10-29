# ColeFang35/yunqiao-customer-service-agent

⭐ 19 · Python · 推送 2026-09-15 · [GitHub](https://github.com/ColeFang35/yunqiao-customer-service-agent) · 个人维护 · 中文 README

**基于 AgentScope 的电商智能客服 Agent，17 个工具全链路**

用 AgentScope 2.0 构建的电商 toC 客服 Agent：ReAct 循环驱动 17 个业务工具，覆盖浏览商品、购物车、下单、支付、查物流、退款、转人工全流程；业务数据一律经工具查询、不靠模型生成。模型三档可切换：通义千问、OpenAI 兼容端点、内置离线规则模型（默认，无需 API Key 即可跑通）。含自研 Fire Trace 调试平台（调用树/火焰图/瀑布时间线）与管理后台；前端经 SSE 展示思考与工具调用。业务数据经 mock_store 抽象，替换实现即可接入真实系统。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 17 个业务工具覆盖售前/售中/售后，写操作先确认后执行
- 默认离线规则模型，clone 后无需 API Key 完整跑通
- Fire Trace 调试平台：span 树、火焰图、瀑布时间线与 TTFT 统计
- 三档模型 + 超时自动降级，多会话 LRU 淘汰与指代消解

## 适用场景

- 搭建电商售前到售后的自动客服
- 体验/改造无需 Key 的本地 Agent 全链路演示
- 通过 Fire Trace 观察与调试 Agent 推理和工具耗时

## 场景标签

`聊天机器人` `LLM 可观测性` · 领域:对话与助手

## 证据(README 行号)

> L3: 基于 AgentScope 2.0 构建的电商智能客服 Agent。用 ReAct 循环驱动推理与工具调用，覆盖「浏览商品 → 加购物车 → 下单 → 支付 → 查订单/物流 → 退款 → 转人工」完整链路；前端通过 SSE 实时展
> L12: - **三档模型 + 自动降级**：通义千问 / 任意 OpenAI 兼容端点 / 离线规则模型可切换；主模型超时或异常时自动切备用模型。

## 星数曲线

```mermaid
xychart-beta
    title "ColeFang35/yunqiao-customer-service-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-29 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `351d4f40f55e` · [字段定义](../../DATASET.md)*
