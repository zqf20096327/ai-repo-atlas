# mateaix/mateclaw

⭐ 1,217 · Java · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/mateaix/mateclaw) · [官网](https://claw.mate.vip) · 组织维护 · 中文 README

**自托管的多智能体数字员工平台：记忆、知识、IM 渠道一体**

基于 Spring Boot 与 Spring AI Alibaba 的自托管个人/团队 AI 代理平台，以"数字员工"形式提供角色、目标、持久记忆、SKILL.md 技能包与 MCP 扩展。支持双运行时：内置 AgentScope 运行时（ReAct、Plan-and-Execute、Team Runs）或外部 DSH CLI 托管循环；模型供应商可配置优先级链，主模型故障时按序重试。知识侧提供 LLM Wiki（摘要、[[链接]]、可溯源引用）与记忆生命周期管理。可通过 Web 控制台、Electron 桌面端、Webchat 嵌入脚本、9 种 IM 渠道与 Plugin SDK 五种界面使用。持久化 Goal 提供检查点与重启续跑。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多供应商优先级链与健康追踪，主模型失效时切换下一个可用供应商
- LLM Wiki 将原始文档摘要为互链页面并保留可溯源引用
- 持久化 Goal 提供检查点、重启恢复与续跑
- 五种使用界面：Web 控制台、Electron 桌面、Webchat 嵌入、IM 渠道、Plugin SDK

## 适用场景

- 搭建可审计、带审批门的多用户 AI 员工工作区
- 通过钉钉/飞书/企业微信等 IM 渠道接入团队 AI 助手
- 将上传的 PDF 与文档整理为互链、可引用的知识库
- 长时间任务在服务重启后从检查点继续执行

## 场景标签

`多智能体` `AI 助手` `知识库管理` · 领域:Agent 开发

## 证据(README 行号)

> L11:  Your second brain
> L33: > Multi-user workspaces. Approval-gated sensitive actions. Full audit trail. Spring Boot Actuator health monitoring
> L103: ### Agent Runtime: native or DSH (2.2.0+)

## 星数曲线

```mermaid
xychart-beta
    title "mateaix/mateclaw 星数(近 23 点)"
    x-axis ["2026-10-26", "2026-10-28", "2026-10-29", "2026-10-30", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 1166 --> 1221
    line [1170, 1172, 1173, 1174, 1175, 1176, 1170, 1187, 1190, 1192, 1194, 1196, 1199, 1200, 1203, 1204, 1206, 1207, 1208, 1209, 1213, 1214, 1217]
```

2026-10-26 1,170 → 2026-11-28 1,217（+47）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `02cfb29cc2ad` · [字段定义](../../DATASET.md)*
