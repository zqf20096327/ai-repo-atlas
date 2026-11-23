# JiamingShi-JsPhys/dsh-token-steward

⭐ 3 · TypeScript · MIT · 推送 2026-11-16 · [GitHub](https://github.com/JiamingShi-JsPhys/dsh-token-steward) · 个人维护 · 中文 README

**给 DSH 用户的本地 LLM 网关：按任务自动选路并容灾**

以 DeepSeek Harness 插件形式运行的本地 OpenAI 兼容网关：接收 OpenAI 形状请求，在 HTTP 层按任务属性（编程/推理/视觉等维度）打分选路，提供四档调度模式（极致便宜/效率/火力/免费档）、429/5xx/401 自动容灾与并发打散。内置 21 家厂商目录、SQLite 精确缓存、路由维度计量台账。需宿主 DeepSeek Harness ≥ 0.2.1-rc.3，仅绑定 127.0.0.1，通过面板或 Agent 对话管理配置。

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

- 四档调度模式按任务维度硬过滤与打分选路
- 容灾：429 冷却、5xx 熔断、上下文超限自动换窗口
- SQLite 精确缓存，命中回放 0 token
- Agent 可通过 token_steward_manage 工具对话式改配置

## 适用场景

- 多上游混合接入时按任务自动分配模型
- 免费/付费模型混合使用并精确记账
- 上游故障时自动切换不中断会话

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: **给 DeepSeek Harness 用的模型矩阵调度中枢：把任意 OpenAI 兼容上游接进同一张矩阵，按任务属性自动选路，失败自动换人，用量与成本一眼可见。**
> L26: Token 管家换了一条路：既然插件改不了请求体，那就在 HTTP 这一层接管整个请求。网关收下 OpenAI 形状的请求，自己决定发给谁、失败了换谁、要不要读缓存，然后把结果原样转回去。上游看到的是一次普通调用，DSH 看到的是
> L120: 网关是微内核：**硬过滤 → 打分 → 降级链**。硬过滤先淘汰不合格的型号（缺能力标签、窗口放不下、被用户下线、非对话模型），打分器再在剩下的里排序，首个失败时按序顶上。

## 星数曲线

```mermaid
xychart-beta
    title "JiamingShi-JsPhys/dsh-token-steward 星数(近 2 点)"
    x-axis ["2026-11-11", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-11 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `a3c88d5484d3` · [字段定义](../../DATASET.md)*
