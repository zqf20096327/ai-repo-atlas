# APEX-Standard/protocol

⭐ 16 · Rust · NOASSERTION · 推送 2026-07-23 · [GitHub](https://github.com/APEX-Standard/protocol) · [官网](https://apexstandard.org/) · 组织维护

**AI 代理连接金融经纪商的开放 MCP 协议规范**

APEX（Agent Protocol for EXchange）是定义 AI 代理如何与金融经纪商、交易商、做市商通信的开放规范，基于 MCP。核心内容包括：五域规范工具词汇表（session/account/order/market/risk，以 apex.* 前缀命名并带 MCP 元数据）、通用金融工具标识符格式（如 APEX:FX:EURUSD）、统一订单模型，使代理无需定制集成即可接入合规经纪商。规范分 Core 与 FX/CFD/加密货币/期货等 Layer 2 层，多资产层为 planned 状态；当前版本 0.3.0-alpha，规范以 CC BY 4.0 授权。面向代理开发者与经纪商实现方。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 五域规范工具词汇表，均带 MCP 元数据标注
- 通用工具标识符格式覆盖 FX/CFD/加密货币/期货
- 分层规范结构：Layer 1 Core 为经纪商强制基线
- 提供参考实现目录与一致性测试套件

## 适用场景

- AI 交易代理接入任意 APEX 兼容经纪商
- 经纪商按规范实现 MCP 端点并通过一致性测试
- 查阅协议设计文档理解各机制的动机与场景

## 场景标签

 · 领域:金融科技/协议规范

## 证据(README 行号)

> L5: The open MCP-based specification for how AI agents communicate with financial brokers, dealers, and market makers.
> L7: APEX defines a canonical tool vocabulary, a universal instrument identifier, and a unified order model — enabling an
> L53: Five domains. Consistent naming. Every tool annotated with MCP metadata.

## 星数曲线

```mermaid
xychart-beta
    title "APEX-Standard/protocol 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `61c8d22232fd` · [字段定义](../../DATASET.md)*
