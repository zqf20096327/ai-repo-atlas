# zencefilefendi/kadi

⭐ 25 · Python · Apache-2.0 · 推送 2026-10-11 · [GitHub](https://github.com/zencefilefendi/kadi) · [官网](https://github.com/zencefilefendi/kadi/blob/main/docs/THEORY.md) · 个人维护

**带 conformal 保证的 LLM 本地裁决层：常规决策本地答，其余升级到 oracle**

置于前沿 LLM（oracle）前方的三层级联判断系统：精确记忆 → 本地 reflex → oracle 升级。仅当统计证书允许时（split-conformal 预测集至多一个标签，或 Learn-then-Test 阈值）本地作答，在可交换性假设下将与 oracle 的分歧概率限制在用户选定 α 内。在线系统包含冻结模型版本、随机校准抽样、anytime-valid 认证与 e-detector 漂移检测；另有 OOD 守卫、PII 脱敏、防篡改账本、HTTP/MCP 服务与 Divan 仪表盘。纯标准库 Python，零依赖，支持 Anthropic/OpenAI 兼容 oracle（含 vLLM、Ollama、llama.cpp、LM Studio）、MCP 接入 Claude Code 及 TypeScript 客户端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三层级联：精确记忆 → 本地 reflex → oracle，本地回答带 Pr(disagree) ≤ α 证书
- conformal 与 anytime-valid LTT 两种策略，含 Mondrian 逐标签界与漂移 e-detector
- 纯标准库 Python 零依赖，支持 HTTP 服务、MCP 工具与 TypeScript 客户端
- Banking77/CLINC150 基准上 126 次运行边界均成立，α=5% 时移除 65%/79% oracle 调用

## 适用场景

- 对工单路由、垃圾标记等高频小决策减少前沿模型调用量
- 为 agent 提供带统计保证的本地裁决 MCP 工具
- 在审计或受监管场景下用 LTT 策略获得时序一致的高概率保证
- 通过 replay → shadow → live 流程安全上线

## 场景标签

`模型网关` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L20: Kadı is a three-tier cascade: exact memory → local reflex → oracle. The middle tier answers **only when a statistic
> L126: Oracles: `AnthropicOracle` (forced enum tool), `OpenAICompatibleOracle` (OpenAI, vLLM, Ollama, llama.cpp, LM Studi

## 星数曲线

```mermaid
xychart-beta
    title "zencefilefendi/kadi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `dfd96a0a0e51` · [字段定义](../../DATASET.md)*
