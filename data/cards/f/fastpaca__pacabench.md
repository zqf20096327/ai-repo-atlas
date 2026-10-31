# fastpaca/pacabench

⭐ 13 · Rust · Apache-2.0 · 推送 2026-09-26 · [GitHub](https://github.com/fastpaca/pacabench) · [官网](https://fastpaca.com) · 个人维护

**本地优先的 LLM Agent 评测框架：可恢复、进程隔离**

用 Rust 编写、经 pip 分发的 LLM agent 基准评测工具。Agent 以子进程运行，通过 stdin/stdout 交换 JSON，单个崩溃不中断整体；每个用例后保存状态，支持中断后恢复与失败重试；内置代理拦截 API 调用（OPENAI_BASE_URL 注入）记录延迟与 token 用量；提供 YAML 单文件配置、TUI 运行界面与 export CLI，评分支持 LLM judge、regex、F1 等。面向在本地跑 agent 基准评测的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 进程隔离运行 agent，单个崩溃记录失败并继续
- 逐用例持久化状态，支持断点恢复与一键重试失败
- 内置代理拦截 API 调用，记录真实延迟与 token 用量
- Agent 通过 stdin/stdout JSON 协议接入，无专属 SDK

## 适用场景

- 本地长时间跑 agent 基准评测，中断后从断点恢复
- 只重跑失败用例并导出结果做分析
- 统计 agent 基准运行的实际 token 成本与延迟

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3:  A local-first harness for LLM agent benchmarks.
> L194: 2. **Proxy**: Intercepts API calls to provide ground-truth metrics (`OPENAI_BASE_URL` injection).

## 星数曲线

```mermaid
xychart-beta
    title "fastpaca/pacabench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c80d0df3db9e` · [字段定义](../../DATASET.md)*
