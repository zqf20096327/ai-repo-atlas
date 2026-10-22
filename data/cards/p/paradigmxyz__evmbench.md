# paradigmxyz/evmbench

⭐ 463 · TypeScript · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/paradigmxyz/evmbench) · [官网](https://paradigm.xyz/evmbench) · 组织维护

**智能合约漏洞挖掘的基准评测与 agent 运行框架**

evmbench 提供一套面向智能合约漏洞检测的评测基准与 agent 运行装置：用户上传合约源码 zip，选择模型与推理级别，系统经 FastAPI 后端、RabbitMQ 队列与 Docker/Kubernetes worker 启动 Codex 的 detect-only 模式运行审计，产出结构化漏洞报告（含 vulnerabilities JSON）并在 Next.js 前端渲染。支持 BYOK 与可选代理令牌两种 OpenAI 凭据模式，默认审计时限 10800 秒。面向区块链安全研究者与评测场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 上传合约源码并驱动 Codex detect-only 模式产出结构化漏洞报告
- FastAPI 后端 + Postgres + RabbitMQ + Docker worker 的作业流水线
- BYOK 与代理令牌两种 OpenAI 凭据处理模式
- 评测代码以固定子模块 frontier-evals/ 收录

## 适用场景

- 评测不同模型在智能合约漏洞检测任务上的表现
- 批量对合约源码跑 agent 审计并查看带文件导航的报告
- 研究面向不可信代码的 agent 沙箱运行安全边界

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L3: **evmbench is a benchmark and agent harness for finding and exploiting smart contract bugs.**
> L27: 4. The worker fetches its bundle from the Secrets Service, unpacks the uploaded zip to `audit/`, then runs Codex in
> L31: 5. The agent writes `submission/audit.md`. The worker validates that the output contains parseable JSON with `{"vul

## 星数曲线

```mermaid
xychart-beta
    title "paradigmxyz/evmbench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 461 --> 465
    line [462, 464, 463]
```

2026-10-18 462 → 2026-10-22 463（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `130bf8d693af` · [字段定义](../../DATASET.md)*
