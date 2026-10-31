# ginsonko/newapi-smart-router

⭐ 18 · Go · AGPL-3.0 · 推送 2026-10-06 · [GitHub](https://github.com/ginsonko/newapi-smart-router) · [官网](https://github.com/ginsonko/newapi-smart-router#readme) · 个人维护 · 中文 README

**面向 New API 站点的每 Key 智能路由与自动容灾系统**

基于 New API 的路由扩展：智能路由 Key 在用户授权范围、倍率上限、端点合同、健康证据与安全重试边界内自动选择分组路线，支持价格/稳定/首字/综合/手动五种策略，提供共享健康、自愈恢复、实际路线计费（Route Receipt）、动态缓存经济与可解释决策日志。四种发行形态：Full 发行版、Certified Bridge、Custom Fork Integration Kit、Agent Parts Kit。当前为 v0.4.0-alpha.1 公开 Alpha，明确列出 Stable 阻断项，纯 Go 核心、AGPL-3.0-only 并另设商业许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 每 Key 策略记忆与倍率上限硬过滤
- 五种路由策略（价格/稳定/首字/综合/手动）
- 共享健康证据与自愈恢复，按错误域分类不互相污染
- Route Receipt 实际路线计费与缓存重建成本经济比较

## 适用场景

- New API 站点部署后为 Key 提供多分组自动容灾与活动价利用
- 长任务挂机时上游故障自动换线，无需改 Key 重启客户端
- 深度魔改 fork 通过 Integration Kit 按语义接点合并接入

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L39: > 面向 New API 站点的每 Key 智能路由、共享健康、自愈恢复、实际路线计费与可解释决策系统。
> L169: Bridge 是针对明确上游版本编译进 New API 的极薄接入层，算法核心、恢复 Worker 和复杂控制面尽量独立。它的作用是补齐纯 Sidecar 无法获得的生命周期接点：

## 星数曲线

```mermaid
xychart-beta
    title "ginsonko/newapi-smart-router 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2915bd4738a9` · [字段定义](../../DATASET.md)*
