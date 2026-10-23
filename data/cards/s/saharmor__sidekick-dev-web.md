# saharmor/sidekick-dev-web

⭐ 118 · TypeScript · Apache-2.0 · 推送 2026-03-23 · [GitHub](https://github.com/saharmor/sidekick-dev-web) · [官网](https://sidekickdev.com) · 个人维护

**为 AI 编程代理生成 GitHub 仓库的 markdown 上下文文件**

Web 应用（React 前端 + FastAPI 后端），读取公开 GitHub 仓库，借助 DeepWiki 的 AI 分析生成面向 Claude、Cursor、Windsurf、Gemini 等 AI 编程代理优化的 markdown 上下文文件，内容涵盖项目概览、架构、开发配置、代码组织与部署等；支持单文件或 ZIP 打包下载。一键脚本 start-dev.sh 同时启动前后端，后端可用 Docker 或 Render 部署；限制：仅支持公开仓库，私有仓库与索引问题仅给出错误反馈。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 面向 Claude/Cursor/Windsurf/Gemini 多代理生成优化的上下文文件
- 基于 DeepWiki 的公开 GitHub 仓库分析
- 单 markdown 文件或 ZIP 归档下载
- 一键脚本 setup：Python 虚拟环境 + 依赖安装 + 双服务启动

## 适用场景

- 为我的 AI 编程代理快速准备某个开源项目的背景文档
- 让 Cursor/Claude 理解陌生仓库的架构与开发配置
- 一次为多个 AI 代理工具批量下载同一仓库的上下文文件

## 场景标签

 · 领域:开发者工具/AI 编程辅助

## 证据(README 行号)

> L3: Automatically generate high-quality markdown context files for AI coding agents like Claude, Cursor, Windsurf, and G
> L14: - **GitHub Integration**: Analyze any public GitHub repository using DeepWiki's AI-powered analysis

## 星数曲线

```mermaid
xychart-beta
    title "saharmor/sidekick-dev-web 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 117 --> 119
    line [118, 118]
```

2026-10-18 118 → 2026-10-23 118（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `5b43fc763265` · [字段定义](../../DATASET.md)*
