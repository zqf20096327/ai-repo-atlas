# leeguooooo/misonote-markdown

⭐ 19 · TypeScript · NOASSERTION · 推送 2025-12-12 · [GitHub](https://github.com/leeguooooo/misonote-markdown) · [官网](https://docs.misonote.com) · 个人维护 · 中文 README

**Markdown 文档管理与预览系统，面向团队部署**

基于 Next.js/React/TypeScript 的 Markdown 文档管理与预览 Web 应用：支持 GitHub Flavored Markdown、Mermaid 图表、全文搜索、树形目录导航、在线编辑与拖拽上传，内置 JWT 认证、bcrypt 密码哈希与管理后台。部署以 Docker 镜像为主（AMD64/ARM64 多架构），提供 Docker Compose、源码 pnpm 构建、PM2 生产运行等方式；另含 CI 代码评审结果通过 Web API 落库的集成，README 中未见独立的 AI 生成/识别功能描述。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 完整 GitHub Flavored Markdown 预览与 Mermaid 图表支持
- 全局搜索、树形目录导航与在线编辑器
- Docker 多架构镜像一键运行，内置 PM2 生产部署
- JWT 认证、bcrypt 密码哈希与管理后台

## 适用场景

- 团队搭建内部文档站点并在线维护 Markdown 文档
- 以 Docker 一条命令快速部署带认证的文档预览服务
- 让 GitHub Actions/Codex 的代码评审结果自动落地到文档库

## 场景标签

 · 领域:团队协作/文档管理

## 证据(README 行号)

> L10: 一个现代化的 Markdown 文档管理和预览系统，支持 Mermaid 图表、全局搜索、目录导航等功能。
> L269: - CI 代码评审发布 API：让 GitHub Actions / Codex 自动 Review 结果通过 Web API 落地到文档库。

## 星数曲线

```mermaid
xychart-beta
    title "leeguooooo/misonote-markdown 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 low · 依据 README sha `d3399b050aba` · [字段定义](../../DATASET.md)*
