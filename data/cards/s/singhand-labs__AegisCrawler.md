# singhand-labs/AegisCrawler

⭐ 16 · Go · GPL-3.0 · 推送 2026-10-30 · [GitHub](https://github.com/singhand-labs/AegisCrawler) · 组织维护 · 中文 README

**录制即规则的浏览器数据采集平台，可选 LLM 增强规则**

由 Go 单二进制服务器、Chrome 录制扩展 PageResearch Agent 和 ScriptCat 用户脚本执行器组成：扩展录制真实页面上的点击/输入/滚动/拖拽并生成 YAML/JSON DSL 规则，服务器以租约认领、心跳续期、清扫恢复与死信队列调度任务，Admin UI 提供规则管理、cron 任务、审计日志与 DAG 视图。可选开启 LLM 规则增强（OpenAI/Anthropic 兼容），增强需经安全扫描与人工 diff 审批；无 LLM 时确定性基线规则照常工作。面向需要长期稳定、可调度采集的开发者/团队，UI 目前为中文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 录制浏览器交互并生成可执行 YAML/JSON DSL 规则
- 租约调度 + 心跳 + 死信队列的任务生命周期
- 可选 LLM 规则增强，经安全扫描与人工 diff 审批后生效
- 单二进制 Go 服务器内嵌 SQLite 与 Admin UI（无 CGO）

## 适用场景

- 把一次人工浏览操作固化成定时采集任务
- 在真实浏览器中按规则执行采集并回传结果
- 需要审计日志与审批流程的团队数据采集

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L24: - **Record → DSL → Task, no code.** The PageResearch Agent extension records clicks,
> L34: - **Optional LLM rule enhancement.** The server can patch a recorded baseline
> L116: approve/reject. The deterministic baseline always works, with or without the

## 星数曲线

```mermaid
xychart-beta
    title "singhand-labs/AegisCrawler 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7e70c72af083` · [字段定义](../../DATASET.md)*
