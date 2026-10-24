# Antseed/antseed

⭐ 125 · TypeScript · GPL-3.0 · 推送 2026-10-23 · [GitHub](https://github.com/Antseed/antseed) · [官网](https://antseed.com) · 组织维护

**P2P AI 推理服务网络：供给方与买方经 DHT 加密直连交易**

构建点对点 AI 服务市场的基础设施：供给方运行 provider 插件对接上游 LLM API（Anthropic、OpenAI 兼容 API、本地 Ollama 等）并在 DHT 网络上发布容量；买方运行 router 插件发现供给方，按价格/延迟/信誉评分，通过本地 HTTP 端点代理请求，可直接替换 ANTHROPIC_BASE_URL 或 OPENAI_BASE_URL。含计量、链上 USDC 支付（Base/Arbitrum）、Prometheus 兼容指标导出与插件机制。使用条款禁止转售订阅凭据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DHT 发现供给方，端到端加密 TCP/WebRTC 直连路由请求
- 本地 HTTP 端点可直接替换 ANTHROPIC_BASE_URL / OPENAI_BASE_URL
- 链上 USDC 存款与会话支付（Base/Arbitrum）
- Prometheus 兼容指标导出与 npm 插件体系

## 适用场景

- 将自有 LLM API 容量作为供给方发布到 P2P 市场计费
- 买方以本地端点接入去中心化 AI 推理服务
- 按价格/延迟/信誉自动选择推理供给方

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: A peer-to-peer AI services network. Providers offer AI services, buyers discover providers via DHT and route request
> L11: **Buyers** run a router plugin that discovers providers, scores them on price/latency/reputation, and proxies reque

## 星数曲线

```mermaid
xychart-beta
    title "Antseed/antseed 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 122 --> 126
    line [123, 125, 125]
```

2026-10-18 123 → 2026-10-24 125（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `c104ff85e8ad` · [字段定义](../../DATASET.md)*
