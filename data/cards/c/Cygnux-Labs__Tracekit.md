# Cygnux-Labs/Tracekit

⭐ 921 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/Cygnux-Labs/Tracekit) · [官网](https://cygnuxlabs.com/tracekit) · 组织维护

**为 AI agent 工具调用提供防篡改审计与策略拦截的记录器**

Tracekit 嵌入 agent 的工具调用路径：每次调用执行前进行允许/拒绝/人工审批判定，调用、决策与结果由 agent 不可触达的签名进程写入哈希链追加式日志，构建方式参照 Certificate Transparency，由独立见证方共同签名。每次运行可导出为 .tkb 文件，任何人在浏览器中即可离线验证，篡改记录会精确定位到具体事件。提供 Python/TypeScript/Go 验证器，MIT 许可，宣称在 480 次试验中拦截全部 8 类篡改攻击。要求 Python 3.9–3.13，框架集成需 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 工具调用执行前的策略门：允许、拒绝或转人工审批，审批绑定精确参数且一次性有效
- 签名进程与哈希链日志，agent 无法修改，丢失事件呈现为签名缺口
- .tkb 导出文件支持离线验证（含浏览器端），篡改定位到具体记录
- 集成 42 种 agent 框架与编码 agent，含 Claude Code hooks、OpenTelemetry、MCP 网关

## 适用场景

- 编码 agent（Claude Code 等）上生产前拦截 rm -rf、force-push 等危险调用
- 向企业客户交付可离线验证的 agent 行为记录文件
- 安全团队建立统一控制点并对接 EU AI Act、ISO 42001 等合规映射
- 审计/GRC 人员自行核验 agent 运行记录而非依赖厂商陈述

## 场景标签

`LLM 可观测性` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L40: |**Stop**|Checks every tool call *before it runs*: allow, deny, or hold it for a person. An approval covers exactly
> L130: `tracekit.instrument()` starts a dev signer (or reuses the running one) and gates and records every tool and model

## 星数曲线

```mermaid
xychart-beta
    title "Cygnux-Labs/Tracekit 星数(近 25 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 73 --> 998
    line [173, 250, 259, 353, 355, 357, 358, 359, 150, 603, 605, 646, 687, 726, 727, 728, 772, 734, 760, 799, 841, 837, 914, 917, 921]
```

2026-10-26 173 → 2026-11-28 921（+748）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `cfbe3787b44e` · [字段定义](../../DATASET.md)*
