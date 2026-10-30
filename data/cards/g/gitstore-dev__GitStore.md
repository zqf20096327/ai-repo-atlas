# gitstore-dev/GitStore

⭐ 19 · Go · AGPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/gitstore-dev/GitStore) · [官网](https://gitstore.dev) · 组织维护

**面向 AI agent 的 Git 驱动无头电商目录引擎**

开源的 Git-backed 无头电商平台：商品、变体、分类以带 YAML frontmatter 的 Markdown 文件管理，通过 Git 分支、diff、评审等工作流修改目录，经 pre-receive 校验与 post-receive 准入检查后才暴露为 GraphQL 查询。由 Go 的 gitstore-api、Rust 的 gitstore-git-service、Go controller 三个服务组成，供开发者、商品运营与 AI agent 编辑生产电商数据并提供可审计历史。README 自述处于早期开发，API 与架构会有破坏性变更；Git 服务为有状态单例，未宣称生产级 HA。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 目录资源为 Markdown + YAML frontmatter 文件，走 Git 工作流
- pre-receive 结构校验 + post-receive 准入，仅投影有效目录到 GraphQL
- Go API（GraphQL + Git Smart HTTP）+ Rust Git 存储服务 + controller 三组件
- make compose 一键运行核心栈并 bootstrap 初始命名空间与仓库

## 适用场景

- 让 AI agent 以文件操作和标准 Git push 更新商品目录
- 以 Git 分支/评审/回滚管理商品内容变更
- 无头架构下通过 GraphQL 查询已准入的目录状态

## 场景标签

 · 领域:电商/基础设施

## 证据(README 行号)

> L6: GitStore is an open-source Git-backed commerce platform where product catalogues are managed as plain files instead 
> L10: The broader thesis is that commerce operations are becoming increasingly agentic. AI agents will generate product d
> L52: - **Automation-friendly**: AI agents can generate and update catalogue content through file operations and standard

## 星数曲线

```mermaid
xychart-beta
    title "gitstore-dev/GitStore 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b4a50679e3e4` · [字段定义](../../DATASET.md)*
