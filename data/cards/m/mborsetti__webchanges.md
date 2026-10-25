# mborsetti/webchanges

⭐ 50 · Python · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/mborsetti/webchanges) · [官网](https://pypi.org/project/webchanges/) · 个人维护

**网页变更监控工具：匿名检测网页/图片/命令变化并通知，含 AI 摘要**

由 urlwatch 2.21 分叉而来的网页变更监控工具：以匿名方式定时抓取网页内容（含图片）或命令输出，与上次结果对比后将变更通知发送到邮件等多种平台。差异比较方式包括 Gemini 生成式 AI 摘要（BETA，需 Google Cloud AI Studio 免费 API Key）、JSON/XML 结构化 diff、图像视觉 diff。通过 JSON Schema 校验的 jobs.yaml/config.yaml 配置任务，支持 cron/Task Scheduler/launchd 调度，可选 curl_cffi 客户端绕过 TLS/JA3 指纹检测。以 Python 包形式经 uv/pip 安装，另有第三方 Docker 镜像与 GitHub Action 实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Gemini 生成式 AI 变更摘要（ai_google differ，标注 BETA）
- JSON/XML 结构化 diff 与图像视觉 diff（BETA）
- JSON-Schema 校验的 jobs.yaml/config.yaml 配置体系
- 可选 curl_cffi HTTP 客户端绕过 TLS/JA3 指纹检测

## 适用场景

- 定时监控网页内容变化并通过邮件等渠道收到通知
- 跟踪 API/JSON 数据或图片的变更并查看结构化差异
- 用自然语言摘要快速理解长网页改了什么

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L10: **webchanges** *anonymously* checks web content (including images) and commands for changes, delivering instant
> L15: - **AI-powered change summaries** via Gemini (`ai_google differ
> L16:  <https://webchanges.readthedocs.io/en/stable/differs.html#ai-google-diff>`__, BETA).

## 星数曲线

```mermaid
xychart-beta
    title "mborsetti/webchanges 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 48 --> 51
    line [49, 50, 50]
```

2026-10-18 49 → 2026-10-25 50（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `df110957ed70` · [字段定义](../../DATASET.md)*
