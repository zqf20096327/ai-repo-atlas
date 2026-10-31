# chaosxingxc-orion/spring-ai-ascend

⭐ 15 · Java · 推送 2026-08-04 · [GitHub](https://github.com/chaosxingxc-orion/spring-ai-ascend) · 个人维护 · 中文 README

**面向华为昇腾/鲲鹏的自托管企业级 agent 运行时平台**

基于 Spring AI + Spring Boot + Java 21 的开源企业级 agent 平台，以 4 个 Maven 模块（agent-runtime/agent-service/agent-bus/BoM）提供双模式编排：同一运行时跑确定性 graph 状态机与 ReAct agent 循环，经 SuspendSignal 共享中断原语。内存、持久化、模型网关、工具授权均为 SPI 接口，通过 @Bean 覆盖扩展。支持多租户与审计日志，dev/research/prod 三档 posture，research/prod 启动时 fail-closed。当前已交付的是硬件无关的 Spring AI/Java 内核；昇腾 NPU 模型服务与鲲鹏调优部署路径为设计目标，尚未交付。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 同一运行时支持 graph 状态机与 ReSpec 式 agent 循环的双向嵌套（SuspendSignal 统一中断）
- 记忆/持久化/模型网关/工具授权/弹性均为 SPI 可插拔接口
- 多租户 run 隔离、持久化幂等与结构化审计日志
- 65 条架构约束·65 个 ADR·32 条 gate 规则的 Code-as-Contract 治理门，漂移即 fail-closed

## 适用场景

- 在自有昇腾/鲲鹏硬件上自建受治理的多租户 agent 运行时
- 用 Spring Boot 方式扩展并替换 agent 平台的内存/模型网关等组件
- 受监管行业（如金融服务）以 fail-closed posture 部署 agent 工作负载

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: > An open-source, enterprise-grade **agent platform** built for the Huawei **Ascend (NPU)** + **Kunpeng (CPU)** stac
> L5: `spring-ai-ascend` lets a team stand up its own governed agent runtime the way it
> L38: - **Dual-mode orchestration.** One runtime runs both deterministic **graph**
> L43: - **Pluggable by SPI, not by patching.** Memory, run persistence, model gateway,

## 星数曲线

```mermaid
xychart-beta
    title "chaosxingxc-orion/spring-ai-ascend 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `21ad8290b58f` · [字段定义](../../DATASET.md)*
