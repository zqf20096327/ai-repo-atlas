# ByteBunny777/Promptrace

⭐ 34 · Python · MIT · 推送 2026-07-08 · [GitHub](https://github.com/ByteBunny777/Promptrace) · 个人维护

**零依赖的 LLM API 调用日志库：记录 token/成本/延迟到 JSONL**

面向调用 LLM API 的 Python 开发者的轻量日志与分析工具：用 LLMLogger 将每次 prompt/response 的 token 数、延迟与估算成本写入纯 JSONL 文件，通过 CLI（stats/tail/export/models）或 Python API 查看汇总统计。零外部依赖，仅用 Python 标准库；无网络调用、无配置。支持关闭明文存储仅保留 SHA-256 哈希，内置可编辑定价表，未知模型报 cost_usd=None。限制：定价表需自行核对与维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 JSONL 存储，可 grep、可 diff，无外部依赖（全部标准库）
- CLI 与 Python API 双通道输出调用统计（按 tag/model 分组、导出 CSV）
- 可关闭明文 prompt/response 存储，仅保留 SHA-256 哈希与长度
- 自定义定价表（dict 或 JSON 文件），未知模型不猜测成本

## 适用场景

- 我在项目里接入 LLM API 后想统计 token 消耗与成本
- 排查哪些 LLM 调用延迟高、按模型或标签分组分析
- 在不想上传数据到外部服务的前提下本地留存调用日志

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L8: Lightweight, **dependency-free** logging and analytics for LLM API calls.
> L10: Log every prompt/response with token counts, latency, and estimated cost to a

## 星数曲线

```mermaid
xychart-beta
    title "ByteBunny777/Promptrace 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-25 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2fcd243bfbbb` · [字段定义](../../DATASET.md)*
