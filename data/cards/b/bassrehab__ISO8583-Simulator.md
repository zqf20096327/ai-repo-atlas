# bassrehab/ISO8583-Simulator

⭐ 56 · Python · AGPL-3.0 · 推送 2026-10-03 · [GitHub](https://github.com/bassrehab/ISO8583-Simulator) · [官网](https://iso8583sim.com/) · 个人维护

**给支付开发者的 ISO 8583 报文解析/构建/校验与发卡行模拟工具包**

面向银行卡支付系统开发者的 Python 工具包：以 Cython 加速的解析（约 182k TPS）与构建（约 150k TPS）为核心，支持 ISO 1987/1993/2003 版本、VISA/Mastercard 等卡组织字段校验、EMV Field 55、PIN block 与 MAC、二进制/BCD/EBCDIC 线格式；附带 CLI、Python SDK、REST API、Jupyter 笔记本与 mock issuer host 的 TCP 模拟服务。AI 部分为可选功能：LLM 解释/生成报文（OpenAI/Anthropic/Google/Ollama）及供 Claude/Cursor 使用的 MCP server（18 个工具）。AGPL-3.0 与商业双许可，闭源使用需商业授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Cython 加速的 ISO 8583 解析/构建/校验（基准约 182k/150k TPS）
- mock issuer host 模拟器：按规则批准/拒绝/延迟/丢弃请求，含 TCP 负载测试
- 支持 6 大卡组织、EMV Field 55、PIN block（ISO 9564）与 MAC、三版本间转换
- MCP server 提供 18 个工具供 AI 助手解析/构建/校验报文，本地运行无需 LLM API key

## 适用场景

- 支付系统开发中解析、构建与校验 ISO 8583 报文
- 本地模拟发卡行主机做联调与吞吐/延迟压测
- 让 AI 助手通过 MCP 直接解读或生成 ISO 8583 报文
- 通过 Jupyter 笔记本学习 ISO 8583 与 EMV 数据

## 场景标签

 · 领域:金融科技/支付协议工具

## 证据(README 行号)

> L10: A high-performance ISO 8583 toolkit for Python: parse, build and validate card payment messages, simulate issuer ho
> L41: - **AI-Powered Features**:
> L44:  - Supports OpenAI, Anthropic, Google, and Ollama (local/offline)

## 星数曲线

```mermaid
xychart-beta
    title "bassrehab/ISO8583-Simulator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-29 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `593992a687dd` · [字段定义](../../DATASET.md)*
