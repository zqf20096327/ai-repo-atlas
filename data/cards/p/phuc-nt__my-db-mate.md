# phuc-nt/my-db-mate

⭐ 15 · TypeScript · NOASSERTION · 推送 2026-08-27 · [GitHub](https://github.com/phuc-nt/my-db-mate) · 个人维护 · 中文 README

**自托管的与数据库对话应用：自然语言提问，只读 SQL 回答并生成图表**

面向 DevOps/DBA 的 self-host 应用（Next.js + TypeScript）：自然语言提问生成只读 SQL 并以图表、仪表盘、指标 digest 等形式回答。核心机制是两层：由用户逐步积累的 context 层（glossary、schema 注释、governed metrics、verified queries）与物理安全层（按 connection 限定可读表、AST 完整检查运行时拦截、credential 加密、审计日志）。支持多步 agentic 分析、BigQuery 成本控制（dry-run、字节硬上限、每日预算）、MCP 暴露 governed metric。许可为 PolyForm Noncommercial，商业使用需另行联系作者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- context 层（glossary/governed metrics/verified queries）与运行时 AST 检查的只读强制
- 一句话生成 4-8 widget 仪表盘、AI 单句改图表（diff 预览、run-before-swap）
- MAD 基线异常检测、data-drift 监控、定时 digest webhook
- MCP tools 只读暴露 governed metric 供外部 AI（Claude/ChatGPT）使用

## 适用场景

- DBA/DevOps 用自然语言应付业务方的临时取数需求
- 自助搭建 AI 辅助图表与仪表盘替代部分拖拽式 BI 工作
- 对生产库做带只读强制与审计日志的受控查询入口
- 通过 MCP 让 Claude/ChatGPT 复用已治理的指标定义

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: **Chat với database của bạn.** Hỏi bằng ngôn ngữ tự nhiên, nhận câu trả lời dựa trên SQL thật, không cần viết truy v
> L7: Chat với database: câu hỏi → SQL → chart
> L23: **Lập luận trên có đo được không?** Có. Trên bộ BIRD mini-dev, tắt lớp context làm giảm **14 điểm** (`qwen/qwen3.7-

## 星数曲线

```mermaid
xychart-beta
    title "phuc-nt/my-db-mate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `15bc4651fe37` · [字段定义](../../DATASET.md)*
