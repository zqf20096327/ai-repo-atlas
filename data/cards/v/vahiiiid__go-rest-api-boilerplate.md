# vahiiiid/go-rest-api-boilerplate

⭐ 71 · Go · MIT · 推送 2026-08-17 · [GitHub](https://github.com/vahiiiid/go-rest-api-boilerplate) · [官网](https://vahiiiid.github.io/go-rest-api-docs/) · 个人维护

**面向 AI 编码助手优化的 Go REST API 脚手架**

Go 语言 REST API 项目模板（GRAB），提供 Clean Architecture 分层、JWT 认证与刷新令牌轮换、多对多 RBAC、PostgreSQL 版本化迁移、Swagger 文档、结构化日志与错误处理、多阶段 Docker 构建和健康检查端点。面向希望快速搭建生产 API 的 Go 开发者。AI 相关部分是以 AGENTS.md 为单一事实源、为 Claude Code、Copilot、Cursor、Windsurf 等 IDE 助手生成的项目规范适配文件，不包含模型功能本身。通过 git clone 加 make quick-start 一条命令启动，也可原生运行（需 Go 1.24+）。

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

- Handler→Service→Repository 三层 Clean Architecture 与依赖注入
- JWT 认证（刷新令牌轮换、复用检测）+ RBAC + 管理员 CLI
- 以 AGENTS.md 为源，为 Claude Code/Copilot/Cursor/Windsurf 提供 IDE 助手规范适配
- Docker 热重载（Air，约 2 秒）与一条命令 quick-start

## 适用场景

- 快速启动一个生产可用的 Go REST API 项目
- 让 AI 编码助手按项目规范生成代码与重构建议
- 团队项目统一后端架构与测试约定

## 场景标签

 · 领域:后端开发/脚手架

## 证据(README 行号)

> L24: GRAB is designed to work seamlessly with your favorite AI coding assistants:
> L33: **Out-of-the-box AI integration**, all built from one canonical guide — `AGENTS.md` — with tool-specific adapters f
> L61: ✅ **Clean Architecture** — Handler → Service → Repository (GO industry standard)

## 星数曲线

```mermaid
xychart-beta
    title "vahiiiid/go-rest-api-boilerplate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-28 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `00fa6d2fa172` · [字段定义](../../DATASET.md)*
