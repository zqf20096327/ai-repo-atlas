# aincient-labs/atelier-cms

⭐ 24 · PHP · GPL-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/aincient-labs/atelier-cms) · [官网](https://aincient-labs.com) · 组织维护

**自托管 AI 原生 CMS：通过对话管理 Drupal 站点并导出静态站**

基于 Drupal 构建的自托管内容管理系统，以对话式 AI 操作台（/atelier）替代传统管理表单：用户用自然语言让助手创建、查找、发布、删除内容，助手在用户账号权限范围内调用工具执行。支持接入 Anthropic/OpenAI API key 或本地 Ollama。站点可导出为纯静态 HTML 部署到任意主机（Netlify/Cloudflare Pages/Vercel/GitHub Pages）。以版本化容器镜像分发，内置 PostgreSQL 16（pgvector）为唯一支持数据库，默认锁定 Drupal 能力范围，通过 atelier CLI 或 Docker Compose 安装升级。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对话式 AI 操作台完成内容全生命周期管理（创建/发布/删除）
- 站点导出为纯静态 HTML，可部署到任意托管服务
- 以版本化容器镜像分发，启动时自动收敛、失败自动回滚
- 支持 Anthropic/OpenAI key 或本地 Ollama 连接，密钥存于站点状态存储

## 适用场景

- 不熟悉 Drupal 的用户用一句话建站并管理内容
- 把站点导出为静态页面部署到 Netlify/Cloudflare 等平台
- 自托管一个带 AI 助手的企业或个人网站

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L7: **The AI-native CMS, by AIncient Labs.**
> L8: Create, find, update, and publish content through an AI operator console —
> L63:  Watch the assistant pick the right tool, create the content, and report back — in one turn.

## 星数曲线

```mermaid
xychart-beta
    title "aincient-labs/atelier-cms 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0e840d21113f` · [字段定义](../../DATASET.md)*
