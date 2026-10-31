# guard0-ai/g0

⭐ 50 · TypeScript · AGPL-3.0 · 推送 2026-09-21 · [GitHub](https://github.com/guard0-ai/g0) · [官网](https://guard0.ai/g0) · 组织维护

**AI agent 与 MCP 供应链的安全治理 CLI：发现、扫描、红队与运行时防护**

面向开发与安全团队的本地优先命令行工具，对 AI agent 代码库及所在机器做安全背景检查：发现机器上的 AI 开发工具与 MCP 服务器配置，用 1,128 条规则（12 个安全域）对 Python/TS/Java/Go 代码评分（A–F），以 3,900+ 对抗载荷做红队测试，生成映射 OWASP/NIST/ISO 42001/EU AI Act 的签名报告与 CycloneDX 1.6 AI-BOM。还提供 MCP 流量运行时代理（deny/redact/coach/alert）、Claude Code hook 防护、CI 集成与机队管理。本地运行无需账号，登录平台为可选功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1,128 条规则、12 个安全域、10 个框架解析器（LangChain/CrewAI/MCP 等）
- MCP 运行时代理：密文校验、Exact-Data-Match、数据流溯源与分级处置
- 3,900+ 对抗载荷红队测试与 CVSS 评分
- 签名 CycloneDX 1.6 AI-BOM 清单与标准映射的审计报告

## 适用场景

- 部署前对 agent 代码库做安全评分与合规审计
- 审查本机 MCP 服务器与 AI 工具供应链是否含已知恶意项
- 在 CI 中用 SARIF/JUnit 输出与基线回归模式做安全门禁
- 对运行中的 MCP 流量做秘密泄露检测与策略执行

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L32: AI agents — and the **tools, MCP servers, and models** behind them — ship faster than anyone can track. g0 backgrou
> L53: |🖥️|**Endpoint**|Discover the 19 AI dev tools & MCP servers on a machine — plus agentic browsers (`--agentic-browse
> L57: |🛡️|**Runtime proxy**|Sit in the live path with a confidence-scored engine: checksum-validated secret detection, Ex

## 星数曲线

```mermaid
xychart-beta
    title "guard0-ai/g0 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-31 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f0065be9a008` · [字段定义](../../DATASET.md)*
