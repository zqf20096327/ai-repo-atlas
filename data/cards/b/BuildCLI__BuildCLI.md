# BuildCLI/BuildCLI

⭐ 164 · Java · MIT · 推送 2026-10-25 · [GitHub](https://github.com/BuildCLI/BuildCLI) · [官网](https://buildcli.dev) · 组织维护

**给 Java 开发者的项目创建、构建、Docker 化与 CI/CD 命令行工具**

面向 Java 项目开发与自动化的命令行工具：从终端初始化项目结构（生成 src/main/java 与 pom.xml）、用 Maven 编译、增删 pom.xml 依赖、创建配置 profile、以 Spring Boot 运行项目；另支持生成 Dockerfile 与 docker-compose.yml 并管理容器生命周期、生成 Jenkins/GitLab/GitHub Actions 流水线配置、依据 Git 提交历史生成 changelog（markdown/html/json）。AI 部分为 Beta 功能：调用本地 Ollama API 为 Java 文件生成内联文档。提供安装脚本与 Releases 下载两种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 初始化/编译/依赖管理/运行 Java 项目的一体化 CLI 命令
- 生成 Dockerfile、docker-compose.yml 并管理容器编排
- 为 Jenkins/GitLab/GitHub Actions 生成 CI/CD 配置
- 调用本地 Ollama 为 Java 文件生成内联文档（Beta）

## 适用场景

- 在终端里快速创建和管理 Java 项目结构与依赖
- 为 Java 项目生成 Docker 与编排配置并启动容器
- 为仓库生成 CI/CD 流水线配置和结构化 changelog
- 用本地 AI 为 Java 代码补充文档注释

## 场景标签

 · 领域:软件开发/构建工具

## 证据(README 行号)

> L10: **BuildCLI** is a command-line interface (CLI) tool for managing and automating common tasks in Java
> L25: - **Document Code**: [Beta] Generates documentation for a Java file using AI.

## 星数曲线

```mermaid
xychart-beta
    title "BuildCLI/BuildCLI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 163 --> 165
    line [164, 164]
```

2026-10-18 164 → 2026-10-29 164（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `4a95432ec4cb` · [字段定义](../../DATASET.md)*
