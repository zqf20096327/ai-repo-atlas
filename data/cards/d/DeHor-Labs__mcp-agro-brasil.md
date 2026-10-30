# DeHor-Labs/mcp-agro-brasil

⭐ 69 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/DeHor-Labs/mcp-agro-brasil) · [官网](https://dehor.dev) · 个人维护

**巴西农业数据的 MCP 服务器：牛/大豆/玉米/奶价与汇率等**

面向 MCP 客户端（Claude Desktop、Claude Code 等）的数据服务器，向 AI 客户端提供巴西农业指标：牛、大豆、玉米、牛奶报价（Scot/CEPEA-ESALQ，经公开页面抓取并本地缓存 15 分钟）、PTAX 汇率、天气（Open-Meteo）、出口数据（Comex Stat）、RSS 行业新闻、CONAB 农事日历及农业单位换算。可选接入 Embrapa AgroAPI（AGROFIT/ZARC 等，需注册凭证，未配置时不注册相应工具）。通过 uvx 免安装或 pip 安装，MIT 许可；CEPEA 数据为非商业许可，商用需另获授权。

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

- 14 个基础工具覆盖报价、天气、汇率、出口、新闻、农事日历与单位换算
- 可选 Embrapa AgroAPI 集成（AGROFIT/ZARC/生物投入品等 8 个工具）
- uvx 免安装运行，或 pip/uv 安装为 Python 包
- 对公开来源做本地 15 分钟缓存抓取

## 适用场景

- 在 Claude Desktop/Code 中查询巴西农产品实时报价与汇率
- 查询按市/州划分的种植与收获窗口（CONAB）
- 通过 MCP 客户端查询 AGROFIT 农药登记与 ZARC 风险信息

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L17: `mcp-agro-brasil` conecta qualquer cliente MCP (Claude Desktop, Claude Code, outros) a indicadores
> L3: MCP server de dados do agronegócio brasileiro: cotações de boi gordo, soja, milho e leite, calendário de safra (CONA

## 星数曲线

```mermaid
xychart-beta
    title "DeHor-Labs/mcp-agro-brasil 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-10-30"]
    y-axis "stars" 68 --> 70
    line [69, 69]
```

2026-10-29 69 → 2026-10-30 69（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3c12355d49ce` · [字段定义](../../DATASET.md)*
