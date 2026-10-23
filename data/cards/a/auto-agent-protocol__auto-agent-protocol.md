# auto-agent-protocol/auto-agent-protocol

⭐ 110 · TypeScript · NOASSERTION · 推送 2026-10-15 · [GitHub](https://github.com/auto-agent-protocol/auto-agent-protocol) · [官网](https://autoagentprotocol.org/) · 组织维护

**开放协议：让 AI 助手可查询车行库存并提交销售线索**

面向汽车与摩托车经销商的开放标准（AAP v2.0.0），定义 AI 助手发现经销商、查询库存、查看车辆详情并提交经客户同意的销售线索的规范。基于 A2A v1.0 JSON-RPC 传输并叠加 Personal Agent Protocol (Poppy) 原生访客接口，经销商在自有网站发布两份发现文件并实现五个标准技能中的若干即可上线；线索可字段级映射到 ADF/XML 供既有 CRM 使用。提供 TypeScript 类型、JSON Schema 与校验器 npm 包及 OpenAPI 3.1 文档。不覆盖支付、金融审批与估值。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- A2A v1.0 + Poppy 双接口规范，JSON-RPC 2.0 为唯一 A2A 传输
- 五个标准技能：dealer.information / inventory.facets / inventory.search / inventory.vehicle / lead.submit
- 官方发布 @autoagentprotocol/types、schemas、validator npm 包
- lead.submit 可映射 ADF/XML 兼容既有经销商 CRM

## 适用场景

- 经销商让自己的库存可被任意 AI 助手发现和查询
- AI 助手开发者按统一协议接入多家车行
- CRM 厂商通过 ADF/XML 映射接收协议线索

## 场景标签

 · 领域:汽车零售/Agent 互操作协议

## 证据(README 行号)

> L24: **For engineers:** AAP 2.0 combines an open A2A v1.0 profile with a native Personal Agent Protocol guest API. A com
> L120: |Transport / data model (BASE)|**A2A v1.0**|The A2A interface carries AAP requests and responses inside `Message.p
> L122: |Adjacent / complementary|**ACP** (Agentic Commerce), **MCP** (Model Context Protocol)|ACP covers commerce checkou

## 星数曲线

```mermaid
xychart-beta
    title "auto-agent-protocol/auto-agent-protocol 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 109 --> 111
    line [110, 110]
```

2026-10-18 110 → 2026-10-23 110（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `c42a97442b63` · [字段定义](../../DATASET.md)*
