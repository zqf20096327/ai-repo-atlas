# omidbakhshi/merge-mind

⭐ 24 · Python · MIT · 推送 2025-11-15 · [GitHub](https://github.com/omidbakhshi/merge-mind) · [官网](https://omidbakhshi.github.io/merge-mind/) · 个人维护

**自托管 GitLab 的 AI 代码审查机器人**

面向自托管 GitLab（12.0+）实例的自托管代码审查机器人，使用 OpenAI GPT-4 模型对合并请求做上下文感知的代码审查，并在 GitLab 上以内联评论形式按严重级别发布问题。针对 Laravel、Nuxt.js、React、Django 等框架提供专项审查规则；通过 Qdrant 向量数据库存储代码嵌入，可从 GitLab 仓库或本地代码库学习团队编码模式。支持多项目配置、CI/CD 集成、React Web 仪表盘、热重载与熔断保护，推荐以 Docker Compose 部署，要求 Python 3.11+ 与 OpenAI API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 OpenAI GPT-4 的合并请求代码审查，输出内联评论与严重级别
- 针对 Laravel/Nuxt.js/React/Django 等框架的专项审查规则
- Qdrant 向量库存储代码嵌入，从代码库与已合并 MR 持续学习
- 提供 Web 仪表盘、健康检查/指标端点与外部服务熔断保护

## 适用场景

- 在自托管 GitLab 的合并请求流程中获得 AI 代码审查
- 按项目配置不同框架的审查规则与团队偏好
- 让审查机器人学习团队代码库模式并持续改进审查结果

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: An intelligent, self-learning code review bot for self-hosted GitLab instances. Uses OpenAI's GPT models to provide 
> L7: - **🤖 AI-Powered Reviews**: Leverages OpenAI GPT-4 for intelligent code analysis

## 星数曲线

```mermaid
xychart-beta
    title "omidbakhshi/merge-mind 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `3dedcbc82189` · [字段定义](../../DATASET.md)*
