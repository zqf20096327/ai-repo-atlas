# votal-ai-hq/ai-red-teaming

⭐ 37 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/votal-ai-hq/ai-red-teaming) · [官网](https://votal.ai) · 组织维护

**面向 Agent 应用的白盒 AI 红队测试框架：读源码生成定向攻击**

Node.js 编写的 LLM/Agent 应用安全测试框架：先对目标应用源码做静态分析，提取工具、角色、守卫与鉴权信息，再据此生成针对该实现的攻击链，覆盖 167 个攻击类别与 170 种策略；被拒后由 PAIR 循环将目标回复与 LLM 裁判判定回传给攻击模型迭代重试。裁判按攻击族施加证据门控，输出 JSON/Markdown 报告与 OWASP LLM Top 10 合规映射。提供 CLI、React 仪表盘、自然语言助手与 Docker 部署四种运行方式，需配置至少一个 LLM API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 源码静态分析驱动的定向攻击生成（工具图/鉴权/守卫感知）
- 167 个攻击类别 × 170 种策略，含多轮渐强攻击（最多 15 轮）
- PAIR 自适应循环：被拒攻击基于目标回复与裁判判定迭代修订
- LLM 裁判按攻击族施加证据门控，并对齐手工标注金标集

## 适用场景

- 上线前对带工具/MCP 的 AI agent 做安全红队测试
- 测试 RAG 应用的投毒、越权与数据外泄风险
- 按 OWASP LLM Top 10 生成合规报告
- 度量守卫的拦截率与误伤率

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: **White-box red teaming for agentic AI apps. Reads your code, finds bugs specific to your stack — not generic prompt
> L11: Most LLM red-teaming tools are black-box: they treat your agent as an opaque endpoint and fire generic adversarial 
> L13: Red-Team AI is built for that gap. It reads your application's source code first, learns your tools, roles, and gua

## 星数曲线

```mermaid
xychart-beta
    title "votal-ai-hq/ai-red-teaming 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-29 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0e8b14bdb0e8` · [字段定义](../../DATASET.md)*
