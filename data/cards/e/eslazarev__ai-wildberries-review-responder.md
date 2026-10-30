# eslazarev/ai-wildberries-review-responder

⭐ 18 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/eslazarev/ai-wildberries-review-responder) · [官网](https://eslazarev.github.io/ai-wildberries-review-responder/) · 个人维护

**用 LLM 自动回复 Wildberries 买家评价的服务**

面向 Wildberries 平台卖家的评价自动回复服务：按定时计划从卖家后台拉取未回复评价，把每条评价（含图片/视频信息）组装成 LLM 提示词，生成指定语气与语言的回复，再通过 Wildberries Feedbacks API 发布回去。卖家的 API 令牌由自己持有，不与第三方共享。支持 YandexGPT 与 OpenAI 兼容模型（含本地 Ollama），可部署到 Yandex Cloud Functions、Docker、Kubernetes（Helm）或本地运行；提示词、模型、频率等通过 settings.yaml 与环境变量配置。生产实测约 0.25 卢布一条回复。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 定时拉取未回复评价并经 LLM 生成回复后发布回 Wildberries API
- 支持 YandexGPT、OpenAI 兼容 API 及本地 Ollama（localhost:11434/v1）
- 卖家自行持有 Wildberries API 令牌，不与第三方共享
- 三种运行方式：Yandex Cloud Functions（Serverless）、Docker、Kubernetes Helm CronJob

## 适用场景

- Wildberries 卖家按计划自动回复买家评价
- 按品牌口径自定义回复语气与提示词模板
- 在自有云环境（Yandex Cloud/K8s/本地）中运行以保留令牌控制权

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L19: Этот сервис автоматически подхватывает новые отзывы из кабинета продавца Wildberries, генерирует ответ через LLM и 
> L36: 3. LLM генерирует ответ в нужном тоне и языке.

## 星数曲线

```mermaid
xychart-beta
    title "eslazarev/ai-wildberries-review-responder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `c13670c6d985` · [字段定义](../../DATASET.md)*
