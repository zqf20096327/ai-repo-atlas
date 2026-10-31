# vllm-doctor/vllm-doctor

⭐ 18 · Rust · Apache-2.0 · 推送 2026-07-31 · [GitHub](https://github.com/vllm-doctor/vllm-doctor) · [官网](http://docs.vllm.doctor/) · 组织维护

**vLLM 推理服务器瓶颈诊断 CLI：从实时指标给出结论**

面向 vLLM 部署的命令行诊断工具：抓取 vLLM /metrics 或 Prometheus 指标，按内置规则（队列压力、TTFT/TPOT、KV cache 压力、错误率、副本不均等）输出最可能的瓶颈、证据与下一步建议；支持 rich 表格或 JSON 结构化输出、本地历史记录与 TOML 阈值配置。README 声明其非仪表盘替代或基准测试工具，定位为单服务器侧诊断快照，可与 GuideLLM 搭配使用。提供安装脚本、Cargo、Docker 三种安装方式。

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

- 内置 9 类诊断规则（队列压力、TTFT/TPOT、KV cache、前缀缓存等）
- 支持 Prometheus 或直接 /metrics 双输入，输出 rich 表格或 JSON
- 本地历史持久化与 --save --watch 变化感知记录
- TOML 按规则配置阈值，mock 数据示例可免装 vLLM 试用

## 适用场景

- 线上 vLLM 服务响应变慢时快速定位瓶颈
- 自动化运维流水线中用 JSON 输出做健康检查
- 结合 GuideLLM 压测时解释服务端症状

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: Diagnose vLLM server bottlenecks from live metrics.
> L7: vLLM Doctor turns live vLLM metrics into a clear diagnosis: the most likely bottleneck, the evidence behind it, and 
> L18: - **Built-in diagnosis rules** — queue pressure, TTFT/TPOT bottlenecks, KV cache pressure, low throughput, error ra

## 星数曲线

```mermaid
xychart-beta
    title "vllm-doctor/vllm-doctor 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-31 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2404fe9219e6` · [字段定义](../../DATASET.md)*
