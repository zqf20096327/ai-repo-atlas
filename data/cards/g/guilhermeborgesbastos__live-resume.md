# guilhermeborgesbastos/live-resume

⭐ 491 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/guilhermeborgesbastos/live-resume) · [官网](https://guilhermeborgesbastos.com/) · 个人维护 · 中文 README

**开源个人简历网站模板，内置浏览器端问答助手**

基于 Angular 21 (LTS) 的个人简历/作品集 Web 应用模板，含响应式布局、英葡双语国际化、SEO 优化、schema.org 结构化数据、Firebase 联系表单与 5 个自定义区块。AI 部分为规则型助手：在浏览器端运行，答案仅从 about/experiences/posts.json 数据组装并引用来源，不使用语言模型或外部服务；另含 Claude Code 技能用于添加文章卡片。通过 git clone + npm 本地运行，或用 Docker 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器端规则型 AI 助手，答案仅来自本地 JSON 数据并引用来源，无语言模型或外部服务
- 英葡双语国际化与移动端手势支持
- 提供 Docker 镜像（amd64/arm64）与 Nginx 双语言部署
- 含 Claude Code 技能，通过 /add-post 命令生成双语文章卡片

## 适用场景

- 搭建个人简历与作品集网站
- 让访客通过问答助手了解我的经历、证书与文章
- 以 Docker 方式部署双语简历站点

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L133: Visitors can ask questions about the CV from the floating **Ask my AI Assistant** button (shown with a robot icon)
> L135: ## ✍️ Adding posts with Claude Code

## 星数曲线

```mermaid
xychart-beta
    title "guilhermeborgesbastos/live-resume 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-10-30"]
    y-axis "stars" 490 --> 492
    line [491, 491]
```

2026-10-28 491 → 2026-10-30 491（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e0c75e949c7d` · [字段定义](../../DATASET.md)*
