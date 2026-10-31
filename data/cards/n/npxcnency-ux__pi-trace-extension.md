# npxcnency-ux/pi-trace-extension

⭐ 22 · Python · MIT · 推送 2026-09-01 · [GitHub](https://github.com/npxcnency-ux/pi-trace-extension) · [官网](https://github.com/npxcnency-ux/pi-trace-extension) · 个人维护 · 中文 README

**pi-agent 的本地追踪查看器：把会话重组为执行视图**

pi-agent 的扩展插件，订阅其生命周期事件，将 message 导向的 session.jsonl 重建为执行树：每个 LLM 调用、工具执行、子代理及耗时、token 成本与结果。每会话产出 events.jsonl（追加式事件流）与 trace.html（单文件、无外部资源的 Langfuse 风格查看器），另提供跨会话仪表盘。全程本地、无网络代码。限制：单用户单机、需 Python 3.8+ 与 Node 18+、绑定 pi-agent 事件流、超 5MB 渲染变慢。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 将 pi 会话重组为 session→interaction→turn 树，区分 aborted/error/ok 并重试检测
- 单文件 trace.html 查看器，无 CDN、无分析脚本
- 跨会话仪表盘（KPI 卡片、可排序搜索表、项目过滤）
- 仅键名脱敏（password/token/secret 等），原始提示词原样落盘

## 适用场景

- 逐步查看 LLM 实际输入输出与工具执行，调试提示词与子代理编排
- 在数据不出本机的环境查看 agent 会话追踪
- 查看每轮 token 用量与成本，无需付费托管面板

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L11: **pi-trace-extension reorganizes a pi-agent session from a *conversation* view into an *execution* view.** pi's own
> L15: - **`events.jsonl`** — machine-readable, append-only event stream
> L16: - **`trace.html`** — a self-contained, single-file, Langfuse-style viewer (zero external assets, opens in any brows

## 星数曲线

```mermaid
xychart-beta
    title "npxcnency-ux/pi-trace-extension 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-31 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c8fdffd78af4` · [字段定义](../../DATASET.md)*
