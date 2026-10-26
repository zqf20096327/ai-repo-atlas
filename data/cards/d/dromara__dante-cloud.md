# dromara/dante-cloud

⭐ 969 · Java · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/dromara/dante-cloud) · [官网](https://www.herodotus.cn) · 个人维护 · 中文 README

**给企业的微服务/单体可切换云原生基座，含 AI Agent 开发支持**

基于 Spring 生态（Spring Boot 4.1、Spring Cloud 2025.1.3、Spring Cloud Alibaba/Tencent）的企业级微服务基座，采用 DDD 设计，拆分为主工程 Dante Cloud 与核心组件库 Dante Engine 两个工程。宣称一套代码可在微服务与单体两种架构间切换；支持多租户、IoT 设备认证、国密数字信封加解密，并定位为面向 AI Agent 开发的智能基座。要求 JDK 25（历史分支 JDK 17/8），主分支为 master，多个历史分支停止维护。协议为 Apache 2.0 附加禁止二次开源等条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一套代码在微服务与单体两种架构间切换
- 拆分 Dante Cloud 主工程与 Dante Engine 组件库，模块可插拔组合
- 覆盖多租户、IoT 设备认证、国密加解密、三级等保等安全体系
- README 明确定位面向 AI Agent 开发的智能基座（未展开 AI 机制细节）

## 适用场景

- 企业在单体与微服务架构间按阶段灵活切换开发
- 数字化转型项目直接使用微服务版，跳过基础组件整合
- 基于组件库像乐高一样组合搭建自己的应用系统
- 学习 Spring 生态组件与 DDD 划分的代码案例

## 场景标签

 · 领域:企业级后端/微服务基础设施

## 证据(README 行号)

> L34: **Dante Cloud** 国内首个支持阻塞式和响应式服务并行的、开箱即用的企业级云原生微服务基座和面向 AI Agent 开发的智能基座。是采用**领域驱动模型(DDD)**设计思想，以「**高质量代码、低安全漏洞**」为核
> L44: **Dante Cloud** 优秀的模块化能力，为系统提供了高度灵活的配置能力、**功能的“可插拔”能力** 以及不同需求场景的适配能力。正因为优秀的模块化体系，使得 **Dante Cloud** 不仅是一套完整的微服务架构，

## 星数曲线

```mermaid
xychart-beta
    title "dromara/dante-cloud 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 968 --> 970
    line [969, 969]
```

2026-10-18 969 → 2026-10-26 969（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 low · 依据 README sha `79729175b5f4` · [字段定义](../../DATASET.md)*
