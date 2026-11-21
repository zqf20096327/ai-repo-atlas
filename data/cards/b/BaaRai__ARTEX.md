# BaaRai/ARTEX

⭐ 13,559 · Go · AGPL-3.0 · 推送 2026-11-20 · [GitHub](https://github.com/BaaRai/ARTEX) · 个人维护

**自托管多 Agent 自主渗透测试平台，发现绑定证据链**

ARTEX 是自托管的 LLM 驱动渗透测试平台：planner 将目标分解为 intent，worker 用真实工具执行并把资产/事实/发现写回资产图与探索图两张关联图。每个发现可绑定捕获的 HTTP 请求/响应作为证据，自主动作经范围门、人工审批门与 token/轮次预算约束。单个 Go 二进制内嵌 Next.js UI，需 PostgreSQL，LLM 端点自配；无预构建镜像，需从本地检出构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双图架构：共享资产图 + 每任务探索图，锚点互联并支撑覆盖统计
- 录流 MITM 代理与浏览器扩展捕获流量，发现绑定到原始请求/响应
- 人工审批门、argv 前缀规则、范围/预算限制与不可信输出边界
- 支持 Anthropic、OpenAI 兼容中转与本地 Ollama，多配置轮换与故障转移

## 适用场景

- 对授权目标执行自主化渗透测试并保留完整审计链
- 漏洞复测：retester agent 重新验证发现是否可复现或已修复
- 企业级资产图管理与测试覆盖可视化
- 与 ScopeSentry 同步资产数据后交给 agent 探索

## 场景标签

`多智能体` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L19: ARTEX is a self-hosted, LLM-driven penetration testing platform. It is not a chat wrapper around
> L9: Self-hosted multi-agent offensive security. A planner explores, workers run real tools,
> L33: - **Self-hosted and model-agnostic.** One Go binary with the Next.js UI embedded, PostgreSQL,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `c031349979c1` · [字段定义](../../DATASET.md)*
