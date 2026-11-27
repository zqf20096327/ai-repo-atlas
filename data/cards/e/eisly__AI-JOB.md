# eisly/AI-JOB

⭐ 4 · Java · 推送 2026-11-26 · [GitHub](https://github.com/eisly/AI-JOB) · 个人维护 · 中文 README

**面向求职者的简历、岗位匹配与模拟面试 AI 应用**

由 Vue 3 前端、Spring Boot 业务后端（Flyway 数据库迁移）和 Python AI Agent 三部分组成的求职场景应用，覆盖求职画像、简历管理与分析、岗位搜索与匹配、专项训练、项目实战和模拟面试。运行依赖 MySQL、Redis、Mailpit（Docker Compose 提供），AI 模型调用需配置 DeepSeek API Key，未配置时默认 auto 模式使用模拟模型；语音识别与合成、网页搜索、代码仓库搜索分别支持配置阿里云百炼、Tavily、Brave、GitHub/Gitee/GitCode 等来源。README 以 Windows PowerShell 本地开发为例说明启动流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三段架构：Vue 3 前端 + Spring Boot 后端 + Python Agent
- 未配置模型 Key 时 auto 模式使用模拟模型运行
- 岗位搜索支持 Tavily、Brave 及 GitHub/Gitee/GitCode 多来源
- 语音识别与合成走阿里云百炼，默认 fake ASR

## 适用场景

- 管理简历并获得简历分析结果
- 搜索岗位并做匹配推荐
- 进行专项训练与模拟面试

## 场景标签

 · 领域:求职/招聘工具

## 证据(README 行号)

> L3: AI-JOB 是一个面向求职场景的应用，涵盖求职画像、简历管理与分析、岗位搜索与匹配、专项训练、项目实战和模拟面试。项目由 Vue 前端、Java 业务后端和 Python Agent 组成；具体功能和运行方式以当前代码为准。
> L12: project/agent/      Python AI Agent


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `30e94b5a591a` · [字段定义](../../DATASET.md)*
