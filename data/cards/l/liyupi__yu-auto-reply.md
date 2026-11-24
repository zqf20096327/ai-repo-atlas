# liyupi/yu-auto-reply

⭐ 887 · Java · 推送 2026-11-23 · [GitHub](https://github.com/liyupi/yu-auto-reply) · 个人维护 · 中文 README

**给社区运营者的多平台监控 AI 自动回复客服工具**

基于 Java Spring Boot 的消息监控与 AI 自动回复系统，将「监听新问题」与「生成回复」通过 Monitor/Answerer 接口解耦，以中介者、工厂、策略模式编排，借助 Spring Scheduler 按 Cron 周期驱动多个任务。内置知识星球提问监控器与 OpenAI 回答器（可切换 gpt-4 等模型），支持 YAML 声明多任务与环境变量动态配置，提供 Dockerfile 与 Railway 一键部署。面向需要 7x24 小时答疑的个人开发者与团队，同时定位为 Java 设计模式教学范例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Monitor 与 Answerer 接口解耦，工厂模式按配置动态组合监控者与回答者
- 内置知识星球提问监控与 OpenAI 回答器，YAML 声明多任务 Cron 调度
- 提供 Dockerfile 与 Railway 一键部署，环境变量覆盖配置
- 默认模拟监控器/回答器支持本地无外部依赖调试

## 适用场景

- 为知识星球社区搭建 7x24 小时自动答疑机器人
- 扩展接入微信公众号、企业微信、钉钉、飞书等平台自动回复
- 二次开发切换 DeepSeek、通义千问、智谱 GLM 等大模型回答器
- 作为 Java 后端设计模式实战学习项目拆解源码

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L21: `yu-auto-reply` 是由 程序员鱼皮 开源的一款基于 Java Spring Boot 的平台消息监控与 AI 自动回复工具。在运营技术社区、知识付费圈子或日常客服群时，维护者往往需要持续回复大量重复性或基础性的提问。
> L79: 1. 项目定义了统一的 `Answerer` 回答者接口，将不同 AI 模型或规则引擎的回复逻辑封装为可替换的实现类。
> L89: 借助上述解耦架构，当你需要把 `yu-auto-reply` 接入微信公众号、企业微信、钉钉、飞书、GitHub Issues 等其他平台，或者切换为 DeepSeek、通义千问、智谱 GLM 等其他大模型时，只需要新增对应的实现


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `ac4e32a2ed3a` · [字段定义](../../DATASET.md)*
