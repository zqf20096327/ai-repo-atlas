# unohee/kis-agent

⭐ 52 · Python · 推送 2026-10-08 · [GitHub](https://github.com/unohee/kis-agent) · [官网](https://unohee.github.io/kis-agent/) · 个人维护

**韩国投资证券 OpenAPI 的 Python 封装与 CLI，支持 LLM Agent 调用**

面向韩国投资证券（KIS）OpenAPI 的 Python 包装库：提供 kis 命令行工具、Agent SDK、实时 WebSocket 数据流，覆盖国内股票、9 个海外交易所、国内外期货期权交易，支持 TWAP/VWAP 算法分单、模拟交易（paper=True 自动切换 URL 与 TR_ID）、智能缓存与限流（18 RPS / 900 RPM）。JSON 输出与 schema 探索功能使其可作为 LLM Agent 的工具使用。使用需在 KIS API 门户申请 APP_KEY/APP_SECRET，模拟交易仅覆盖 336 个 API 中的 43 个。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 国内 KOSPI/KOSDAQ 与美日中等 9 个海外交易所行情与交易
- WebSocket 实时数据流与 TWAP/VWAP 算法分单
- JSON 输出与 schema 探索，供 LLM Agent 作为工具调用
- paper=True 自动切换模拟交易环境（43/336 个 API 支持）

## 适用场景

- 用 Python 或 CLI 查询行情并执行股票/期货交易
- 构建接入韩国投资证券接口的自动交易程序
- 把证券查询与下单能力接入 LLM Agent 或 MCP 工具链

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: 한국투자증권 OpenAPI Python 래퍼 - Korea Investment & Securities Trading API Client
> L35: - **LLM Agent 연동**: JSON 출력 + 스키마 탐색으로 AI 에이전트 도구로 활용

## 星数曲线

```mermaid
xychart-beta
    title "unohee/kis-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-25 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `5428429ed49f` · [字段定义](../../DATASET.md)*
