# xynehq/xyne

⭐ 696 · TypeScript · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/xynehq/xyne) · [官网](https://xyne.ai) · 组织维护

**面向工作的 AI 优先搜索与问答引擎，聚合企业应用数据**

连接 Google Workspace（Drive/Docs/Gmail/日历/联系人等）、Slack、Atlassian、GitHub 等工作应用，安全索引数据并构建关系图，提供跨应用的搜索与带来源引用的问答体验。模型无关，可接入任意 LLM 或云服务商，也可经 Ollama 指向本地 DeepSeek；自托管部署，权限实时继承源应用，声明不在用户数据上训练、无遥测。README 首行声明仓库已迁移至 juspay/xyne-spaces，此处不再维护。通过 docker-compose 单命令部署，也支持本地与 AWS EC2 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 连接多工作应用并索引数据、构建关系图，输出带来源的回答
- 模型无关：可接任意 LLM/云服务商，也可经 Ollama 跑本地 DeepSeek
- 自托管（本地/本地机房/云），权限继承源应用并实时生效
- docker-compose 单命令部署

## 适用场景

- 在公司内部跨 SaaS 应用、文档、邮件、消息统一搜索与提问
- 追踪某客户/工单/功能相关的全部信息
- 在企业内私有化部署 AI 搜索而不外发数据

## 场景标签

 · 领域:企业搜索/生成式问答

## 证据(README 行号)

> L17: Xyne is an AI-first Search & Answer Engine for work. We’re an OSS alternative to Glean, Gemini and MS Copilot.
> L19: Your work information has become fragmented — across so many SaaS apps, docs, files, repos, projects, issues, email

## 星数曲线

```mermaid
xychart-beta
    title "xynehq/xyne 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 695 --> 697
    line [696, 696]
```

2026-10-18 696 → 2026-10-23 696（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `e35999e76b0f` · [字段定义](../../DATASET.md)*
