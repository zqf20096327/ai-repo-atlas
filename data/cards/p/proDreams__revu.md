# proDreams/revu

⭐ 25 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/proDreams/revu) · [官网](https://pressanybutton.ru/) · 个人维护

**自托管的 AI Pull Request 代码评审服务**

ReVu 是自托管的 AI 代码评审工具，以两种方式运行：常驻服务器接收 GitHub/Gitea/GitLab/Bitbucket 的 webhook 并将评审结果发布回 PR；或在 GitHub Actions、GitLab CI、Gitea Actions 中以 revu review 命令运行。支持 comment 与 inline 两种评审模式，重复评审会记住先前意见不重复报错；deep 模式下模型可读取仓库结构与函数全文；发布前将评论与 diff 核对以过滤虚构行号。兼容 OpenAI API 及兼容服务（OpenRouter、LocalAI、LM Studio），另接入 GigaChat 与 YandexGPT。单个 YAML 配置文件配置，以 Docker 镜像分发；服务器模式需要域名与 SSL（与 Git 服务器同 Docker 网络时可省），需 Git 提供商的 PAT 与 AI 提供商 API key。技术栈为 Python 3.13+、FastAPI。

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

- Webhook 服务器与 CI 管道两种运行方式
- 支持 GitHub/Gitea/GitLab/Bitbucket，一个实例服务多个连接
- 重复评审记住先前意见，修复项不重复报告
- deep 模式提供仓库结构与函数级上下文，发布前校验评论对应的 diff 行

## 适用场景

- 在 PR 流程中让 AI 先做一轮评审再交给人看
- 用同一实例同时评审 GitHub、GitLab（含 self-managed）与 Gitea 上的仓库
- 通过 OpenAI 兼容接口接入自建或本地模型做私有化代码评审

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L33: ReVu — это AI-ревью для Pull Request: self-hosted вебхук-сервис либо команда в пайплайне.
> L78:  * Совместимость с **OpenAI API** и его альтернативами (OpenRouter, LocalAI, LM Studio и др.), а также
> L83:  * Можно использовать локальные модели (например, DeepSeek, Qwen), запуская их отдельно в вашей инфраструктуре.

## 星数曲线

```mermaid
xychart-beta
    title "proDreams/revu 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-27 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `a955b9198a51` · [字段定义](../../DATASET.md)*
