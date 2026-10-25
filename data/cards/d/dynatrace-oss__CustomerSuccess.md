# dynatrace-oss/CustomerSuccess

⭐ 37 · Apache-2.0 · 推送 2026-08-26 · [GitHub](https://github.com/dynatrace-oss/CustomerSuccess) · 组织维护

**给 Dynatrace 平台管理员的观测性采用与运维仪表盘集合**

Dynatrace 维护的开源解决方案集合，面向平台管理员，包含三个组件：Dynatrace Tenant Review 仪表盘（分析配置与能力采用状态）、Platform Adoption Dashboard（59 个磁贴，覆盖用户活跃度、工作流健康、DPA Score 与 Dynatrace Assist/AI 使用分析，含 AI 生成的叙述性报告）、Software Obsolescence Management（JavaScript Workflow 定期从 endoflife.date/deps.dev 等开源 API 刷新过时数据，配合 DQL 仪表盘给出维护优先级）。安装方式均为下载 JSON 定义并导入租户的 Dashboards 应用；仪表盘设计为只读权限，数据不离开租户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个可导入的 Dynatrace 仪表盘/工作流 JSON 组件
- 7 维 DPA Score 与 Gaps & Actions 磁贴分析平台采用情况
- Dynatrace Assist 报告磁贴与 AI 叙述性报告（近 30 天）
- 从 endoflife.date/deps.dev 拉取软件过时数据并匹配原生数据

## 适用场景

- 导入仪表盘分析团队对 Dynatrace 平台的采用与闲置能力
- 用 AI 叙述报告总结采用趋势与下一步建议
- 审计软件组合的过时与漏洞风险并排定维护优先级

## 场景标签

 · 领域:IT 可观测性/运维

## 证据(README 行号)

> L27: This Dashboard leverages Grail™ events, query execution telemetry, workflow events and billing data to surface acti
> L50: - Track Dynatrace Assist and Dynatrace Intelligence usage across the platform
> L52: - Generate a **Dynatrace Assist narrative report** summarizing adoption trends, top users, trending/fading apps, an

## 星数曲线

```mermaid
xychart-beta
    title "dynatrace-oss/CustomerSuccess 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24", "2026-10-25"]
    y-axis "stars" 35 --> 38
    line [37, 36, 37, 37]
```

2026-10-18 37 → 2026-10-25 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3df1db5fa944` · [字段定义](../../DATASET.md)*
