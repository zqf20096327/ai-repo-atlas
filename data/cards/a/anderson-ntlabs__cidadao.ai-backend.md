# anderson-ntlabs/cidadao.ai-backend

⭐ 35 · Python · MIT · 推送 2026-10-07 · [GitHub](https://github.com/anderson-ntlabs/cidadao.ai-backend) · 个人维护

**巴西政府透明度数据的多智能体分析后端 API**

Cidadão.AI 的 FastAPI 后端：以 20 个具巴西文化身份命名的 AI 智能体（其中 17 个从事政府透明度分析），从 30 余个联邦与州级政府 API（Portal da Transparência、PNCP、TCE 等）读取合同与支出数据，经编排器协调进行异常检测（FFT、Z-score、IQR）、模式分析与葡萄牙语自然语言问答，通过 SSE 流式聊天返回。主 LLM 为 Maritaca AI，Anthropic Claude 作为自动降级备选。部署于 Railway（PostgreSQL+Redis），本地默认 SQLite 与内存缓存。本仓库为 MIT 开源镜像，issue 与 PR 不被跟踪，实际演进在平台侧。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20 个智能体，17 个面向政府透明度分析（异常检测、法律分析、审计等）
- 集成 30+ 巴西联邦与州级政府透明度 API
- SSE 流式实时聊天，葡萄牙语自然语言接口
- 1,514 个测试，覆盖率 76.29%

## 适用场景

- 用葡萄牙语自然语言查询巴西政府合同与支出异常
- 自动监控透明度门户数据并生成调查报告
- 复用智能体代码向巴西 AI 解决方案库提交方案

## 场景标签

`多智能体` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L50: **Democratizando o acesso aos dados de transparência governamental brasileira através de 20 agentes de IA especiali
> L114: **Cidadão.AI** analisa contratos governamentais brasileiros usando **20 agentes de IA especializados** com identid
> L121: - **Chat em Tempo Real** - Respostas SSE streaming dos agentes

## 星数曲线

```mermaid
xychart-beta
    title "anderson-ntlabs/cidadao.ai-backend 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6b0668328327` · [字段定义](../../DATASET.md)*
