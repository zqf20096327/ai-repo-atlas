# yigitkonur/cli-batch-requester

⭐ 19 · Rust · MIT · 推送 2026-02-21 · [GitHub](https://github.com/yigitkonur/cli-batch-requester) · 个人维护

**面向 LLM 端点的高吞吐批量请求 CLI 客户端**

用 Rust 编写的命令行与库两用的批量 API 请求客户端：读取 JSONL 请求文件，向多个 LLM 端点分发请求，支持加权负载均衡、指数退避重试、按端点健康冷却、HTTP/2 连接池，结果与错误分别流式写入成功/失败文件。基于 Tokio 异步运行时，README 声称在普通硬件上达到 10k+ req/s。通过 cargo 安装，也可构建为 Rust 库使用；构建时如遇 OpenSSL 报错需 libssl-dev 或改用 rustls 特性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Tokio 异步运行时下的高吞吐批量请求分发
- 多端点/多 API key 加权负载均衡与健康冷却
- 指数退避重试与流式落盘输出（成功/错误分离）
- CLI 与 Rust 库两种使用形式

## 适用场景

- 批量跑 10 万条 LLM 请求并保存结果
- 在多个 API key/端点间分摊请求应对限流
- 作为 Rust 库嵌入自己的批处理管道

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L1: high-throughput batch API client for LLM workloads. load-balances across endpoints, retries with backoff, streams re
> L15: - **10k+ req/sec** on modest hardware (Tokio async runtime, work-stealing)
> L16: - **weighted load balancing** across multiple endpoints/API keys

## 星数曲线

```mermaid
xychart-beta
    title "yigitkonur/cli-batch-requester 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1760a37d47a2` · [字段定义](../../DATASET.md)*
